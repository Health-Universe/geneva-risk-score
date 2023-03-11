import streamlit as st

def calculate_geneva_risk_score(age, gender, bmi, history_of_vte, active_cancer, recent_surgery_or_trauma, comorbidities):
    if gender == "Male":
        score = 1.19 * age
    else:
        score = 1.64 * age
    
    score += 1.88
    
    if bmi >= 25:
        score += 0.10
    elif bmi >= 30:
        score += 0.43
    
    if history_of_vte:
        score += 1.53
    
    if active_cancer:
        score += 1.60
    
    if recent_surgery_or_trauma:
        score += 1.03
    
    if comorbidities >= 2:
        score += 1.06
    
    return score

st.title("Geneva Risk Score for VTE Prophylaxis Prediction")

age = st.slider("What is your age?", min_value=18, max_value=100, value=50, step=1)
gender = st.selectbox("What is your gender?", options=["Male", "Female"])
bmi = st.slider("What is your BMI?", min_value=10, max_value=60, value=25, step=1)
history_of_vte = st.checkbox("Do you have a history of VTE?")
active_cancer = st.checkbox("Do you have active cancer?")
recent_surgery_or_trauma = st.checkbox("Have you had recent surgery or trauma?")
comorbidities = st.slider("How many comorbidities do you have?", min_value=0, max_value=10, value=0, step=1)

st.button("Calculate Geneva Risk Score"):
score = calculate_geneva_risk_score(age, gender, bmi, history_of_vte, active_cancer, recent_surgery_or_trauma, comorbidities)
st.write(f"Your Geneva Risk Score for VTE Prophylaxis is: {score:.2f}")
