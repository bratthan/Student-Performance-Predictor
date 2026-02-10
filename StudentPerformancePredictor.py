import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Agg')


targetFile = "realistic_students.csv"  # "Student1.csv" "synthetic_Students.csv" veya olarak da değiştirilebilir
df = pd.read_csv(targetFile, encoding='latin1')

gradeDict = {'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
             'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0,
             'D-': 0.7, 'F': 0.0}

creditMap={
"CMSE107": 4, "MATH163": 3, "ENGL191": 3, "MATH151": 4, "PHYS101": 4, "CMSE100": 0, "CMSE112": 4, "ENGL192": 3, "MATH152": 4, "PHYS102": 4,
"HIST280": 2, "CMSE201": 4, "CMSE211": 4, "CMSE231": 4, "MATH241": 4, "CHEM101": 4, "CMSE222": 4, "CMSE242": 4, "MATH373": 3, "ENGL201": 3,
"COMM433": 3, "CMSE321": 4, "CMSE351": 4, "CMSE371": 4, "COMM107": 3, "MATH322": 3, "CMSE322": 4, "CMSE318": 4, "IENG355": 3, "CMSE473": 4,
"CMSE423": 4,"CMSE428": 4, "ECON101": 3,


"PSYC107": 4, "BIOL105": 3, "MATH167": 3, "ENGL191": 3, "HIST280": 2, "PSYC109": 4, "PHIL104": 3, "SOCI101": 3, "ENGL192": 3, "PSYC116": 3,
"PSYC216": 3, "PSYC221": 3, "SOCI203": 3, "PSYC213": 3, "ITEC105": 3, "PSYC214": 4, "PSYC222": 3, "PSYC282": 3, "PSYC253": 3, "NUTD121": 3,
"PSYC331": 3, "PSYC340": 3, "PSYC380": 3, "RUSS111": 3, "PSYC342": 3, "PSYC341": 3, "PSYC 377": 3, "PSYC370": 3, "PSYC382": 3, "SBSB203": 3,
"PSYC435": 3, "PSYC447": 3, "PHIL403": 3, "GERM111": 3, "PSYC448": 3, "PSYC356": 3, "PSYC455": 3
}

def seperateGrade(text):
    if not isinstance(text, str): return None
    for not_letter, puan in gradeDict.items():
        if text.endswith(" " + not_letter):
            return puan
    return None


def processGrade(value):
    if isinstance(value, (int, float, np.float64, np.int64)):
        return value
    return seperateGrade(value)


if 'Summary' in df.columns:
    dfFinal = df[["Crs.Code", "Summary", "Cr"]].copy().dropna()
    dfFinal["Puan"] = dfFinal["Summary"].apply(processGrade)
else:
    id_vars = [col for col in ['Id: ', 'Area: '] if col in df.columns]
    course_cols = [col for col in df.columns if col not in id_vars]

    valid_areas = ["Software", "Psychology"]
    dfFiltered = df[df['Area: '].isin(valid_areas)]

    if dfFiltered.empty:
        print("Uyarı: Seçili alanlarda öğrenci bulunamadı!")
        dfOneStudent = df.iloc[[0]]
    else:
        dfOneStudent = dfFiltered.iloc[[5]]
    print(dfOneStudent)
    dfFinal = dfOneStudent.melt(id_vars=id_vars, value_vars=course_cols, var_name='Crs.Code', value_name='NoteValue')
    dfFinal["Summary"] = dfFinal["Crs.Code"]
    dfFinal["Cr"] = dfFinal["Crs.Code"].map(creditMap)
    dfFinal["Puan"] = dfFinal["NoteValue"].apply(processGrade)

dfCollumns = dfFinal.dropna(subset=['Cr', 'Puan']).copy()
dfCollumns["Cr"] = pd.to_numeric(dfCollumns["Cr"])
dfCollumns["Ch"] = dfCollumns["Cr"] * dfCollumns["Puan"]
dfSimule = dfCollumns.copy()
target_course = 'CMSE423'
new_grade_letter = 'D'
if target_course in dfSimule['Crs.Code'].values:
    dfSimule.loc[dfSimule['Crs.Code'] == target_course, ' Summary'] = f"{target_course} {new_grade_letter}"
    dfSimule.loc[dfSimule['Crs.Code'] == target_course, 'Puan'] = gradeDict[new_grade_letter]
    dfSimule["Ch"] = dfSimule["Cr"] * dfSimule["Puan"]

oldCgpa = dfCollumns["Ch"].sum() / dfCollumns["Cr"].sum()
newCgpa = dfSimule["Ch"].sum() / dfSimule["Cr"].sum()
print(f"Eski CGPA: {oldCgpa:.2f}")
print(f"Yeni CGPA: {newCgpa:.2f}")
status = [f'Current {oldCgpa:.2f}', f'Simulation {newCgpa:.2f}']
values = [oldCgpa, newCgpa]
plt.figure(figsize=(5.5, 5.5))
bars = plt.bar(status, values, color=['darkred', 'skyblue'])
plt.axhline(y=2.0, color='red', linestyle='--', label='Critical Point (2.00)')
for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2, yval + 0.05, round(yval, 4),
        ha='center', va='bottom', fontweight='bold'
    )

plt.ylim(0.00, 4.00)
plt.title('Situation: Current vs. Simulation')
plt.ylabel('CGPA')
plt.legend()
plt.savefig('analysisGPA.png')
print("Graph 'analysisGPA.png' saved with detailed labels.")
