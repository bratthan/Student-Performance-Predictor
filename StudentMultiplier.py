import random
import pandas as pd
import numpy as np

dictArea={"Software": 0.82, "Psychology": 0.88,
#"Nursing": 0.92, "Architecture": 0.85, "Pharmacy": 0.87
          }
print(dict)
dictCourses={
"Software":["CMSE107","MATH163", "ENGL191","MATH151","PHYS101", "CMSE100", "CMSE112", "ENGL192", "MATH152", "PHYS102", "HIST280", "CMSE201",
"CMSE211", "CMSE231", "MATH241", "CHEM101", "CMSE222", "CMSE242", "MATH373", "ENGL201", "COMM433","CMSE321", "CMSE351", "CMSE371",
"COMM107", "MATH322", "CMSE322", "CMSE318", "IENG355", "CMSE473", "CMSE423", "CMSE428", "ECON101"],

"Psychology":["PSYC107", "BIOL105", "MATH167", "ENGL191", "HIST280", "PSYC109", "PHIL104", "SOCI101", "ENGL192", "PSYC116","PSYC216",
"PSYC221", "SOCI203", "PSYC213", "ITEC105", "PSYC214", "PSYC222", "PSYC282", "PSYC253", "NUTD121", "PSYC331", "PSYC340", "PSYC380",
"RUSS111", "PSYC342", "PSYC341", "PSYC 377", "PSYC370", "PSYC382", "SBSB203", "PSYC435", "PSYC447", "PHIL403", "GERM111", "PSYC448",
"PSYC356", "PSYC455"],
#"Nursing":["NURS263","ENGL193","BIO232","PAT196"],
#"Pharmacy":["PHAM452","CHEM101","IENG342","PHAM436"],
#"Architecture":["ARC213","PHYS101","ARCH341","MATH242"]
             }
class StudentGenerator:
    def __init__(self,dictArea,dictCourses):
        self.dictArea=dictArea
        self.dictCourses=dictCourses

    def generateOneStudent (self,studentId):

        selectedArea=random.choice(list(self.dictArea.keys()))
        areaWeight=self.dictArea[selectedArea]

        studentAbility=np.random.normal(loc=2.5,scale=0.7)

        studentDict={"Id: ": studentId,"Area: ": selectedArea}

        for course in self.dictCourses[selectedArea]:
            note=(studentAbility*areaWeight)+ np.random.uniform(-0.7,0.8)
            note= np.clip(note, 0.0, 4.0)
            studentDict[course]=round(note,2)

        return studentDict

    def generateManyStudents(self, count):
        allStudents=[]
        for i in range(count):
            student= self.generateOneStudent(i)
            allStudents.append(student)
        return allStudents

gen = StudentGenerator(dictArea, dictCourses)
dataList=gen.generateManyStudents(1000)
df=pd.DataFrame(dataList)
df.to_csv("synthetic_Students.csv", index=False)


