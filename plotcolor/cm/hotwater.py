
from matplotlib.colors import ListedColormap
from numpy import nan, inf

# Used to reconstruct the colormap in viscm
parameters = {'xp': [-2.8935958853237764, 35.280423722519373, 19.410325683303682],
              'yp': [-28.676470588235247, -17.524509803921518, 24.080882352941217],
              'min_Jp': 16.8316831683,
              'max_Jp': 71.6831683168}

cm_data = [[ 0.08168512, 0.04477401, 0.50087085],
           [ 0.08677009, 0.04967084, 0.49983979],
           [ 0.09177034, 0.0542003 , 0.4988847 ],
           [ 0.09669254, 0.05842286, 0.49800162],
           [ 0.10154255, 0.06238468, 0.49718686],
           [ 0.10632557, 0.06612194, 0.49643694],
           [ 0.11104623, 0.06966361, 0.49574861],
           [ 0.11570926, 0.07303315, 0.49511846],
           [ 0.12031961, 0.0762498 , 0.49454287],
           [ 0.12487879, 0.07933026, 0.49402023],
           [ 0.12938993, 0.08228833, 0.49354799],
           [ 0.13385592, 0.08513584, 0.49312368],
           [ 0.13827937, 0.08788296, 0.49274499],
           [ 0.14266273, 0.09053853, 0.49240974],
           [ 0.14700822, 0.09311029, 0.49211582],
           [ 0.15131815, 0.09560498, 0.49186112],
           [ 0.15559545, 0.09802835, 0.49164306],
           [ 0.15984056, 0.10038608, 0.49146073],
           [ 0.16405518, 0.10268298, 0.49131241],
           [ 0.16824087, 0.10492331, 0.49119647],
           [ 0.1723991 , 0.10711096, 0.49111132],
           [ 0.17653125, 0.10924942, 0.49105546],
           [ 0.18063861, 0.11134184, 0.49102745],
           [ 0.18472241, 0.11339112, 0.49102589],
           [ 0.18878378, 0.11539989, 0.49104946],
           [ 0.19282381, 0.11737056, 0.49109686],
           [ 0.19684375, 0.11930526, 0.4911667 ],
           [ 0.20084484, 0.12120592, 0.49125755],
           [ 0.20482742, 0.12307461, 0.4913687 ],
           [ 0.20879236, 0.12491307, 0.49149901],
           [ 0.21274049, 0.12672291, 0.49164742],
           [ 0.21667258, 0.12850562, 0.49181286],
           [ 0.22058937, 0.13026258, 0.49199432],
           [ 0.22449156, 0.13199509, 0.49219081],
           [ 0.22837982, 0.13370437, 0.49240137],
           [ 0.23225479, 0.13539154, 0.49262506],
           [ 0.23611707, 0.13705767, 0.49286097],
           [ 0.23996723, 0.13870376, 0.4931082 ],
           [ 0.24380582, 0.14033074, 0.4933659 ],
           [ 0.24763336, 0.14193951, 0.4936332 ],
           [ 0.25145033, 0.14353091, 0.49390928],
           [ 0.25525722, 0.14510571, 0.49419332],
           [ 0.25905446, 0.14666469, 0.49448454],
           [ 0.26284248, 0.14820855, 0.49478214],
           [ 0.26662169, 0.14973797, 0.49508536],
           [ 0.27039246, 0.1512536 , 0.49539346],
           [ 0.27415518, 0.15275606, 0.4957057 ],
           [ 0.27791017, 0.15424595, 0.49602134],
           [ 0.28165777, 0.15572382, 0.49633968],
           [ 0.28539829, 0.15719023, 0.49666002],
           [ 0.28913203, 0.1586457 , 0.49698167],
           [ 0.29285926, 0.16009072, 0.49730395],
           [ 0.29658026, 0.1615258 , 0.4976262 ],
           [ 0.30029527, 0.16295139, 0.49794775],
           [ 0.30400452, 0.16436796, 0.49826796],
           [ 0.30770823, 0.16577594, 0.4985862 ],
           [ 0.31140663, 0.16717576, 0.49890183],
           [ 0.31509989, 0.16856783, 0.49921424],
           [ 0.31878821, 0.16995257, 0.49952282],
           [ 0.32247176, 0.17133035, 0.49982696],
           [ 0.32615069, 0.17270158, 0.50012608],
           [ 0.32982515, 0.17406662, 0.5004196 ],
           [ 0.33349528, 0.17542583, 0.50070695],
           [ 0.3371612 , 0.17677959, 0.50098755],
           [ 0.34082304, 0.17812823, 0.50126086],
           [ 0.34448095, 0.17947209, 0.50152627],
           [ 0.34813529, 0.18081136, 0.50178297],
           [ 0.35178582, 0.18214654, 0.50203076],
           [ 0.35543264, 0.18347795, 0.50226913],
           [ 0.35907579, 0.18480592, 0.50249756],
           [ 0.36271535, 0.18613076, 0.50271556],
           [ 0.36635136, 0.18745279, 0.50292265],
           [ 0.36998387, 0.18877232, 0.50311835],
           [ 0.3736129 , 0.19008964, 0.5033022 ],
           [ 0.3772385 , 0.19140506, 0.50347373],
           [ 0.38086068, 0.19271888, 0.50363251],
           [ 0.38447964, 0.19403128, 0.50377787],
           [ 0.38809542, 0.19534254, 0.50390933],
           [ 0.3917078 , 0.19665306, 0.50402677],
           [ 0.39531676, 0.19796312, 0.50412979],
           [ 0.3989223 , 0.19927299, 0.504218  ],
           [ 0.4025244 , 0.20058295, 0.50429104],
           [ 0.40612304, 0.20189326, 0.50434852],
           [ 0.40971819, 0.20320418, 0.50439012],
           [ 0.41330997, 0.2045159 , 0.50441527],
           [ 0.41689843, 0.20582863, 0.50442356],
           [ 0.42048328, 0.20714276, 0.50441498],
           [ 0.42406449, 0.20845852, 0.50438926],
           [ 0.427642  , 0.20977615, 0.50434609],
           [ 0.43121577, 0.2110959 , 0.50428521],
           [ 0.43478575, 0.21241799, 0.50420636],
           [ 0.43835204, 0.21374257, 0.50410906],
           [ 0.44191458, 0.21506988, 0.50399309],
           [ 0.44547315, 0.2164002 , 0.50385847],
           [ 0.44902768, 0.21773377, 0.50370501],
           [ 0.45257812, 0.21907077, 0.50353251],
           [ 0.45612442, 0.22041141, 0.5033408 ],
           [ 0.45966657, 0.22175586, 0.50312962],
           [ 0.46320461, 0.22310426, 0.50289865],
           [ 0.4667383 , 0.22445687, 0.50264804],
           [ 0.47026759, 0.22581389, 0.50237767],
           [ 0.47379241, 0.22717547, 0.50208743],
           [ 0.47731271, 0.22854178, 0.50177723],
           [ 0.48082849, 0.22991296, 0.5014469 ],
           [ 0.48433971, 0.23128915, 0.5010963 ],
           [ 0.48784622, 0.23267055, 0.50072556],
           [ 0.49134797, 0.23405728, 0.50033462],
           [ 0.49484493, 0.23544948, 0.49992344],
           [ 0.49833704, 0.23684727, 0.499492  ],
           [ 0.50182428, 0.23825078, 0.49904023],
           [ 0.50530659, 0.23966011, 0.49856817],
           [ 0.5087839 , 0.24107539, 0.49807588],
           [ 0.5122562 , 0.24249671, 0.49756335],
           [ 0.51572344, 0.24392417, 0.49703061],
           [ 0.51918561, 0.24535784, 0.49647767],
           [ 0.52264262, 0.24679785, 0.49590471],
           [ 0.52609448, 0.24824424, 0.4953117 ],
           [ 0.52954118, 0.24969708, 0.49469868],
           [ 0.53298272, 0.25115643, 0.4940657 ],
           [ 0.53641907, 0.25262234, 0.49341282],
           [ 0.53985021, 0.25409488, 0.49274018],
           [ 0.54327605, 0.25557413, 0.49204806],
           [ 0.54669669, 0.25706008, 0.49133631],
           [ 0.55011213, 0.25855276, 0.490605  ],
           [ 0.55352238, 0.2600522 , 0.48985422],
           [ 0.55692747, 0.26155843, 0.48908404],
           [ 0.56032734, 0.26307148, 0.48829469],
           [ 0.56372193, 0.2645914 , 0.48748653],
           [ 0.56711139, 0.26611814, 0.48665928],
           [ 0.57049576, 0.26765172, 0.48581304],
           [ 0.57387506, 0.26919212, 0.48494789],
           [ 0.57724932, 0.27073934, 0.48406392],
           [ 0.58061859, 0.27229338, 0.48316121],
           [ 0.58398266, 0.27385432, 0.48224052],
           [ 0.5873418 , 0.27542206, 0.48130135],
           [ 0.59069605, 0.27699657, 0.48034374],
           [ 0.59404546, 0.27857785, 0.47936777],
           [ 0.59739009, 0.28016586, 0.47837353],
           [ 0.60072998, 0.28176059, 0.47736107],
           [ 0.60406519, 0.283362  , 0.47633048],
           [ 0.60739552, 0.28497017, 0.47528259],
           [ 0.61072125, 0.28658498, 0.47421679],
           [ 0.61404245, 0.2882064 , 0.47313308],
           [ 0.61735919, 0.28983439, 0.47203153],
           [ 0.62067152, 0.29146892, 0.47091217],
           [ 0.6239795 , 0.29310997, 0.46977506],
           [ 0.62728319, 0.29475749, 0.46862024],
           [ 0.63058266, 0.29641147, 0.46744775],
           [ 0.6338778 , 0.29807191, 0.46625815],
           [ 0.63716874, 0.29973876, 0.4650513 ],
           [ 0.64045563, 0.30141197, 0.46382689],
           [ 0.64373853, 0.30309149, 0.46258493],
           [ 0.64701751, 0.3047773 , 0.46132545],
           [ 0.65029261, 0.30646937, 0.46004846],
           [ 0.65356391, 0.30816767, 0.45875395],
           [ 0.65683145, 0.30987218, 0.45744193],
           [ 0.66009529, 0.31158286, 0.4561124 ],
           [ 0.66335549, 0.31329968, 0.45476536],
           [ 0.6666121 , 0.31502264, 0.45340078],
           [ 0.66986515, 0.3167517 , 0.45201873],
           [ 0.67311458, 0.31848688, 0.45061973],
           [ 0.67636058, 0.32022812, 0.44920313],
           [ 0.6796032 , 0.3219754 , 0.44776889],
           [ 0.68284249, 0.3237287 , 0.44631699],
           [ 0.68607849, 0.32548801, 0.44484737],
           [ 0.68931125, 0.32725331, 0.44336   ],
           [ 0.69254081, 0.32902459, 0.44185484],
           [ 0.69576722, 0.33080183, 0.44033182],
           [ 0.6989905 , 0.33258504, 0.43879091],
           [ 0.7022107 , 0.33437421, 0.43723203],
           [ 0.70542784, 0.33616932, 0.43565513],
           [ 0.70864197, 0.33797038, 0.43406014],
           [ 0.71185312, 0.33977738, 0.43244699],
           [ 0.71506131, 0.34159032, 0.43081561],
           [ 0.71826657, 0.3434092 , 0.42916593],
           [ 0.72146894, 0.34523403, 0.42749786],
           [ 0.72466842, 0.34706481, 0.42581132],
           [ 0.72786505, 0.34890154, 0.42410623],
           [ 0.73105885, 0.35074423, 0.42238249],
           [ 0.73424983, 0.35259288, 0.42064001],
           [ 0.73743802, 0.35444752, 0.41887868],
           [ 0.74062343, 0.35630814, 0.41709842],
           [ 0.74380607, 0.35817476, 0.41529911],
           [ 0.74698597, 0.36004739, 0.41348064],
           [ 0.75016313, 0.36192604, 0.41164291],
           [ 0.75333757, 0.36381073, 0.40978578],
           [ 0.75650929, 0.36570147, 0.40790913],
           [ 0.75967831, 0.36759828, 0.40601285],
           [ 0.76284463, 0.36950118, 0.40409679],
           [ 0.76600827, 0.37141017, 0.40216082],
           [ 0.76916923, 0.37332529, 0.40020479],
           [ 0.77232751, 0.37524653, 0.39822856],
           [ 0.77548313, 0.37717394, 0.39623196],
           [ 0.77863609, 0.37910751, 0.39421484],
           [ 0.78178633, 0.38104728, 0.39217746],
           [ 0.78493381, 0.38299328, 0.39012001],
           [ 0.78807864, 0.3849455 , 0.38804161],
           [ 0.79122082, 0.38690396, 0.38594206],
           [ 0.79436036, 0.38886869, 0.38382116],
           [ 0.79749726, 0.3908397 , 0.38167872],
           [ 0.80063153, 0.39281701, 0.37951452],
           [ 0.80376318, 0.39480064, 0.37732832],
           [ 0.80689221, 0.3967906 , 0.3751199 ],
           [ 0.81001863, 0.39878691, 0.37288901],
           [ 0.81314244, 0.40078959, 0.3706354 ],
           [ 0.81626366, 0.40279865, 0.36835878],
           [ 0.8193821 , 0.40481412, 0.36606038],
           [ 0.82249789, 0.40683601, 0.36373916],
           [ 0.8256111 , 0.40886432, 0.36139416],
           [ 0.82872175, 0.41089908, 0.35902506],
           [ 0.83182985, 0.41294028, 0.35663152],
           [ 0.83493541, 0.41498795, 0.35421318],
           [ 0.83803844, 0.41704209, 0.35176968],
           [ 0.84113896, 0.41910273, 0.3493006 ],
           [ 0.84423688, 0.42116985, 0.34680655],
           [ 0.84733213, 0.42324348, 0.34428809],
           [ 0.85042491, 0.42532362, 0.34174287],
           [ 0.85351525, 0.42741028, 0.33917044],
           [ 0.85660316, 0.42950346, 0.33657028],
           [ 0.85968867, 0.43160316, 0.33394186],
           [ 0.86277179, 0.43370941, 0.33128462],
           [ 0.86585243, 0.43582218, 0.32859947],
           [ 0.86893054, 0.43794148, 0.32588654],
           [ 0.87200635, 0.44006732, 0.32314307],
           [ 0.87507988, 0.44219971, 0.32036838],
           [ 0.87815115, 0.44433863, 0.31756174],
           [ 0.88122021, 0.4464841 , 0.3147224 ],
           [ 0.88428696, 0.4486361 , 0.31185093],
           [ 0.88735133, 0.45079461, 0.30894811],
           [ 0.89041358, 0.45295965, 0.30601019],
           [ 0.89347374, 0.45513122, 0.30303622],
           [ 0.89653184, 0.45730932, 0.3000252 ],
           [ 0.89958792, 0.45949395, 0.29697605],
           [ 0.90264176, 0.46168504, 0.29389167],
           [ 0.90569359, 0.46388263, 0.29076801],
           [ 0.90874352, 0.46608672, 0.28760283],
           [ 0.91179158, 0.46829731, 0.28439479],
           [ 0.91483783, 0.4705144 , 0.28114245],
           [ 0.91788208, 0.4727379 , 0.27784828],
           [ 0.92092449, 0.47496784, 0.27450857],
           [ 0.92396522, 0.47720425, 0.27111991],
           [ 0.92700431, 0.47944712, 0.26768048],
           [ 0.9300418 , 0.48169643, 0.26418829],
           [ 0.93307745, 0.48395207, 0.26064721],
           [ 0.93611157, 0.48621412, 0.25704973],
           [ 0.93914425, 0.48848259, 0.25339297],
           [ 0.94217553, 0.49075747, 0.24967431],
           [ 0.94520532, 0.49303868, 0.24589391],
           [ 0.94823364, 0.49532618, 0.2420502 ],
           [ 0.9512607 , 0.49762006, 0.23813578],
           [ 0.95428657, 0.4999203 , 0.2341471 ],
           [ 0.95731126, 0.50222687, 0.23008121],
           [ 0.96033459, 0.50453962, 0.22594026],
           [ 0.96335688, 0.5068587 , 0.22171273],
           [ 0.96637818, 0.5091841 , 0.21739362],
           [ 0.96939855, 0.51151581, 0.21297737]]

hotwater = ListedColormap(cm_data, name=__file__)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    try:
        from viscm import viscm
        viscm(hotwater)
    except ImportError:
        print("viscm not found, falling back on simple display")
        plt.imshow(np.linspace(0, 100, 256)[None, :], aspect='auto',
                   cmap=hotwater)
    plt.show()
