'''
HemoPheno4HF
SCRIPT DESCRIPTION: Generation of MVDDs
CODE DEVELOPED BY: Josephine Lamp
ORGANIZATION: University of Virginia, Charlottesville, VA
LAST UPDATED: 8/24/2020
'''

import random
import networkx as nx
from MVDD.MVDD import MVDD
import copy
from collections import OrderedDict
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.tree import export_graphviz
from sklearn.model_selection import GridSearchCV
from sklearn import tree
import pickle
import pydotplus
import collections
from networkx.drawing.nx_pydot import *
from MVDD.MVDD import MVDD
import Params as params
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np
import random
from itertools import permutations
import re


# Generate a random MVDD from a starting list of nodes
# INPUT = list of feature nodes, and the maximum number of branches allowed from each node
# OUTPUT = returns a MVDD object class with the created network x dot graph
def generateRandomMVDD(nodes, maxBranches):

    #Generate dot graph
    dot = nx.DiGraph()
    edgeDict = [] # track edges already added

    # Terminal nodes
    dot.add_node("1", shape="box")
    dot.add_node("2", shape="box")
    dot.add_node("3", shape="box")
    dot.add_node("4", shape="box")
    dot.add_node("5", shape="box")

    #Add nodes to class
    for n in nodes:
        dot.add_node(n)

    availableNodes = copy.deepcopy(nodes) #nodes available to choose
    childNodes = []

    #start with root
    currNode = random.choice(nodes)  # pick random node
    root = currNode
    availableNodes.remove(currNode)
    for nb in range(random.randint(1, maxBranches)): #add edges to other nodes
        selected = random.choice(availableNodes)
        style = random.randint(1, 2)
        if style == 1:
            dot, edgeDict = addEdge(dot, currNode, selected, 'solid', edgeDict)
        else:
            dot, edgeDict = addEdge(dot, currNode, selected, 'dashed', edgeDict)

        childNodes.append(selected)

    childNodes = list(set(childNodes))

    while childNodes != []:
        dot, childNodes, availableNodes, edgeDict = addChildNodesRandom(dot, childNodes, maxBranches, availableNodes, edgeDict)

    newMvdd = MVDD(features=nodes, dot=dot, root=root)

    return newMvdd

# Add child nodes to a dot graph
# INPUT = dot graph, list of child nodes to add, the number of max branches, a list of available nodes to select from, and a dictionary of edges
# OUTPUT = returns the dot graph, the list of new child nodes, the updated list of available nodes and the updated dictionary of edges
def addChildNodesRandom(dot, childNodes, maxBranches, availableNodes, edgeDict):
    for c in childNodes:  # remove new parents
        availableNodes.remove(c)

    if availableNodes == []: #no more nodes to add
        dot, edgeDict = addTerminalNodesRandom(dot, childNodes, edgeDict)
        return dot, [], availableNodes, edgeDict
    else:
        newChildren = []

        if len(availableNodes) < 6: #can add some terminal nodes
            for currNode in childNodes:

                for nb in range(random.randint(2, maxBranches)):  # add edges to other nodes
                    if random.randint(1, 2) == 1:
                        selected = random.choice(availableNodes)
                        style = random.randint(1, 2)
                        if style == 1:
                            dot, edgeDict = addEdge(dot, currNode, selected, 'solid', edgeDict)
                        else:
                            dot, edgeDict = addEdge(dot, currNode, selected, 'dashed', edgeDict)

                        newChildren.append(selected)

                    else:
                        dot, edgeDict = addTerminalNodesRandom(dot, childNodes, edgeDict)

        else: #just add internal nodes
            for currNode in childNodes:
                for nb in range(random.randint(2,maxBranches)): #add edges to other nodes
                    selected = random.choice(availableNodes)
                    style = random.randint(1,2)
                    if style == 1:
                        dot, edgeDict = addEdge(dot, currNode, selected, 'solid', edgeDict)
                    else:
                        dot, edgeDict = addEdge(dot, currNode, selected, 'dashed', edgeDict)

                    newChildren.append(selected)

        newChildren = list(set(newChildren))
        return dot, newChildren, availableNodes, edgeDict

# Add terminal (leaf) nodes to dot graph
# INPUT = dot graph, list of child nodes to add and a dictionary of edges
# OUTPUT = returns the dot graph and the updated dictionary of edges
def addTerminalNodesRandom(dot, childNodes, edgeDict):
    terms = ["1", "2", "3", "4", "5"]
    for c in childNodes:
        selected = random.choice(terms)
        dot, edgeDict = addEdge(dot, c, selected, 'solid', edgeDict, terminal=True)

    return dot, edgeDict

