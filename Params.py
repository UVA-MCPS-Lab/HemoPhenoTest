'''
HemoPheno4HF
SCRIPT DESCRIPTION: Parameters needed for HemoPheno Process
CODE DEVELOPED BY: Josephine Lamp
ORGANIZATION: University of Virginia, Charlottesville, VA
LAST UPDATED: 8/24/2020
'''

#List of hemo features
hemo = ['RAP', 'PAS', 'PAD', 'PAMN', 'PCWP', 'PCWPMod', 'PCWPA', 'PCWPMN', 'CO',
        'CI', 'SVRHemo', 'MIXED', 'BPSYS', 'BPDIAS', 'HRTRT', 'RATHemo', 'MAP',
        'MPAP', 'CPI', 'PP', 'PPP', 'PAPP', 'SVR', 'RAT', 'PPRatio', 'Age',
        'EjF']

#List of hemo ranges for each feature
hemoDict = {'RAP': [0.0, 85.0],
            'PAS': [0.0, 90.0],
            'PAD': [0.0, 59.0],
            'PAMN': [0.0, 82.0],
            'PCWP': [0.0, 53.0],
            'PCWPMod': [0.0, 53.0],
            'PCWPA': [0.0, 53.0],
            'PCWPMN': [0.0, 49.0],
            'CO': [0.0, 25.0],
            'CI': [0.0, 4.81],
            'SVRHemo': [0.0, 6866.0],
            'MIXED': [0.0, 627.0],
            'BPSYS': [0.0, 168.0],
            'BPDIAS': [0.0, 125.0],
            'HRTRT': [0.0, 125.0],
            'RATHemo': [0.0, 3.74],
            'MAP': [0.0, 226.0],
            'MPAP': [0.0, 129.3333333],
            'CPI': [0.0, 1.820192166],
            'PP': [-55.0, 106.0],
            'PPP': [-0.833333333, 0.736842105],
            'PAPP': [0.0, 0.8444444440000001],
            'SVR': [0.0, 10755.555559999999],
            'RAT': [0.0, 3.736842105],
            'PPRatio': [-0.8870967740000001, 9.666666667000001],
            'Age': [23.0, 88.0],
            'EjF': [0.0, 45.0]}

hemoParamsV1 = {'RAP': [10.617021276595745, 0.0, 18.553571428571427, 7.586956521739131, 13.4],
 'PAS': [40.72727272727273,
  0.0,
  68.52631578947368,
  41.61267605633803,
  55.55474452554745],
 'PAD': [18.363636363636363,
  0.0,
  37.87719298245614,
  18.007042253521128,
  26.598540145985403],
 'PAMN': [29.47826086956522,
  0.0,
  48.01754385964912,
  26.431654676258994,
  36.63970588235294],
 'PCWP': [18.35,
  0.0,
  34.94736842105263,
  13.991869918699187,
  23.404580152671755],
 'PCWPMod': [18.75,
  0.0,
  34.94736842105263,
  15.02112676056338,
  24.014598540145986],
 'PCWPA': [15.0,
  0.0,
  35.21739130434783,
  14.154761904761905,
  23.307692307692307],
 'PCWPMN': [19.586206896551722,
  0.0,
  33.891304347826086,
  13.474358974358974,
  22.54320987654321],
 'CO': [3.7411111111111106,
  0.0,
  3.5160000000000005,
  5.093714285714286,
  3.9403731343283583],
 'CI': [1.9777777777777774,
  0.0,
  1.7485185185185186,
  2.491205673758865,
  2.0285496183206106],
 'SVRHemo': [1228.2777777777778,
  0.0,
  1583.611111111111,
  1129.2272727272727,
  1375.6124031007753],
 'MIXED': [57.666666666666664,
  0.0,
  48.666666666666664,
  59.1551724137931,
  62.945205479452056],
 'BPSYS': [91.14634146341463,
  0.0,
  109.45614035087719,
  106.95774647887323,
  107.56934306569343],
 'BPDIAS': [55.36585365853659,
  0.0,
  70.05263157894737,
  58.929577464788736,
  63.496350364963504],
 'HRTRT': [69.6086956521739,
  0.0,
  87.66666666666667,
  80.71126760563381,
  81.11678832116789],
 'RATHemo': [0.558974358974359,
  0.0,
  0.5444642857142857,
  0.49983193277310917,
  0.573359375],
 'MAP': [128.05691057219514,
  0.0,
  156.1578947385965,
  146.24413145725353,
  149.90024330656937],
 'MPAP': [52.969696969090904,
  0.0,
  93.77777777842105,
  53.61737089197183,
  73.28710462328468],
 'CPI': [0.5518146055483871,
  0.0,
  0.594531357,
  0.8027217163758865,
  0.6766359743664122],
 'PP': [35.78048780487805,
  0.0,
  39.40350877192982,
  48.028169014084504,
  44.07299270072993],
 'PPP': [0.3647878179512195,
  0.0,
  0.3597870333157895,
  0.44713453375352114,
  0.40356013221167886],
 'PAPP': [0.5427914533636363,
  0.0,
  0.44163834891228076,
  0.5615927534366196,
  0.5140710068321168],
 'SVR': [2589.8704747812503,
  0.0,
  3513.218464888889,
  2413.2820651742645,
  3095.4708408330825],
 'RAT': [0.558393595948718, 0.0, 0.5442847839642857, 0.0, 0.0],
 'PPRatio': [0.9062159425121952,
  0.0,
  0.46722958124561403,
  0.6172521843098592,
  0.5632871878759124],
 'Age': [59.145833333333336,
  56.61764705882353,
  54.45614035087719,
  57.183098591549296,
  56.56934306569343],
 'EjF': [20.6,
  18.84375,
  16.07017543859649,
  21.18840579710145,
  18.696969696969695]}

