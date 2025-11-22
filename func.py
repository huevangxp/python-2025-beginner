data = [
    {"username": "bounsoukvang01", "age": 24, "phone": "202-555-0134", "email": "bounsoukvang01@example.com", "salary": 55000, "address": "123 Riverside St, Vientiane"},
    {"username": "chanthavong02", "age": 29, "phone": "202-555-0177", "email": "chanthavong02@example.com", "salary": 62000, "address": "45 Mekong Rd, Luang Prabang"},
    {"username": "somchai03", "age": 31, "phone": "202-555-0142", "email": "somchai03@example.com", "salary": 48000, "address": "12 Ban Phonsavang, Savannakhet"},
    {"username": "anousone04", "age": 27, "phone": "202-555-0199", "email": "anousone04@example.com", "salary": 70000, "address": "77 Lane Xang Ave, Vientiane"},
    {"username": "phoutthasone05", "age": 30, "phone": "202-555-0113", "email": "phoutthasone05@example.com", "salary": 52000, "address": "9 Donkoy Village, Vientiane"},
    {"username": "vilay06", "age": 22, "phone": "202-555-0166", "email": "vilay06@example.com", "salary": 46000, "address": "88 Chomphet District, Champasak"},
    {"username": "manivanh07", "age": 34, "phone": "202-555-0188", "email": "manivanh07@example.com", "salary": 68000, "address": "55 Sisattanak, Vientiane"},
    {"username": "somsanith08", "age": 28, "phone": "202-555-0109", "email": "somsanith08@example.com", "salary": 61000, "address": "33 Nongbone Rd, Vientiane"},
    {"username": "khampheng09", "age": 26, "phone": "202-555-0150", "email": "khampheng09@example.com", "salary": 53000, "address": "105 Ban Saphanthong, Vientiane"},
    {"username": "noy10", "age": 23, "phone": "202-555-0170", "email": "noy10@example.com", "salary": 45000, "address": "4 Thakhek Center, Khammouane"},
    {"username": "chanthaly11", "age": 32, "phone": "202-555-0192", "email": "chantaly11@example.com", "salary": 69000, "address": "22 Pakxe Town, Champasak"},
    {"username": "dalavanh12", "age": 25, "phone": "202-555-0181", "email": "dalavanh12@example.com", "salary": 54000, "address": "98 Viengkham District, Luang Prabang"},
    {"username": "sengkeo13", "age": 29, "phone": "202-555-0124", "email": "sengkeo13@example.com", "salary": 62000, "address": "66 Ban Theirn, Vientiane"},
    {"username": "khamla14", "age": 35, "phone": "202-555-0148", "email": "khamla14@example.com", "salary": 75000, "address": "13 Hongsa District, Xayaboury"},
    {"username": "oun15", "age": 21, "phone": "202-555-0186", "email": "oun15@example.com", "salary": 42000, "address": "19 Phonhong, Vientiane Province"},
    {"username": "xay16", "age": 33, "phone": "202-555-0197", "email": "xay16@example.com", "salary": 67000, "address": "109 Ban Naxay, Vientiane"},
    {"username": "phailin17", "age": 27, "phone": "202-555-0174", "email": "phailin17@example.com", "salary": 58000, "address": "76 Oudomxay Central, Oudomxay"},
    {"username": "souksavanh18", "age": 30, "phone": "202-555-0194", "email": "souksavanh18@example.com", "salary": 60000, "address": "51 Saravane Town, Saravane"},
    {"username": "mixay19", "age": 24, "phone": "202-555-0107", "email": "mixay19@example.com", "salary": 50000, "address": "7 Ban Simeuang, Vientiane"},
    {"username": "amphone20", "age": 28, "phone": "202-555-0180", "email": "amphone20@example.com", "salary": 62000, "address": "35 Lak 30, Vientiane Province"},
    {"username": "ketkeo21", "age": 31, "phone": "202-555-0116", "email": "ketkeo21@example.com", "salary": 70000, "address": "49 Ban Thongkang, Vientiane"},
    {"username": "latsamy22", "age": 22, "phone": "202-555-0160", "email": "latsamy22@example.com", "salary": 43000, "address": "12 Attapeu Center, Attapeu"},
    {"username": "phetsamay23", "age": 26, "phone": "202-555-0191", "email": "phetsamay23@example.com", "salary": 55000, "address": "242 Ban Khounta, Savannakhet"},
    {"username": "soukanya24", "age": 29, "phone": "202-555-0129", "email": "soukanya24@example.com", "salary": 61000, "address": "14 Ban Thanaleng, Vientiane"},
    {"username": "somlith25", "age": 34, "phone": "202-555-0189", "email": "somlith25@example.com", "salary": 68000, "address": "201 Xiengkhouang Center, Xiengkhouang"},
]


 

newData = min(data, key=lambda a: a["age"])
oldest_user = sorted(data, key=lambda u: u["age"], reverse=True)[0]
print(oldest_user)

# find username souksavanh18
searchUsername = 

