import streamlit as st
import random

# Page Configuration
st.set_page_config(
    page_title="Al-Ahli Hospital Advanced Respiratory Command Center",
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
st.markdown("<div class='main-title'>🫁 Master Respiratory & Ventilatory Decision Support Tool</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Acute Desat Approach, CO2 Narcosis Protocol, and Advanced NIV/Ventilator Settings Panel</div>", unsafe_allow_html=True)

# Professional Badge (The Everlasting Agreement)
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Clinical Project Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Core Framework:</strong> Comprehensive Hypoxemia & Hypercapnia Management, Gold-Standard Ventilatory Titration Protocols
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Layout Configuration: Split Screen
col_input, col_output = st.columns([1.1, 1.2])

# ==============================================================================
# LEFT COLUMN: Patient Demographics, Vitals, Mental Status & Gas Labs
# ==============================================================================
with col_input:
    st.markdown("<div class='section-header'>🩺 1. Baseline Demographics & Respiratory Vitals</div>", unsafe_allow_html=True)
    with st.expander("👤 Patient Vital Profile", expanded=True):
        age = st.number_input("Age (Years):", min_value=18, max_value=100, value=65, key="resp_age")
        weight = st.number_input("Ideal Body Weight (kg) [Crucial for Vent Settings]:", min_value=30, max_value=150, value=70)
        rr = st.number_input("Respiratory Rate (bpm):", min_value=6, max_value=50, value=32)
        spo2 = st.number_input("Initial Oxygen Saturation (SpO2 %):", min_value=40, max_value=100, value=82)
        current_oxygen = st.radio("Current Oxygen Therapy Device:", ("Room Air (21%)", "Nasal Cannula", "Simple Face Mask", "Non-Rebreather Mask (NRM)"))

    st.markdown("<div class='section-header'>🧠 2. Neurological & Mental Status Evaluation</div>", unsafe_allow_html=True)
    with st.expander("🧠 GCS & CO2 Narcosis Check", expanded=True):
        mental_status = st.radio(
            "What is the patient's level of consciousness?",
            ("Alert and Oriented",
             "Somnolent / Drowsy (Arousable to speech, but drifts back to sleep)",
             "Stuporous / Obtunded (Responds only to vigorous/painful stimuli)",
             "Comatose (Unresponsive to painful stimuli / CO2 Narcosis suspected)")
        )
        airway_reflexes = st.radio("Are airway protective reflexes intact? (Gag / Cough):", ("Yes, Intact", "No, Impaired/Absent"))

    st.markdown("<div class='section-header'>🩸 3. Blood Gas Analysis (ABG/VBG Panel)</div>", unsafe_allow_html=True)
    with st.expander("🧪 Current Gas Metrics", expanded=True):
        ph = st.number_input("Arterial pH:", min_value=6.80, max_value=7.80, value=7.24, step=0.01)
        paco2 = st.number_input("Partial Pressure of Carbon Dioxide (PaCO2 mmHg):", min_value=10, max_value=150, value=78)
        pao2 = st.number_input("Partial Pressure of Oxygen (PaO2 mmHg):", min_value=30, max_value=500, value=52)

    st.markdown("<div class='section-header'>🦻 4. Quick Bedside Chest Auscultation</div>", unsafe_allow_html=True)
    with st.expander("🫁 Chest Exam Findings", expanded=True):
        chest_exam = st.radio(
            "Bilateral lung auscultation findings:",
            ("Clear Lung Sounds (No crackles/wheeze)", 
             "Unilateral Absent/Decreased Breath Sounds",
             "Bilateral Diffuse Crackles / Crepitations",
             "Diffuse Wheezing / Expiratory Rhonchi")
        )

# ==============================================================================
# RIGHT COLUMN: Master Clinical Algorithms, Re-evaluations, & Vent Settings
# ==============================================================================
with col_output:
    
    # ------------------------------------------------------------------
    # CLINICAL ASSESSMENT: THE CO2 NARCOSIS & ENCEPHALOPATHY THREAD
    # ------------------------------------------------------------------
    st.markdown("<div class='section-header'>🧠 5. Acute Encephalopathy & CO2 Retainer Approach</div>", unsafe_allow_html=True)
    
    if paco2 > 45 and mental_status != "Alert and Oriented":
        st.error(f"""
        🚨 **CRITICAL DIAGNOSIS: Hypercapnic Encephalopathy (CO2 Narcosis)!**
        The patient has an elevated PaCO2 of **{paco2} mmHg** matching a diminished mental state (**{mental_status}**). 
        * **Pathophysiology:** High CO2 acts as a central nervous system depressant. Worsening acidemia (pH: {ph}) puts the patient at immediate risk of respiratory arrest.
        * **Immediate Warning:** Avoid uncontrolled high-flow oxygen masks if the patient is a known COPD retainer without ventilatory support, as this will further worsen hypercapnia by knocking out their hypoxic drive.
        """)
    else:
        st.success("🟢 **Neurological Status:** No acute signs of advanced CO2 narcosis at this moment. Continue monitoring.")

    # ------------------------------------------------------------------
    # STEP-BY-STEP OXYGEN ESCALATION & THE "WHAT NEXT?" PROTOCOL
    # ------------------------------------------------------------------
    st.markdown("---")
    st.markdown("<div class='section-header'>🎯 6. Oxygenation Strategy & Response Monitoring</div>", unsafe_allow_html=True)
    
    st.write("#### **Phase A: The Initial Oxygen Plan**")
    if paco2 > 50:
        st.warning("⚠️ **Target Saturation Restriction:** Because the patient is actively retaining CO2, target a strict oxygen saturation of **88-92%** (Not 100%) to preserve the chemical respiratory drive while you prepare the machine.")
    else:
        st.info("Target standard saturation of **92-96%** using sequential escalation (Nasal Cannula ➡️ Simple Mask ➡️ Non-Rebreather Mask).")

    st.write("#### **Phase B: Post-Oxygen Re-evaluation (What Happened Next?)**")
    post_o2_scenario = st.selectbox(
        "Select the patient's response 30 minutes after initiating oxygen therapy:",
        ["Select Scenario...", 
         "Scenario 1: SpO2 improved to 90%, patient is alert, ABG shows stable/improving pH and CO2.",
         "Scenario 2: SpO2 is 95%, but patient became markedly more drowsy/obtunded, repeat PaCO2 rose from 78 to 92 mmHg.",
         "Scenario 3: Refractory Hypoxemia. SpO2 remains < 85% despite a Non-Rebreather Mask, patient is tachypneic and exhausting."]
    )

    if post_o2_scenario == "Scenario 1: SpO2 improved to 90%, patient is alert, ABG shows stable/improving pH and CO2.":
        st.success("✅ **Success:** Patient is responding well. Maintain current therapy, check serial blood gases, and treat the underlying cause (e.g., bronchodilators/steroids for COPD).")
    elif post_o2_scenario == "Scenario 2: SpO2 is 95%, but patient became markedly more drowsy/obtunded, repeat PaCO2 rose from 78 to 92 mmHg.":
        st.error("🚨 **CRITICAL ALERT: Oxygen-Induced Hypercapnia / Respiratory Failure!** The excess oxygen suppressed the patient's respiratory drive. The patient is failing. **You must immediately escalate to positive pressure ventilation (NIV or Intubation)!**")
    elif post_o2_scenario == "Scenario 3: Refractory Hypoxemia. SpO2 remains < 85% despite a Non-Rebreather Mask, patient is tachypneic and exhausting.":
        st.error("🚨 **CRITICAL ALERT: True Intrapulmonary Shunt / ARDS Physiology!** Oxygen alone cannot cross the fluid-filled alveoli. **Patient requires immediate recruitment via PEEP/IPAP (NIV or Mechanical Ventilation)!**")

    # ------------------------------------------------------------------
    # ADVANCED VENTILATORY TOOL: NIV & MECHANICAL VENTILATION SETTINGS
    # ------------------------------------------------------------------
    st.markdown("---")
    st.markdown("<div class='section-header'>📟 7. Advanced Ventilatory Management & Settings Panel</div>", unsafe_allow_html=True)
    
    # Selection of Modality
    vent_modality = st.radio("Choose the indicated ventilatory support modality:", ("Non-Invasive Ventilation (BiPAP)", "Invasive Mechanical Ventilation (Intubation)"))
    
    if vent_modality == "Non-Invasive Ventilation (BiPAP)":
        st.write("#### **🛠️ Local Protocol BiPAP Initial Settings:**")
        
        # Absolute contraindication check
        if airway_reflexes == "No, Impaired/Absent" or "Comatose" in mental_status:
            st.markdown("""
            <div style="background-color: #FEF2F2; padding: 15px; border-radius: 8px; border-left: 6px solid #EF4444;">
                <strong style="color: #991B1B !important;">🛑 CRITICAL CONTRAINDICATION DETECTED!</strong><br>
                <span style="color: #1F2937 !important; font-size: 14px;">Patient is comatose or lacks airway protective reflexes. <strong>BiPAP is strictly contraindicated due to high aspiration risk.</strong> Proceed immediately to Endotracheal Intubation!</span>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="background-color: #F0FDF4; padding: 18px; border-radius: 8px; border-left: 6px solid #10B981;">
                <strong style="color: #166534 !important;">📟 Initial BiPAP (NIV) Setup for Hypercapnic Failure:</strong>
                <ul style="color: #1F2937 !important; font-size: 14px; margin-left: 20px; line-height: 1.7; list-style-type: square;">
                    <li><strong>IPAP (Inspiratory Positive Airway Pressure):</strong> Start at <strong>10 - 12 cm H2O</strong>. Titrate up by 2 cm H2O every 15 mins (Max 20) to clear CO2 and assist work of breathing.</li>
                    <li><strong>EPAP (Expiratory Positive Airway Pressure):</strong> Start at <strong>4 - 5 cm H2O</strong> (Acts as PEEP to prevent alveolar collapse).</li>
                    <li><strong>FiO2:</strong> Titrate to the lowest setting required to achieve an SpO2 of 88-92% (for chronic retainers).</li>
                    <li><strong>Monitoring Rule:</strong> Recheck an ABG in <strong>1 hour</strong>. If pH remains &lt; 7.25 and PaCO2 is rising, prepare for intubation.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    elif vent_modality == "Invasive Mechanical Ventilation (Intubation)":
        st.write("#### **🛠️ Lung Protective Ventilation Parameters (Bedside Calculations):**")
        
        # Calculations for Tidal Volume (6 mL/kg to 8 mL/kg of Ideal Body Weight)
        vt_low = weight * 6
        vt_high = weight * 8
        
        if "Bilateral Diffuse Crackles" in chest_exam:
            strategy = "ARDS/Alveolar Flooding Strategy (Strict Low Tidal Volumes Required)"
            recommended_vt = vt_low
            recommended_peep = "10 - 14 cm H2O (High PEEP for alveolar recruitment)"
        else:
            strategy = "Obstructive/Hypercapnic Strategy (COPD/Asthma - Allow time for expiration)"
            recommended_vt = vt_low  # Still start protective
            recommended_peep = "5 cm H2O (Low PEEP to avoid gas trapping / Auto-PEEP)"

        st.markdown(f"""
        <div style="background-color: #EFF6FF; padding: 18px; border-radius: 8px; border-left: 6px solid #3B82F6;">
            <strong style="color: #1E40AF !important;">📟 Calculated Initial Ventilator Settings ({strategy}):</strong>
            <ul style="color: #1F2937 !important; font-size: 14px; margin-left: 20px; line-height: 1.7;">
                <li><strong>Ventilator Mode:</strong> Assist Control / Volume Control (AC/VC) to ensure full baseline support.</li>
                <li><strong>Target Tidal Volume (Vt):</strong> <strong>{recommended_vt} mL</strong> (Calculated strictly at 6 mL/kg of Ideal Body Weight: {weight} kg). Range: {vt_low}-{vt_high} mL.</li>
                <li><strong>Respiratory Rate (RR):</strong> Set at <strong>12 - 16 bpm</strong>. <em>(For severe COPD with a pH of {ph}, allow a lower rate or prolonged expiration to prevent breath-stacking).</em></li>
                <li><strong>PEEP Setup:</strong> Set at <strong>{recommended_peep}</strong>.</li>
                <li><strong>FiO2:</strong> Start at 100% post-intubation, then rapidly titrate down below 60% as tolerated to avoid oxygen toxicity.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # ------------------------------------------------------------------
    # DYNAMIC INTERACTIVE BOARD MCQ GENERATOR (THE CRITICAL VENTILATION HUB)
    # ------------------------------------------------------------------
    st.markdown("---")
    st.markdown("<div class='section-header'>📚 8. High-Yield Board Review Challenge (Ventilation Specialist Hub)</div>", unsafe_allow_html=True)
    
    vent_pool = [
        {
            "id": 1,
            "case": "A 68-year-old severe COPD patient is brought to Al-Ahli ED with acute somnolence. Initial ABG shows: pH 7.21, PaCO2 85 mmHg, PaO2 48 mmHg. The resident starts a Non-Rebreather Mask at 15L/min. 30 minutes later, the patient is completely unarousable to painful stimuli. A repeat ABG shows pH 7.12, PaCO2 102 mmHg.",
            "question": "What is the most appropriate next step in the clinical management of this patient?",
            "options": ["A) Increase the oxygen flow on the mask to 20L/min and add a nebulizer", "B) Initiate high-dose intravenous sodium bicarbonate infusion", "C) Initiate immediate Endotracheal Intubation and Invasive Mechanical Ventilation", "D) Apply a BiPAP mask with an IPAP of 18 cm H2O and EPAP of 5 cm H2O"],
            "correct": "C) Initiate immediate Endotracheal Intubation and Invasive Mechanical Ventilation",
            "explanation": "While BiPAP is the first-line choice for acute hypercapnic COPD exacerbations, this patient has now developed severe CO2 Narcosis and is comatose (unarousable to pain). A comatose state with loss of airway protective reflexes is an absolute contraindication for non-invasive ventilation (BiPAP). Immediate intubation is required."
        },
        {
            "id": 2,
            "case": "An intubated 70 kg patient with severe acute respiratory distress syndrome (ARDS) is placed on a volume-control mode. The resident sets the tidal volume at 650 mL to normalize a mild respiratory acidosis.",
            "question": "According to ARDSnet guidelines and modern internal medicine board standards, why is this setting dangerous?",
            "options": ["A) It will induce severe respiratory alkalosis instantly", "B) It causes high tidal volume barotrauma/volutrauma; the target should be strictly 6 mL/kg (~420 mL)", "C) It will completely turn off the patient's intrinsic renal compensation mechanisms", "D) Volume-control mode cannot deliver tidal volumes larger than 500 mL physically"],
            "correct": "B) It causes high tidal volume barotrauma/volutrauma; the target should be strictly 6 mL/kg (~420 mL)",
            "explanation": "In ARDS, the lungs are stiff and severely congested ('Baby Lung' concept). Utilizing high tidal volumes (like 650 mL for a 70 kg patient, which is >9 mL/kg) causes volutrauma and increases mortality. Lung-protective ventilation demands lower tidal volumes (6 mL/kg of ideal body weight, approx 420 mL) and accepting permissive hypercapnia if necessary."
        }
    ]

    if 'vent_q' not in st.session_state:
        st.session_state.vent_q = random.choice(vent_pool)
        
    if st.button("🔄 Generate Another Advanced Ventilatory Board Question"):
        st.session_state.vent_q = random.choice(vent_pool)
        
    current_q = st.session_state.vent_q
    
    st.warning(f"**Clinical Scenario:** {current_q['case']}")
    st.write(f"❓ **Question:** {current_q['question']}")
    
    user_ans = st.radio("Select your answer from below:", current_q['options'], key=f"vent_q_{current_q['id']}")
    
    if st.expander("🔑 Reveal Correct Answer & Dr. Ihab's Clinical Explanation"):
        if user_ans == current_q['correct']:
            st.success(f"🎯 **Correct!** The answer is {current_q['correct']}")
        else:
            st.error(f"❌ **Incorrect Choice.** The correct answer is {current_q['correct']}")
        st.markdown(f"**Explanation:** {current_q['explanation']}")

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 12px;'>Al-Ahli Hospital Advanced Respiratory Center App © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