hemoRelopsV1 = {'RAP': ['>=', '<=', '<=', '>'], 'PAS': ['>=', '<', '>=', '<='], 'PAD': ['>=', '>', '<=', '>='], 'PAMN': ['<=', '<=', '>=', '>='], 'PCWP': ['<=', '>=', '>=', '>='], 'PCWPMod': ['>=', '>=', '>=', '<='], 'PCWPA': ['<=', '<=', '<=', '<='], 'PCWPMN': ['>=', '<=', '<=', '>='], 'CO': ['>=', '<=', '>=', '>='], 'CI': ['>=', '<=', '<', '>='], 'SVRHemo': ['>', '<=', '>=', '>='], 'MIXED': ['<=', '<=', '<=', '<='], 'BPSYS': ['>=', '>=', '>=', '<='], 'BPDIAS': ['>=', '<=', '<=', '>='], 'HRTRT': ['<=', '<=', '<=', '>='], 'RATHemo': ['>=', '>=', '<=', '>='], 'MAP': ['>=', '>=', '>=', '>='], 'MPAP': ['>=', '>=', '>=', '>='], 'CPI': ['<=', '>=', '<=', '>='], 'PP': ['<=', '<=', '<=', '>='], 'PPP': ['>=', '>=', '>=', '>='], 'PAPP': ['>=', '<=', '<=', '<='], 'SVR': ['>=', '>=', '<=', '>='], 'RAT': ['<=', '>=', '<=', '<='], 'PPRatio': ['<=', '<=', '<=', '>='], 'Age': ['>=', '<=', '>=', '<='], 'EjF': ['>=', '>=', '>=', '>=']}


#list of possible outcomes
outcomes = ['Death', 'Rehospitalization', 'Readmission']

allData = ['Age', 'Gender', 'Race', 'Wt', 'BMI', 'InitialHospDays', 'TotalHospDays', 'NYHA', 'MLHFS', 'AF', 'AlchE',
           'ANGP', 'AOREG', 'AOST', 'ARRH', 'CABG', 'CARREST', 'COPD', 'CVD', 'CYTOE', 'DEPR', 'DIAB', 'FAMILE', 'GOUT',
           'HEPT', 'HTN', 'HYPERE', 'HTRANS', 'ICD', 'IDIOPE', 'ISCHD', 'ISCHEME', 'MALIG', 'MI', 'MTST', 'OTHUNE',
           'PACE', 'PERIPAE', 'PMRG', 'PTCI', 'PTREG', 'PVD', 'RENALI', 'SMOKING', 'STERD', 'STROKE', 'SVT', 'TDP',
           'TIA', 'VAHD', 'VALVUE', 'VF', 'SixFtWlk', 'VO2', 'ALB', 'ALT', 'AST', 'BUN', 'CRT', 'DIAL', 'HEC', 'HEM',
           'PLA', 'POT', 'SOD', 'TALB', 'TOTP', 'WBC', 'ACE', 'BET', 'NIT', 'ANGIO', 'CINF', 'DIUR', 'AMR', 'ATE',
           'BEN', 'BIS', 'BUM', 'CAND', 'CAP', 'CAR', 'DIGX', 'DIN', 'DOB', 'DOP', 'ENA', 'ETH', 'FOS', 'FUR', 'LIS',
           'LOSA', 'MET', 'MIL', 'MON', 'NAT', 'NIG', 'NIP', 'OTHAA', 'OTHA', 'OTHB', 'OTHD', 'PRO', 'QUI', 'RAM',
           'TOP', 'TOR', 'TRA', 'VALSA', 'EjF', 'BPDIAS', 'BPSYS', 'HR', 'PV', 'MAP', 'PP', 'PPP', 'PPRatio']

