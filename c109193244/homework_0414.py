class School:
    def __init__(self,name):
        self.name=name
        self.campus=None
class Campus:
    def __init__(self,campus):
        self.campus=campus
        self.college=None
class College:
    def __init__(self,college):
        self.college=college
        self.department=None
class Department:
    def __init__(self,department):
        self.department=department
        self.student=None
class Student:
    def __init__(self,sid,name):
        self.sid=sid
        self.name=name

a=School("NKUST")
a.campus=Campus("YanchaoCampus")
a.campus.college=College("BusinessIntelligenceSchool")
a.campus.college.department=Department("IntelligentCommerce")
a.campus.college.department.student=Student("C109193244","Huang-I Chan")