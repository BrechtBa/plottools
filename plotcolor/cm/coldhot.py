
from matplotlib.colors import ListedColormap
from numpy import nan, inf

# Used to reconstruct the colormap in viscm
parameters = {'xp': [-5.1014704335016461, 33.527001788720582, 36.565196233164983],
              'yp': [-25.78125, -12.326388888888886, 22.395833333333314],
              'min_Jp': 25.3879941435,
              'max_Jp': 54.6875}

cm_data = [[ 0.08766493, 0.20496868, 0.5005953 ],
           [ 0.09569416, 0.20542743, 0.49950499],
           [ 0.10318865, 0.20588266, 0.49844233],
           [ 0.11023909, 0.20633444, 0.49740685],
           [ 0.11691375, 0.20678281, 0.49639808],
           [ 0.12326553, 0.20722781, 0.49541559],
           [ 0.12933636, 0.20766947, 0.49445892],
           [ 0.13516231, 0.20810748, 0.49352676],
           [ 0.14076898, 0.20854219, 0.49261957],
           [ 0.1461795 , 0.20897361, 0.49173699],
           [ 0.15141351, 0.20940175, 0.49087862],
           [ 0.15648774, 0.2098266 , 0.49004405],
           [ 0.16141662, 0.21024817, 0.48923291],
           [ 0.16621341, 0.21066629, 0.48844444],
           [ 0.17088909, 0.21108092, 0.48767822],
           [ 0.17545241, 0.21149221, 0.48693433],
           [ 0.17991193, 0.21190012, 0.4862124 ],
           [ 0.1842753 , 0.21230463, 0.48551205],
           [ 0.18854936, 0.21270568, 0.48483295],
           [ 0.19274028, 0.21310323, 0.48417472],
           [ 0.19685413, 0.21349712, 0.48353676],
           [ 0.20089615, 0.21388725, 0.4829186 ],
           [ 0.20487024, 0.21427371, 0.4823203 ],
           [ 0.20878062, 0.21465645, 0.48174151],
           [ 0.21263119, 0.21503539, 0.48118188],
           [ 0.21642554, 0.21541046, 0.48064108],
           [ 0.22016699, 0.21578159, 0.48011875],
           [ 0.2238586 , 0.21614868, 0.47961455],
           [ 0.22750375, 0.21651152, 0.47912783],
           [ 0.23110491, 0.21687005, 0.47865836],
           [ 0.23466417, 0.21722429, 0.478206  ],
           [ 0.23818387, 0.21757414, 0.4777704 ],
           [ 0.24166618, 0.2179195 , 0.47735121],
           [ 0.24511317, 0.21826026, 0.47694809],
           [ 0.24852675, 0.21859632, 0.47656066],
           [ 0.25190874, 0.21892758, 0.47618858],
           [ 0.25526088, 0.21925391, 0.47583147],
           [ 0.25858519, 0.21957506, 0.47548871],
           [ 0.26188299, 0.21989099, 0.47516007],
           [ 0.26515553, 0.22020165, 0.4748453 ],
           [ 0.26840419, 0.22050692, 0.47454404],
           [ 0.2716303 , 0.22080667, 0.47425589],
           [ 0.27483511, 0.22110078, 0.47398046],
           [ 0.27801983, 0.22138912, 0.47371735],
           [ 0.28118561, 0.22167156, 0.47346616],
           [ 0.28433355, 0.22194797, 0.47322649],
           [ 0.28746468, 0.22221822, 0.47299792],
           [ 0.29058002, 0.22248218, 0.47278003],
           [ 0.29368091, 0.22273956, 0.47257214],
           [ 0.2967679 , 0.22299037, 0.47237407],
           [ 0.29984183, 0.22323449, 0.47218539],
           [ 0.30290356, 0.22347179, 0.47200565],
           [ 0.30595388, 0.22370212, 0.47183442],
           [ 0.30899358, 0.22392537, 0.47167122],
           [ 0.31202341, 0.22414138, 0.47151559],
           [ 0.31504408, 0.22435004, 0.47136706],
           [ 0.31805629, 0.2245512 , 0.47122516],
           [ 0.32106068, 0.22474474, 0.47108938],
           [ 0.32405791, 0.22493052, 0.47095925],
           [ 0.32704857, 0.22510841, 0.47083427],
           [ 0.33003326, 0.22527829, 0.47071393],
           [ 0.33301253, 0.22544003, 0.47059771],
           [ 0.33598696, 0.22559348, 0.47048508],
           [ 0.33895721, 0.22573846, 0.47037544],
           [ 0.34192357, 0.22587493, 0.47026836],
           [ 0.34488652, 0.22600278, 0.47016333],
           [ 0.34784651, 0.22612189, 0.4700598 ],
           [ 0.35080397, 0.22623214, 0.46995723],
           [ 0.35375931, 0.22633343, 0.46985508],
           [ 0.35671292, 0.22642565, 0.46975279],
           [ 0.35966518, 0.22650869, 0.46964981],
           [ 0.36261645, 0.22658246, 0.46954559],
           [ 0.36556707, 0.22664684, 0.46943955],
           [ 0.36851735, 0.22670176, 0.46933114],
           [ 0.3714676 , 0.22674711, 0.46921979],
           [ 0.37441812, 0.2267828 , 0.46910493],
           [ 0.37736916, 0.22680876, 0.46898599],
           [ 0.38032099, 0.2268249 , 0.4688624 ],
           [ 0.38327385, 0.22683114, 0.4687336 ],
           [ 0.38622796, 0.22682742, 0.46859899],
           [ 0.38918353, 0.22681365, 0.46845802],
           [ 0.39214077, 0.22678978, 0.46831012],
           [ 0.39509984, 0.22675574, 0.4681547 ],
           [ 0.39806093, 0.22671147, 0.46799121],
           [ 0.40102418, 0.22665693, 0.46781907],
           [ 0.40398974, 0.22659205, 0.46763772],
           [ 0.40695774, 0.2265168 , 0.46744659],
           [ 0.40992829, 0.22643113, 0.46724512],
           [ 0.4129015 , 0.22633501, 0.46703276],
           [ 0.41587746, 0.22622839, 0.46680896],
           [ 0.41885625, 0.22611125, 0.46657316],
           [ 0.42183796, 0.22598357, 0.46632482],
           [ 0.42482262, 0.22584531, 0.4660634 ],
           [ 0.42781031, 0.22569646, 0.46578837],
           [ 0.43080104, 0.22553701, 0.46549919],
           [ 0.43379487, 0.22536694, 0.46519535],
           [ 0.4367918 , 0.22518625, 0.46487633],
           [ 0.43979185, 0.22499492, 0.46454162],
           [ 0.44279503, 0.22479296, 0.46419071],
           [ 0.44580132, 0.22458037, 0.46382312],
           [ 0.44881072, 0.22435716, 0.46343835],
           [ 0.4518232 , 0.22412332, 0.46303592],
           [ 0.45483875, 0.22387888, 0.46261537],
           [ 0.45785731, 0.22362385, 0.46217622],
           [ 0.46087886, 0.22335824, 0.46171803],
           [ 0.46390334, 0.22308208, 0.46124035],
           [ 0.4669307 , 0.22279538, 0.46074274],
           [ 0.46996088, 0.22249817, 0.46022478],
           [ 0.47299381, 0.22219047, 0.45968603],
           [ 0.47602944, 0.22187232, 0.45912611],
           [ 0.47906767, 0.22154375, 0.4585446 ],
           [ 0.48210843, 0.22120478, 0.45794112],
           [ 0.48515164, 0.22085546, 0.45731529],
           [ 0.48819721, 0.22049582, 0.45666674],
           [ 0.49124505, 0.2201259 , 0.45599511],
           [ 0.49429506, 0.21974574, 0.45530005],
           [ 0.49734714, 0.21935537, 0.45458123],
           [ 0.5004012 , 0.21895485, 0.4538383 ],
           [ 0.50345712, 0.21854421, 0.45307097],
           [ 0.5065148 , 0.2181235 , 0.45227891],
           [ 0.50957422, 0.2176927 , 0.45146175],
           [ 0.51263519, 0.2172519 , 0.45061925],
           [ 0.51569759, 0.21680117, 0.44975117],
           [ 0.51876131, 0.21634056, 0.44885725],
           [ 0.52182621, 0.2158701 , 0.44793721],
           [ 0.52489218, 0.21538986, 0.44699083],
           [ 0.52795911, 0.21489988, 0.44601787],
           [ 0.53102687, 0.21440022, 0.44501809],
           [ 0.53409535, 0.2138909 , 0.44399129],
           [ 0.53716441, 0.213372  , 0.44293726],
           [ 0.54023394, 0.21284355, 0.44185581],
           [ 0.54330382, 0.21230561, 0.44074676],
           [ 0.54637391, 0.21175822, 0.43960992],
           [ 0.54944411, 0.21120143, 0.43844514],
           [ 0.55251427, 0.21063529, 0.43725226],
           [ 0.55558429, 0.21005984, 0.43603113],
           [ 0.55865404, 0.20947514, 0.43478162],
           [ 0.56172344, 0.20888116, 0.43350352],
           [ 0.56479236, 0.20827799, 0.43219675],
           [ 0.56786064, 0.20766569, 0.43086124],
           [ 0.57092815, 0.20704431, 0.42949691],
           [ 0.57399477, 0.20641389, 0.42810365],
           [ 0.57706039, 0.20577447, 0.42668138],
           [ 0.58012489, 0.20512609, 0.42523003],
           [ 0.58318814, 0.20446879, 0.42374953],
           [ 0.58625003, 0.2038026 , 0.42223982],
           [ 0.58931046, 0.20312756, 0.42070086],
           [ 0.59236929, 0.20244371, 0.41913259],
           [ 0.59542642, 0.20175107, 0.41753498],
           [ 0.59848174, 0.20104967, 0.41590801],
           [ 0.60153514, 0.20033955, 0.41425165],
           [ 0.60458655, 0.19962068, 0.4125658 ],
           [ 0.60763582, 0.19889314, 0.41085055],
           [ 0.61068284, 0.19815695, 0.40910589],
           [ 0.61372751, 0.19741215, 0.40733183],
           [ 0.61676971, 0.19665874, 0.40552837],
           [ 0.61980935, 0.19589675, 0.40369554],
           [ 0.62284634, 0.19512619, 0.40183334],
           [ 0.62588056, 0.19434707, 0.39994182],
           [ 0.62891193, 0.19355942, 0.39802099],
           [ 0.63194036, 0.19276323, 0.39607089],
           [ 0.63496574, 0.19195852, 0.39409156],
           [ 0.63798799, 0.19114529, 0.39208305],
           [ 0.64100702, 0.19032353, 0.39004539],
           [ 0.64402275, 0.18949327, 0.38797864],
           [ 0.64703507, 0.18865449, 0.38588286],
           [ 0.65004391, 0.1878072 , 0.38375812],
           [ 0.65304918, 0.18695139, 0.38160447],
           [ 0.65605081, 0.18608705, 0.37942196],
           [ 0.65904871, 0.18521417, 0.37721067],
           [ 0.66204282, 0.18433274, 0.37497066],
           [ 0.66503305, 0.18344274, 0.37270198],
           [ 0.66801933, 0.18254415, 0.37040472],
           [ 0.67100159, 0.18163694, 0.36807893],
           [ 0.67397977, 0.1807211 , 0.36572467],
           [ 0.67695379, 0.1797966 , 0.36334204],
           [ 0.67992356, 0.17886345, 0.36093115],
           [ 0.68288904, 0.17792158, 0.358492  ],
           [ 0.68585017, 0.17697095, 0.35602467],
           [ 0.6888069 , 0.17601152, 0.35352921],
           [ 0.69175916, 0.17504326, 0.35100569],
           [ 0.6947069 , 0.17406611, 0.34845415],
           [ 0.69765007, 0.17308003, 0.34587466],
           [ 0.70058861, 0.17208496, 0.34326725],
           [ 0.70352247, 0.17108085, 0.34063198],
           [ 0.70645161, 0.17006763, 0.33796888],
           [ 0.70937597, 0.16904526, 0.33527799],
           [ 0.71229552, 0.16801365, 0.33255933],
           [ 0.7152102 , 0.16697275, 0.32981295],
           [ 0.71811992, 0.16592256, 0.32703899],
           [ 0.72102469, 0.16486293, 0.32423733],
           [ 0.72392449, 0.16379376, 0.32140795],
           [ 0.72681926, 0.16271498, 0.31855085],
           [ 0.72970898, 0.16162649, 0.315666  ],
           [ 0.73259362, 0.1605282 , 0.31275337],
           [ 0.73547313, 0.15942   , 0.30981293],
           [ 0.73834751, 0.15830179, 0.3068446 ],
           [ 0.7412167 , 0.15717346, 0.30384832],
           [ 0.7440807 , 0.15603489, 0.30082401],
           [ 0.74693947, 0.15488597, 0.29777157],
           [ 0.74979299, 0.15372656, 0.29469087],
           [ 0.75264124, 0.15255654, 0.29158178],
           [ 0.7554842 , 0.15137576, 0.28844414],
           [ 0.75832185, 0.15018409, 0.28527781],
           [ 0.76115409, 0.14898151, 0.28208278],
           [ 0.76398099, 0.14776772, 0.27885861],
           [ 0.76680253, 0.14654256, 0.27560507],
           [ 0.7696187 , 0.14530586, 0.27232186],
           [ 0.77242949, 0.14405744, 0.26900869],
           [ 0.77523488, 0.1427971 , 0.26566522],
           [ 0.77803487, 0.14152466, 0.26229107],
           [ 0.78082946, 0.1402399 , 0.25888583],
           [ 0.78361862, 0.1389426 , 0.25544905],
           [ 0.78640236, 0.13763255, 0.25198023],
           [ 0.78918068, 0.1363095 , 0.24847884],
           [ 0.79195357, 0.13497321, 0.24494429],
           [ 0.79472103, 0.13362341, 0.24137591],
           [ 0.79748306, 0.13225984, 0.23777301],
           [ 0.80023966, 0.13088221, 0.23413481],
           [ 0.80299083, 0.12949021, 0.23046046],
           [ 0.80573658, 0.12808354, 0.22674905],
           [ 0.8084769 , 0.12666186, 0.22299956],
           [ 0.81121181, 0.12522484, 0.21921089],
           [ 0.81394131, 0.12377209, 0.21538184],
           [ 0.8166654 , 0.12230325, 0.21151108],
           [ 0.8193841 , 0.1208179 , 0.20759718],
           [ 0.82209741, 0.11931562, 0.20363855],
           [ 0.82480531, 0.11779605, 0.1996336 ],
           [ 0.82750784, 0.11625866, 0.19558031],
           [ 0.83020501, 0.1147029 , 0.19147654],
           [ 0.83289685, 0.11312826, 0.18731997],
           [ 0.83558335, 0.11153417, 0.18310804],
           [ 0.83826454, 0.10992004, 0.17883792],
           [ 0.84094044, 0.10828523, 0.17450645],
           [ 0.84361105, 0.10662908, 0.17011014],
           [ 0.84627639, 0.10495087, 0.16564507],
           [ 0.84893648, 0.10324984, 0.16110686],
           [ 0.85159134, 0.10152518, 0.15649059],
           [ 0.85424099, 0.09977602, 0.1517907 ],
           [ 0.85688544, 0.09800144, 0.14700088],
           [ 0.85952471, 0.09620045, 0.14211395],
           [ 0.86215883, 0.09437197, 0.13712167],
           [ 0.86478781, 0.09251486, 0.13201454],
           [ 0.86741167, 0.09062789, 0.12678153],
           [ 0.87003044, 0.08870972, 0.12140973],
           [ 0.87264415, 0.0867589 , 0.11588389],
           [ 0.8752528 , 0.08477388, 0.1101858 ],
           [ 0.87785643, 0.08275293, 0.1042935 ],
           [ 0.88045505, 0.08069421, 0.0981801 ],
           [ 0.8830487 , 0.07859568, 0.09181218],
           [ 0.88563739, 0.07645512, 0.0851474 ],
           [ 0.88822115, 0.07427006, 0.0781309 ],
           [ 0.89080001, 0.07203779, 0.07068959],
           [ 0.89337398, 0.06975531, 0.06272268],
           [ 0.89594311, 0.06741927, 0.05408478],
           [ 0.8985074 , 0.06502592, 0.04455319]]

coldhot = ListedColormap(cm_data, name=__file__)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    try:
        from viscm import viscm
        viscm(coldhot)
    except ImportError:
        print("viscm not found, falling back on simple display")
        plt.imshow(np.linspace(0, 100, 256)[None, :], aspect='auto',
                   cmap=coldhot)
    plt.show()