allDataDict = {'Age': [20.0, 88.0],
               'Gender': [1.0, 2.0],
               'Race': [1.0, 98.0],
               'Wt': [0.0, 134.0],
               'BMI': [0.0, 57.06555671],
               'InitialHospDays': [0.0, 51.0],
               'TotalHospDays': [1.0, 154.0],
               'NYHA': [0.0, 4.0],
               'MLHFS': [0.0, 105.0],
               'AF': [0.0, 1.0],
               'AlchE': [0.0, 1.0],
               'ANGP': [0.0, 1.0],
               'AOREG': [0.0, 1.0],
               'AOST': [0.0, 1.0],
               'ARRH': [0.0, 1.0],
               'CABG': [0.0, 1.0],
               'CARREST': [0.0, 1.0],
               'COPD': [0.0, 1.0],
               'CVD': [0.0, 1.0],
               'CYTOE': [0.0, 1.0],
               'DEPR': [0.0, 1.0],
               'DIAB': [0.0, 1.0],
               'FAMILE': [0.0, 1.0],
               'GOUT': [0.0, 1.0],
               'HEPT': [0.0, 1.0],
               'HTN': [0.0, 1.0],
               'HYPERE': [0.0, 1.0],
               'HTRANS': [0.0, 3.0],
               'ICD': [0.0, 1.0],
               'IDIOPE': [0.0, 1.0],
               'ISCHD': [0.0, 1.0],
               'ISCHEME': [0.0, 1.0],
               'MALIG': [0.0, 1.0],
               'MI': [0.0, 1.0],
               'MTST': [0.0, 1.0],
               'OTHUNE': [0.0, 1.0],
               'PACE': [0.0, 1.0],
               'PERIPAE': [0.0, 1.0],
               'PMRG': [0.0, 1.0],
               'PTCI': [0.0, 1.0],
               'PTREG': [0.0, 1.0],
               'PVD': [0.0, 1.0],
               'RENALI': [0.0, 1.0],
               'SMOKING': [0.0, 3.0],
               'STERD': [0.0, 1.0],
               'STROKE': [0.0, 1.0],
               'SVT': [0.0, 1.0],
               'TDP': [0.0, 1.0],
               'TIA': [0.0, 1.0],
               'VAHD': [0.0, 1.0],
               'VALVUE': [0.0, 1.0],
               'VF': [0.0, 1.0],
               'SixFtWlk': [0.0, 2000.0],
               'VO2': [0.0, 27.5],
               'ALB': [0.0, 8.2],
               'ALT': [0.0, 1037.0],
               'AST': [0.0, 995.0],
               'BUN': [0.0, 139.0],
               'CRT': [0.0, 10.0],
               'DIAL': [0.0, 2.0],
               'HEC': [0.0, 533.0],
               'HEM': [0.0, 81.0],
               'PLA': [0.0, 649.0],
               'POT': [0.0, 8.0],
               'SOD': [0.0, 148.0],
               'TALB': [0.0, 2.4],
               'TOTP': [0.0, 14.8],
               'WBC': [0.0, 85.0],
               'ACE': [0.0, 1.0],
               'BET': [0.0, 1.0],
               'NIT': [0.0, 1.0],
               'ANGIO': [0.0, 1.0],
               'CINF': [0.0, 1.0],
               'DIUR': [0.0, 1.0],
               'AMR': [0.0, 0.0],
               'ATE': [0.0, 100.0],
               'BEN': [0.0, 120.0],
               'BIS': [0.0, 2.5],
               'BUM': [0.0, 56.0],
               'CAND': [0.0, 37.5],
               'CAP': [0.0, 400.0],
               'CAR': [0.0, 100.0],
               'DIGX': [0.0, 125.0],
               'DIN': [0.0, 270.0],
               'DOB': [0.0, 10.0],
               'DOP': [0.0, 3.0],
               'ENA': [0.0, 40.0],
               'ETH': [0.0, 0.0],
               'FOS': [0.0, 60.0],
               'FUR': [0.0, 1320.0],
               'LIS': [0.0, 80.0],
               'LOSA': [0.0, 320.0],
               'MET': [0.0, 200.0],
               'MIL': [0.0, 2.5],
               'MON': [0.0, 240.0],
               'NAT': [0.0, 180.0],
               'NIG': [0.0, 50.0],
               'NIP': [0.0, 0.2],
               'OTHAA': [0.0, 320.0],
               'OTHA': [0.0, 300.0],
               'OTHB': [0.0, 200.0],
               'OTHD': [0.0, 40.0],
               'PRO': [0.0, 60.0],
               'QUI': [0.0, 80.0],
               'RAM': [0.0, 40.0],
               'TOP': [0.0, 120.0],
               'TOR': [0.0, 960.0],
               'TRA': [0.0, 0.0],
               'VALSA': [0.0, 320.0],
               'EjF': [0.0, 45.0],
               'BPDIAS': [0.0, 100.0],
               'BPSYS': [0.0, 170.0],
               'HR': [0.0, 181.0],
               'PV': [-581.505997, 241.4103924],
               'MAP': [0.0, 235.33333330000002],
               'PP': [0.0, 103.0],
               'PPP': [0.0, 0.818181818],
               'PPRatio': [0.0, 1.534482759]}

clusterHemoScoreDict = {'RAP': [10.617021276595745, 0.0, 18.553571428571427, 7.586956521739131, 13.4],
 'PAS': [40.72727272727273,
  0.0,
  68.52631578947368,
  41.61267605633803,
  55.55474452554745],
 'PAD': [18.363636363636363,
  0.0,
  37.87719298245614,
  18.007042253521128,
  26.598540145985403],
 'PAMN': [29.47826086956522,
  0.0,
  48.01754385964912,
  26.431654676258994,
  36.63970588235294],
 'PCWP': [18.35,
  0.0,
  34.94736842105263,
  13.991869918699187,
  23.404580152671755],
 'PCWPMod': [18.75,
  0.0,
  34.94736842105263,
  15.02112676056338,
  24.014598540145986],
 'PCWPA': [15.0,
  0.0,
  35.21739130434783,
  14.154761904761905,
  23.307692307692307],
 'PCWPMN': [19.586206896551722,
  0.0,
  33.891304347826086,
  13.474358974358974,
  22.54320987654321],
 'CO': [3.7411111111111106,
  0.0,
  3.5160000000000005,
  5.093714285714286,
  3.9403731343283583],
 'CI': [1.9777777777777774,
  0.0,
  1.7485185185185186,
  2.491205673758865,
  2.0285496183206106],
 'SVRHemo': [1228.2777777777778,
  0.0,
  1583.611111111111,
  1129.2272727272727,
  1375.6124031007753],
 'MIXED': [57.666666666666664,
  0.0,
  48.666666666666664,
  59.1551724137931,
  62.945205479452056],
 'BPSYS': [91.14634146341463,
  0.0,
  109.45614035087719,
  106.95774647887323,
  107.56934306569343],
 'BPDIAS': [55.36585365853659,
  0.0,
  70.05263157894737,
  58.929577464788736,
  63.496350364963504],
 'HRTRT': [69.6086956521739,
  0.0,
  87.66666666666667,
  80.71126760563381,
  81.11678832116789],
 'RATHemo': [0.558974358974359,
  0.0,
  0.5444642857142857,
  0.49983193277310917,
  0.573359375],
 'MAP': [128.05691057219514,
  0.0,
  156.1578947385965,
  146.24413145725353,
  149.90024330656937],
 'MPAP': [52.969696969090904,
  0.0,
  93.77777777842105,
  53.61737089197183,
  73.28710462328468],
 'CPI': [0.5518146055483871,
  0.0,
  0.594531357,
  0.8027217163758865,
  0.6766359743664122],
 'PP': [35.78048780487805,
  0.0,
  39.40350877192982,
  48.028169014084504,
  44.07299270072993],
 'PPP': [0.3647878179512195,
  0.0,
  0.3597870333157895,
  0.44713453375352114,
  0.40356013221167886],
 'PAPP': [0.5427914533636363,
  0.0,
  0.44163834891228076,
  0.5615927534366196,
  0.5140710068321168],
 'SVR': [2589.8704747812503,
  0.0,
  3513.218464888889,
  2413.2820651742645,
  3095.4708408330825],
 'RAT': [0.558393595948718, 0.0, 0.5442847839642857, 0.0, 0.0],
 'PPRatio': [0.9062159425121952,
  0.0,
  0.46722958124561403,
  0.6172521843098592,
  0.5632871878759124],
 'Age': [59.145833333333336,
  56.61764705882353,
  54.45614035087719,
  57.183098591549296,
  56.56934306569343],
 'EjF': [20.6,
  18.84375,
  16.07017543859649,
  21.18840579710145,
  18.696969696969695],
 'cluster': [2.0, 3.0, 0.0, 1.0, 4.0],
 'Death': [0.5,
  0.17647058823529413,
  0.05263157894736842,
  0.5633802816901409,
  0.35766423357664234],
 'Rehosp': [-0.16666666666666666,
  -0.29411764705882354,
  -0.6140350877192983,
  -0.22535211267605634,
  -0.4744525547445255],
 'Readmission': [0.75,
  0.5882352941176471,
  0.6140350877192983,
  0.6338028169014085,
  0.708029197080292]}


