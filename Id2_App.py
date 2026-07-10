import streamlit as st

# هيكل التشخيص والتتبع التفاعلي (Infective Endocarditis Example)
def ie_module():
    st.header("❤️ Infective Endocarditis Management")
    
    # 1. التشخيص التفاعلي
    st.subheader("🔍 Diagnostic Triage")
    fever = st.checkbox("Persistent Fever?")
    echo_pos = st.checkbox("Vegetations on Echo?")
    blood_culture = st.text_input("Blood Culture Result:")
    
    # 2. آلية التتبع (Monitoring)
    st.subheader("📊 Monitoring & Tracking")
    days = st.slider("Treatment Day:", 1, 42, 1)
    vitals = st.text_area("Daily Observations (Temp/Hemodynamics):")
    
    # 3. محرك العلاج الذكي
    st.subheader("💊 Rx Strategy")
    creatinine = st.number_input("Current Serum Cr:")
    # (المنطق هنا يحسب الجرعة بناءً على وظائف الكلى)
    st.info("Recommended Rx: Vancomycin (dose adjusted) + Rocephin.")

# دمج الوحدات في نظام واحد
def main():
    st.title("🛡️ Al-Ahli Clinical Command Center")
    module = st.selectbox("Select Condition:", ["Infective Endocarditis", "Brucellosis", "Meningitis", "Diabetic Foot"])
    
    if module == "Infective Endocarditis":
        ie_module()
    # يمكنك إضافة بقية الوحدات هنا...
