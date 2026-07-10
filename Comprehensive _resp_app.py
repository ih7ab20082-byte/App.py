import streamlit as st
import random
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="Al-Ahli Hospital Comprehensive Respiratory Command Center",
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
    .result-box { background-color: #F8FAFC; padding: 20px; border-radius: 8px; border: 1px solid #E2E8F0; margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

# App Header & Branding
st.markdown("<div class='main-title'>🫁 The Master Respiratory & Hypoxemia Expert System</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Full Clinical Approach: Integrates Vitals, Chest Exam, Complete ABG Synthesis, Chest X-ray, and Differential Diagnosis</div>", unsafe_allow_html=True)

# Professional Badge (The Everlasting Agreement)
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Clinical Project Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Core Engine:</strong> AI-Driven Differential Matrix (COPD vs Asthma vs Pulmonary Edema vs PE vs ARDS)
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Split Screen Design
col_inputs, col_expert_system = st.columns([1.1, 1.2])

# ==============================================================================
# LEFT COLUMN: DATA ACQUISITION (VITALS, ABG, EXAM, & X-RAY)
# ==============================================================================
with col_inputs:
    
    # 1. CLINICAL SITUATION & VITALS
    st.markdown("<div class='section-header'>🩺 1. Bedside Vitals & Clinical Presentation</div>", unsafe_allow_html=True)
    with st.expander("👤 Vitals & History", expanded=True):
        age = st.number_input("Age (Years):", min_value=18, max_value=100, value=65)
        weight = st.number_input("Ideal Body Weight (kg):", min_value=30, max_value=150, value=70)
        spo2 = st.number_input("Oxygen Saturation (SpO2 %):", min_value=40, max_value=100, value=84)
        fio2_percent = st.number_input("Current FiO2 (%):", min_value=21, max_value=100, value=21, step=5, help="Room air is 21%.")
        onset = st.radio("Onset of Dyspnea:", ("Hyperacute (Seconds to Minutes)", "Acute/Subacute (Hours to Days)"))
        jvd = st.checkbox("Jugular Venous Distension (JVD) / Peripheral Edema present")

    # 2. CHEST EXAMINATION
    st.markdown("<div class='section-header'>🦻 2. Focused Chest Auscultation</div>", unsafe_allow_html=True)
    with st.expander("🫁 Auscultation Profile", expanded=True):
        chest_exam = st.radio(
            "Bilateral lung auscultation findings:",
            ("Bilateral Diffuse Wet Crackles / Crepitations",
             "Diffuse Prolonged Expiratory Wheezing",
             "Completely Clear Lung Sounds",
             "Unilateral Decreased Breath Sounds")
        )

    # 3. ABG TRIPLE SYNTHESIS PANEL
    st.markdown("<div class='section-header'>🩸 3. Advanced ABG/VBG Input</div>", unsafe_allow_html=True)
    with st.expander("🧪 Acid-Base & Gas Metrics", expanded=True):
        ph = st.number_input("Arterial pH:", min_value=6.80, max_value=7.80, value=7.26, step=0.01)
        paco2 = st.number_input("Partial Pressure of Carbon Dioxide (PaCO2 mmHg):", min_value=10, max_value=150, value=65)
        pao2 = st.number_input("Partial Pressure of Oxygen (PaO2 mmHg):", min_value=30, max_value=500, value=55)
        hco3 = st.number_input("Bicarbonate (HCO3- mEq/L):", min_value=5, max_value=60, value=28)

    # 4. CHEST X-RAY DIAGNOSTIC PORT (NEW)
    st.markdown("<div class='section-header'>📸 4. Chest X-Ray Imaging Port</div>", unsafe_allow_html=True)
    with st.expander("🖼️ Radiographic Analysis & Image Upload", expanded=True):
        uploaded_file = st.file_uploader("Upload Patient's Chest X-Ray (JPEG/PNG):", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Patient Chest X-Ray", use_container_width=True)
        
        xray_finding = st.selectbox(
            "Select primary radiographic finding confirmed by clinical eye:",
            ["Choose Finding...",
             "Bilateral Diffuse Infiltrates (Bat-wing pattern / Cardiomegaly)",
             "Bilateral Infiltrates (Patchy peripheral, without cardiomegaly / ARDS-like)",
             "Hyperinflation (Flattened diaphragms, increased retrosternal space / COPD-Asthma)",
             "Completely Clear Lung Fields / Normal Parenchyma",
             "Pneumothorax / Visceral Pleural Line Visited"]
        )

# ==============================================================================
# RIGHT COLUMN: THE AI EXPERT BRAIN & DIFFERENTIAL MATRIX APPROACH
# ==============================================================================
with col_expert_system:
    st.markdown("<div class='section-header'>🧠 5. Master Expert Analysis & Differential Diagnostic Matrix</div>", unsafe_allow_html=True)
    
    # --- INTERNAL PHYSIOLOGICAL CALCULATIONS ---
    fio2_decimal = fio2_percent / 100.0
    alveolar_o2 = (fio2_decimal * (760 - 47)) - (paco2 / 0.8)
    aa_gradient = alveolar_o2 - pao2
    expected_gradient = (age / 4) + 4
    pf_ratio = pao2 / fio2_decimal

    # --- ABG ACID-BASE INTERPRETATION ENGINE ---
    abg_status = ""
    if ph < 7.35:
        if paco2 > 45:
            abg_status = "Acute Respiratory Acidosis"
            if hco3 > 26: abg_status += " with partial metabolic compensation (Chronic Retainer component)"
        elif hco3 < 22:
            abg_status = "Primary Metabolic Acidosis"
    elif ph > 7.45:
        if paco2 < 35: abg_status = "Acute Respiratory Alkalosis"
        elif hco3 > 26: abg_status = "Primary Metabolic Alkalosis"
    else:
        abg_status = "Normal pH or Fully Compensated Mixed Acid-Base Disorder"

    # --- DISPLAY HIGH-LEVEL METRICS ---
    st.markdown(f"""
    <div style="background-color: #EEF2F6; padding: 12px; border-radius: 8px; margin-bottom: 15px; border-left: 4px solid #1E3A8A;">
        <strong>📊 Physiological Summary:</strong><br>
        • <strong>Acid-Base Status:</strong> {abg_status}<br>
        • <strong>Calculated A-a Gradient:</strong> {aa_gradient:.1f} mmHg (Expected Normal for age: {expected_gradient:.1f} mmHg)<br>
        • <strong>P/F Ratio:</strong> {pf_ratio:.1f}
    </div>
    """, unsafe_allow_html=True)

    # --- THE COMPREHENSIVE CLINICAL DIFFERENTIAL MATRIX ---
    st.write("### 🎯 Final Differential Diagnosis & Thinking Matrix:")
    
    # 1. ACUTE CARDIOGENIC PULMONARY EDEMA
    if "Crackles" in chest_exam and "Bat-wing" in xray_finding:
        st.error("""
        💥 **PRIMARY SUSPECT: Acute Cardiogenic Pulmonary Edema (Fluid Overload)**
        * **Why?** Combination of bilateral diffuse crackles, high A-a gradient, and classic radiographic pulmonary congestion (Bat-wing/Cardiomegaly).
        * **Immediate Action Plan:** 
            1. Sit the patient fully upright.
            2. Give IV Furosemide (Lasix) aggressive bolus (e.g., 40-80mg or double their home dose).
            3. Initiate **NIV (BiPAP)** immediately to push fluid out of alveoli. 
            4. **BiPAP Settings:** IPAP: 12 cm H2O, EPAP: 6-8 cm H2O (High EPAP/PEEP is key to recruit flooded alveoli).
        """)

    # 2. ARDS vs SEVERE LOBAR PNEUMONIA
    elif "Crackles" in chest_exam and "ARDS-like" in xray_finding:
        st.error(f"""
        💥 **PRIMARY SUSPECT: Acute Respiratory Distress Syndrome (ARDS) / Severe Pneumonia**
        * **Why?** Diffuse crackles with patchy infiltrates without overt cardiomegaly, and a severely low P/F Ratio of **{pf_ratio:.1f}** (<300 signifies ARDS).
        * **Immediate Action Plan:**
            1. Start empiric broad-spectrum IV antibiotics immediately.
            2. High risk of non-invasive ventilatory failure. If intubated, utilize **Strict Lung-Protective Ventilation Settings**: Tidal Volume = **{weight * 6} mL** (6 mL/kg), High PEEP (10-14 cm H2O).
        """)

    # 3. COPD / ASTHMA ACUTE EXACERBATION
    elif "Wheezing" in chest_exam or "Hyperinflation" in xray_finding:
        st.warning(f"""
        ⚠️ **PRIMARY SUSPECT: Acute Exacerbation of COPD / Severe Bronchial Asthma**
        * **Why?** Diffuse expiratory wheezing, hyperinflated lungs on X-ray, and profound respiratory acidosis (pH: {ph}, PaCO2: {paco2} mmHg) proving acute ventilatory fatigue.
        * **Immediate Action Plan:**
            1. Continuous nebulization with SABA (Salbutamol) + SAMA (Ipratropium Bromide).
            2. Administer IV Corticosteroids (Hydrocortisone 100mg or Methylprednisolone).
            3. **Ventilatory Protocol:** Since pH is {ph} (Acidotic) and patient is somnolent, initiate **NIV (BiPAP)**. 
            4. **BiPAP Settings:** IPAP: 10-12 cm H2O, EPAP: 4-5 cm H2O (Keep EPAP low to allow expiration and prevent air-trapping / Auto-PEEP). Target SpO2: **88-92% strictly**.
        """)

    # 4. PULMONARY EMBOLISM (PE)
    elif "Clear" in chest_exam and "Clear" in xray_finding:
        st.error("""
        🚨 **PRIMARY SUSPECT: Acute Pulmonary Embolism (PE)**
        * **Why?** The classic clinical paradox! The patient is profoundly hypoxemic with an elevated A-a gradient, but the **lungs are completely clear to auscultation and the X-ray is normal**. Air is moving, but blood flow is blocked!
        * **Immediate Action Plan:**
            1. Calculate the full Wells' Criteria.
            2. Order an emergent **CTPA**. If contraindicated due to renal function or unavailable at this hour, request an urgent **Bedside Echocardiography** to evaluate for acute Right Ventricular (RV) strain or McConnell's sign.
            3. Start empirical Therapeutic Anticoagulation (LMWH Enoxaparin) if no absolute contraindications exist.
        """)

    # 5. PNEUMOTHORAX EMERGENCY
    elif "Unilateral" in chest_exam or "Pneumothorax" in xray_finding:
        st.dark_markdown("""
        🚨 **CRITICAL EMERGENCY: Acute Pneumothorax**
        * **Why?** Unilateral loss of breath sounds combined with a clear visceral pleural line on X-ray.
        * **Immediate Action Plan:** Immediate needle decompression if hemodynamically unstable (Tension Pneumothorax), followed by urgent insertion of a Tube Thoracostomy (Chest Tube). **Avoid BiPAP/NIV as positive pressure will worsen a pneumothorax instantly!**
        """)
        
    else:
        st.info("💡 **Clinical Matrix Standby:** Please enter more clinical coordinates (Exam findings, ABG, and X-ray choices) on the left panel to synthesize a targeted diagnostic pathway.")

    # ------------------------------------------------------------------
    # POST-OXYGENATION DYNAMIC SIMULATOR (THE RESPONSE TRACKER)
    # ------------------------------------------------------------------
    st.markdown("---")
    st.markdown("<div class='section-header'>🔄 6. Dynamic Response Tracker (Post-Oxygen Challenge)</div>", unsafe_allow_html=True)
    
    post_o2_choice = st.selectbox(
        "Evaluate the patient 20-30 minutes after initiating your oxygen/NIV plan:",
        ["Choose response scenario...",
         "Response A: SpO2 stabilized at 91%, pH improved to 7.32, patient is awake and speaking in sentences.",
         "Response B: SpO2 is 96%, but patient is now obtunded and lethargic. Repeat PaCO2 skyrocketed to 88 mmHg.",
         "Response C: Severe Refractory Hypoxemia. SpO2 remains trapped at 82% despite 100% FiO2 on Non-Rebreather Mask."]
    )

    if "Response A" in post_o2_choice:
        st.success("🟢 **Favorable Response:** Patient is ventilating and clearing CO2. Maintain current oxygenation/bronchodilator regimen. Monitor serial ABGs closely.")
    elif "Response B" in post_o2_choice:
        st.error("🚨 **CO2 NARCOSIS / RESPIRATORY ARREST RISK:** Hyperoxia has blunted the hypoxic respiratory drive. The patient is losing consciousness due to advanced respiratory acidosis. **Abort passive mask oxygenation immediately and perform Endotracheal Intubation!**")
    elif "Response C" in post_o2_choice:
        st.error("🚨 **REFRACTORY SHUNT FAILURE:** Alveoli are completely closed or filled with fluid. Oxygen cannot dissolve. Patient needs invasive mechanical ventilation with recruitment maneuvers or urgent ICU admission for protective high PEEP ventilation.")

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 12px;'>Al-Ahli Hospital Advanced Respiratory Center App © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