clusterAllDataScoreDict = {'Age': [47.36363636363637,
  63.3448275862069,
  61.394366197183096,
  55.78260869565217,
  56.7196261682243],
 'Gender': [1.4189723320158103,
  1.1477832512315271,
  1.147887323943662,
  1.2608695652173914,
  1.233644859813084],
 'Race': [4.24901185770751,
  4.1330049261083746,
  2.795774647887324,
  3.8447204968944098,
  3.6448598130841123],
 'Wt': [83.1577786232636,
  83.49493970387756,
  84.13081193671756,
  86.8566198905369,
  79.1652565260396],
 'BMI': [29.027806400843886,
  27.26397329721053,
  28.464810185118107,
  29.37512948922535,
  27.408522750891088],
 'InitialHospDays': [7.2,
  9.346733668341708,
  8.707142857142857,
  9.656050955414013,
  7.710280373831775],
 'TotalHospDays': [14.225296442687746,
  19.625615763546797,
  15.485915492957746,
  18.888198757763973,
  14.102803738317757],
 'NYHA': [3.2904564315352696,
  3.4381443298969074,
  3.3970588235294117,
  3.414473684210526,
  3.2666666666666666],
 'MLHFS': [76.66666666666667,
  72.75384615384615,
  72.96428571428571,
  71.21019108280255,
  72.74766355140187],
 'AF': [0.0,
  0.7241379310344828,
  0.0,
  0.6459627329192547,
  0.028037383177570093],
 'AlchE': [0.21686746987951808,
  0.059113300492610835,
  0.056338028169014086,
  0.16149068322981366,
  0.2616822429906542],
 'ANGP': [0.0,
  0.6600985221674877,
  0.7253521126760564,
  0.024844720496894408,
  0.38317757009345793],
 'AOREG': [0.040160642570281124,
  0.03940886699507389,
  0.04225352112676056,
  0.07453416149068323,
  0.056074766355140186],
 'AOST': [0.008032128514056224,
  0.06896551724137931,
  0.0,
  0.037267080745341616,
  0.037383177570093455],
 'ARRH': [0.01606425702811245,
  0.9901477832512315,
  0.0,
  0.9937888198757764,
  0.06542056074766354],
 'CABG': [0.0,
  0.645320197044335,
  0.6338028169014085,
  0.012422360248447204,
  0.2523364485981308],
 'CARREST': [0.008032128514056224,
  0.18719211822660098,
  0.0,
  0.14906832298136646,
  0.0],
 'COPD': [0.11244979919678715,
  0.24630541871921183,
  0.19718309859154928,
  0.09937888198757763,
  0.205607476635514],
 'CVD': [0.040160642570281124,
  0.18719211822660098,
  0.19718309859154928,
  0.09937888198757763,
  0.1308411214953271],
 'CYTOE': [0.01606425702811245,
  0.009852216748768473,
  0.0,
  0.037267080745341616,
  0.0],
 'DEPR': [0.17670682730923695,
  0.2413793103448276,
  0.2535211267605634,
  0.17391304347826086,
  0.08411214953271028],
 'DIAB': [0.20883534136546184,
  0.4039408866995074,
  0.5492957746478874,
  0.2732919254658385,
  0.22429906542056074],
 'FAMILE': [0.12048192771084337,
  0.019704433497536946,
  0.09859154929577464,
  0.09937888198757763,
  0.24299065420560748],
 'GOUT': [0.07630522088353414,
  0.2955665024630542,
  0.18309859154929578,
  0.20496894409937888,
  0.16822429906542055],
 'HEPT': [0.11244979919678715,
  0.12807881773399016,
  0.04225352112676056,
  0.049689440993788817,
  0.056074766355140186],
 'HTN': [0.46586345381526106,
  0.49261083743842365,
  0.5,
  0.4472049689440994,
  0.4392523364485981],
 'HYPERE': [0.2248995983935743,
  0.10344827586206896,
  0.18309859154929578,
  0.2608695652173913,
  0.308411214953271],
 'HTRANS': [2.3238866396761133,
  2.054726368159204,
  2.0869565217391304,
  2.122448979591837,
  2.2427184466019416],
 'ICD': [0.10040160642570281,
  0.49261083743842365,
  0.09859154929577464,
  0.5031055900621118,
  0.09345794392523364],
 'IDIOPE': [0.642570281124498,
  0.059113300492610835,
  0.028169014084507043,
  0.5714285714285714,
  0.29906542056074764],
 'ISCHD': [0.0, 1.0, 1.0, 0.13664596273291926, 0.8878504672897196],
 'ISCHEME': [0.008032128514056224,
  0.9802955665024631,
  1.0,
  0.11180124223602485,
  0.6074766355140186],
 'MALIG': [0.0321285140562249,
  0.059113300492610835,
  0.11267605633802817,
  0.09937888198757763,
  0.07476635514018691],
 'MI': [0.0,
  0.8866995073891626,
  0.9577464788732394,
  0.08695652173913043,
  0.4485981308411215],
 'MTST': [0.008032128514056224,
  0.019704433497536946,
  0.0,
  0.012422360248447204,
  0.018691588785046728],
 'OTHUNE': [0.3172690763052209,
  0.054187192118226604,
  0.1267605633802817,
  0.2919254658385093,
  0.308411214953271],
 'PACE': [0.11646586345381527,
  0.4433497536945813,
  0.19718309859154928,
  0.30434782608695654,
  0.07476635514018691],
 'PERIPAE': [0.0642570281124498, 0.0, 0.0, 0.0, 0.0],
 'PMRG': [0.040160642570281124,
  0.10837438423645321,
  0.04225352112676056,
  0.2484472049689441,
  0.11214953271028037],
 'PTCI': [0.0,
  0.4630541871921182,
  0.6549295774647887,
  0.012422360248447204,
  0.06542056074766354],
 'PTREG': [0.024096385542168676,
  0.04926108374384237,
  0.0,
  0.11180124223602485,
  0.037383177570093455],
 'PVD': [0.01606425702811245,
  0.19704433497536947,
  0.29577464788732394,
  0.062111801242236024,
  0.11214953271028037],
 'RENALI': [0.0,
  0.10582010582010581,
  0.029411764705882353,
  0.024844720496894408,
  0.05714285714285714],
 'SMOKING': [1.538152610441767,
  2.2786069651741294,
  2.1357142857142857,
  1.4585987261146496,
  1.7289719626168225],
 'STERD': [0.04819277108433735,
  0.03940886699507389,
  0.04225352112676056,
  0.062111801242236024,
  0.056074766355140186],
 'STROKE': [0.008032128514056224,
  0.15763546798029557,
  0.1267605633802817,
  0.09937888198757763,
  0.11214953271028037],
 'SVT': [0.0,
  0.3645320197044335,
  0.0,
  0.4472049689440994,
  0.037383177570093455],
 'TDP': [0.0, 0.0, 0.0, 0.012422360248447204, 0.0],
 'TIA': [0.0321285140562249,
  0.04926108374384237,
  0.07042253521126761,
  0.012422360248447204,
  0.056074766355140186],
 'VAHD': [0.10441767068273092,
  0.22660098522167488,
  0.08450704225352113,
  0.2857142857142857,
  0.18691588785046728],
 'VALVUE': [0.05622489959839357,
  0.06896551724137931,
  0.014084507042253521,
  0.14906832298136646,
  0.037383177570093455],
 'VF': [0.008032128514056224,
  0.10837438423645321,
  0.0,
  0.16149068322981366,
  0.0],
 'SixFtWlk': [614.8448915809524,
  484.3793604678362,
  463.239073220339,
  575.6604377235773,
  526.6697134065934],
 'VO2': [11.511666666666667,
  9.571833333333332,
  9.58415909090909,
  10.903333333333334,
  11.496060606060604],
 'ALB': [3.6194244604316546,
  3.726785714285714,
  3.616666666666667,
  3.616964285714286,
  3.6032786885245898],
 'ALT': [47.85294117647059,
  37.90983606557377,
  27.848837209302324,
  40.98245614035088,
  28.983050847457626],
 'AST': [45.173611111111114,
  37.30252100840336,
  31.42528735632184,
  38.4054054054054,
  33.698412698412696],
 'BUN': [30.950819672131146,
  42.75103092783505,
  39.74328358208955,
  34.59220779220779,
  35.26019417475728],
 'CRT': [1.3842622950819672,
  1.7487437185929648,
  1.6390225563909775,
  1.4396103896103898,
  1.5192307692307696],
 'DIAL': [0.36961538461538457,
  0.4473684210526316,
  0.36195081967213116,
  0.32524358974358974,
  0.34239130434782605],
 'HEC': [41.26342592592593,
  36.68563535911603,
  36.24285714285714,
  40.63071428571429,
  38.6381443298969],
 'HEM': [12.916666666666666,
  12.125414364640884,
  11.923846153846153,
  13.235714285714286,
  12.818556701030927],
 'PLA': [249.41611374407583,
  212.20454545454547,
  203.75877192982455,
  234.57101449275362,
  232.20860215053764],
 'POT': [4.28530612244898,
  4.217171717171717,
  4.232089552238806,
  4.214935064935064,
  4.361538461538462],
 'SOD': [135.7283950617284,
  136.02020202020202,
  135.955223880597,
  135.98701298701297,
  136.66346153846155],
 'TALB': [0.864,
  0.8503937007874016,
  0.9082352941176473,
  0.8273504273504273,
  0.7999999999999999],
 'TOTP': [7.086324786324785,
  7.107476635514018,
  7.128378378378378,
  6.980582524271845,
  6.975438596491228],
 'WBC': [8.074357798165137,
  7.962044198895028,
  7.390170940170939,
  7.733928571428572,
  7.8365625],
 'ACE': [0.8571428571428571,
  0.7389162561576355,
  0.6408450704225352,
  0.7453416149068323,
  0.8130841121495327],
 'BET': [0.6254980079681275,
  0.5763546798029556,
  0.6056338028169014,
  0.5403726708074534,
  0.5849056603773585],
 'NIT': [0.2948207171314741,
  0.5073891625615764,
  0.5,
  0.30434782608695654,
  0.44339622641509435],
 'ANGIO': [0.16996047430830039,
  0.12315270935960591,
  0.15492957746478872,
  0.16770186335403728,
  0.14953271028037382],
 'CINF': [1.0, 1.0, 1.0, 1.0, 1.0],
 'DIUR': [0.952191235059761,
  0.9655172413793104,
  0.9295774647887324,
  0.9316770186335404,
  0.9626168224299065],
 'AMR': [0.0, 0.0, 0.0, 0.0, 0.0],
 'ATE': [26.625, 45.625, 31.25, 20.833333333333332, 25.0],
 'BEN': [31.022727272727273, 31.875, 21.5625, 31.666666666666668, 23.25],
 'BIS': [0.0, 2.5, 0.0, 0.0, 0.0],
 'BUM': [4.6875, 24.4, 6.833333333333333, 12.181818181818182, 8.5],
 'CAND': [8.0, 16.0, 20.5, 26.0, 32.0],
 'CAP': [105.845,
  67.05163043478261,
  79.46428571428571,
  100.2840909090909,
  130.35714285714286],
 'CAR': [19.151960784313726,
  23.093220338983052,
  20.536931818181817,
  23.445833333333333,
  21.274305555555557],
 'DIGX': [0.19323979591836735,
  0.1429878787878788,
  1.3268691588785047,
  0.3787,
  0.16666666666666666],
 'DIN': [72.5, 68.93939393939394, 69.42857142857143, 72.5, 84.70588235294117],
 'DOB': [3.4166666666666665,
  4.085714285714286,
  2.625,
  3.15625,
  2.9285714285714284],
 'DOP': [3.0, 2.1955555555555555, 2.0, 3.0, 0.0],
 'ENA': [21.96969696969697,
  11.694444444444445,
  23.94736842105263,
  21.01851851851852,
  14.0],
 'ETH': [0.0, 0.0, 0.0, 0.0, 0.0],
 'FOS': [40.0, 20.0, 0.0, 16.666666666666668, 29.0],
 'FUR': [192.87557603686636,
  202.57309941520467,
  193.7391304347826,
  206.376,
  155.36458333333334],
 'LIS': [25.192307692307693,
  19.6875,
  21.833333333333332,
  22.1875,
  25.333333333333332],
 'LOSA': [67.5, 56.25, 82.3076923076923, 57.8125, 53.333333333333336],
 'MET': [64.54054054054055,
  55.96590909090909,
  61.328125,
  57.06521739130435,
  68.63636363636364],
 'MIL': [0.3, 0.34500000000000003, 0.375, 0.7071428571428572, 0.275],
 'MON': [105.0,
  49.255319148936174,
  63.333333333333336,
  52.04545454545455,
  80.43478260869566],
 'NAT': [26.57571428571428,
  0.40700000000000003,
  1.056,
  0.5074999999999998,
  0.01],
 'NIG': [50.0, 6.35, 0.0, 5.0, 0.0],
 'NIP': [0.2, 0.0, 0.0, 0.0, 0.0],
 'OTHAA': [192.85714285714286, 151.0, 50.0, 162.5, 50.0],
 'OTHA': [132.0, 156.66666666666666, 0.0, 120.0, 0.0],
 'OTHB': [70.53571428571429, 41.25, 50.0, 12.5, 62.5],
 'OTHD': [0.0, 0.0, 40.0, 0.0, 0.0],
 'PRO': [0.0, 0.0, 0.0, 0.0, 60.0],
 'QUI': [22.5, 11.25, 15.0, 19.545454545454547, 31.071428571428573],
 'RAM': [10.972222222222221,
  7.361111111111111,
  11.964285714285714,
  13.0,
  13.25],
 'TOP': [11.1,
  18.48965517241379,
  19.32,
  18.962500000000002,
  12.225000000000001],
 'TOR': [199.0909090909091, 155.0, 102.17391304347827, 148.4, 206.0],
 'TRA': [0.0, 0.0, 0.0, 0.0, 0.0],
 'VALSA': [200.0,
  133.33333333333334,
  106.66666666666667,
  146.66666666666666,
  186.66666666666666],
 'EjF': [18.012345679012345,
  20.261306532663315,
  20.607142857142858,
  18.70186335403727,
  20.02970297029703],
 'BPDIAS': [66.38333333333334,
  62.38,
  62.419117647058826,
  62.920529801324506,
  65.99065420560747],
 'BPSYS': [106.20833333333333,
  101.14,
  104.81617647058823,
  100.34437086092716,
  106.45794392523365],
 'HR': [86.1375,
  78.78282828282828,
  76.82352941176471,
  78.9271523178808,
  80.59813084112149],
 'PV': [-11.343419192071822,
  3.3861266169135797,
  13.35442782514737,
  -6.643097938272729,
  2.2448401728202247],
 'MAP': [150.46388888941667,
  142.72666666335002,
  146.42892156617646,
  142.2913907265563,
  150.45171339439253],
 'PP': [39.825,
  38.76,
  42.39705882352941,
  37.42384105960265,
  40.467289719626166],
 'PPP': [0.37127317722916664,
  0.37807431946500003,
  0.39744399595588237,
  0.3711082680728477,
  0.3767531310093457],
 'PPRatio': [0.4850592261924686,
  0.512106856348485,
  0.5833919192148147,
  0.4923205185099338,
  0.5198026447009346],
 'cluster': [2.0, 3.0, 1.0, 0.0, 4.0],
 'Death': [0.6205533596837944,
  0.28078817733990147,
  0.43661971830985913,
  0.37888198757763975,
  0.5700934579439252],
 'Rehosp': [-0.05138339920948617,
  -0.5467980295566502,
  -0.352112676056338,
  -0.42857142857142855,
  -0.17757009345794392],
 'Readmission': [0.6837944664031621,
  0.5270935960591133,
  0.6056338028169014,
  0.6024844720496895,
  0.7757009345794392]}

