class University:
    def __init__(self, name):
        self.name = name
        self.cps = []


class Campus:
    def __init__(self, name):
        self.name = name
        self.dps = []


class Department:
    def __init__(self, name):
        self.name = name


dict_nkust = {
    "建工校區": [
        "資訊工程系",
        "化學材料與材料工程系",
        "土木工程系",
        "機械工程系",
        "電機工程系",
        "電子工程系",
        "模具工程系",
        "工業工程與管理系",
    ],
    "旗津校區": ["航運管理系", "輪機工程系", "海事資訊科技系"],
    "第一校區": [
        "電腦與通訊工程系",
        "營建工程系",
        "環境與安全衛生工程系",
        "工業設計系",
        "機電工程系",
        "應用英語系",
        "應用日語系",
        "應用德語系",
        "資訊管理系",
        "運籌管理系",
        "行銷與流通管理系",
        "金融系",
        "風險管理與保險系",
        "財務管理系",
    ],
    "楠梓校區": [
        "半導體工程系",
        "航運管理系",
        "供應鏈管理系",
        "海洋休閒管理系",
        "造船及海洋工程系",
        "電訊工程系",
        "海洋環境工程系",
        "漁業生產與管理系",
        "水產食品科學系",
        "水產養殖系",
        "海洋生物技術系",
        "商務資訊應用系",
    ],
    "燕巢校區": [
        "國際企業系",
        "金融資訊系",
        "人力資源發展系",
        "文化創意產業系",
        "企業管理系",
        "觀光管理系",
        "會計資訊系",
        "智慧商務系",
        "財政稅務系",
    ],
}
nkust = University("高雄科技大學")

for keys, value in dict_nkust.items():
    nkust.cps.append(Campus(keys))
    cpsl = len(nkust.cps)
    for departments in value:
        nkust.cps[cpsl - 1].dps.append(Department(departments))
