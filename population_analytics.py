import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("realistic_students.csv")
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

def calculate_cgpa(row):
    total_ch = 0
    total_cr = 0
    for course, grade in row.items():
        if course in creditMap and pd.notnull(grade):
            total_ch += grade * creditMap[course]
            total_cr += creditMap[course]
    return total_ch / total_cr if total_cr > 0 else 0

df['CGPA'] = df.apply(calculate_cgpa, axis=1)

plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")

plt.subplot(1, 2, 1)
sns.histplot(df['CGPA'], kde=True, color="skyblue", bins=50)
plt.title('University-Wide CGPA Distribution')
plt.axvline(df['CGPA'].mean(), color='red', linestyle='--', label=f'Mean: {df["CGPA"].mean():.2f}')
plt.legend()

plt.subplot(1, 2, 2)
sns.boxplot(x='Area: ', y='CGPA', data=df, )
plt.title('Performance by Department')
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('population_analysis.png')
print("Analiz tamamlandı: population_analysis.png oluşturuldu.")