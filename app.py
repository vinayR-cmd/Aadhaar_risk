import streamlit as st
import pandas as pd
import joblib
import numpy as np

# -------------------------------
# App Config
# -------------------------------
st.set_page_config(
    page_title="Aadhaar Biometric Risk Analyzer",
    page_icon="🆔",
    layout="wide"
)

st.title("🆔 Aadhaar Biometric Risk Analyzer")
st.markdown("""
Predict **biometric update risk** using Aadhaar enrolment patterns
and generate **actionable governance insights**.
""")

# -------------------------------
# Load Model
# -------------------------------
@st.cache_resource
def load_model():
    return joblib.load("best_model.pkl")

model = load_model()

# -------------------------------
# Upload Data
# -------------------------------
st.header("📂 Upload Monthly Enrolment Data")
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is None:
    st.info("Please upload a CSV file to proceed.")
    st.stop()

df = pd.read_csv(uploaded_file)

# -------------------------------
# Validate Columns
# -------------------------------
required_cols = [
    'state', 'district',
    'age_0_5', 'age_5_17', 'age_18_greater',
    'total_enrollments',
    'child_enrolment_ratio',
    'teen_enrolment_ratio',
    'adult_enrolment_ratio',
    'enrollment_risk_score',
    'month_num'
]

missing_cols = [c for c in required_cols if c not in df.columns]
if missing_cols:
    st.error(f"Missing required columns: {missing_cols}")
    st.stop()

# -------------------------------
# Prediction
# -------------------------------
X = df[[
    'age_0_5', 'age_5_17', 'age_18_greater',
    'total_enrollments',
    'child_enrolment_ratio',
    'teen_enrolment_ratio',
    'adult_enrolment_ratio',
    'enrollment_risk_score',
    'month_num'
]]

df['predicted_bio_risk'] = model.predict(X)

# -------------------------------
# Risk Categorization
# -------------------------------
def risk_level(x):
    if x <= 0.35:
        return "Low"
    elif x <= 0.50:
        return "Medium"
    else:
        return "High"

df['risk_level'] = df['predicted_bio_risk'].apply(risk_level)

# -------------------------------
# State-wise Summary
# -------------------------------
st.header("📊 State-wise Risk Summary")

state_summary = (
    df.groupby('state')['predicted_bio_risk']
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

st.dataframe(state_summary)

st.metric("🔴 Highest Risk State", state_summary.iloc[0]['state'])
st.metric("🟢 Lowest Risk State", state_summary.iloc[-1]['state'])

st.subheader("State-wise Average Risk")
st.bar_chart(state_summary.set_index('state'))

# -------------------------------
# State Deep Dive
# -------------------------------
st.header("🏙️ State Deep Dive")

selected_state = st.selectbox("Select State", df['state'].unique())
state_df = df[df['state'] == selected_state]

district_summary = (
    state_df.groupby('district')['predicted_bio_risk']
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

st.subheader("District-wise Risk Ranking")
st.dataframe(district_summary)
st.bar_chart(district_summary.set_index('district'))

# -------------------------------
# Recommendations
# -------------------------------
st.subheader("⚠️ Recommended Actions")

avg_state_risk = district_summary['predicted_bio_risk'].mean()

if avg_state_risk > 0.5:
    st.error("""
    🔴 High Risk:
    - Deploy biometric update camps
    - Enable OTP-based fallback authentication
    - Increase mobile enrolment units
    """)
elif avg_state_risk > 0.35:
    st.warning("""
    🟡 Medium Risk:
    - Monitor biometric trends
    - Schedule periodic update drives
    """)
else:
    st.success("""
    🟢 Low Risk:
    - Routine monitoring
    - No immediate action required
    """)

# -------------------------------
# Download Results
# -------------------------------
st.header("⬇️ Download Predictions")

csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download Prediction CSV",
    csv,
    "biometric_risk_predictions.csv",
    "text/csv"
)
