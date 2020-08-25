'''
HemoPheno4HF
SCRIPT DESCRIPTION: Main Runner Class for Learning Scors from the Trained MVDDs
CODE DEVELOPED BY: Josephine Lamp
ORGANIZATION: University of Virginia, Charlottesville, VA
LAST UPDATED: 8/24/2020
'''

from MVDD.MVDD import MVDD
import MVDD.MVDD_Generator as mvGen
import networkx as nx
from networkx.drawing.nx_pydot import *
import Params as params


#Expects param dict of 27 parameters, and select one of 3 outcomes
#Returns a text file location to display the graph, a integer score value and a string phenotype to be displayed
#Outcome can be "Death" "Rehospitalization" "Readmission"
def runHemo(paramDict, outcome):

    #check for strings in paramDict
    for p in paramDict:
        if paramDict[p] == "":
            paramDict[p] = 0
        else:
            paramDict[p] = float(paramDict[p])

    #load tree
    dot = read_dot('test2params.dot')
    dot = nx.DiGraph(dot)
    mvdd = MVDD(params.hemo, dot, root='PAMN')
    mvdd.featureDict = params.hemoDict

    #Predict score
    score, path = mvdd.predictScore(paramDict)
    path[-2] = '->'
    stringPath = ' '.join(path)
    print(stringPath)

    return 'TreeFiles/treeParams2.png', score, stringPath #will be displayed on webpage


#Expects a param dict of 119 parameters
def runAllData(paramDict):
    pass




def main():
    pass
#     runHemo({"Age":"","BPDIAS":"","BPSYS":"3232","CI":"","CO":"","CPI":"","CWP":"12333","EjF":"","HRTRT":"","MAP":"","MIXED":"","MPAP":"","PAD":"","PAMN":"","PAPP":"","PAS":"","PCWPA":"","PCWPMN":"","PCWPMod":"","PP":"","PPP":"","PPRatio":"","RAP":"","RAT":"","RATHemo":"","SVRHemo":"","VR":""}
# , 'Death')


if __name__ == "__main__":
    main()