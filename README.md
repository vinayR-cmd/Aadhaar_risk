<!-- ===================== -->
<!-- 🛡️ SEVASHIELD README -->
<!-- ===================== -->

<p align="center">
  <img src="![Seva_Shield_poster](https://github.com/user-attachments/assets/facd8063-42e5-4344-abda-52e63b0f5f7d)
" alt="SevaShield Banner" width="100%"/>
</p>

<h1 align="center">🛡️ SevaShield</h1>

<p align="center">
  <b>AI-Powered Aadhaar Risk Intelligence for Inclusive Welfare</b>
</p>

<p align="center">
  🔍 Predict • 🧠 Analyze • 🏛️ Protect
</p>

---

## 🌐 Live Demo
🚀 **Web Application**  
👉 https://huggingface.co/spaces/vinay7410/Aadhaar_risk_2

📊 **Sample Input Dataset (CSV)**  
👉 https://github.com/vinayR-cmd/Seva_Shield/blob/main/aadhar_project_datasets/dummy_enrolment_monthly_1000_rows.csv

---

## 🧩 What is SevaShield?

**SevaShield** is an AI-driven decision-support system that identifies **regions at high risk of Aadhaar biometric authentication failures**, helping governments take **preventive action** before welfare exclusion occurs.

It combines **Aadhaar enrolment trends**, **biometric update behavior**, and **machine learning** to predict **future biometric risk hotspots** at a **monthly, district level**.

> 🎯 **Mission:** *Ensure that no eligible citizen loses welfare benefits due to avoidable biometric issues.*

---

## ❓ Why This Problem Matters

Many Indian government schemes rely heavily on Aadhaar-based biometric verification:

- 🏗️ **MGNREGA**
- 🌾 **Public Distribution System (PDS)**
- 👴 **Social Pensions**
- 🚜 **PM-KISAN**
- 🏥 **Healthcare & Subsidy Schemes**

### 🚨 Ground Reality
Biometric failures occur due to:
- Child growth (0–5 years)
- Manual labour & fingerprint wear
- Aging population
- Low biometric update frequency
- Infrastructure gaps in remote regions

➡️ These failures lead to **authentication denial → benefit exclusion**.

---

## 💡 Our Solution

**SevaShield works as an early-warning system**:

- 📊 Analyzes Aadhaar enrolment & update patterns
- 🔗 Correlates enrolment risk with biometric update behavior
- 🤖 Uses ML to **predict next-month biometric risk**
- 🗺️ Identifies **high-risk states & districts**
- 🏛️ Generates **policy-ready insights**

---

## 📂 Dataset Information

### 🔗 Official Source
- UIDAI Open Data Portal (Public, anonymized, non-sensitive)

### 📊 Dataset Scale
- 🧾 **Total records:** ~ **18+ lakh**
- 📁 **Data types used:**
  - Aadhaar Enrolment Data
  - Biometric Update Data
  - Demographic Update Data
- 🗓️ Time-series (daily → monthly aggregation)
- 🗺️ Granularity: State → District → Month

---

## 🧠 Feature Engineering

### 🔢 Key Ratios
**Enrolment-side**
- `child_enrolment_ratio`
- `teen_enrolment_ratio`
- `adult_enrolment_ratio`

**Biometric-side**
- `child_bio_ratio`
- `adult_bio_ratio`

### ⚠️ Risk Score Design
A composite **risk score (0–1)** is computed to represent biometric vulnerability.

> Higher score → higher likelihood of biometric authentication failure.

---

## 🤖 Machine Learning Pipeline

- **Problem Type:** Regression
- **Model Used:** RandomForestRegressor
- **Why Random Forest?**
  - Handles non-linear relationships
  - Robust to noisy policy data
  - Strong performance on tabular datasets
  - Feature importance interpretability

### 🎯 Target Variable
- `bio_risk_score` (monthly, district-level)

### 📥 Input Features
- Enrolment ratios
- Age-group distributions
- Aggregated enrolment & update counts
- Temporal features (month)

---

## 📈 Outputs & Insights

- 🗺️ State-wise biometric risk ranking
- 📍 District-level vulnerability mapping
- 📆 Future biometric update load prediction
- 📊 Downloadable prediction reports
- 🏛️ Actionable policy recommendations

---

## 🖥️ Web Application Features

- 📤 Upload monthly Aadhaar data (CSV)
- 🔽 State-wise dropdown analysis
- 📊 Interactive charts & tables
- 🚨 Highlight high-risk regions
- 📥 Download model predictions
- 🧠 AI-generated insights for decision-makers

---

## 🛠️ Tech Stack

| Layer | Tools |
|------|------|
| Language | Python |
| Data Processing | Pandas, NumPy |
| ML | Scikit-learn (Random Forest) |
| Visualization | Matplotlib, Seaborn |
| Web App | Streamlit |
| Deployment | Hugging Face Spaces |
| Version Control | Git & GitHub |

---

## 🏛️ Policy Impact

**SevaShield enables governments to:**
- Proactively deploy biometric update camps
- Improve Aadhaar infrastructure planning
- Reduce welfare exclusion
- Optimize administrative resources
- Strengthen trust in digital governance

---

## 🔮 Future Enhancements

- 📍 GIS-based heatmaps
- 🧠 SHAP-based explainability
- 🔔 Automated alerts for risk spikes
- 📊 Policymaker dashboard
- 🔁 Integration with real-time authentication failure data

---

## 📜 Disclaimer

This project is for **research and policy insight purposes only**.  
No personal or sensitive Aadhaar data is used.

---

<p align="center">
⭐ If you found this project impactful, consider starring the repo!
</p>
