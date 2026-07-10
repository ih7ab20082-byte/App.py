import streamlit as st

# Page Config
st.set_page_config(page_title="Al-Ahli Sepsis & Stewardship", page_icon="🦠", layout="wide")

# Styling
st.markdown("<div style='text-align: center; color: #991B1B; font-weight: bold; font-size: 30px;'>🦠 Sepsis Management & Stewardship Engine</div>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; font-style: italic;'>Clinical Director: Dr. Ihab Abbass Abu Hilail | Al-Ahli Hospital</div>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🚀 Sepsis Initial Resuscitation", "💊 Stewardship Drug Picker", "📈 De-escalation Protocol"])

# TAB 1: Sepsis
with tab1:
    st.markdown("### 🚑 Quick Sepsis Screening (qSOFA)")
    rr = st.number_input("Respiratory Rate (≥ 22/min):", 0, 50, 20)
    mental = st.checkbox("Altered Mental Status")
    sbp = st.number_input("Systolic BP (≤ 100 mmHg):", 50, 200, 110)
    
    score = (1 if rr >= 22 else 0) + (1 if mental else 0) + (1 if sbp <= 100 else 0)
    if score >= 2:
        st.error(f"qSOFA Score: {score} - High Risk of Sepsis! Start 1-hour Bundle Immediately.")
    else:
        st.success(f"qSOFA Score: {score} - Monitor closely.")

# TAB 2: Drug Picker (Stewardship)
with tab2:
    st.markdown("### 💊 Targeted Antimicrobial Stewardship")
    source = st.selectbox("Suspected Source of Infection:", ["Community-Acquired Pneumonia", "UTI (Complicated)", "Skin & Soft Tissue Infection"])
    severity = st.radio("Patient Severity:", ("Stable", "Unstable/Septic"))
    
    st.write("---")
    st.markdown("#### 💡 Clinical Recommendation (Local Availability Adjusted):")
    if source == "Community-Acquired Pneumonia" and severity == "Stable":
        st.info("Primary: Ceftriaxone 1-2g IV q24h + Azithromycin PO.\n\n*Alternative (If Ceftriaxone missing):* Levofloxacin 750mg IV q24h.")
    elif source == "UTI (Complicated)" and severity == "Unstable/Septic":
        st.warning("Primary: Piperacillin/Tazobactam (if available) OR Ceftriaxone + Gentamicin.\n\n*If allergic/resource limited:* Ciprofloxacin 400mg IV q12h.")
    else:
        st.write("Please consult ID specialist for escalated sepsis cases.")

# TAB 3: De-escalation
with tab3:
    st.markdown("### 📉 48-Hour De-escalation Check")
    st.write("1. Does the patient show clinical improvement?")
    st.write("2. Are the blood/urine culture results available?")
    st.write("3. Can we switch from broad-spectrum to pathogen-directed therapy?")
    if st.button("Check De-escalation Readiness"):
        st.success("Proceed to simplify therapy if patient is afebrile for 24h and clinically improved!")
