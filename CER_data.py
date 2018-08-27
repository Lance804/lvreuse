import math

class CER_data(object):

    def __init__(self, x_data, y_data):
        self.x_data = x_data
        self.y_data = y_data


SRM_dev = CER_data(
    x_data=[34.41773, 1545.3127, 2132.38, 3531.84, 10559.523, 29919.422, 35185.902, 40778.46, 65220.6, 127653.47],
    y_data=[113.6659, 917.3229, 1204.5044, 988.12634, 2312.912, 4647.786, 4902.308, 3638.7456, 9987.446, 10120.208]
)

turbo_fed_dev = CER_data(
    x_data=[133.81903, 152.19873, 250.63344, 673.61206, 818.0472, 1705.3505, 1573.6854, 1685.9604, 3165.9941, 8381.78],
    y_data=[2641.3523, 3206.8723, 3936.8616, 5957.9663, 6881.573, 8546.317, 9678.603, 11230.634, 13780.293, 19279.154]
)

pressure_fed_dev = CER_data(
    x_data=[2.1583464, 47.369507, 76.376595, 109.647026, 118.151505, 177.21681, 209.16373],
    y_data=[216.07182, 615.2648, 758.4653, 858.8503, 921.1465, 969.70807, 1060.8213]
)

air_breathing_dev = CER_data(
    x_data=[864.0047, 1042.5288, 1483.114, 2238.1948, 3935.606, 4439.844],
    y_data=[10466.711, 10677.881, 11252.391, 11743.629, 15888.575, 17244.148]
)

liquid_prop_module_dev = CER_data(
    x_data=[181.24493, 186.71986, 216.03627, 665.61176, 923.54144, 1190.072, 4461.387, 8475.182],
    y_data=[364.00378, 293.96866, 284.26764, 492.81876, 887.24524, 763.7384, 1927.11, 2958.9045]
)

expendable_ballistic_stage_dev = CER_data(
    x_data=[1283.3704, 1538.9001, 1672.3915, 2203.5168, 3908.279, 5202.732, 10585.031, 11245.124, 11469.577, 24968.125, 27994.953, 95387.055],
    y_data=[4493.8257, 6533.529, 7391.403, 6536.97, 8766.523, 11522.142, 14489.42, 20394.78, 14710.571, 31225.203, 34644.742, 50847.312]
)

reusable_ballistic_stage_dev = CER_data(
    x_data=[29571.68, 33787.57, 36050.445, 38676.98, 44795.87, 171864.08, 405549.88, 672735.25, 999036.25],
    y_data=[46193.137, 41951.613, 43693.152, 43827.43, 52668.18, 84118.09, 103521.96, 150108.92, 162616.67]
)

winged_orbital_vehicles_dev = CER_data(
    x_data=[8774.656, 17048.535, 29383.527, 57715.66, 53788.04, 59761.344, 73537.984, 105940.79],
    y_data=[33946.78, 43995.86, 50758.94, 62728.98, 64474.727, 69394.734, 77297.64, 78831.0]
)

advanced_aircraft_dev = CER_data(
    x_data=[9958.551, 13837.7295, 17941.764, 21011.38, 29414.59, 92108.81, 90685.83, 129486.79],
    y_data=[25846.477, 26051.908, 26004.469, 27346.531, 33955.04, 40786.832, 44454.727, 48402.62]
)

flyback_booster_dev = CER_data(
    x_data=[17750.406, 33629.273, 41438.617, 185470.6],
    y_data=[32142.688, 43564.516, 49827.266, 71355.5]
)

crewed_ballistic_reentry_capsule_dev = CER_data(
    x_data=[894.0184, 1996.6698, 5391.9497],
    y_data=[7437.588, 8155.6533, 15299.015]
)

crewed_space_system = CER_data(
    x_data=[2946.6975, 4203.5815, 13247.841, 17115.299, 57443.727, 278895.28],
    y_data=[22162.35, 30283.627, 44301.105, 43414.305, 62267.27, 148017.44]
)

SRM_strap_on_prod = CER_data(
    x_data=[15.693767, 32.34515, 38.244335, 45.476242, 76.79392, 45.67809, 1081.1544, 1266.9338, 1521.7239,
            2106.906, 4180.016, 5811.58, 11174.037, 30380.219, 36560.51, 65254.32, 82293.7],
    y_data=[6.4278674, 9.921296, 10.935386, 11.882671, 13.495174, 14.835967, 37.062252, 40.165512, 38.19472,
            42.986588, 65.44362, 81.56608, 103.90032, 157.16173, 175.16621, 251.56572, 283.4309]
)

liquid_storable_prod = CER_data(
    x_data=[41.516968, 57.09724, 91.89363, 117.48607, 159.07037, 208.50084, 825.0005, 912.2837, 1027.2314, 1420.3281, 8412.832],
    y_data=[14.42016, 15.142205, 20.565947, 20.914621, 27.447914, 35.4931, 62.560764, 81.936, 78.731834, 81.65546, 231.95496]
)

liquid_cryo_prod = CER_data(
    x_data=[134.27802, 152.88782, 1574.1053, 1703.413, 3181.3308],
    y_data=[45.070126, 49.99756, 137.74219, 188.14326, 316.08774]
)

turbojet_prod = CER_data(
    x_data=[2087.8093, 1886.7289, 4277.4854],
    y_data=[135.77345, 141.02576, 218.0098]
)

storable_ballistic_stage_prod = CER_data(
    x_data=[783.68896, 899.9267, 1874.6211, 2214.1091, 3009.1702, 3948.4155, 6075.5107, 11556.278, 28017.28, 85031.984],
    y_data=[64.13001, 116.19791, 117.34558, 123.27801, 137.20741, 210.39647, 256.49707, 315.06998, 689.411, 1244.7727]
)

cryo_ballistic_stage_prod = CER_data(
    x_data=[961.1333, 1298.5214, 1470.3142, 2400.992, 8261.439, 32291.346],
    y_data=[105.42263, 147.07135, 163.87299, 233.37228, 493.2801, 1109.7167]
)

modern_turbo_fed_prod = CER_data(
    x_data=[723.2016, 6593.2046],
    y_data=[43.54339, 130.7584]
)

"""solid_booster_dev = CER_data(
    x_data=[11436.089, 31271.062, 36586.43, 39327.535, 63267.285, 86835.17],
    y_data=[3172.8008, 5036.0806, 5734.68, 5796.9756, 9284.008, 12238.791]
) #### CHECK THIS!!

solid_stage_dev = CER_data(
    x_data=[7366.4, 14626.3],
    y_data=[2772.38, 4316.98]"""

CER_data_list = [SRM_dev, turbo_fed_dev, pressure_fed_dev, air_breathing_dev, liquid_prop_module_dev,
                    expendable_ballistic_stage_dev, reusable_ballistic_stage_dev,
                    winged_orbital_vehicles_dev, advanced_aircraft_dev, flyback_booster_dev,
                    crewed_ballistic_reentry_capsule_dev, crewed_space_system, SRM_strap_on_prod,
                    liquid_storable_prod, liquid_cryo_prod, storable_ballistic_stage_prod,
                    cryo_ballistic_stage_prod, turbojet_prod]