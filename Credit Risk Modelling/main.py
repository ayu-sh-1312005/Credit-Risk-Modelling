import streamlit as st

from prediction_helper import predict

st.set_page_config(page_title="Credit Risk Predictor", layout="wide")

st.title("💳 Credit Risk Prediction")

# -------- Row 1 --------
c1, c2, c3 = st.columns(3)

with c1:
    age = st.number_input("Age", 18, 100, 30)

with c2:
    income = st.number_input("Income", 0.0)

with c3:
    loan_tenure_months = st.number_input("Loan Tenure (months)", 1, 360, 12)

# -------- Row 2 --------
c1, c2, c3 = st.columns(3)

with c1:
    loan_amount = st.number_input("Loan Amount", 0.0)

with c2:
    credit_utilization_ratio = st.number_input("Credit Utilization Ratio", 0.0, 1.0, 0.3)

with c3:
    total_dpd = st.number_input("Avg Days past due", 0,step=1)

# -------- Row 3 --------
c1, c2, c3 = st.columns(3)

with c2:
    delinquent_months = st.number_input("Delinquent Months", 0, 60, 0)

with c3:
    number_of_open_accounts = st.number_input("Number of Open Accounts", 0, 20, )

# -------- Row 4 --------
c1, c2, c3 = st.columns(3)

with c1:
    residence_type = st.selectbox("Residence Type", ["Owned", "Rented"])

with c2:
    loan_purpose = st.selectbox("Loan Purpose", ["Education", "Home", "Personal"])

with c3:
    loan_type = st.selectbox("Loan Type", ["Secured", "Unsecured"])

# -------- Button --------
st.markdown("---")

if st.button("🚀 Calculate Risk"):

    input_data = {
        'age': age,
        'income': income,
        'loan_tenure_months': loan_tenure_months,
        'loan_amount': loan_amount,
        'credit_utilization_ratio': credit_utilization_ratio,
        'total_dpd': total_dpd,
        'delinquent_months': delinquent_months,
        'number_of_open_accounts': number_of_open_accounts,
        'residence_type': residence_type,
        'loan_purpose': loan_purpose,
        'loan_type': loan_type
    }
    probability,credit_score,rating=predict(input_data)

    st.write(f'Default Probability: {probability}%')
    st.write(f'Credit Score: {credit_score}')
    st.write(f'Rating: {rating}')
    st.json(input_data)