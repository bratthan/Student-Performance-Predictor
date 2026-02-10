import random
import pandas as pd
import numpy as np


dictArea = {"Software": 0.82, "Psychology": 0.88}

dictCourses = {
    "Software": [
        "CMSE107", "MATH163", "ENGL191", "MATH151", "PHYS101",  # 1. Dönem
        "CMSE112", "ENGL192", "MATH152", "PHYS102", "HIST280", "CMSE201",  # 2. Dönem
        "CMSE211", "CMSE231", "MATH241", "CHEM101", "CMSE222", "CMSE242",  # 3. Dönem
        "MATH373", "ENGL201", "COMM433", "CMSE321", "CMSE351", "CMSE371",  # 4. Dönem
        "COMM107", "MATH322", "CMSE322", "CMSE318", "IENG355", "CMSE473",  # 5-6. Dönem
        "CMSE423", "CMSE428", "ECON101"  # Son sınıflar
    ],
    "Psychology": ["PSYC107", "BIOL105", "MATH167", "ENGL191", "HIST280",# 1. Dönem
                   "PSYC109", "PHIL104", "SOCI101", "ENGL192", "PSYC116",# 2. Dönem
                   "PSYC216", "PSYC221", "SOCI203", "PSYC213", "ITEC105",# 3. Dönem
                   "PSYC214", "PSYC222", "PSYC282", "PSYC253", "NUTD121",# 4. Dönem
                   "PSYC331", "PSYC340", "PSYC380", "RUSS111", "PSYC342",# 5. Dönem
                   "PSYC341", "PSYC 377", "PSYC370", "PSYC382", "SBSB203",# 6. Dönem
                   "PSYC435", "PSYC447", "PHIL403", "GERM111", "PSYC448",# 7. Dönem
                   "PSYC356", "PSYC455"]
}


class RealisticStudentGenerator:
    def __init__(self, dictArea, dictCourses):
        self.dictArea = dictArea
        self.dictCourses = dictCourses

    def generateOneStudent(self, studentId):
        selectedArea = random.choice(list(self.dictArea.keys()))

        abilities = {
            "math": np.random.normal(2.3, 0.9),  # Matematik/Fizik kafası
            "code": np.random.normal(2.4, 1.1),  # Algoritma kafası (daha değişken)
            "verbal": np.random.normal(2.6, 0.7)  # Sözel
        }

        studentDict = {"Id: ": studentId, "Area: ": selectedArea}
        past_grades = {}  #

        for course in self.dictCourses[selectedArea]:
            if any(x in course for x in ["MATH", "PHYS", "CHEM", "STAT", "ECON"]):
                base_val = abilities["math"]
            elif any(x in course for x in ["CMSE", "COMP", "ITEC"]):
                base_val = abilities["code"]
            elif any(x in course for x in ["ENGL", "HIST", "COMM", "SOC", "PSYC", "IENG"]):
                base_val = abilities["verbal"]
            else:
                base_val = (abilities["math"] + abilities["code"]) / 2

            difficulty = 0
            if "10" in course or "11" in course: difficulty = 0.4
            if "2" in course: difficulty = -0.3


            chain_effect = 0
            if course == "CMSE112" and "CMSE107" in past_grades:
                if past_grades["CMSE107"] < 1.8:
                    chain_effect = -0.4  # Temel yoksa çakılır
                elif past_grades["CMSE107"] > 3.5:
                    chain_effect = 0.2  # Temel sağlamsa uçar

            if course == "MATH152" and "MATH151" in past_grades:
                chain_effect = (past_grades["MATH151"] - 2.0) * 0.4

            note = base_val + difficulty + chain_effect + np.random.normal(0, 0.5)

            if np.random.random() < 0.04:
                note -= 2.0

            note = np.clip(note, 0.0, 4.0)
            final_grade = round(note, 2)

            studentDict[course] = final_grade
            past_grades[course] = final_grade

        return studentDict

    def generateManyStudents(self, count):
        allStudents = []
        for i in range(count):
            student = self.generateOneStudent(i)
            allStudents.append(student)
        return allStudents


print("Students are generating...")
gen = RealisticStudentGenerator(dictArea, dictCourses)
dataList = gen.generateManyStudents(5000)
df = pd.DataFrame(dataList)
df.to_csv("realistic_Students.csv", index=False)
print("Data set has just saved: realistic_Students.csv")
