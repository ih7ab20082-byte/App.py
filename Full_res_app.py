import streamlit as st
import random
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="Al-Ahli Hospital Advanced Respiratory & Ventilatory Center",
    page_icon="🫁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Branding and Comprehensive Medical Style
st.markdown("""
    <style>
    .main-title { font-size:32px !important; font-weight: bold; color: #1E3A8A; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:16px !important; color: #4B5563; text-align: center; margin-bottom: 25px; font-style: italic; }
    .branding-bar { background-color: #F3F4F6; padding: 20px; border-radius: 10px; border-left: 6px solid #EF4444; margin-bottom: 25px; }
    .branding-bar strong { color: #1E3A8A !important; font-weight: bold; }
    .branding-text { color: #1F2937 !important; font-size: 16px !important; line-height: 1.6; }
    .section-header { font-size:22px !important; font-weight: bold; color: #B91C1C; margin-top: 15px; margin-bottom: 15px; }
    .protocol-box { background-color: #F8FAFC; padding: 20px; border-radius: 8px; border: 1px solid #E2E8F0; margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

# App Header & Branding
st.markdown("<div class='main-title'>🫁 The Master Respiratory Failure & Ventilatory Lifecycle Engine</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>From Initial Emergency Desat Presentation to Advanced Post-Ventilation ABG Titration & Troubleshooting</div>", unsafe_allow_html=True)

# Professional Badge (The Everlasting Agreement)
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Clinical Project Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Core Framework:</strong> Integrated Hypoxemia/Hypercapnia Logic, Modern Mechanical Ventilation Target Profiles
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Navigation Tabs for the Patient Lifecycle
tab_initial, tab_followup, tab_troubleshooting, tab_board_review = st.tabs([
    "🚀 Phase 1: Initial Presentation & Diagnosis", 
    "📊 Phase 2: Post-Ventilation/NIV ABG Follow-up", 
    "🔧 Phase 3: Ventilator Troubleshooting Alarms",
    "📚 Phase 4: Board Review Challenge Hub"
])

# ==============================================================================
# TAB 1: INITIAL PRESENTATION & DIAGNOSTIC MATRIX
# ==============================================================================
with tab_initial:
    col_inputs, col_expert_system = st.columns([1.1, 1.2])

    with col_inputs:
        st.markdown("<div class='section-header'>🩺 Bedside Vitals & Presentation</div>", unsafe_allow_html=True)
        with st.expander("👤 Patient Demographics & Oxygen Status", expanded=True):
            age = st.number_input("Age (Years):", min_value=18, max_value=100, value=65, key="init_age")
            weight = st.number_input("Ideal Body Weight (kg):", min_value=30, max_value=150, value=70, key="init_weight")
            spo2 = st.number_input("Oxygen Saturation (SpO2 %):", min_value=40, max_value=100, value=83)
            fio2_percent = st.number_input("Current Delivered FiO2 (%):", min_value=21, max_value=100, value=21, step=5, help="Room air is 21%.")
            jvd = st.checkbox("Jugular Venous Distension (JVD) / Peripheral Edema present")

        st.markdown("<div class='section-header'>🧠 Neurological & Mental Status Evaluation</div>", unsafe_allow_html=True)
        with st.expander("🧠 Consciousness Check (CO2 Narcosis Screening)", expanded=True):
            mental_status = st.radio(
                "What is the patient's level of consciousness?",
                ("Alert and Oriented",
                 "Somnolent / Drowsy (Arousable to speech, but drifts back to sleep)",
                 "Stuporous / Obtunded (Responds only to vigorous/painful stimuli)",
                 "Comatose (Unresponsive / High risk of CO2 Narcosis)")
            )
            airway_reflexes = st.radio("Are airway protective reflexes intact? (Gag / Cough):", ("Yes, Intact", "No, Impaired/Absent"))

        st.markdown("<div class='section-header'>🦻 Focused Chest Auscultation</div>", unsafe_allow_html=True)
        with st.expander("🫁 Auscultation Profile", expanded=True):
            chest_exam = st.radio(
                "Bilateral lung auscultation findings:",
                ("Bilateral Diffuse Wet Crackles / Crepitations",
                 "Diffuse Prolonged Expiratory Wheezing",
                 "Completely Clear Lung Sounds",
                 "Unilateral Decreased Breath Sounds")
            )

        st.markdown("<div class='section-header'>🩸 Initial Blood Gas Analysis (T0 ABG)</div>", unsafe_allow_html=True)
        with st.expander("🧪 Gas Metrics Panel (T0)", expanded=True):
            ph = st.number_input("Arterial pH (T0):", min_value=6.80, max_value=7.80, value=7.24, step=0.01)
            paco2 = st.number_input("Partial Pressure of Carbon Dioxide (PaCO2 mmHg - T0):", min_value=10, max_value=150, value=76)
            pao2 = st.number_input("Partial Pressure of Oxygen (PaO2 mmHg - T0):", min_value=30, max_value=500, value=54)
            hco3 = st.number_input("Bicarbonate (HCO3- mEq/L - T0):", min_value=5, max_value=60, value=27)

        st.markdown("<div class='section-header'>📸 Chest X-Ray Imaging Port</div>", unsafe_allow_html=True)
        with st.expander("🖼️ Radiographic Profile", expanded=True):
            uploaded_file = st.file_uploader("Upload Patient's Chest X-Ray (JPEG/PNG):", type=["jpg", "jpeg", "png"])
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Patient Chest X-Ray", use_container_width=True)
            
            xray_finding = st.selectbox(
                "Select primary radiographic finding confirmed by clinical eye:",
                ["Choose Finding...",
                 "Bilateral Diffuse Infiltrates (Bat-wing pattern / Cardiomegaly)",
                 "Bilateral Infiltrates (Patchy peripheral, without cardiomegaly / ARDS-like)",
                 "Hyperinflation (Flattened diaphragms / COPD-Asthma)",
                 "Completely Clear Lung Fields / Normal Parenchyma",
                 "Pneumothorax / Visceral Pleural Line Visited"]
            )

        st.markdown("<div class='section-header'>🧬 Pulmonary Embolism Screening (Wells' Panel)</div>", unsafe_allow_html=True)
        with st.expander("🗂️ PE Risk Checklist", expanded=True):
            c1 = st.checkbox("Clinical signs/symptoms of DVT [+3.0]")
            c2 = st.checkbox("PE is the #1 diagnosis OR equally likely [+3.0]")
            c3 = st.checkbox("Heart Rate > 100 beats per minute [+1.5]")
            c4 = st.checkbox("Immobilization (&ge; 3 days) or Surgery within past 4 weeks [+1.5]")
            c5 = st.checkbox("Previous objectively diagnosed PE or DVT [+1.5]")
            c6 = st.checkbox("Hemoptysis [+1.0]")
            c7 = st.checkbox("Malignancy under active treatment/palliation [+1.0]")

    with col_expert_system:
        st.markdown("<div class='section-header'>🧠 Master Expert Synthesis Engine</div>", unsafe_allow_html=True)
        
        # Physiological Math
        fio2_decimal = fio2_percent / 100.0
        alveolar_o2 = (fio2_decimal * (760 - 47)) - (paco2 / 0.8)
        aa_gradient = alveolar_o2 - pao2
        expected_gradient = (age / 4) + 4
        pf_ratio = pao2 / fio2_decimal

        # Summary Badge
        st.markdown(f"""
        <div style="background-color: #EEF2F6; padding: 15px; border-radius: 8px; margin-bottom: 15px; border-left: 4px solid #1E3A8A;">
            <strong>📊 Bedside Physiological Metrics:</strong><br>
            • <strong>Calculated A-a Gradient:</strong> {aa_gradient:.1f} mmHg (Expected Normal: {expected_gradient:.1f} mmHg)<br>
            • <strong>P/F Ratio:</strong> {pf_ratio:.1f}
        </div>
        """, unsafe_allow_html=True)

        # Brain Analysis of CO2 Narcosis
        if paco2 > 45 and mental_status != "Alert and Oriented":
            st.error(f"🚨 **CRITICAL STATUS DETECTED:** Hypercapnic Encephalopathy (CO2 Narcosis). High PaCO2 ({paco2} mmHg) is actively depressing the central nervous system. Immediate ventilation support needed!")

        # Differential Core Matrix
        st.write("### 🎯 Final Differential Diagnosis & Strategy:")
        
        if "Crackles" in chest_exam and "Bat-wing" in xray_finding:
            st.error("""
            💥 **PRIMARY SUSPECT: Acute Cardiogenic Pulmonary Edema (Fluid Overload)**
            * **Action:** Sit upright, high-dose IV Lasix. 
            * **Ventilatory Support:** Initiate **BiPAP**. Target a high EPAP/PEEP to recruit flooded alveoli.
            * **Initial Settings:** IPAP: 12-14 cm H2O, EPAP: 6-8 cm H2O.
            """)
        elif "Crackles" in chest_exam and "ARDS-like" in xray_finding:
            st.error(f"""
            💥 **PRIMARY SUSPECT: Acute Respiratory Distress Syndrome (ARDS) / Severe Pneumonia**
            * **Action:** Broad-spectrum IV antibiotics. Low P/F Ratio ({pf_ratio:.1f}) confirms ARDS severity.
            * **Invasive Settings (If Intubated):** Volume Control mode, Strict Tidal Volume = **{weight * 6} mL** (6 mL/kg of IBW), PEEP: 10-14 cm H2O.
            """)
        elif "Wheezing" in chest_exam or "Hyperinflation" in xray_finding:
            st.warning(f"""
            ⚠️ **PRIMARY SUSPECT: Acute Exacerbation of COPD / Severe Bronchial Asthma**
            * **Action:** Continuous nebulization (Salbutamol + Ipratropium), IV Corticosteroids. 
            * **Ventilatory Support:** If pH < 7.30, start **BiPAP**. Target SpO2: **88-92% strictly** to avoid blunting hypoxic drive.
            * **Initial Settings:** IPAP: 10-12 cm H2O, EPAP: 4-5 cm H2O (Keep EPAP low to allow prolonged expiration and avoid air-trapping / Auto-PEEP).
            """)
        elif "Clear" in chest_exam and "Clear" in xray_finding:
            st.error("""
            🚨 **PRIMARY SUSPECT: Acute Pulmonary Embolism (PE)**
            * **Why?** Classic V/Q Shunt mismatch. Patient is severely hypoxic but lungs are clean on exam and X-ray.
            * **Action:** Check Wells' score. Order immediate CTPA. If delayed or contraindicated, perform bedside Echo to screen for Right Ventricular (RV) strain, and initiate empirical therapeutic anticoagulation.
            """)
        elif "Unilateral" in chest_exam or "Pneumothorax" in xray_finding:
            st.error("""
            🚨 **CRITICAL EMERGENCY: Acute Pneumothorax**
            * **Action:** Immediate chest tube insertion. **NIV/BiPAP is strictly contraindicated** as positive pressure will expand the pneumothorax into a tension emergency!
            """)
        else:
            st.info("💡 Clinical Matrix Standby: Adjust the data on the left panel to synthesize the final pathway.")

        # Step-by-Step Oxygen Oxygenation Pathways
        st.write("#### **🥇 Step-by-Step Oxygen Titration Strategy:**")
        if spo2 < 85:
            st.markdown("🔴 **Critical Hypoxemia:** Place a Non-Rebreather Mask (NRM) immediately at 12-15 L/min. If no immediate improvement or if respiratory acidosis is present, prepare for positive pressure support (NIV or Intubation).")
        elif 85 <= spo2 < 92:
            st.markdown("🟡 **Moderate Hypoxemia:** Start Simple Face Mask (5-10 L/min) or high-flow nasal cannula. If the patient is a chronic COPD retainer, maintain a strict window of **88-92%**.")
        else:
            st.markdown("🟢 **Mild Hypoxemia:** Nasal Cannula at 2-4 L/min is sufficient. Monitor respiratory fatigue.")

        # Post Oxygen Challenge Evaluation
        st.write("#### **🔄 Post-Oxygen Challenge (What Happened Next?):**")
        post_o2 = st.selectbox(
            "Select the patient's clinical trend 20-30 minutes after oxygen therapy:",
            ["Choose Response Scenario...",
             "Scenario A: SpO2 stabilized at 91%, patient is alert, ABG parameters are stable.",
             "Scenario B: SpO2 is 96%, but patient became lethargic/obtunded. PaCO2 rose significantly.",
             "Scenario C: True Refractory Shunt. SpO2 remains < 85% despite maximum oxygen via mask."]
        )
        if "Scenario A" in post_o2:
            st.success("✅ Favorable response. Maintain current support and monitor closely.")
        elif "Scenario B" in post_o2:
            st.error("🚨 **CO2 Narcosis Triggered!** Uncontrolled high-flow oxygen has suppressed the hypoxic respiratory drive. The patient is failing. **Abort passive mask therapy immediately and transition to BiPAP or Intubation!**")
        elif "Scenario C" in post_o2:
            st.error("🚨 **Refractory Shunt Failure:** Alveoli are completely flooded or collapsed. Passive mask oxygen cannot cross the membrane. **Patient requires active recruitment via PEEP/IPAP (NIV or Intubation) immediately!**")

# ==============================================================================
# TAB 2: POST-VENTILATION/NIV ABG FOLLOW-UP & TITRATION
# ==============================================================================
with tab_followup:
    st.markdown("<div class='section-header'>📊 Advanced Ventilatory & Gas Follow-up Protocol</div>", unsafe_allow_html=True)
    st.write("Use this phase once the patient is initiated on **NIV (BiPAP)** or **Invasive Mechanical Ventilation** to track and fix the serial blood gas trends (T1 vs T0).")

    current_modality = st.radio("Current Patient Ventilatory Support Modality:", ("NIV (BiPAP)", "Mechanical Ventilation (Intubation)"), key="follow_mod")

    col_t0, col_t1 = st.columns(2)
    with col_t0:
        st.write("### 🩸 Baseline Metrics (Before Support - T0)")
        paco2_t0 = st.number_input("Baseline PaCO2 (mmHg):", min_value=15, max_value=150, value=76, key="t0_co2")
        ph_t0 = st.number_input("Baseline Arterial pH:", min_value=6.80, max_value=7.80, value=7.24, key="t0_ph")
    with col_t1:
        st.write("### 🩸 Follow-up Metrics (1 Hour on Support - T1)")
        paco2_t1 = st.number_input("Current PaCO2 (mmHg):", min_value=15, max_value=150, value=68, key="t1_co2")
        ph_t1 = st.number_input("Current Arterial pH:", min_value=6.80, max_value=7.80, value=7.29, key="t1_ph")
        pao2_t1 = st.number_input("Current PaO2 (mmHg):", min_value=15, max_value=500, value=62, key="t1_o2")

    if st.button("🧠 Synthesize Trend & Adjust Settings"):
        st.markdown("### 📋 Dr. Ihab's Clinical Action Recommendation:")
        
        # Logic for CO2 Clearance (Ventilation)
        if ph_t1 < 7.35 and paco2_t1 > 45:
            st.error("⚠️ **Persistent Respiratory Acidosis Detected:** The current ventilatory settings are insufficient to clear carbon dioxide (Hypoventilation).")
            if current_modality == "NIV (BiPAP)":
                st.markdown("""
                * **Action:** Increase **IPAP by 2 cm H2O** (e.g., if it was 12, escalate to 14). This broadens the pressure support ($\Delta P = \text{IPAP} - \text{EPAP}$), increases tidal volume, and enhances $CO_2$ clearance.
                * **Note:** Ensure there is no massive air leak around the BiPAP mask blunting volume delivery.
                """)
            else:
                st.markdown(f"""
                * **Action:** Increase the **Tidal Volume** to the higher safe limit (up to {weight * 8} mL, 8 mL/kg) OR increase the **Respiratory Rate** on the ventilator by 2-4 breaths per minute to increase Minute Ventilation ($\text{MV} = \text{TV} \times \text{RR}$).
                """)
        elif ph_t1 >= 7.35 and paco2_t1 < 45:
            st.success("✅ **Adequate Ventilation achieved:** Acidosis has resolved. Maintain current settings and evaluate for possible weaning protocols if the primary pathology is resolving.")
        elif ph_t1 > 7.45 and paco2_t1 < 35:
            st.warning("⚠️ **Respiratory Alkalosis (Over-ventilation):** The patient is blowing off too much $CO_2$.")
            if current_modality == "NIV (BiPAP)":
                st.markdown("* **Action:** Decrease **IPAP by 2 cm H2O** to safely reduce the delivered tidal volumes.")
            else:
                st.markdown("* **Action:** Reduce the ventilator **Respiratory Rate** or slightly decrease the **Tidal Volume** to avoid inducing severe alkalemia.")

        # Logic for Oxygenation (PaO2 / PEEP / FiO2)
        if pao2_t1 < 60:
            st.error(f"⚠️ **Persistent Hypoxemia (Current PaO2: {pao2_t1} mmHg):** Alveolar oxygenation is still sub-optimal.")
            if current_modality == "NIV (BiPAP)":
                st.markdown("* **Action:** Increase **EPAP by 2 cm H2O** (to increase recruitment) and increase the oxygen blender/flow rate attached to the machine.")
            else:
                st.markdown("* **Action:** Increase **PEEP by 2 cm H2O** to recruit collapsed alveoli, and temporarily raise the **FiO2** until PaO2 is stabilized between 60-80 mmHg (Target SpO2: 92-96%).")
        else:
            st.success("🟢 **Oxygenation is Safe:** PaO2 is satisfactory. Attempt to taper FiO2 below 60% as quickly as possible to prevent oxygen free-radical tissue toxicity.")

# ==============================================================================
# TAB 3: VENTILATOR TROUBLESHOOTING & CRITICAL ALARMS
# ==============================================================================
with tab_troubleshooting:
    st.markdown("<div class='section-header'>🔧 Bedside Troubleshooting: The 'Fighting the Vent' Protocol</div>", unsafe_allow_html=True)
    st.write("When a patient on mechanical ventilation triggers an alarm or shows sudden desaturation, follow this structured troubleshooting algorithm immediately:")

    alarm_type = st.selectbox(
        "Identify the active Ventilator Alarm or Clinical Event:",
        ["Select Alarm...",
         "High Peak Airway Pressure Alarm (High PIP)",
         "Low Airway Pressure / Low Minute Volume Alarm",
         "The Patient is 'Fighting the Ventilator' / Severe Asynchrony",
         "Sudden Severe Drop in SpO2 while on the Ventilator"]
    )

    st.markdown("<div class='protocol-box'>", unsafe_allow_html=True)
    if alarm_type == "High Peak Airway Pressure Alarm (High PIP)":
        st.error("""
        🚨 **High Pressure = Increased Resistance or Decreased Compliance!**
        * **Step 1:** Check a **Plateau Pressure (Pplat)** via an inspiratory hold on the ventilator.
        * **If Pplat is High (> 30 cm H2O):** The problem is compliance (the lung is stiff or filled). Rule out: **Pneumothorax, worsening Pulmonary Edema, Mainstem Intubation, or ARDS progression**.
        * **If Pplat is Normal (< 30 cm H2O):** The problem is airway resistance (obstructed flow). Rule out: **Biting the tube, mucus plugging, or severe bronchospasm**. Pass a suction catheter and give nebulized bronchodilators.
        """)
    elif alarm_type == "Low Airway Pressure / Low Minute Volume Alarm":
        st.warning("""
        ⚠️ **Low Pressure = System Leak or Disconnection!**
        * **Step 1:** Check the entire circuit from the machine to the patient's endotracheal tube.
        * **Step 2:** Look for common leak sources: **Disconnected tubing, a deflated endotracheal tube cuff (check cuff pressure), or a displaced tube**.
        * **Step 3:** If no leak is found and the patient is on BiPAP, tighten the mask harness straps or change the mask size to secure an airtight seal.
        """)
    elif alarm_type == "The Patient is 'Fighting the Ventilator' / Severe Asynchrony":
        st.info("""
        🧠 **Patient-Ventilator Asynchrony Protocol:**
        * **Clinical Review:** The patient's native respiratory drive is out of sync with the machine's breath cycle.
        * **Step 1:** Rule out pain, anxiety, or delirium. Optimize analgesia first (e.g., Fentanyl infusion).
        * **Step 2:** If it's an obstructive patient (COPD/Asthma), they may be experiencing **Auto-PEEP (Gas Trapping)**. Disconnect the circuit briefly to allow a full exhalation, then decrease the ventilator respiratory rate or increase the expiratory time (I:E Ratio to 1:3 or 1:4).
        * **Step 3:** If asynchrony persists and compromises gas exchange, optimize sedation (e.g., Propofol or Midazolam).
        """)
    elif alarm_type == "Sudden Severe Drop in SpO2 while on the Ventilator":
        st.error("""
        💥 **CRITICAL EMERGENCY: Execute the DOPE Mnemonic Instantly!**
        * **D - Displacement:** Has the endotracheal tube slipped out of the trachea or into the right mainstem bronchus? Check tube markings and auscultate.
        * **O - Obstruction:** Is the tube kinked or blocked by a massive mucus plug? Suction the patient immediately.
        * **P - Pneumothorax:** Look for unilateral absent breath sounds, tracheal deviation, or high airway pressures. Perform immediate needle decompression or insert a chest tube.
        * **E - Equipment Failure:** Is the ventilator malfunctioning or disconnected from oxygen supply lines? **Disconnect the patient from the machine and ventilate manually using an Ambu-bag with 100% oxygen until the issue is solved.**
        """)
    else:
        st.write("Select an active bedside alarm from the dropdown menu above to display the precise step-by-step troubleshooting protocol.")
    st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 4: HIGH-YIELD BOARD REVIEW CHALLENGE
# ==============================================================================
with tab_board_review:
    st.markdown("<div class='section-header'>📚 High-Yield Respiratory & Ventilatory Board Review Challenge</div>", unsafe_allow_html=True)
    st.write("Test your knowledge and prepare your residents for professional board exams with these complex, high-yield clinical scenarios.")

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
            "case": "A 58-year-old female is admitted with severe sepsis. On day 2, she develops acute respiratory distress with bilateral diffuse infiltrates on her chest X-ray. Her PaO2 is 60 mmHg while receiving oxygen via a non-rebreather mask estimated at an FiO2 of 60% (0.60). Echocardiogram shows a normal ejection fraction and no left atrial hypertension.",
            "question": "What is the P/F ratio, and what is the diagnosis based on the Berlin criteria?",
            "options": ["A) P/F ratio 250; Mild ARDS", "B) P/F ratio 100; Moderate ARDS", "C) P/F ratio 100; Severe ARDS", "D) P/F ratio 150; Moderate ARDS"],
            "correct": "B) P/F ratio 100; Moderate ARDS",
            "explanation": "P/F ratio = PaO2 / FiO2 = 60 / 0.60 = 100. According to the Berlin criteria, a P/F ratio between 100 and 200 in the presence of bilateral infiltrates and the absence of a cardiogenic cause satisfies the criteria for Moderate Acute Respiratory Distress Syndrome (ARDS)."
        },
        {
            "id": 3,
            "case": "A 68-year-old severe COPD patient is brought to Al-Ahli ED with acute somnolence. Initial ABG shows: pH 7.21, PaCO2 85 mmHg, PaO2 48 mmHg. The resident starts a Non-Rebreather Mask at 15L/min. 30 minutes later, the patient is completely unarousable to painful stimuli. A repeat ABG shows pH 7.12, PaCO2 102 mmHg.",
            "question": "What is the most appropriate next step in the clinical management of this patient?",
            "options": ["A) Increase the oxygen flow on the mask to 20L/min and add a nebulizer", "B) Initiate high-dose intravenous sodium bicarbonate infusion", "C) Initiate immediate Endotracheal Intubation and Invasive Mechanical Ventilation", "D) Apply a BiPAP mask with an IPAP of 18 cm H2O and EPAP of 5 cm H2O"],
            "correct": "C) Initiate immediate Endotracheal Intubation and Invasive Mechanical Ventilation",
            "explanation": "While BiPAP is the first-line choice for acute hypercapnic COPD exacerbations, this patient has now developed severe CO2 Narcosis and is comatose (unarousable to pain). A comatose state with loss of airway protective reflexes is an absolute contraindication for non-invasive ventilation (BiPAP). Immediate intubation is required."
        }
    ]

    if 'master_resp_q' not in st.session_state:
        st.session_state.master_resp_q = random.choice(resp_pool)
        
    if st.button("🔄 Generate Another Advanced Board Question", key="gen_q"):
        st.session_state.master_resp_q = random.choice(resp_pool)
        
    current_q = st.session_state.master_resp_q
    
    st.warning(f"**Clinical Scenario:** {current_q['case']}")
    st.write(f"❓ **Question:** {current_q['question']}")
    
    user_ans = st.radio("Select your answer from below:", current_q['options'], key=f"mq_{current_q['id']}")
    
    if st.expander("🔑 Reveal Correct Answer & Dr. Ihab's Clinical Explanation"):
        if user_ans == current_q['correct']:
            st.success(f"🎯 **Correct!** The answer is {current_q['correct']}")
        else:
            st.error(f"❌ **Incorrect Choice.** The correct answer is {current_q['correct']}")
        st.markdown(f"**Explanation:** {current_q['explanation']}")

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 12px;'>Al-Ahli Hospital Respiratory Center App © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
