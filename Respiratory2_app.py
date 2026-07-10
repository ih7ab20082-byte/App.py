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
st.markdown("<div class='main-title'>🫁 Acute Respiratory Failure & Hypoxemia Approach Engine</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Advanced Diagnostic Algorithms, A-a Gradient, P/F Ratio, & Step-by-Step Desat Approach</div>", unsafe_allow_html=True)

# Professional Badge (The Everlasting Agreement)
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Clinical Project Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Core Framework:</strong> Comprehensive Approach to Hypoxemia, ARDS Berlin Criteria, & Local Protocol Guidelines
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Layout Configuration: Split Screen
col_input, col_output = st.columns([1.1, 1.2])

# ==============================================================================
# LEFT COLUMN: Patient Metrics, ABG Labs & Clinical Exam Finding
# ==============================================================================
with col_input:
    st.markdown("<div class='section-header'>🩺 1. Patient Demographics & Oxygen Vitals</div>", unsafe_allow_html=True)
    with st.expander("👤 Patient Oxygen Profile", expanded=True):
        age = st.number_input("Age (Years):", min_value=18, max_value=100, value=60, key="resp_age")
        rr = st.number_input("Respiratory Rate (bpm):", min_value=8, max_value=50, value=28)
        spo2 = st.number_input("Oxygen Saturation (SpO2 %):", min_value=40, max_value=100, value=85)
        fio2_percent = st.number_input("Delivered Oxygen Concentration (FiO2 %):", min_value=21, max_value=100, value=21, step=5, 
                                     help="Room air is 21%. Nasal Cannula 1-6 L/min (~24-40%). Simple Mask (~40-60%). Non-Rebreather (~60-90%).")

    st.markdown("<div class='section-header'>🦻 2. Quick Bedside Chest Auscultation (The Desat Mindmap)</div>", unsafe_allow_html=True)
    with st.expander("🫁 Chest Exam Findings", expanded=True):
        chest_exam = st.radio(
            "What do you hear upon bilateral lung auscultation?",
            ("Clear Lung Sounds (No crackles/wheeze)", 
             "Unilateral Absent/Decreased Breath Sounds",
             "Bilateral Diffuse Crackles / Crepitations",
             "Diffuse Wheezing / Expiratory Rhonchi")
        )

    st.markdown("<div class='section-header'>🩸 3. Arterial Blood Gas (ABG) Inputs</div>", unsafe_allow_html=True)
    with st.expander("🧪 Gas Metrics Panel", expanded=True):
        pao2 = st.number_input("Partial Pressure of Oxygen (PaO2 mmHg):", min_value=30, max_value=500, value=58)
        paco2 = st.number_input("Partial Pressure of Carbon Dioxide (PaCO2 mmHg):", min_value=10, max_value=150, value=48)
        ph = st.number_input("Arterial pH:", min_value=6.80, max_value=7.80, value=7.32, step=0.01)

    st.markdown("<div class='section-header'>🧬 4. Pulmonary Embolism Screening (Wells' Panel)</div>", unsafe_allow_html=True)
    with st.expander("🗂️ PE Risk Checklist", expanded=True):
        c1 = st.checkbox("Clinical signs/symptoms of DVT (objective swelling, pain) [+3.0]")
        c2 = st.checkbox("PE is the #1 diagnosis OR equally likely as alternative [+3.0]")
        c3 = st.checkbox("Heart Rate > 100 beats per minute [+1.5]")
        c4 = st.checkbox("Immobilization (&ge; 3 days) or Surgery within past 4 weeks [+1.5]")
        c5 = st.checkbox("Previous objectively diagnosed PE or DVT [+1.5]")
        c6 = st.checkbox("Hemoptysis [+1.0]")
        c7 = st.checkbox("Malignancy under active treatment/palliation [+1.0]")

