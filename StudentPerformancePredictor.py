import pandas as pd
import matplotlib
matplotlib.use('Agg')
df = pd.read_csv("Student1.csv", encoding='latin1')
dfCollumns = df[["Crs.Code", "Summary", "Cr"]].dropna()
gradeDict = {'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
             'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0,
             'D-': 0.7, 'F': 0.0}


def seperateGrade(text):
    for not_letter, puan in gradeDict.items():
        if text.endswith(" " + not_letter):
            return puan
    return None

dfCollumns["Puan"] = dfCollumns["Summary"].apply(seperateGrade)
dfCollumns["Cr"] = pd.to_numeric(dfCollumns["Cr"], errors='coerce')
dfCollumns["Ch"] = dfCollumns["Cr"] * dfCollumns["Puan"]
dfCollumns = dfCollumns.dropna()

print(dfCollumns)
print("Total CR:", dfCollumns["Cr"].sum())
print("Total CH:", dfCollumns["Ch"].sum())
print("Total CGPA:", dfCollumns["Ch"].sum() / dfCollumns["Cr"].sum())

#Simulation
dfSimule = dfCollumns.copy()
#dfSimule.loc[dfSimule['Crs.Code'] == 'PSYC370', 'Summary'] = "PSYC370 B"
dfSimule.loc[dfSimule['Crs.Code'] == 'CMSE423', 'Summary'] = "CMSE423 D+"
#dfSimule.loc[dfSimule['Crs.Code'] == 'AE01', 'Summary'] = "CMSE428 D+"


dfSimule["Grade"] = dfSimule["Summary"].apply(seperateGrade)
dfSimule["Cr"] = pd.to_numeric(dfSimule["Cr"], errors='coerce')
dfSimule["Ch"] = dfSimule["Cr"] * dfSimule["Grade"]
dfSimule = dfSimule.dropna()
print(dfSimule)
print("Total NEW CR:", dfSimule["Cr"].sum())
print("Total NEW CH:", dfSimule["Ch"].sum())
print("Total NEW CGPA:", dfSimule["Ch"].sum() / dfSimule["Cr"].sum())
print("Total OLD CGPA:", dfCollumns["Ch"].sum() / dfCollumns["Cr"].sum())  #Simulation End

compare_df = pd.merge(
    dfCollumns[['Crs.Code', 'Summary', 'Puan', 'Ch']],
    dfSimule[['Crs.Code', 'Summary', 'Puan', 'Ch']],
    on='Crs.Code',
    suffixes=('Old', 'New')
)

degisenler = compare_df[compare_df['SummaryOld'] != compare_df['SummaryNew']].copy()

degisenler['GradeChange'] = degisenler['PuanNew'] - degisenler['PuanOld']
degisenler['ChChange'] = degisenler['ChNew'] - degisenler['ChOld']

print("\n                               New CGPA")
print(degisenler[['Crs.Code', 'SummaryOld', 'SummaryNew', 'ChOld', 'ChNew', 'ChChange']])

oldCgpa = dfCollumns["Ch"].sum() / dfCollumns["Cr"].sum()
newCgpa = dfSimule["Ch"].sum() / dfSimule["Cr"].sum()

print(f"\nGeneral Situation:")
print(f"Old CGPA: {oldCgpa:.2f}")
print(f"New CGPA: {newCgpa:.2f}")
print(f"Difference: {newCgpa - oldCgpa:+.4f}")

import matplotlib.pyplot as plt

status = [f'Current {oldCgpa: .2f}', f'Simulation {newCgpa: .2f}']
values = [dfCollumns["Ch"].sum() / dfCollumns["Cr"].sum(),
            dfSimule["Ch"].sum() / dfSimule["Cr"].sum()]

plt.figure(figsize=(10, 6))
bars = plt.bar(status, values, color=['darkred', 'skyblue'])

plt.axhline(y=2.0, color='red', linestyle='--', label='Critical Point (2.00)')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.001, round(yval, 4), ha='center', va='bottom')

plt.ylim(1.00, 4.00)
plt.title('Situation: Current vs. Simulation')
plt.ylabel('CGPA')
plt.legend()
plt.savefig('analysisGPA.png')
print("Graph 'analysisGPA.png' saved.")