# Generate a random MVDD from a starting list of nodes
# INPUT = list of feature nodes, and the maximum number of branches allowed from each node
# OUTPUT = returns a MVDD object class with the created network x dot graph
def generateMVDDFeatureImportance(nodes, terminalOrder, maxBranches):

    #Generate dot graph
    dot = nx.DiGraph()
    edgeDict = [] # track edges already added

    # Terminal nodes
    dot.add_node("1", shape="box")
    dot.add_node("2", shape="box")
    dot.add_node("3", shape="box")
    dot.add_node("4", shape="box")
    dot.add_node("5", shape="box")

    #Add nodes to class
    for n in nodes:
        dot.add_node(n)

    availableNodes = copy.deepcopy(nodes) #nodes available to choose
    childNodes = []

    #start with root
    currNode = nodes[0]  # pick first node
    root = currNode
    availableNodes.remove(currNode)
    count = 0
    for nb in range(random.randint(2, maxBranches-1)): #add edges to other nodes
        selected = availableNodes[count]
        count += 1
        style = random.randint(1, 2)
        if style == 1:
            dot, edgeDict = addEdge(dot, currNode, selected, 'solid', edgeDict)
        else:
            dot, edgeDict = addEdge(dot, currNode, selected, 'dashed', edgeDict)

        childNodes.append(selected)

    childNodes = list(OrderedDict.fromkeys(childNodes))

    while childNodes != []:
        dot, childNodes, availableNodes, edgeDict = addChildNodes(dot, childNodes, maxBranches, availableNodes, edgeDict, terminalOrder)

    newMvdd = MVDD(features=nodes, dot=dot, root=root)

    return newMvdd

# Add child nodes to a dot graph
# INPUT = dot graph, list of child nodes to add, the number of max branches, a list of available nodes to select from, and a dictionary of edges
# OUTPUT = returns the dot graph, the list of new child nodes, the updated list of available nodes and the updated dictionary of edges
def addChildNodes(dot, childNodes, maxBranches, availableNodes, edgeDict, terminalOrder):
    for c in childNodes:  # remove new parents
        availableNodes.remove(c)

    if availableNodes == []: #no more nodes to add
        dot, edgeDict = addTerminalNodes(dot, childNodes, edgeDict, terminalOrder)
        return dot, [], availableNodes, edgeDict
    else:
        newChildren = []

        if len(availableNodes) < 6: #can add some terminal nodes
            for currNode in childNodes:
                for nb in range(random.randint(2, maxBranches-1)):  # add edges to other nodes
                    if random.randint(1, 2) == 1:
                        firstThird = int(len(availableNodes) / 3)
                        if firstThird < 4:
                            rand = random.randint(0, len(availableNodes)-1)
                        else:
                            rand = random.randint(0, firstThird)
                        selected = availableNodes[rand]
                        style = random.randint(1, 2)
                        if style == 1:
                            dot, edgeDict = addEdge(dot, currNode, selected, 'solid', edgeDict)
                        else:
                            dot, edgeDict = addEdge(dot, currNode, selected, 'dashed', edgeDict)

                        newChildren.append(selected)

                    else:
                        dot, edgeDict = addTerminalNodes(dot, childNodes, edgeDict, terminalOrder)

        else: #just add internal nodes
            for currNode in childNodes:
                for nb in range(random.randint(2,maxBranches-1)): #add edges to other nodes
                    firstThird = int(len(availableNodes) / 3)
                    if firstThird < 4:
                        rand = random.randint(0, len(availableNodes)-1)
                    else:
                        rand = random.randint(0, firstThird)
                    selected = availableNodes[rand]
                    style = random.randint(1,2)
                    if style == 1:
                        dot, edgeDict = addEdge(dot, currNode, selected, 'solid', edgeDict)
                    else:
                        dot, edgeDict = addEdge(dot, currNode, selected, 'dashed', edgeDict)

                    newChildren.append(selected)

        newChildren = list(OrderedDict.fromkeys(newChildren))
        return dot, newChildren, availableNodes, edgeDict

