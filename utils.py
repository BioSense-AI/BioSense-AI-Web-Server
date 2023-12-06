import json
import time
import Adafruit_ADS1x15
import wiringpi
ecg_list = ['13342', '13307', '13353', '13391', '13414', '13441', '13471', '13487', '13514', '13497', '13512', '13525', '13521', '13578', '14077', '14459', '14501', '14338', '13815', '13317', '13437', '13438', '13451', '13505', '13502', '12873', '13159', '19631', '19526', '12159', '11879', '13138', '13017', '13013', '13083', '13162', '13288', '13396', '13506', '13634', '13786', '13950', '14149', '14509', '14834', '14830', '14566', '14094', '13082', '12812', '12838', '12855', '12892', '12972', '12951', '12985', '13020', '13079', '13056', '13108', '13150', '13166', '13192', '13224', '13257', '13257', '13302', '13328', '13312', '13337', '13390', '13369', '13388', '13395', '13455', '13411', '13426', '13464', '13507', '13498', '13498', '13506', '13546', '13866', '14411', '14563', '14399', '13995', '13440', '13443', '13448', '13468', '13457', '13460', '13015', '12709', '19000', '20581', '13132', '11223', '13293', '12949', '13041', '13104', '13127', '13228', '13361', '13433', '13572', '13753', '13876', '14036', '14245', '14684', '14961', '14710', '14545', '13819', '13036', '12783', '12851', '12828', '12900', '12945', '12937', '12994', '13060', '13051', '13071', '13136', '13164', '13193', '13192', '13260', '13251', '13259', '13308', '13335', '13321', '13357', '13366', '13356', '13369', '13437', '13440', '13434', '13460', '13444', '13472', '13458', '13531', '13514', '13520', '13590', '14182', '14462', '14473', '14231', '13695', '13327', '13362', '13383', '13374', '13405', '13409', '12401', '14193', '20407', '18532', '11576', '12175', '13125', '12996', '13041', '13104', '13176', '13253', '13356', '13490', '13585', '13765', '13979', '14096', '14357', '14819', '14927', '14581', '14414', '13407', '12897', '12805', '12866', '12849', '12905', '12962', '12982', '12991', '13037', '13092', '13095', '13091', '13149', '13150', '13197', '13214', '13233', '13221', '13287', '13329', '13339', '13343', '13376', '13361', '13390', '13422', '13452', '13441', '13471', '13488', '13507', '13502', '13542', '13557', '13548', '13850', '14368', '14526', '14426', '14074', '13473', '13364', '13412', '13447', '13455', '13416', '13413', '11842', '17119', '21589', '14535', '10756', '13302', '13033', '13073', '13081', '13146', '13224', '13366', '13439', '13611', '13752', '13929', '14116', '14381', '14821', '14975', '14615', '14391', '13320', '12826', '12795', '12868', '12911', '12938', '12943', '12992', '13018', '13025', '13117', '13093', '13108', '13141', '13171', '13204', '13188', '13257', '13248', '13257', '13268', '13329', '13328', '13355', '13364', '13412', '13422', '13408', '13445', '13456', '13446', '13464', '13492', '13505', '13485', '13676', '14244', '14477', '14442', '14137', '13565', '13344', '13403', '13443', '13451', '13449', '13364', '11863', '17127', '21648', '15015', '10517', '13206', '12999', '13050', '13059', '13179', '13246', '13300', '13390', '13530', '13630', '13787', '13997', '14171', '14539', '14897', '14829', '14556', '14133', '13087', '12791', '12818', '12869', '12911', '12906', '12971', '13032', '13037', '13055', '13092', '13107', '13139', '13154', '13186', '13156', '13188', '13229', '13221', '13256', '13280', '13316', '13313', '13366', '13388', '13360', '13390', '13414', '13433', '13439', '13464', '13491', '13497', '13536', '13519', '13564', '14061', '14493', '14530', '14315', '13853', '13367', '13386', '13429', '13456', '13444', '13458', '13056', '12602', '18835', '20764', '13425', '11080', '13307', '13033', '13080', '13084', '13139', '13232', '13347', '13418', '13585', '13716', '13890', '14077', '14258', '14663', '14980', '14801', '14522', '13828', '13019', '12794', '12851', '12873', '12886', '12936', '12946', '13052', '13031', '13061', '13101', '13148', '13146', '13164', '13209', '13176', '13191', '13232', '13250', '13287', '13303', '13323', '13327', '13341', '13382', '13414', '13389', '13437', '13428', '13445', '13468', '13504', '13463', '13495', '13501', '13589', '14149', '14452', '14497', '14231', '13741', '13336', '13378', '13365', '13405', '13403', '13452', '12646', '13794', '20301', '18368', '11297', '12557', '13077', '13039', '13073', '13130', '13164', '13294', '13437', '13583', '13733', '13875', '14064', '14196', '14613', '14957', '14790', '14513', '13799', '12985', '12778', '12844', '12865', '12909', '12957', '12926', '12975', '13036', '13052', '13063', '13059', '13103', '13138', '13191', '13216', '13223', '13253', '13293', '13307', '13328', '13317', '13373', '13396', '13445', '13477', '13465', '13447', '13441', '13497', '13477', '13498', '13502', '13536', '13530', '14061', '14445', '14539', '14344', '13848', '13353', '13378', '13406', '13408', '13443', '13464', '12577', '13909', '20254', '18632', '11574', '12300', '13105', '13029', '13102', '13136', '13209', '13301', '13401', '13531', '13654', '13800', '13997', '14143', '14491', '14911', '14882', '14552', '14207', '13134', '12810', '12840', '12847', '12889', '12915', '12993', '13005', '13035', '13048', '13107', '13103', '13137', '13166', '13179', '13197', '13229', '13233', '13279', '13279', '13306', '13332', '13359', '13361', '13399', '13383', '13405', '13412', '13424', '13419', '13411', '13473', '13455', '13497', '13466', '13752', '14324', '14511', '14450', '14061', '13448', '13353', '13351', '13389', '13394', '13429', '13316', '11938', '17667', '21438', '14214', '10684', '13307', '12997', '13056', '13086', '13164', '13249', '13341', '13415', '13567', '13730', '13893', '14116', '14356', '14755', '14978', '14653', '14420', '13482', '12901', '12810', '12819', '12885', '12938', '12966', '12940', '13023', '13054', '13102', '13096', '13169', '13202', '13196', '13204', '13247', '13254', '13265', '13269', '13338', '13343', '13332', '13365', '13367', '13374', '13399', '13460', '13455', '13468', '13507', '13534', '13492', '13530', '13528', '13594', '14148', '14490', '14495', '14231', '13750', '13360', '13399', '13424', '13439', '13455', '13437', '12273', '14850', '20968', '17608', '11046', '12678', '13057', '13054', '13099', '13127', '13213', '13292', '13414', '13487', '13661', '13817', '14039', '14165', '14541', '14913', '14860', '14547', '14057', '13102', '12814', '12851', '12911', '12913', '12947', '12969', '13014', '13048', '13030', '13096', '13123', '13126', '13199', '13196', '13237', '13225', '13321', '13264', '13262', '13281', '13384', '13372', '13371', '13389', '13431', '13435', '13441', '13518', '13517', '13524', '13561', '13537', '13547', '13544', '13921', '14427', '14516', '14411', '14029', '13408', '13401', '13426', '13438', '13434', '13481', '13356', '11906', '17297', '21618', '14679', '10587', '13301', '12981', '13054', '13068', '13163', '13213', '13310', '13415', '13565', '13713', '13863', '14034', '14208', '14610', '14932', '14803', '14561', '14004', '13066', '12762', '12828', '12860', '12879', '12936', '12953', '12993', '12982', '13025', '13061', '13091', '13118', '13166', '13157', '13183', '13211', '13191', '13264', '13257', '13316', '13356', '13333', '13395', '13418', '13392', '13438', '13463', '13422', '13424', '13454', '13468', '13502', '13512', '13521', '13536', '14053', '14426', '14511', '14302', '13846', '13344', '13403', '13416', '13420', '13389', '13429', '12825', '13065', '19446', '19864', '12457', '11583', '13176', '12999', '13076', '13096', '13135', '13238', '13305', '13434', '13635', '13732', '13877', '14075', '14346', '14729', '14989', '14710', '14490', '13624', '12975', '12788', '12820', '12908', '12896', '12923', '12949', '13009', '13042', '13029', '13080', '13099', '13105', '13143', '13155', '13144', '13179', '13235', '13199', '13238', '13258', '13303', '13310', '13356', '13382', '13366', '13408', '13426', '13424', '13413', '13460', '13443', '13494', '13515', '13530', '13654', '14245', '14514', '14494', '14156', '13555', '13433', '13432', '13442', '13448', '13507', '13313', '12129', '18293', '21100', '13581', '10996', '13340', '13052', '13110', '13140', '13187', '13276', '13365', '13481', '13634', '13760', '13908', '14073', '14358', '14771', '14976', '14688', '14470', '13517', '12884', '12796', '12842', '12874', '12933', '12914', '12984', '12985', '13049', '13064', '13063', '13107', '13113', '13163', '13184', '13230', '13229', '13258', '13277', '13290', '13297', '13339', '13326', '13374', '13383', '13416', '13396', '13401', '13421', '13466', '13465', '13482', '13497', '13508', '13529', '14067', '14454', '14511', '14293', '13831', '13341', '13393', '13399', '13402', '13421', '13389', '12549', '13832', '20193', '18620', '11626', '12280', '13106', '13024', '13087', '13076', '13141', '13282', '13422', '13489', '13650', '13828', '14027', '14153', '14566', '14893', '14831', '14568', '14141', '13110', '12788', '12837', '12865', '12857', '12932', '12951', '12982', '12986', '13040', '13056', '13087', '13086', '13143', '13174', '13196', '13228', '13247', '13273', '13297', '13312', '13341', '13318', '13359', '13366', '13386', '13377', '13402', '13426', '13437', '13473', '13515', '13500', '13527', '13529', '13808', '14362', '14523', '14443', '14039', '13428', '13381', '13418', '13404', '13398', '13468', '13199', '12270', '18500', '21014', '13540', '10994', '13288', '12978', '13066', '13074']
# with open("./ecg_dump.txt","r") as f:
#     for line in f:
#         ecg_list.append(line.split()[0].strip(","))
#     print(ecg_list)

# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115(address=0x48,busnum=0)

GAIN = 1

def get_ecg_adc_arr(rate):
    array = []
    for i in range(20):
        a0 = adc.read_adc(0,gain=GAIN)
        array.append(a0)
        time.sleep(rate)
    return json.dumps({'ecg_data': array})

def get_ecg_adc():
    return adc.read_adc(0, gain=GAIN)
    # return json.dumps({'ecg_data': array})

def get_point():
    if len(ecg_list) <= get_point.counter :
        get_point.counter = 0
    val = ecg_list[get_point.counter]
    get_point.counter += 1
    return val
get_point.counter = 0

def get_points(n):
    temp_list = []
    for i in range(n):
        temp_list.append(ecg_list[(n*get_points.counter)+i])
    print(get_points.counter)
    get_points.counter += 1
    return temp_list
get_points.counter = 0
# return json.dumps({'ecg_data': ecg_data})

def find_lead_status():
    wiringpi.wiringPiSetup()
    wiringpi.pinMode(23, 0) # sets GPIO 23 to input
    wiringpi.pinMode(25, 0) # sets GPIO 25 to input
    input1 = wiringpi.digitalRead(23)
    input2 = wiringpi.digitalRead(25)
    print(input1, input2)
    return True if (input1 == 1 and input2 == 1) else False

# for i in range(10):
#     print(find_lead_status())
#     time.sleep(2)