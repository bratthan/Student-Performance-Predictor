#  Student Performance Predictor & Academic Digital Twin

An advanced **Data Science** pipeline designed to simulate, analyze, and forecast academic performance. This project evolves from a simple GPA calculator into a sophisticated **Academic Digital Twin** using Monte Carlo simulations and Machine Learning.

---

##  Tech Stack
* **Language:** Python 3.12
* **Data Handling:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Linear Regression)
* **Visualization:** Matplotlib, Seaborn
* **Statistical Modeling:** SciPy (Normal Distribution, Z-Score Analysis)

---

##  Project Phases

### Phase 1: Deterministic GPA Engine & Simulation
* **Core Logic:** Developed a robust parser for university transcripts (CSV).
* **Universal Adapter:** Built a layer to handle both real transcripts and synthetic datasets.
* **Situation Analysis:** Implemented a "What-if" mode to see how specific course grades impact the overall CGPA.

---

### Phase 2: Realistic Student Generator
* **Stochastic Synthesis:** Generated a population of **5,000+ students** with randomized but realistic ability profiles.
* **Multi-Dimensional Abilities:** Divided student talent into three categories: **Math, Code, and Verbal**.
* **Complexity Layers:** Integrated "Chain Effects" (prerequisites like MATH151 influencing MATH152) and "Academic Shocks" (random failure risks).


---

### Phase 3: Population Analytics
* **EDA (Exploratory Data Analysis):** Analyzed the university's "Bell Curve" distribution using Seaborn.
* **Comparative Insights:** Used Box Plots to observe the difficulty gap between the Software Engineering and Psychology departments.

---

### Phase 4: Machine Learning (Predictive Modeling)
* **Algorithm:** Multiple Linear Regression.
* **Goal:** Predicting the outcome of senior-level courses (e.g., CMSE423) based on 30+ prior course variables.
* **Performance Report:**
    * **Sample Size:** 2488 Students
    * **Success Rate (R2 Score):** %77.53
    * **Mean Squared Error (MSE):** 0.2527
* **Insight:** The model captures the underlying logic of academic success with high reliability.

$$y = \beta_0 + \beta_1x_1 + \beta_2x_2 + \dots + \beta_nx_n + \epsilon$$



---

### Phase 5: Monte Carlo & Digital Twin Risk Engine
* **Digital Twin:** Constructs a virtual replica of a student's academic DNA using **Momentum** (trend analysis) and **Inferred Abilities**.
* **Probabilistic Forecasting:** Runs **10,000 simulations** to create a probability distribution of future outcomes.
* **The Verdict:** Provides a **90% Confidence Zone**, offering a professional-grade risk assessment instead of a single-point prediction.


---

##  Key Philosophical Features
1. **Academic Momentum:** The engine detects if a student is on an "upward trend" and rewards progress in its forecasts.
2. **Chain Effect Logic:** Prerequisite success is mathematically tied to advanced course potential.
3. **Inconsistency Detection:** By calculating student-specific volatility, the engine identifies "unpredictable" academic paths.

---
*Developed by **bratthan** - Bridging the gap between raw data and academic success.*