#Most important features for hemo by outcome
hemoFeatureImportance = ['Age', 'EjF', ' RAP', ' MIXED', ' MPAP', ' BPSYS', ' PAD', ' CO', ' PAS', ' PAMN', ' RATHemo', ' CPI', ' RAT', ' SVR', ' PCWPMod', ' PCWPA', ' PCWPMN', ' SVRHemo', ' BPDIAS', ' MAP', ' PP', ' PPP', ' PPRatio', ' PCWP', ' CI', ' PAPP', ' HRTRT']

hemoFeatureImportanceDeath = ['Age', 'EjF', ' RAP', ' PCWPMod', ' BPSYS', ' PAMN', ' PCWP', ' CO', ' HRTRT', ' RATHemo', ' MAP', ' RAT', ' PAS', ' PAD', ' CI', ' SVRHemo', ' MIXED', ' MPAP', ' CPI', ' PCWPA', ' PCWPMN', ' BPDIAS', ' PP', ' PPP', ' PAPP', ' SVR', ' PPRatio']

hemoFeatureImportanceRehosp = ['Age', 'EjF', ' PAD', ' PCWPMN', ' MIXED', ' PP', ' PPRatio', ' RAP', ' PAMN', ' PCWP', ' MPAP', ' PAS', ' PCWPA', ' CO', ' SVRHemo', ' BPSYS', ' BPDIAS', ' MAP', ' PPP', ' PAPP', ' PCWPMod', ' RATHemo', ' CPI', ' RAT', ' CI', ' HRTRT', ' SVR']

