import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

df = pd.read_csv("realistic_students.csv")
course_cols = [c for c in df.columns if any(x in str(c) for x in ["MATH", "CMSE", "PHYS", "ENGL"])]

global_difficulty = df[course_cols].mean().to_dict()
global_volatility = df[course_cols].std().to_dict()


def build_digital_twin(student_id):
    student = df[df['Id: '] == student_id].iloc[0]

    abilities = {}
    for cat, keywords in {"math": ["MATH", "PHYS"], "code": ["CMSE"], "verbal": ["ENGL", "HIST"]}.items():
        cat_courses = [c for c in course_cols if any(k in c for k in keywords)]
        if cat_courses:
            student_avg = student[cat_courses].mean()
            pop_avg = df[cat_courses].mean().mean()
            abilities[cat] = student_avg / pop_avg  # 1.0 nötr, >1.0 üstün yetenek
        else:
            abilities[cat] = 1.0

    early_avg = student[[c for c in course_cols if "10" in c]].mean()
    late_avg = student[[c for c in course_cols if "3" in c]].mean()
    momentum = (late_avg / early_avg) if early_avg > 0 else 1.0

    target_course = "CMSE423"
    num_sims = 10000
    simulated_grades = []

    course_base_diff = global_difficulty.get(target_course, 2.5)

    for _ in range(num_sims):
        base = (abilities["code"] * 0.7 + abilities["math"] * 0.3) * course_base_diff * momentum

        noise = np.random.normal(0, 0.4)
        shocks = -1.5 if np.random.random() < 0.05 else 0  # Ani kriz ihtimali

        final_note = np.clip(base + noise + shocks, 0.0, 4.0)
        simulated_grades.append(final_note)

    plt.figure(figsize=(12, 6))
    sns.histplot(simulated_grades, kde=True, color="indigo", bins=40)

    expected_value = np.mean(simulated_grades)
    confidence_interval = np.percentile(simulated_grades, [5, 95])

    plt.axvline(expected_value, color='white', lw=2, label=f'Expected: {expected_value:.2f}')
    plt.fill_betweenx([0, 400], confidence_interval[0], confidence_interval[1], color='indigo', alpha=0.1, label='90% Confidence Zone')

    plt.title(
        f"DIGITAL TWIN ANALYSIS: Student {student_id}\nTarget: {target_course} | Momentum: {momentum:.2f} | Math Ability: {abilities['math']:.2f}")
    plt.legend()
    plt.savefig(f"digital_twin_{student_id}.png")

    return simulated_grades

results = build_digital_twin(student_id=150)
print("Monte Carlo Simulasyonu tamamlandı.")