# Add terminal (leaf) nodes to dot graph
# INPUT = dot graph, list of child nodes to add and a dictionary of edges
# OUTPUT = returns the dot graph and the updated dictionary of edges
def addTerminalNodes(dot, childNodes, edgeDict, terminalOrder):
    for c in range(len(childNodes)):
        if c >= len(terminalOrder):
            selected = random.choice(terminalOrder)
        else:
            selected = terminalOrder[c]
        dot, edgeDict = addEdge(dot, childNodes[c], selected, 'solid', edgeDict, terminal=True)

    return dot, edgeDict



# Add an edge to a dot graph
# INPUT = dot graph, current node and selected node to add the edge between, the type of the edge [dashed for or, and solid for and operators], a dictionary of edges,
#         and a check if the edge is connecting a terminal node or not
# OUTPUT = returns the dot graph and the updated dictionary of edges
def addEdge(dot, currNode, selected, type, edgeDict, terminal=False):
    key = currNode + selected + type

    if terminal:
        #check for any other terminal nodes already connected to the node
        termCount = 0
        for i in range(1,6):
            k = currNode + str(i) + type
            if k in edgeDict:
                termCount += 1

        if termCount > 2:
            pass
        else:
            dot.add_edge(currNode, selected, style=type)
            # dot.add_edges_from(currNode, selected, {'style':type}, {'op':'&'}, {'param': '9'})
            key = currNode + selected + type
            edgeDict.append(key)

    else:
        if key in edgeDict:
            pass #edge already in graph
        else:
            dot.add_edge(currNode, selected, style=type)
            key = currNode + selected + type
            edgeDict.append(key)

    return dot, edgeDict

# Updates or adds RANDOM parameters to a dot graph
# INPUT = the MVDD object and a list of average values
# OUTPUT = returns the updated mvdd
def addGraphParamsRandom(mvdd, aveValues):
    dot = mvdd.dot
    # for ed in nx.bfs_edges(dot, mvdd.root):
    for n in nx.nodes(dot):
        # currNode = ed[0]
        # lower = mvdd.featureDict[currNode][0]
        # upper = mvdd.featureDict[currNode][1]

        numEdges = len(dot.edges(n))
        for edg in dot.edges(n):
            if edg[1] in ['1', '2', '3', '4', '5']:
                val = aveValues[n][int(edg[1])-1]
                val = float("{:.2f}".format(val))
                op = random.choice(['<=', '>='])
                label = op + " " + str(val)
                dot.edges[n, edg[1]]['label'] = label
                dot.edges[n, edg[1]]['op'] = op
                dot.edges[n, edg[1]]['param'] = str(val)
            else:
                pos = random.randint(0,4)
                val = aveValues[n][pos]
                val = float("{:.2f}".format(val))
                op = random.choice(["<=", ">="])
                label = op + " " + str(val)
                dot.edges[n, edg[1]]['label'] = label
                dot.edges[n, edg[1]]['op'] = op
                dot.edges[n, edg[1]]['param'] = str(val)

    mvdd.dot = dot

    return mvdd

# Updates or adds specified parameters to a dot graph
# INPUT = the MVDD object, a dictionary with params and the values to add, if the params should be added in order or randomly
# OUTPUT = returns the updated mvdd, the parameters used and the relops used
def addGraphParams(mvdd, paramValues, relopValues, inorder=True):
    usedParams = {}
    usedRelops = {}
    for key in paramValues:
        usedParams[key] = []
        usedRelops[key] = []

    dot = mvdd.dot

    for n in nx.nodes(dot):
        if inorder:
            count = 0
            for edg in dot.edges(n):
                val = paramValues[n][count]
                val = float("{:.2f}".format(val))
                op = relopValues[n][count]
                label = op + " " + str(val)
                dot.edges[n, edg[1]]['label'] = label
                dot.edges[n, edg[1]]['op'] = op
                dot.edges[n, edg[1]]['param'] = str(val)

                usedParams[n].append(val)
                usedRelops[n].append(op)

                count += 1
        else:
            for edg in dot.edges(n):
                idx = random.randint(0, len(relopValues[n])-1)
                val = paramValues[n][idx]
                val = float("{:.2f}".format(val))
                op = relopValues[n][idx]
                label = op + " " + str(val)
                dot.edges[n, edg[1]]['label'] = label
                dot.edges[n, edg[1]]['op'] = op
                dot.edges[n, edg[1]]['param'] = str(val)

                usedParams[n].append(val)
                usedRelops[n].append(op)

    mvdd.dot = dot

    return mvdd, usedParams, usedRelops