hemoFeatureImportanceReadmission = ['Age', 'EjF', ' MIXED', ' RATHemo', ' SVR', ' RAT', ' PCWPA', ' BPSYS', ' RAP', ' PAS', ' PAD', ' PAMN', ' PCWP', ' PCWPMod', ' PCWPMN', ' CO', ' CI', ' SVRHemo', ' BPDIAS', ' HRTRT', ' MAP', ' MPAP', ' CPI', ' PP', ' PPP', ' PAPP', ' PPRatio']

allDataFeatureImportance = [' TotalHospDays', ' CRT', ' PP', ' PPRatio', ' InitialHospDays', ' SixFtWlk_M6', ' BUN', ' ACE', ' BEN', ' PPP', 'Age', ' AF', ' ARRH', ' MI', ' SixFtWlk', ' SixFtWlk_M3', ' BET', ' FUR', ' BPDIAS', ' BPSYS', ' MAP', ' Race', ' HYPERE', ' IDIOPE', ' VO2', ' VO2_M3', ' HEM', ' CINF', ' DIN', ' LIS', ' MON', ' TOR', ' VALSA', ' Wt', ' BMI', ' ANGP', ' AOREG', ' AOST', ' CARREST', ' FAMILE', ' HTN', ' ISCHEME', ' PERIPAE', ' PTCI', ' TIA', ' VAHD', ' ALB', ' TALB', ' TOTP', ' DIUR', ' MET', ' MIL', ' NAT', ' OTHB', ' TOP', ' EjF', ' CVD', ' CYTOE', ' DEPR', ' DIAB', ' GOUT', ' HEPT', ' ISCHD', ' MALIG', ' OTHUNE', ' PTREG', ' PVD', ' RENALI', ' SMOKING', ' STERD', ' SVT', ' ALT', ' AST', ' DIAL', ' POT', ' SOD', ' BUM', ' CAND', ' CAP', ' CAR', ' DIGX', ' DOB', ' DOP', ' ENA', ' LOSA', ' OTHA', ' QUI', ' HR', ' Gender', ' AlchE', ' CABG', ' COPD', ' HTRANS', ' ICD', ' MTST', ' PACE', ' PMRG', ' STROKE', ' TDP', ' VALVUE', ' VF', ' HEC', ' PLA', ' WBC', ' NIT', ' ANGIO', ' AMR', ' ATE', ' BIS', ' ETH', ' FOS', ' NIG', ' NIP', ' OTHAA', ' OTHD', ' PRO', ' RAM', ' TRA', ' PV']