# ==============================================================================
# RIGHT COLUMN: The Broad Approach to Desat, Calculations & Protocols
# ==============================================================================
with col_output:
    st.markdown("<div class='section-header'>🧠 5. Master Mindmap: How to Think of This Desat Patient</div>", unsafe_allow_html=True)
    
    # Dynamic Diagnostic Approach based on Chest Exam and Vitals
    if "Clear" in chest_exam:
        st.warning(f"""
        🔍 **Thinking Pathway for Clear Lungs + Desat:**
        When a patient is hypoxemic but the chest is completely clear, your differential diagnosis must strictly focus on:
        *   **Pulmonary Embolism (PE):** Classic mismatch where air enters but blood flow is blocked. Check the Wells' score below!
        *   **Hypoventilation:** Check the PaCO2. Since PaCO2 is **{paco2} mmHg**, if it's high, this confirms respiratory drive failure (Drug overdose, Neuromuscular weakness, or severe COPD fatigue).
        *   **Anatomical Shunt / Methaemoglobinemia:** Rare causes if the above are ruled out.
        """)
    elif "Unilateral Absent" in chest_exam:
        st.error("""
        🚨 **Thinking Pathway for Unilateral Absent Sounds:**
        This is an emergency! You must immediately rule out:
        *   **Pneumothorax:** Especially if the patient is unstable or has a history of emphysema/bullae. Consider urgent bedside ultrasound (Blue Protocol) or needle decompression if in shock.
        *   **Massive Pleural Effusion or Mucus Plug / Atelectasis:** Obstructing a main bronchus.
        """)
    elif "Bilateral Diffuse Crackles" in chest_exam:
        st.error("""
        💦 **Thinking Pathway for Fluid / Alveolar Filling:**
        The alveoli are flooded. You must differentiate between:
        *   **Cardiogenic Pulmonary Edema (Heart Failure):** Check if the patient has JVD, high blood pressure, or a history of cardiac disease.
        *   **Non-Cardiogenic Pulmonary Edema (ARDS / Severe Pneumonia):** Check the calculated P/F Ratio below to evaluate for ARDS criteria.
        """)
    elif "Diffuse Wheezing" in chest_exam:
        st.info("""
        💨 **Thinking Pathway for Airway Obstruction:**
        The airways are narrowed. This is a classic presentation of:
        *   **Acute Exacerbation of COPD or Bronchial Asthma.**
        *   **Cardiac Asthma:** Sometimes left ventricular failure causes airway edema mimicking a wheeze. Always double-check volume status!
        """)

    # ------------------------------------------------------------------
    # ADVANCED PHYSIOLOGICAL CALCULATIONS
    # ------------------------------------------------------------------
    st.markdown("---")
    st.markdown("<div class='section-header'>🎯 6. Bedside Oxygenation & Lung Mechanics Metrics</div>", unsafe_allow_html=True)
    
    # 1. A-a Gradient
    fio2_decimal = fio2_percent / 100.0
    alveolar_o2 = (fio2_decimal * (760 - 47)) - (paco2 / 0.8)
    aa_gradient = alveolar_o2 - pao2
    expected_gradient = (age / 4) + 4

    # 2. P/F Ratio (PaO2 / FiO2)
    pf_ratio = pao2 / fio2_decimal

    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.metric(label="Calculated A-a Gradient:", value=f"{aa_gradient:.1f} mmHg",
                  delta="Pathological Lung Shunt/V-Q" if aa_gradient > expected_gradient else "Normal Lung Mechanics")
    with col_m2:
        st.metric(label="Calculated P/F Ratio:", value=f"{pf_ratio:.1f}",
                  delta="ARDS Range (<300)" if pf_ratio < 300 else "Acceptable")

    # ARDS Berlin Classification Check
    if pf_ratio < 300:
        st.markdown("**🚨 ARDS Berlin Criteria Analysis:**")
        if 200 < pf_ratio <= 300: st.warning("🔸 **Mild ARDS:** Consider optimized PEEP on Non-Invasive Ventilation (BiPAP) if stable.")
        elif 100 < pf_ratio <= 200: st.error("🚨 **Moderate ARDS:** High risk of failure on non-invasive measures. Prepare for protective lung ventilation parameters.")
        elif pf_ratio <= 100: st.error("💥 **Severe ARDS:** Critical emergency. Immediate endotracheal intubation, protective low-tidal volume ventilation, and consideration for prone positioning.")

    # ------------------------------------------------------------------
    # LOCAL OXYGENATION THERAPY STEPS
    # ------------------------------------------------------------------
    st.markdown("---")
    st.markdown("<div class='section-header'>💊 7. Local Protocol: Step-by-Step Oxygen Titration</div>", unsafe_allow_html=True)
    
    st.write(f"Current Patient Oxygen Saturation: **{spo2}%** on FiO2: **{fio2_percent}%**")
    
    st.markdown("""
    🥇 **The Desat Clinical Action Protocol:**
    *   **Step 1 [Mild Drop - SpO2 90-92%]:** Initiate **Nasal Cannula** at 2-6 L/min. If the patient is a chronic COPD retainer, target an explicit saturation window of **88-92%** to avoid knocking out their hypoxic respiratory drive.
    *   **Step 2 [Moderate Drop - SpO2 85-89%]:** Escalate immediately to a **Simple Face Mask** (5-10 L/min) or a **Venturi Mask** if strict FiO2 titration is required.
    *   **Step 3 [Severe Drop / Refractory Hypoxemia - SpO2 < 85%]:** Strap on a **Non-Rebreather Mask (NRM)** with the reservoir bag fully inflated at 12-15 L/min.
    *   **Step 4 [Ventilatory Failure]:** If the ABG shows a pH < 7.30 and PaCO2 > 50 with respiratory distress, do not rely on masks. Escalate directly to **Non-Invasive Ventilation (BiPAP)** using local protocol entry criteria (IPEP/EPEP setup).
    """)

    # Wells Score Outcome
    wells_score = 0.0
    for cond in [c1, c2, c3, c4, c5, c6, c7]:
        if cond:
            if cond in [c1, c2]: wells_score += 3.0
            elif cond in [c3, c4, c5]: wells_score += 1.5
            else: wells_score += 1.0

    if wells_score > 4.0 and "Clear" in chest_exam:
        st.error(f"⚠️ **High Clinical Correlation:** Patient has clear lungs and a Wells' Score of **{wells_score}**. This strongly flags an **Acute Pulmonary Embolism**. Prioritize local CTPA or empirical anticoagulation.")

    # ------------------------------------------------------------------
    # DYNAMIC INTERACTIVE BOARD MCQ GENERATOR (ADVANCED RESPIRATORY)
    # ------------------------------------------------------------------
    st.markdown("---")
    st.markdown("<div class='section-header'>📚 8. High-Yield Board Review (Hypoxemia & Desat Specialist Hub)</div>", unsafe_allow_html=True)
    
    resp_pool = [
        {
            "id": 1,
            "case": "A 58-year-old female is admitted with severe sepsis from a urinary tract infection. On day 2, she develops acute respiratory distress with bilateral diffuse infiltrates on her chest X-ray. Her PaO2 is 60 mmHg while receiving oxygen via a non-rebreather mask estimated at an FiO2 of 60% (0.60). Echocardiogram shows a normal ejection fraction and no left atrial hypertension.",
            "question": "What is the P/F ratio, and what is the diagnosis based on the Berlin criteria?",
            "options": ["A) P/F ratio 250; Mild ARDS", "B) P/F ratio 100; Moderate ARDS", "C) P/F ratio 100; Severe ARDS", "D) P/F ratio 150; Moderate ARDS"],
            "correct": "B) P/F ratio 100; Moderate ARDS",
            "explanation": "P/F ratio = PaO2 / FiO2 = 60 / 0.60 = 100. According to the Berlin criteria, a P/F ratio between 100 and 200 in the presence of bilateral infiltrates and the absence of a cardiogenic cause satisfies the criteria for Moderate Acute Respiratory Distress Syndrome (ARDS)."
        },
        {
            "id": 2,
            "case": "A 44-year-old male is brought into the Al-Ahli emergency department completely obtunded following an accidental sedative ingestion. His pulse oximeter reads an SpO2 of 84% on room air. ABG is drawn: pH 7.22, PaCO2 70 mmHg, PaO2 50 mmHg. The calculated A-a gradient matches his expected age-adjusted normal gradient exactly.",
            "question": "Which of the following statements is true regarding this patient's clinical situation?",
            "options": ["A) The patient has an acute pulmonary embolism and requires immediate thrombolysis", "B) The hypoxemia is caused by a V/Q mismatch due to aspiration pneumonia", "C) The hypoxemia is a pure consequence of Alveolar Hypoventilation; the lung tissue is intact", "D) High-flow nasal cannula alone will completely fix the underlying acid-base clearance defect"],
            "correct": "C) The hypoxemia is a pure consequence of Alveolar Hypoventilation; the lung tissue is intact",
            "explanation": "A normal A-a gradient combined with hypercapnic respiratory failure proves that the hypoxemia is purely secondary to hypoventilation (decreased respiratory rate/tidal volume). Because the alveolar-capillary membrane is functioning normally, the primary problem is ventilation, which requires reversing the sedation or providing ventilatory support (like BiPAP or mechanical ventilation), not just oxygen therapy alone."
        }
    ]

    if 'resp_q_v2' not in st.session_state:
        st.session_state.resp_q_v2 = random.choice(resp_pool)
        
    if st.button("🔄 Generate Another Advanced Board Question"):
        st.session_state.resp_q_v2 = random.choice(resp_pool)
        
    current_q = st.session_state.resp_q_v2
    
    st.warning(f"**Clinical Scenario:** {current_q['case']}")
    st.write(f"❓ **Question:** {current_q['question']}")
    
    user_ans = st.radio("Select your answer from below:", current_q['options'], key=f"resp_q_v2_{current_q['id']}")
    
    if st.expander("🔑 Reveal Correct Answer & Dr. Ihab's Clinical Explanation"):
        if user_ans == current_q['correct']:
            st.success(f"🎯 **Correct!** The answer is {current_q['correct']}")
        else:
            st.error(f"❌ **Incorrect Choice.** The correct answer is {current_q['correct']}")
        st.markdown(f"**Explanation:** {current_q['explanation']}")

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 12px;'>Al-Ahli Hospital Respiratory Center App © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
