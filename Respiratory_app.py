import streamlit as st
import random

# Page Configuration
st.set_page_config(
    page_title="Al-Ahli Hospital Respiratory Command Center",
    page_icon="🫁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Branding and Signature Style
st.markdown("""
    <style>
    .main-title { font-size:32px !important; font-weight: bold; color: #1E3A8A; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:16px !important; color: #4B5563; text-align: center; margin-bottom: 25px; font-style: italic; }
    .branding-bar { background-color: #F3F4F6; padding: 20px; border-radius: 10px; border-left: 6px solid #EF4444; margin-bottom: 25px; }
    .branding-bar strong { color: #1E3A8A !important; font-weight: bold; }
    .branding-text { color: #1F2937 !important; font-size: 16px !important; line-height: 1.6; }
    .section-header { font-size:22px !important; font-weight: bold; color: #B91C1C; margin-top: 15px; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# App Header & Branding
st.markdown("<div class='main-title'>🫁 Acute Respiratory Failure & Pulmonary Embolism Engine</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Advanced Diagnostic Algorithms, A-a Gradient Calculator & Oxygenation Protocols</div>", unsafe_allow_html=True)

# Professional Badge (The Everlasting Agreement)
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Clinical Project Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Core Framework:</strong> BTS/ERS Respiratory Guidelines & Wells' Criteria adapted to Local Resource Optimization
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Layout Configuration: Split Screen
col_input, col_output = st.columns([1.1, 1.2])

# ==============================================================================
# LEFT COLUMN: Patient Clinical Presentation, ABG Labs & Device Status
# ==============================================================================
with col_input:
    st.markdown("<div class='section-header'>🩺 1. Patient Demographics & Vital Signs</div>", unsafe_allow_html=True)
    with st.expander("👤 Patient Vitals", expanded=True):
        age = st.number_input("Age (Years):", min_value=18, max_value=100, value=60, key="resp_age")
        rr = st.number_input("Respiratory Rate (bpm):", min_value=8, max_value=50, value=28)
        spo2 = st.number_input("Oxygen Saturation (SpO2 %):", min_value=40, max_value=100, value=86)
        fio2_percent = st.number_input("Current Delivered Oxygen Concentration (FiO2 %):", min_value=21, max_value=100, value=21, step=5, help="Room air is 21%. Nasal Cannula 1-6L/min provides ~24-40%. Non-Rebreather provides ~60-90%.")

    st.markdown("<div class='section-header'>🩸 2. Arterial Blood Gas (ABG) Panel</div>", unsafe_allow_html=True)
    with st.expander("🧪 Gas Metrics", expanded=True):
        pao2 = st.number_input("Partial Pressure of Oxygen (PaO2 mmHg):", min_value=30, max_value=500, value=60)
        paco2 = st.number_input("Partial Pressure of Carbon Dioxide (PaCO2 mmHg):", min_value=10, max_value=150, value=50)
        ph = st.number_input("Arterial pH:", min_value=6.80, max_value=7.80, value=7.31, step=0.01)

    st.markdown("<div class='section-header'>🧬 3. Pulmonary Embolism (Wells' Criteria Panel)</div>", unsafe_allow_html=True)
    with st.expander("🗂️ PE Clinical Risk Assessment", expanded=True):
        st.write("**Select all clinical signs present in the patient:**")
        c1 = st.checkbox("Clinical signs/symptoms of DVT (objective swelling, pain) [+3.0]")
        c2 = st.checkbox("PE is the #1 diagnosis OR equally likely as other alternatives [+3.0]")
        c3 = st.checkbox("Heart Rate > 100 beats per minute [+1.5]")
        c4 = st.checkbox("Immobilization (&ge; 3 days) or Surgery within past 4 weeks [+1.5]")
        c5 = st.checkbox("Previous objectively diagnosed PE or DVT [+1.5]")
        c6 = st.checkbox("Hemoptysis [+1.0]")
        c7 = st.checkbox("Malignancy (under active treatment or palliation) [+1.0]")

# ==============================================================================
# RIGHT COLUMN: Calculations, Diagnostic Algorithms & Oxygenation Pathways
# ==============================================================================
with col_output:
    st.markdown("<div class='section-header'>🎯 4. Bedside Calculations & Physiological Analysis</div>", unsafe_allow_html=True)
    
    # 1. Calculate Wells Score
    wells_score = 0.0
    if c1: wells_score += 3.0
    if c2: wells_score += 3.0
    if c3: wells_score += 1.5
    if c4: wells_score += 1.5
    if c5: wells_score += 1.5
    if c6: wells_score += 1.0
    if c7: wells_score += 1.0

    # 2. Advanced A-a Gradient Calculation
    # Formula: PAO2 = (FiO2 * (Patm - PH2O)) - (PaCO2 / R)
    # Standard: Patm = 760 mmHg, PH2O = 47 mmHg, R = 0.8
    fio2_decimal = fio2_percent / 100.0
    alveolar_o2 = (fio2_decimal * (760 - 47)) - (paco2 / 0.8)
    aa_gradient = alveolar_o2 - pao2
    
    # Expected Normal A-a Gradient for age = (Age / 4) + 4
    expected_gradient = (age / 4) + 4

    # Metrics Grid Display
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.metric(label="Calculated A-a Gradient:", value=f"{aa_gradient:.1f} mmHg", 
                  delta=f"Expected Normal: {expected_gradient:.1f}" if aa_gradient <= expected_gradient else "ELEVATED GRADIENT")
    with col_m2:
        st.metric(label="Wells' PE Risk Score:", value=f"{wells_score:.1f} Points")

    # ------------------------------------------------------------------
    # PHYSIOLOGICAL INTERPRETATION BASED ON DR. IHAB'S ALGORITHM
    # ------------------------------------------------------------------
    st.write("#### **Physiological Hypoxia Interpretation:**")
    if aa_gradient > expected_gradient:
        st.error("🚨 **Elevated A-a Gradient Detected:** The hypoxemia is caused by intrinsic lung pathology. This indicates **V/Q Mismatch, Shunt, or Diffusion Limitation** (e.g., Pulmonary Embolism, Pneumonia, Pulmonary Edema, or Severe COPD Exacerbation).")
    else:
        if paco2 > 45:
            st.warning("⚠️ **Normal A-a Gradient with Hypercapnia:** The hypoxemia is driven purely by **Alveolar Hypoventilation** (e.g., Central nervous system depression, drug overdose, or neuromuscular weakness). The lungs themselves are clear.")
        else:
            st.success("🟢 **Normal A-a Gradient:** Alveolar-arterial oxygen transfer is normal. Consider external causes like low ambient oxygen or artifact.")

    # ------------------------------------------------------------------
    # LOCAL HOSPITAL PHARMACOPOEIA PROTOCOLS (OXYGENATION & PE)
    # ------------------------------------------------------------------
    st.markdown("---")
    st.markdown("<div class='section-header'>💊 5. Local Protocol & Oxygen Escalation Pathway</div>", unsafe_allow_html=True)
    
    st.write("#### **Step-by-Step Oxygen Titration Strategy (Target SpO2: 92-96%, or 88-92% in COPD):**")
    
    if spo2 < 92:
        st.markdown(f"""
        <div style="background-color: #FEF2F2; padding: 15px; border-radius: 8px; border-left: 5px solid #EF4444; margin-bottom: 15px;">
            <strong style="color: #991B1B !important;">🚨 OXYGENATION ESCALATION REQUIRED (Current SpO2: {spo2}%):</strong>
            <ul style="color: #1F2937 !important; font-size: 14px; margin-left: 20px; line-height: 1.6; list-style-type: decimal;">
                <li><strong>Initial Action:</strong> If currently on room air, start <strong>Nasal Cannula at 2-6 L/min</strong> (FiO2 ~28-40%).</li>
                <li><strong>Escalation Plan:</strong> If hypoxemia persists, escalate to a <strong>Simple Face Mask (5-10 L/min)</strong> or a <strong>Non-Rebreather Mask (10-15 L/min)</strong> to deliver maximum FiO2.</li>
                <li><strong>Ventilatory Check:</strong> Since pH is <strong>{ph}</strong> and PaCO2 is <strong>{paco2} mmHg</strong>, if respiratory acidosis is present with fatigue, immediately initiate <strong>Non-Invasive Ventilation (BiPAP)</strong> or call for ICU consultation.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.success("🟢 **Oxygenation Acceptable:** Maintain current delivery device and monitor respiratory fatigue.")

    # Pulmonary Embolism Local Protocol Decision
    st.write("#### **Pulmonary Embolism (PE) Clinical Decision Tool:**")
    if wells_score > 4.0:
        st.markdown(f"""
        <div style="background-color: #FFFBEB; padding: 15px; border-radius: 8px; border-left: 5px solid #F59E0B;">
            <strong style="color: #92400E !important;">⚠️ PE IS CLINICALLY LIKELY (Score: {wells_score})</strong>
            <ul style="color: #1F2937 !important; font-size: 14px; margin-left: 20px; line-height: 1.6;">
                <li><strong>Primary Directive:</strong> Order an immediate <strong>CT Pulmonary Angiography (CTPA)</strong>.</li>
                <li><strong>Al-Ahli Restricted Protocol Option:</strong> If CTPA is delayed or contraindicated (e.g., GFR is too low), perform an urgent <strong>Bedside Echocardiography</strong> to look for signs of right ventricular (RV) strain / McConnell's sign.</li>
                <li><strong>Therapeutic Intervention:</strong> In the absence of high bleeding risks, start <strong>Therapeutic Anticoagulation</strong> (Low Molecular Weight Heparin/Enoxaparin or Unfractionated Heparin) immediately while awaiting definitive imaging.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info(f"🔹 **PE Unlikely (Score: {wells_score}):** Consider ordering a highly sensitive **D-Dimer assay** to safely rule out pulmonary embolism under local protocol guidelines.")

    # ------------------------------------------------------------------
    # DYNAMIC INTERACTIVE BOARD MCQ GENERATOR (RESPIRATORY HUB)
    # ------------------------------------------------------------------
    st.markdown("---")
    st.markdown("<div class='section-header'>📚 6. High-Yield Respiratory Board Review Challenge</div>", unsafe_allow_html=True)
    
    resp_pool = [
        {
            "id": 1,
            "case": "A 65-year-old male with a history of heavy smoking presents to the emergency department with acute onset worsening dyspnea. ABG on room air reveals: pH 7.28, PaCO2 68 mmHg, PaO2 52 mmHg. His calculated A-a gradient is found to be within the normal expected physiological range for his age.",
            "question": "What is the primary underlying pathophysiological mechanism explaining this patient's hypoxemia?",
            "options": ["A) Acute Pulmonary Embolism causing a massive V/Q mismatch", "B) Alveolar Hypoventilation secondary to severe respiratory muscle fatigue / COPD exacerbation", "C) Intracardiac right-to-left shunt bypass", "D) Lobar Pneumonia causing severe alveolar consolidation"],
            "correct": "B) Alveolar Hypoventilation secondary to severe respiratory muscle fatigue / COPD exacerbation",
            "explanation": "A normal A-a gradient in the presence of hypoxemia and hypercapnia (high PaCO2) is pathognomonic for Alveolar Hypoventilation. This means the lungs themselves are transferring gas normally, but the respiratory pump is failing to clear CO2 and bring in oxygen, typically seen in acute-on-chronic respiratory failure or sedative overdoses."
        },
        {
            "id": 2,
            "case": "A 45-year-old female undergoes an orthopedic procedure. On post-op day 3, she develops sudden severe chest pain and dyspnea. Her heart rate is 112 bpm, and her lungs are clear to auscultation. Due to acute kidney injury, a CTPA cannot be performed immediately.",
            "question": "According to local clinical protocols for a likely PE, what is the best immediate alternative step?",
            "options": ["A) Discontinue all oxygen therapy and recheck the patient in 4 hours", "B) Perform a bedside Echocardiogram to evaluate for RV strain and initiate empirical therapeutic anticoagulation if safe", "C) Order an urgent high-resolution chest CT without contrast", "D) Start aggressive intravenous fluid boluses of 2 Liters Normal Saline"],
            "correct": "B) Perform a bedside Echocardiogram to evaluate for RV strain and initiate empirical therapeutic anticoagulation if safe",
            "explanation": "When a CTPA is contraindicated due to renal failure or unavailable, local protocols and guidelines recommend utilizing a bedside echocardiogram to check for acute right ventricular strain or dysfunction. If the clinical index of suspicion is high (Wells > 4), empirical therapeutic anticoagulation should be initiated if there are no absolute bleeding contraindications."
        }
    ]

    if 'resp_q' not in st.session_state:
        st.session_state.resp_q = random.choice(resp_pool)
        
    if st.button("🔄 Generate Another Respiratory Board Question"):
        st.session_state.resp_q = random.choice(resp_pool)
        
    current_resp_q = st.session_state.resp_q
    
    st.warning(f"**Clinical Scenario:** {current_resp_q['case']}")
    st.write(f"❓ **Question:** {current_resp_q['question']}")
    
    user_ans_resp = st.radio("Select your answer from below:", current_resp_q['options'], key=f"resp_q_{current_resp_q['id']}")
    
    if st.expander("🔑 Reveal Correct Answer & Dr. Ihab's Clinical Explanation"):
        if user_ans_resp == current_resp_q['correct']:
            st.success(f"🎯 **Correct!** The answer is {current_resp_q['correct']}")
        else:
            st.error(f"❌ **Incorrect Choice.** The correct answer is {current_resp_q['correct']}")
        st.markdown(f"**Explanation:** {current_resp_q['explanation']}")

# Footer Signature (The Unshakable Standard)
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 12px;'>Al-Ahli Hospital Respiratory Center App © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
