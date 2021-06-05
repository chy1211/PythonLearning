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


cpsname = ["建工校區", "旗津校區", "第一校區", "楠梓校區", "燕巢校區"]
dpsname = ["智商", "金資", "會資", "財稅", "觀光"]
nkust = University("高雄科技大學")
for i in cpsname:
    print(i)
    nkust.cps.append(Campus(i))
for i in dpsname:
    print(i)
    nkust.cps[4].dps.append(Department(i))