allDataFeatureImportanceDeath = [' InitialHospDays', ' TotalHospDays', ' AF', ' AOREG', ' ARRH', ' HTN', ' HYPERE', ' MI', ' VAHD', ' SixFtWlk_M6', ' BUN', ' CRT', ' ACE', ' BET', ' BEN', ' FUR', ' LIS', ' BPDIAS', ' MAP', ' PP', ' PPRatio', 'Age', ' Race', ' Wt', ' BMI', ' ANGP', ' AOST', ' DIAB', ' FAMILE', ' ISCHEME', ' PTREG', ' PVD', ' SVT', ' SixFtWlk', ' SixFtWlk_M3', ' VO2', ' VO2_M3', ' HEM', ' SOD', ' TALB', ' DIUR', ' CAP', ' CAR', ' DIN', ' MET', ' MON', ' OTHB', ' TOP', ' TOR', ' VALSA', ' EjF', ' BPSYS', ' PPP', ' Gender', ' AlchE', ' CABG', ' CARREST', ' COPD', ' CVD', ' CYTOE', ' DEPR', ' GOUT', ' HEPT', ' HTRANS', ' ICD', ' IDIOPE', ' ISCHD', ' MALIG', ' MTST', ' OTHUNE', ' PACE', ' PERIPAE', ' PMRG', ' PTCI', ' RENALI', ' SMOKING', ' STERD', ' STROKE', ' TDP', ' TIA', ' VALVUE', ' VF', ' ALB', ' ALT', ' AST', ' DIAL', ' HEC', ' PLA', ' POT', ' TOTP', ' WBC', ' NIT', ' ANGIO', ' CINF', ' AMR', ' ATE', ' BIS', ' BUM', ' CAND', ' DIGX', ' DOB', ' DOP', ' ENA', ' ETH', ' FOS', ' LOSA', ' MIL', ' NAT', ' NIG', ' NIP', ' OTHAA', ' OTHA', ' OTHD', ' PRO', ' QUI', ' RAM', ' TRA', ' HR', ' PV']