def generateTree(xData, yData, classes, learningCriteria='gini', maxLevels=None, minSamplesPerLeaf=5, modelName='MVDD'):

    #First learn a decision tree classifier to boost the learning process
    dt = DecisionTreeClassifier(criterion=learningCriteria, random_state=100,
                                max_depth=maxLevels, min_samples_leaf=minSamplesPerLeaf)
    dt.fit(xData, yData)

    #Convert decision tree into dot graph
    dot_data = tree.export_graphviz(dt,
                                    feature_names=xData.columns,
                                    class_names=classes,
                                    out_file=None,
                                    filled=True,
                                    rounded=True)
    graph = pydotplus.graph_from_dot_data(dot_data)

    #Recolor the nodes
    colors = ('palegreen', 'honeydew', 'lightyellow', 'mistyrose', 'lightcoral')
    nodes = graph.get_node_list()

    for node in nodes:
        if node.get_name() not in ('node', 'edge'):
            vals = dt.tree_.value[int(node.get_name())][0]
            maxPos = np.argmax(vals)
            node.set_fillcolor(colors[maxPos])

    # Convert decision tree dot data to decision diagram
    dot = nx.nx_pydot.from_pydot(graph)
    dot = nx.DiGraph(dot)

    # Get terminal indices
    terminalIndices = []
    for n in dot.nodes:
        label = dot.nodes[n]['label']
        label = label.replace("\"", "")
        labelSplit = label.split('\\n')[0]
        tokens = labelSplit.split(' ')

        if tokens[0] == learningCriteria: #NOTE was 'gini'
            terminalIndices.append(n)

    for n in dot.nodes:
        label = dot.nodes[n]['label']
        label = label.replace("\"", "")
        labelSplit = label.split('\\n')[0]
        tokens = labelSplit.split(' ')
        leftLabel, leftOp, rightLabel, rightOp, param = getLeftRightLabels(tokens)

        if tokens[0] != 'gini':
            nodeLabel = re.sub(labelSplit, '', dot.nodes[n]['label'])
            nodeLabel = nodeLabel.replace("\"", "")
            nodeLabel = tokens[0] + nodeLabel
            dot.nodes[n]['label'] = nodeLabel

        count = 0
        for edg in dot.edges(n):
            if edg[0] in terminalIndices or edg[1] in terminalIndices or count == 0:
                dot.edges[edg[0], edg[1]]['label'] = leftLabel
                dot.edges[edg[0], edg[1]]['op'] = leftOp
                dot.edges[edg[0], edg[1]]['param'] = param
                dot.edges[edg[0], edg[1]]['style'] = 'solid'

                dot.edges[edg[0], edg[1]]['headlabel'] = ""
                count += 1
            else:
                dot.edges[edg[0], edg[1]]['label'] = rightLabel
                dot.edges[edg[0], edg[1]]['op'] = rightOp
                dot.edges[edg[0], edg[1]]['param'] = param
                dot.edges[edg[0], edg[1]]['style'] = 'dashed'

                dot.edges[edg[0], edg[1]]['headlabel'] = ""

    #Create MVDD
    mvdd = MVDD(features=xData.columns, dot=dot, root='0', model=dt)
    mvdd.terminalIndices = terminalIndices

    #Save model to file
    pickle.dump(mvdd, open(modelName+'.sav', 'wb'))

    #Save tree to file
    mvdd.saveDotFile(modelName)
    mvdd.saveToFile(modelName, 'pdf')
    mvdd.saveToFile(modelName, 'png')

    return mvdd


# Helper methods
def getLeftRightLabels(tokens):
    leftLabel = tokens[1] + " " + tokens[2]
    leftOp = tokens[1]
    param = tokens[2]

    if leftOp == '<=':
        rightOp = '>'
    elif leftOp == '>=':
        rightOp = '<'
    elif leftOp == '>':
        rightOp = '<='
    else:
        rightOp = '>='

    rightLabel = rightOp + " " + param

    return leftLabel, leftOp, rightLabel, rightOp, param


def loadMVDDFromFile(modelName):
    return pickle.load(open(modelName + '.sav', 'rb'))

def findBestModelParams(xData, yData, params):
    dt = DecisionTreeClassifier()

    gs = GridSearchCV(dt, params)
    gs.fit(xData, yData)

    print("Best parameters set found on training set:")
    print(gs.best_params_)

    y_true, y_pred = yData, gs.predict(xData)
    print(classification_report(y_true, y_pred))
