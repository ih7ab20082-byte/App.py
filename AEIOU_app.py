import streamlit as st
import math

# Page Configuration
st.set_page_config(
    page_title="Al-Ahli Emergency Dialysis Predictor (AEIOU)",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for Emergency and Intensive Care Rigor
st.markdown("""
    <style>
    .main-title { font-size:30px !important; font-weight: bold; color: #991B1B; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:15px !important; color: #4B5563; text-align: center; margin-bottom: 25px; font-style: italic; }
    .branding-bar { background-color: #FEF2F2; padding: 20px; border-radius: 10px; border-left: 6px solid #991B1B; margin-bottom: 25px; }
    .branding-bar strong { color: #991B1B !important; font-weight: bold; }
    .branding-text { color: #1F2937 !important; font-size: 15px !important; line-height: 1.6; }
    .section-header { font-size:20px !important; font-weight: bold; color: #991B1B; margin-top: 15px; margin-bottom: 15px; border-bottom: 2px solid #E5E7EB; padding-bottom: 5px; }
    .status-box { padding: 15px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #E5E7EB; }
    .board-header { font-size:22px !important; font-weight: bold; color: #D97706; margin-top: 30px; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<div class='main-title'>🚨 Al-Ahli Hospital Emergency Dialysis Predictor (AEIOU)</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Advanced Inpatient Decision Support System (CDSS) with Integrated Kinetic GFR & Toxic Ingestion Panel</div>", unsafe_allow_html=True)

# Professional Branding Block
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Project Founder & Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Clinical Core:</strong> KDIGO Acute Kidney Injury Criteria, Kinetic GFR (kGFR) Tracking, AEIOU Hyperacute Dialysis Framework
    </div>
</div>
""", unsafe_allow_html=True)

# Layout Split
col_input, col_dashboard = st.columns([1, 1.2])

# ==============================================================================
# LEFT COLUMN: CRITICAL LABS & RECOGNITION TRIGGERS
# ==============================================================================
with col_input:
    st.markdown("<div class='section-header'>📋 1. Kinetic GFR & Baseline Labs</div>", unsafe_allow_html=True)
    
    # Kinetic GFR Input Block to fix unstable tracking issues
    baseline_creat = st.number_input("Baseline/Yesterday Creatinine (mg/dL):", min_value=0.4, max_value=15.0, value=1.2, step=0.1)
    current_creat = st.number_input("Current/Today Creatinine (mg/dL):", min_value=0.4, max_value=15.0, value=2.6, step=0.1)
    time_interval = st.number_input("Time Interval Between Samples (Hours):", min_value=4, max_value=72, value=24, step=4)
    
    # Electrolytes and Blood Gas
    ph = st.number_input("Arterial pH [Normal: 7.35 - 7.45]:", min_value=6.50, max_value=7.80, value=7.21, step=0.01)
    hco3 = st.number_input("Serum Bicarbonate (HCO3- mEq/L):", min_value=2.0, max_value=40.0, value=12.0, step=1.0)
    potassium = st.number_input("Serum Potassium (K+ mEq/L):", min_value=2.0, max_value=9.0, value=6.2, step=0.1)
    bun = st.number_input("Blood Urea Nitrogen (BUN mg/dL):", min_value=5, max_value=300, value=95, step=5)
    
    st.markdown("<div class='section-header'>🫁 2. ECG Guard & Volume Status</div>", unsafe_allow_html=True)
    ecg_changes = st.selectbox(
        "Hyperkalemia ECG Manifestations:",
        ["No hyperkalemic ECG changes",
         "Peaked/Tented T-waves only",
         "PR prolongation / Flat P waves",
         "Severe: QRS widening / Sine wave pattern"]
    )
    fluid_overload_refractory = st.checkbox("Refractory Fluid Overload (Acute Pulmonary Edema unresponsive to high-dose IV Diuretics)", value=False)
    urine_output_24h = st.number_input("Total 24-Hour Urine Output (mL):", min_value=0, max_value=5000, value=250, step=50)
    
    st.markdown("<div class='section-header'>🧪 3. Ingestion & Symptomatic Uremia</div>", unsafe_allow_html=True)
    toxic_substance = st.selectbox(
        "Suspected Dialyzable Ingestion (The 'I' in AEIOU):",
        ["None / Not Applicable", 
         "Lithium Tox (Level > 4.0 mEq/L or severe neuro signs)", 
         "Toxic Alcohol (Methanol / Ethylene Glycol with high anion gap)", 
         "Salicylates / Aspirin Overdose (Level > 100 mg/dL or severe acidosis)", 
         "Theophylline / Phenobarbital Severe Toxicity"]
    )
    has_uremic_encephalopathy = st.checkbox("Uremic Encephalopathy (Altered mental status, severe asterixis)", value=False)
    has_uremic_pericarditis = st.checkbox("Uremic Pericarditis / Friction Rub", value=False)

    # ==========================================================================
    # INTERNAL LOGIC & MATHEMATICS
    # ==========================================================================
    # Kinetic Creatinine Clearance / GFR Estimation Formula (Simplified for Acute Shifts)
    # Delta Creatinine per hour
    delta_cr = (current_creat - baseline_creat) / time_interval
    # Kinetic index approximation: if creatinine rises rapidly, effective clearance drops towards zero
    if current_creat > 0:
        kinetic_clearance_factor = max(0.0, 1.0 - (delta_cr / 0.5)) # 0.5 mg/dL/hr is absolute cessation of clearance
    else:
        kinetic_clearance_factor = 1.0

# ==============================================================================
# RIGHT COLUMN: EMERGENCY DIALYSIS SCOREBOARD & TRIGGER ANALYSIS
# ==============================================================================
with col_dashboard:
    st.markdown("<div class='section-header'>⚡ Hyperacute Dialysis Indication Scoreboard</div>", unsafe_allow_html=True)
    
    aeiou_triggers = []
    urgency_score = 0
    
    # A - Acidosis
    if ph < 7.15 or hco3 < 10:
        aeiou_triggers.append("🔴 **[A] - Severe Refractory Metabolic Acidosis**")
        urgency_score += 3
    elif ph < 7.30:
        urgency_score += 1
        
    # E - Electrolytes
    if potassium >= 6.5 or "Severe" in ecg_changes:
        aeiou_triggers.append("🔴 **[E] - Malignant Hyperkalemia / ECG Instability**")
        urgency_score += 3
    elif potassium >= 5.5 or "Peaked" in ecg_changes:
        urgency_score += 1
        
    # I - Ingestion
    if toxic_substance != "None / Not Applicable":
        aeiou_triggers.append(f"🔴 **[I] - Toxic Ingestion Verified: {toxic_substance}**")
        urgency_score += 3
        
    # O - Overload
    if fluid_overload_refractory:
        aeiou_triggers.append("🔴 **[O] - Refractory Volume Overload & Pulmonary Edema**")
        urgency_score += 3
    elif urine_output_24h < 400:
        urgency_score += 1
        
    # U - Uremia
    if has_uremic_encephalopathy or has_uremic_pericarditis or bun > 100:
        aeiou_triggers.append("🔴 **[U] - Advanced Symptomatic Uremic End-Organ Injury**")
        urgency_score += 3
    elif bun > 60:
        urgency_score += 1

    # Display Urgency Level Matrix
    st.markdown("### 🚨 Emergency Status & Action Matrix")
    
    if len(aeiou_triggers) > 0:
        if urgency_score >= 5 or "Severe" in ecg_changes or fluid_overload_refractory:
            status_color = "#FEF2F2"
            border_color = "#991B1B"
            text_recommend = "❌ **CRITICAL EMERGENCE:** Absolute criteria met. Immediately activate the Nephrology Dialysis team on-call. Secure central venous access (dialysis catheter). Prepare for imminent ultrafiltration."
        else:
            status_color = "#FFFBEB"
            border_color = "#D97706"
            text_recommend = "⚠️ **URGENT THREAT:** Dynamic criteria building up. Initiate aggressive medical shifting, hold all nephrotoxins, and re-check serum chemistry in 4 hours."
    else:
        status_color = "#F0FDF4"
        border_color = "#15803D"
        text_recommend = "🟢 **STABLE RANGES:** No immediate indications for emergent renal replacement therapy. Monitor fluid balances closely."
        
    st.markdown(f"""
    <div class='status-box' style='background-color: {status_color}; border: 2px solid {border_color};'>
        <strong>Clinical Direction Strategy:</strong><br>{text_recommend}
    </div>
    """, unsafe_allow_html=True)

    # TABS FOR METABOLIC BREAKDOWN
    with st.container():
        tab_kinetic, tab_shift, tab_tox = st.tabs(["📉 Real-Time Kinetic GFR", "🍏 Electrolyte Guard", "🧪 Dialyzable Toxin Data"])
        
        with tab_kinetic:
            st.markdown("### 📉 Acute Kidney Injury Kinetic Analysis")
            st.write(f"⏱️ **Creatinine Accumulation Velocity:** `{delta_cr * 24:.2f} mg/dL / 24 hours`")
            
            # Dynamic warning block based on user's image logic
            if delta_cr > 0.03:
                st.error(f"⚠️ **WARNING:** True clearance is dropping precipitously! The current effective clearance index is only **{kinetic_clearance_factor * 100:.0f}%** of expected function due to hyperacute accumulation.")
            else:
                st.success("Clearance kinetics are within predictable steady-state boundaries.")
                
        with tab_shift:
            st.markdown("### 🍏 Emergency Anti-Hyperkalemia Command")
            st.write(f"📊 **Current Serum Potassium:** `{potassium} mEq/L` (ECG Status: `{ecg_changes}`)")
            
            if "Severe" in ecg_changes or potassium >= 6.0:
                st.markdown("""
                🚨 **MANDATORY MEMBRANE STABILIZATION ORDER:**
                * **First Priority:** Give **10 mL of 10% Calcium Gluconate IV** over 3-5 minutes immediately to protect the myocardium against ventricular fibrillation.
                * **Shifting Therapy:** 10 Units of Regular Insulin + 50 mL of Dextrose 50% IV.
                """)
            else:
                st.write("🟢 No emergency cardiac membrane stabilization triggered.")

        with tab_tox:
            st.markdown("### 🧪 Dialyzable Ingestion Clearances")
            if toxic_substance != "None / Not Applicable":
                st.warning(f"🎯 **Target Clearance Protocol Enabled for:** `{toxic_substance}`")
                st.markdown("""
                * **Mechanism:** Hemodialysis provides exceptional clearance for low molecular weight, water-soluble molecules with low volumes of distribution.
                * **Note:** Intermittent hemodialysis is superior to CRRT for hyperacute toxin removal (especially in Salicylate and Lithium poisonings).
                """)
            else:
                st.write("🟢 No toxic dialyzable ingestion selected.")

# ==============================================================================
# HIGH-YIELD BOARD EXAM REVIEW MATERIAL
# ==============================================================================
st.markdown("---")
st.markdown("<div class='board-header'>🎓 High-Yield Board-Level Review (Al-Ahli Scientific Research Club)</div>", unsafe_allow_html=True)

with st.expander("❓ Click to Reveal the Board Question & Rationale"):
    st.markdown("""
    **Clinical Scenario:** A 42-year-old female is brought to the Al-Ahli emergency department by her family due to profound lethargy and persistent vomiting. The family notes she has a history of bipolar affective disorder. On presentation, she is confused and disoriented. Labs reveal: Serum Creatinine **2.9 mg/dL** (Baseline was 0.8 mg/dL 48 hours ago), Serum Potassium **4.9 mEq/L**, Arterial pH **7.32**, and a **Serum Lithium Level of 4.8 mEq/L**. 
    
    **According to professional toxicological and nephrological clinical guidelines, what is the most appropriate definitive management step for this patient?**
    
    * **A)** Aggressive intravenous volume expansion with 0.9% Normal Saline alone.
    * **B)** Emergency initiation of Intermittent Hemodialysis (IHD).
    * **C)** Administration of intravenous Sodium Bicarbonate to alkalinize the urine.
    * **D)** Continuous Renal Replacement Therapy (CRRT) at a low filtration rate.
    
    ---
    
    ### 📝 Comprehensive Scientific Rationale:
    * **The Correct Answer is B.** Lithium toxicity is a classic indication for the **[I] - Ingestion** criteria in the AEIOU framework. Emergent hemodialysis is strongly indicated for lithium toxicity when serum levels exceed **4.0 mEq/L**, or if the level is $> 2.5\ mEq/L$ accompanied by severe neurological symptoms or acute kidney injury ($AKI$) that limits the body's ability to clear the drug.
    * **Why other options are incorrect:** Volume expansion (Option A) is useful for mild toxicity, but with an explicit level of 4.8 and severe neurological changes, it is insufficient. Intermittent Hemodialysis (Option B) is highly preferred over CRRT (Option D) for hyperacute intoxication because it maximizes the clearance velocity of Lithium from the vascular compartment.
    """)

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 11px;'>Al-Ahli Hospital Internal Medicine CDSS Platforms © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