allDataFeatureImportanceRehosp = [' Race', ' InitialHospDays', ' TotalHospDays', ' AF', ' ARRH', ' IDIOPE', ' MI', ' PTCI', ' SixFtWlk', ' BUN', ' CRT', ' ACE', ' BEN', ' FUR', ' MON', ' BPSYS', ' PP', ' PPP', ' PPRatio', 'Age', ' ANGP', ' AOST', ' CARREST', ' CYTOE', ' DEPR', ' FAMILE', ' GOUT', ' HEPT', ' HYPERE', ' ISCHD', ' ISCHEME', ' SMOKING', ' TIA', ' SixFtWlk_M3', ' SixFtWlk_M6', ' VO2', ' VO2_M3', ' ALB', ' HEM', ' POT', ' TALB', ' TOTP', ' BET', ' CINF', ' DIGX', ' DIN', ' LIS', ' LOSA', ' QUI', ' TOP', ' VALSA', ' HR', ' MAP', ' Gender', ' Wt', ' BMI', ' AlchE', ' AOREG', ' CABG', ' COPD', ' CVD', ' DIAB', ' HTN', ' HTRANS', ' ICD', ' MALIG', ' MTST', ' OTHUNE', ' PACE', ' PERIPAE', ' PMRG', ' PTREG', ' PVD', ' RENALI', ' STERD', ' STROKE', ' SVT', ' TDP', ' VAHD', ' VALVUE', ' VF', ' ALT', ' AST', ' DIAL', ' HEC', ' PLA', ' SOD', ' WBC', ' NIT', ' ANGIO', ' DIUR', ' AMR', ' ATE', ' BIS', ' BUM', ' CAND', ' CAP', ' CAR', ' DOB', ' DOP', ' ENA', ' ETH', ' FOS', ' MET', ' MIL', ' NAT', ' NIG', ' NIP', ' OTHAA', ' OTHA', ' OTHB', ' OTHD', ' PRO', ' RAM', ' TOR', ' TRA', ' EjF', ' BPDIAS', ' PV']

allDataFeatureImportanceReadmission = [' BMI', ' TotalHospDays', ' PERIPAE', ' BUN', ' CINF', ' DIN', ' MIL', ' NAT', ' TOR', ' PP', ' PPP', ' PPRatio', 'Age', ' IDIOPE', ' MALIG', ' OTHUNE', ' STERD', ' SixFtWlk', ' SixFtWlk_M3', ' SixFtWlk_M6', ' ALB', ' ALT', ' AST', ' CRT', ' DIAL', ' POT', ' SOD', ' TALB', ' TOTP', ' DIUR', ' BUM', ' DOP', ' ENA', ' FUR', ' MON', ' OTHA', ' OTHB', ' QUI', ' VALSA', ' EjF', ' BPDIAS', ' Gender', ' Race', ' Wt', ' InitialHospDays', ' AF', ' AlchE', ' ANGP', ' AOREG', ' AOST', ' ARRH', ' CABG', ' CARREST', ' COPD', ' CVD', ' CYTOE', ' DEPR', ' DIAB', ' FAMILE', ' GOUT', ' HEPT', ' HTN', ' HYPERE', ' HTRANS', ' ICD', ' ISCHD', ' ISCHEME', ' MI', ' MTST', ' PACE', ' PMRG', ' PTCI', ' PTREG', ' PVD', ' RENALI', ' SMOKING', ' STROKE', ' SVT', ' TDP', ' TIA', ' VAHD', ' VALVUE', ' VF', ' VO2', ' VO2_M3', ' HEC', ' HEM', ' PLA', ' WBC', ' ACE', ' BET', ' NIT', ' ANGIO', ' AMR', ' ATE', ' BEN', ' BIS', ' CAND', ' CAP', ' CAR', ' DIGX', ' DOB', ' ETH', ' FOS', ' LIS', ' LOSA', ' MET', ' NIG', ' NIP', ' OTHAA', ' OTHD', ' PRO', ' RAM', ' TOP', ' TRA', ' BPSYS', ' HR', ' PV', ' MAP']







