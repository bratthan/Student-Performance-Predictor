import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


df = pd.read_csv("realistic_students.csv")

sw_df = df[df['Area: '] == 'Software'][["CMSE107","MATH163", "ENGL191","MATH151","PHYS101", "CMSE112", "ENGL192", "MATH152", "PHYS102", "HIST280", "CMSE201",
"CMSE211", "CMSE231", "MATH241", "CHEM101", "CMSE222", "CMSE242", "MATH373", "ENGL201", "COMM433","CMSE321", "CMSE351", "CMSE371",
"COMM107", "MATH322", "CMSE322", "CMSE318", "IENG355", "CMSE473", "CMSE423", "CMSE428", "ECON101"]].dropna()

X = sw_df[["CMSE107","MATH163", "ENGL191","MATH151","PHYS101", "CMSE112", "ENGL192", "MATH152", "PHYS102", "HIST280", "CMSE201",
"CMSE211", "CMSE231", "MATH241", "CHEM101", "CMSE222", "CMSE242", "MATH373", "ENGL201", "COMM433","CMSE321", "CMSE351", "CMSE371",
"COMM107", "MATH322", "CMSE322", "CMSE318", "IENG355", "CMSE473", "CMSE428", "ECON101"]] # Girdiler
y = sw_df['CMSE423']                        # Tahmin edilecek hedef


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(len(sw_df))
print("--- MODEL PERFORMANS RAPORU ---")
print(f"Başarı Oranı (R2 Score): %{r2_score(y_test, y_pred)*100:.2f}")
print(f"Hata Payı (MSE): {mean_squared_error(y_test, y_pred):.4f}")
print("-" * 30)

plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.6, color='darkgreen', label='Tahminler')
plt.plot([y.min(), y.max()], [y.min(), y.max()], '--r', lw=2, label='Mükemmel Doğruluk Çizgisi')
plt.xlabel('Gerçekleşen Notlar')
plt.ylabel('Tahmin Edilen Notlar')
plt.title('Software Bölümü: CMSE423 Not Tahmin Başarısı')
plt.legend()
plt.savefig('ml_prediction_results.png')
print("Tahmin grafiği 'ml_prediction_results.png' olarak kaydedildi.")