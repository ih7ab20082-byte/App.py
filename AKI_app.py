import streamlit as st
import random

# Page Configuration
st.set_page_config(
    page_title="Al-Ahli Hospital AKI & Renal Dosing Center",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Branding and Signature Style
st.markdown("""
    <style>
    .main-title { font-size:32px !important; font-weight: bold; color: #1E3A8A; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:16px !important; color: #4B5563; text-align: center; margin-bottom: 25px; font-style: italic; }
    .branding-bar { background-color: #F3F4F6; padding: 20px; border-radius: 10px; border-left: 6px solid #2563EB; margin-bottom: 25px; }
    .branding-bar strong { color: #1E3A8A !important; font-weight: bold; }
    .branding-text { color: #1F2937 !important; font-size: 16px !important; line-height: 1.6; }
    .section-header { font-size:22px !important; font-weight: bold; color: #1E3A8A; margin-top: 15px; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# App Header & Branding
st.markdown("<div class='main-title'>⚡ Acute Kidney Injury (AKI) & Renal Dosing Center</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Local Adaptive Protocol & Drug Dosing Engine for Al-Ahli Hospital Ward Protocols</div>", unsafe_allow_html=True)

# Professional Badge
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Clinical Lead & Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Framework:</strong> 2012 KDIGO Clinical Practice Guidelines for Acute Kidney Injury
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Layout Configuration: Split Screen
col_input, col_output = st.columns([1, 1.2])

# ==============================================================================
# LEFT COLUMN: Patient Metrics, Kinetics & Input Analytics
# ==============================================================================
with col_input:
    st.markdown("<div class='section-header'>🧪 1. Patient Renal Metrics & Function</div>", unsafe_allow_html=True)
    
    with st.expander("👤 Patient Vital Parameters", expanded=True):
        age = st.number_input("Age (Years):", min_value=18, max_value=110, value=60)
        gender = st.radio("Gender:", ("Male", "Female"))
        weight = st.number_input("Actual Body Weight (kg):", min_value=35, max_value=220, value=75)
        
    with st.expander("📊 Creatinine Kinetics (KDIGO Staging)", expanded=True):
        baseline_cr = st.number_input("Baseline Serum Creatinine (mg/dL) - *Prior stable value or lowest known*:", min_value=0.3, max_value=12.0, value=1.0, step=0.1)
        current_cr = st.number_input("Current Serum Creatinine (mg/dL):", min_value=0.3, max_value=12.0, value=2.2, step=0.1)
        urine_output = st.radio("Urine Output History over the last 6-24 hours:",
                                ("Normal (> 0.5 mL/kg/h)", 
                                 "< 0.5 mL/kg/h for 6 - 12 hours", 
                                 "< 0.5 mL/kg/h for ≥ 12 hours", 
                                 "Anuria / Severe Oliguria (< 0.3 mL/kg/h) for ≥ 24h or Anuria ≥ 12h"))

    # Calculate CrCl using Cockcroft-Gault Equation
    if gender == "Male":
        crcl = ((140 - age) * weight) / (72 * current_cr)
    else:
        crcl = (((140 - age) * weight) / (72 * current_cr)) * 0.85

    # ADVANCED NEPHROLOGY TOOL: DYNAMIC FENA & FEUREA CALCULATOR
    st.markdown("---")
    st.markdown("<div class='section-header'>🔬 2. Advanced Diagnostic Calculator (FeNa / FeUrea)</div>", unsafe_allow_html=True)
    with st.expander("🧬 Etiology Differentiation (Pre-renal vs. ATN)", expanded=False):
        st.info("💡 Fill this optional panel to differentiate Pre-renal Azotemia from Acute Tubular Necrosis (ATN).")
        is_on_diuretic = st.radio("Is the patient currently taking a Loop Diuretic (e.g., Furosemide)?", ("No", "Yes"))
        
        u_na = st.number_input("Urine Sodium (mEq/L):", min_value=0.0, max_value=200.0, value=0.0)
        p_na = st.number_input("Plasma Sodium (mEq/L):", min_value=100.0, max_value=180.0, value=140.0)
        u_cr = st.number_input("Urine Creatinine (mg/dL):", min_value=0.0, max_value=400.0, value=0.0)
        p_cr = current_cr
        
        u_urea = st.number_input("Urine Urea Nitrogen (mg/dL) - *Required if on diuretic*:", min_value=0.0, max_value=2000.0, value=0.0)
        p_urea = st.number_input("Blood Urea Nitrogen (BUN) (mg/dL):", min_value=0.0, max_value=200.0, value=40.0)

    st.markdown("---")
    st.markdown("<div class='section-header'>💊 3. Antibiotic Selection & Dosing Engine</div>", unsafe_allow_html=True)
    selected_abx = st.selectbox(
        "Select Antibiotic to Calculate Renal Dose Adjustment:",
        [
            "Tazocin (Piperacillin/Tazobactam)", 
            "Meropenem (Meronem)", 
            "Vancomycin", 
            "Colistin (CMS)", 
            "Tigecycline (Tygacil)",
            "Zavicefta (Ceftazidime/Avibactam)",
            "Ceftriaxone (Rocephin)"
        ]
    )

# ==============================================================================
# RIGHT COLUMN: Diagnostic Results, PK/PD Engine & Dynamic MCQ Hub
# ==============================================================================
with col_output:
    st.markdown("<div class='section-header'>🎯 4. Automated KDIGO Diagnosis & Staging</div>", unsafe_allow_html=True)
    
    # KDIGO Logic Calculation
    cr_ratio = current_cr / baseline_cr
    cr_diff = current_cr - baseline_cr
    kdigo_stage = 0
    kdigo_criteria = "No AKI detected based on provided creatinine values."
    
    if cr_ratio >= 3.0 or current_cr >= 4.0 or "Anuria" in urine_output:
        kdigo_stage = 3
        kdigo_criteria = "Creatinine ≥ 3.0x baseline OR Current Creatinine ≥ 4.0 mg/dL OR Severe Oliguria/Anuria."
    elif 2.0 <= cr_ratio < 3.0 or "≥ 12 hours" in urine_output:
        kdigo_stage = 2
        kdigo_criteria = "Creatinine 2.0x to 2.9x relative to baseline value."
    elif 1.5 <= cr_ratio < 2.0 or cr_diff >= 0.3 or "6 - 12 hours" in urine_output:
        kdigo_stage = 1
        kdigo_criteria = "Creatinine increase ≥ 0.3 mg/dL within 48h OR 1.5x-1.9x baseline increase."

    if kdigo_stage == 0:   st.success("🟢 **Diagnosis: No Acute Kidney Injury Criteria Met**")
    elif kdigo_stage == 1: st.warning("⚠️ **Diagnosis: ACUTE KIDNEY INJURY - KDIGO STAGE 1**")
    elif kdigo_stage == 2: st.error("🚨 **Diagnosis: ACUTE KIDNEY INJURY - KDIGO STAGE 2**")
    elif kdigo_stage == 3: 
        st.error("💥 **CRITICAL: ACUTE KIDNEY INJURY - KDIGO STAGE 3**")
        st.markdown("🔥 **High Risk of Renal Replacement Therapy (Hemodialysis) Allocation! Evaluate for AEIOU Emergent Indications.**")

    st.info(f"**KDIGO Criteria Analysis:** {kdigo_criteria}")
    st.metric(label="Calculated Current Creatinine Clearance (CrCl via Cockcroft-Gault):", value=f"{crcl:.1f} mL/min")

    # Process Advanced Diagnostics (FeNa vs FeUrea)
    if u_na > 0 and u_cr > 0:
        st.markdown("#### 🧬 Dynamic Nephrology Diagnostics Output:")
        fena = (u_na * p_cr) / (p_na * u_cr) * 100
        
        if is_on_diuretic == "Yes" and u_urea > 0 and p_urea > 0:
            feurea = (u_urea * p_cr) / (p_urea * u_cr) * 100
            st.write(f"📊 **Calculated FeUrea:** {feurea:.1f}% *(Preferred index: Patient is on loop diuretics)*")
            if feurea < 35:
                st.success("🟢 **Diagnostic Impression:** Consistent with **Pre-renal Azotemia** (Hypoperfusion). Fluid resuscitation indicated if no fluid overload signs.")
            else:
                st.error("🔴 **Diagnostic Impression:** Consistent with **Intrinsic Renal Injury / Acute Tubular Necrosis (ATN)**.")
        else:
            st.write(f"📊 **Calculated FeNa:** {fena:.1f}%")
            if is_on_diuretic == "Yes":
                st.warning("⚠️ *Warning: FeNa is clinically unreliable because the patient is taking active loop diuretics. Please input Urine Urea to calculate FeUrea.*")
            
            if fena < 1.0:
                st.success("🟢 **Diagnostic Impression:** Consistent with **Pre-renal Azotemia** (FeNa < 1%).")
            elif fena > 2.0:
                st.error("🔴 **Diagnostic Impression:** Consistent with **Intrinsic Renal Injury / ATN** (FeNa > 2%).")
            else:
                st.warning("🟡 **Diagnostic Impression:** Indeterminate grey-zone (FeNa 1-2%). Correlation with clinical context required.")

    # ------------------------------------------------------------------
    # RENAL DOSING OUTPUT ENGINE
    # ------------------------------------------------------------------
    st.markdown("---")
    st.markdown("<div class='section-header'>📋 5. Adjusted Pharmacokinetic Dosing Guide</div>", unsafe_allow_html=True)
    st.write(f"### 🧪 Targeted Drug: **{selected_abx}**")
    st.caption(f"Calculated for Weight: {weight} kg | Current GFR Estimate: {crcl:.1f} mL/min")

    if selected_abx == "Tazocin (Piperacillin/Tazobactam)":
        st.info("💡 *Standard Normal Dose:* 4.5g IV q6h")
        if crcl > 40:      st.success("🟢 **No Adjustment Needed:** Give **4.5 g IV every 6 hours**.")
        elif 20 <= crcl <= 40: st.warning("⚠️ **Renal Adjusted Dose:** Give **3.375 g IV every 6 hours**.")
        else:              st.error("🚨 **Severe Renal Dosing:** Give **2.25 g IV every 6 hours**.")

    elif selected_abx == "Meropenem (Meronem)":
        st.info("💡 *Standard Normal Dose:* 1g IV every 8 hours")
        if crcl > 50:      st.success("🟢 **No Adjustment Needed:** Give **1 g IV every 8 hours**.")
        elif 26 <= crcl <= 50: st.warning("⚠️ **Renal Adjusted Dose:** Give **1 g IV every 12 hours**.")
        elif 10 <= crcl <= 25: st.warning("⚠️ **Renal Adjusted Dose:** Give **500 mg IV every 12 hours**.")
        else:              st.error("🚨 **Severe Renal Dosing:** Give **500 mg IV every 24 hours**.")

    elif selected_abx == "Vancomycin":
        st.info("💡 *Vancomycin requires weight-based loading, then trough-guided interval adjustments.*")
        load_dose = min(round((weight * 20) / 250) * 250, 2000)
        st.success(f"💉 **Stat Loading Dose (All GFR ranges):** Administer **{load_dose} mg IV once** slowly over 2 hours.")
        if crcl > 60:       st.write("🔄 **Maintenance Interval:** 15 mg/kg **every 12 hours**.")
        elif 40 <= crcl <= 60:  st.write("🔄 **Maintenance Interval:** 15 mg/kg **every 24 hours**.")
        elif 20 <= crcl <= 39:  st.write("🔄 **Maintenance Interval:** 15 mg/kg **every 48 hours**.")
        else:               st.error("🚨 **Severe Renal Failure (CrCl < 20 mL/min):** Pulse dose only based on random pre-dose levels. **Do NOT schedule maintenance doses.** Recheck Vancomycin random level in 24-48 hours.")

    elif selected_abx == "Colistin (CMS)":
        st.success("💉 **STAT Loading Dose Required:** Give **9 Million IU IV infusion** over 1 hour immediately to reach therapeutic levels.")
        if crcl > 50:
            st.write("🔄 **Maintenance Dose:** **4.5 Million IU IV every 12 hours**.")
        elif 10 <= crcl <= 50:
            st.warning("⚠️ **Renal Adjusted Maintenance:** Reduce to **3.5 Million IU IV every 12 hours**.")
        else:
            st.error("🚨 **Severe Renal Failure Maintenance (<10):** Reduce to **2.5 Million IU IV every 12 hours (or up to 24h depending on clinical response)**.")
        st.error("⚠️ *Nephrotoxicity Warning:* Monitor serum creatinine daily. Avoid concomitant aminoglycosides if possible.")

    elif selected_abx == "Tigecycline (Tygacil)":
        st.success("🟢 **No Renal Adjustment Required:** Cleared via non-renal pathways.")
        st.write("💉 **Dosing Command:** Give **100 mg IV loading dose STAT**, followed by **50 mg IV every 12 hours**.")
        st.info("💡 Ideal choice for MDR infections with advanced AKI / ESRD, except for primary bacteremia or UTIs (poor serum/urine concentrations).")

    elif selected_abx == "Zavicefta (Ceftazidime/Avibactam)":
        st.info("💡 *Standard Normal Dose:* 2.5 g IV every 8 hours")
        if crcl > 50:
            st.success("🟢 **No Adjustment Needed:** **2.5 g IV every 8 hours**.")
        elif 31 <= crcl <= 50:
            st.warning("⚠️ **Renal Adjusted Dose:** **1.25 g IV every 8 hours**.")
        elif 16 <= crcl <= 30:
            st.warning("⚠️ **Renal Adjusted Dose:** **0.94 g IV every 8 hours**.")
        elif 6 <= crcl <= 15:
            st.error("🚨 **Renal Adjusted Dose:** **0.94 g IV every 12 hours**.")
        else:
            st.error("🚨 **Severe Renal Failure (≤5):** **0.94 g IV every 24 hours**.")

    elif selected_abx == "Ceftriaxone (Rocephin)":
        st.success("🟢 **No Adjustment Required for Renal Impairment Alone:** Dual hepatic/renal elimination. Give **1 g to 2 g IV every 24 hours** safely.")

    # ------------------------------------------------------------------
    # DYNAMIC INTERACTIVE BOARD MCQ GENERATOR
    # ------------------------------------------------------------------
    st.markdown("---")
    st.markdown("<div class='section-header'>📚 6. Dynamic Board Review Challenge (Randomized Hub)</div>", unsafe_allow_html=True)
    
    questions_pool = [
        {
            "id": 1,
            "case": "A 72-year-old male with severe diarrhea for 3 days has a BP of 95/55 mmHg. Labs: Creatinine 2.1 mg/dL (Baseline 0.9), BUN 62 mg/dL. Urine Sodium is 12 mEq/L. He takes Furosemide daily for heart failure.",
            "question": "Which parameter is most reliable to confirm a pre-renal state in this specific patient?",
            "options": ["A) FeNa < 1%", "B) FeUrea < 35%", "C) Urine Osmolality < 350 mOsm/kg", "D) Muddy brown granular casts on urinalysis"],
            "correct": "B) FeUrea < 35%",
            "explanation": "Because the patient is on a loop diuretic, sodium excretion is altered, making FeNa falsely high. Fractional Excretion of Urea (FeUrea < 35%) bypasses diuretic actions on the loop of Henle and confirms a pre-renal state."
        },
        {
            "id": 2,
            "case": "A 58-year-old female undergoes a contrast CT angiography. 48 hours later, her serum creatinine rises from 1.0 mg/dL to 1.9 mg/dL. Urinalysis reveals no cellular elements but a FeNa of 0.8% and high urine specific gravity.",
            "question": "What is the most likely pathophysiological mechanism during this early phase of Contrast-Induced Nephropathy (CIN)?",
            "options": ["A) Acute allergic interstitial inflammation", "B) Intra-renal vasoconstriction and medullary ischemia", "C) Direct mechanical tubular obstruction by crystals", "D) Immune-complex deposition in the glomerulus"],
            "correct": "B) Intra-renal vasoconstriction and medullary ischemia",
            "explanation": "Contrast nephropathy initially mimics a pre-renal state with a FeNa < 1% due to intense intra-renal adenosine-mediated vasoconstriction causing medullary hypoxia, alongside direct outer medullary cellular injury."
        },
        {
            "id": 3,
            "case": "A 45-year-old patient is treated for severe Pseudomonas bacteremia with Piperacillin/Tazobactam and Tobramycin. On day 7, creatinine rises from 0.8 to 2.4 mg/dL. Urinalysis reveals muddy brown casts and a FeNa of 2.4%.",
            "question": "What is the most definitive diagnosis for this patient's acute kidney injury?",
            "options": ["A) Acute Interstitial Nephritis (AIN)", "B) Pre-renal volume depletion", "C) Aminoglycoside-Induced Acute Tubular Necrosis (ATN)", "D) Post-renal obstruction"],
            "correct": "C) Aminoglycoside-Induced Acute Tubular Necrosis (ATN)",
            "explanation": "Aminoglycosides accumulate inside proximal convoluted tubule epithelial cells causing necrosis. This breaks down the tubule's ability to concentrate urine and reabsorb sodium, leading to a FeNa > 2% and classic muddy brown casts."
        }
    ]

    if 'selected_q' not in st.session_state:
        st.session_state.selected_q = random.choice(questions_pool)
        
    if st.button("🔄 Generate Another Board Question"):
        st.session_state.selected_q = random.choice(questions_pool)
        
    current_q = st.session_state.selected_q
    
    st.warning(f"**Patient Scenario:** {current_q['case']}")
    st.write(f"❓ **Question:** {current_q['question']}")
    
    user_ans = st.radio("Select your answer from below:", current_q['options'], key=f"q_{current_q['id']}")
    
    if st.expander("🔑 Reveal Correct Answer & Dr. Ihab's Clinical Explanation"):
        if user_ans == current_q['correct']:
            st.success(f"🎯 **Correct!** The answer is {current_q['correct']}")
        else:
            st.error(f"❌ **Incorrect Choice.** The correct answer is {current_q['correct']}")
        st.markdown(f"**Explanation:** {current_q['explanation']}")

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 12px;'>Al-Ahli Hospital Advanced Clinical Decision Platform © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
