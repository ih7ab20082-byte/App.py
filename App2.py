import streamlit as st
import random

# Page Configuration
st.set_page_config(
    page_title="Al-Ahli Hospital CDSS Platform",
    page_icon="🏥",
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

# Navigation Sidebar
with st.sidebar:
    st.markdown("### 🧭 Main Navigation")
    current_module = st.radio(
        "Select Clinical Module:",
        ("🧠 Acute Stroke Center (AHA/ASA)", "⚡ AKI & Renal Dosing Engine (KDIGO)")
    )
    st.markdown("---")
    st.caption("Designed for Al-Ahli Hospital Internal Medicine Residency Program.")

# ==============================================================================
# MODULE 1: ACUTE STROKE CENTER
# ==============================================================================
if current_module == "🧠 Acute Stroke Center (AHA/ASA)":
    st.markdown("<div class='main-title'>🧠 Al-Ahli Hospital Advanced Stroke Command Center</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Comprehensive Clinical Decision Support System - Based on AHA/ASA Guidelines</div>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='branding-bar'>
        <div class='branding-text'>
            <strong>Project Founder & Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
            <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
            <strong>Scope:</strong> Evidence-Based Clinical Protocols & Medical Education
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_eval, col_action = st.columns([1.2, 1])
    with col_eval:
        st.markdown("<div class='section-header'>📋 1. Patient Demographics & Time Metrics</div>", unsafe_allow_html=True)
        with st.expander("👤 Quick Patient Profile", expanded=True):
            p_name = st.text_input("Patient Name / Initials (Optional):", placeholder="e.g., John Doe")
            p_age = st.number_input("Age:", min_value=1, max_value=120, value=65, key="stroke_age")
            p_sex = st.radio("Gender:", ("Male", "Female"), key="stroke_sex")
            p_weight = st.number_input("Patient Weight (kg):", min_value=30, max_value=200, value=70, key="stroke_weight")
            p_creatinine = st.number_input("Serum Creatinine (mg/dL):", min_value=0.3, max_value=10.0, value=1.2, step=0.1, key="stroke_creat")

        with st.expander("⏱️ Door-to-Needle Quality Timer", expanded=True):
            onset_time = st.number_input("Time since symptom onset (Hours):", min_value=0.0, max_value=168.0, value=2.0, step=0.5)
            door_time = st.number_input("ED Arrival to Imaging Completion (Minutes):", min_value=1, max_value=180, value=25)
            
        st.markdown("---")
        st.markdown("<div class='section-header'>🔬 2. Neuroimaging Modality & NIHSS Assessment</div>", unsafe_allow_html=True)
        imaging_type = st.radio("Select Initial Imaging & Findings:", ("Non-Contrast CT: Ischemic Stroke Path (No acute hemorrhage)", "Diffusion MRI (DWI): Confirmed Acute Ischemic Infarct", "Non-Contrast CT: Hemorrhagic Stroke Path (Acute ICH)"))

        nihss_calculated = False
        total_nihss = 0
        if "Ischemic" in imaging_type or "Diffusion" in imaging_type:
            with st.expander("📝 Comprehensive NIHSS Calculator (AHA/ASA Standard)", expanded=True):
                n1a = st.radio("1a. Level of Consciousness (LOC):", (0, 1, 2, 3), format_func=lambda x: {0:"0: Alert", 1:"1: Somnolent", 2:"2: Obtunded", 3:"3: Comatose"}[x])
                n1b = st.radio("1b. LOC Questions (Current Month & Age):", (0, 1, 2), format_func=lambda x: {0:"0: Answers both correctly", 1:"1: Answers one correctly", 2:"2: Answers neither correctly"}[x])
                n1c = st.radio("1c. LOC Commands (Open/Close Eyes & Grip):", (0, 1, 2), format_func=lambda x: {0:"0: Performs both correctly", 1:"1: Performs one correctly", 2:"2: Performs neither"}[x])
                n2 = st.radio("2. Best Gaze (Horizontal Eye Movements):", (0, 1, 2), format_func=lambda x: {0:"0: Normal", 1:"1: Partial gaze palsy", 2:"2: Forced deviation"}[x])
                n3 = st.radio("3. Visual Fields:", (0, 1, 2, 3), format_func=lambda x: {0:"0: No loss", 1:"1: Partial hemianopia", 2:"2: Complete hemianopia", 3:"3: Bilateral hemianopia"}[x])
                n4 = st.radio("4. Facial Palsy:", (0, 1, 2, 3), format_func=lambda x: {0:"0: Normal symmetric", 1:"1: Minor paralysis", 2:"2: Partial paralysis", 3:"3: Complete paralysis"}[x])
                n5 = st.radio("5. Motor Arm (Worst Limb):", (0, 1, 2, 3, 4), format_func=lambda x: {0:"0: No drift", 1:"1: Drift", 2:"2: Effort against gravity", 3:"3: No effort against gravity", 4:"4: No movement"}[x])
                n6 = st.radio("6. Motor Leg (Worst Limb):", (0, 1, 2, 3, 4), format_func=lambda x: {0:"0: No drift", 1:"1: Drift", 2:"2: Effort against gravity", 3:"3: No effort against gravity", 4:"4: No movement"}[x])
                n7 = st.radio("7. Limb Ataxia:", (0, 1, 2), format_func=lambda x: {0:"0: Absent", 1:"1: Present in one limb", 2:"2: Present in two or more"}[x])
                n8 = st.radio("8. Sensory:", (0, 1, 2), format_func=lambda x: {0:"0: Normal", 1:"1: Mild-to-moderate loss", 2:"2: Severe or total loss"}[x])
                n9 = st.radio("9. Best Language (Aphasia):", (0, 1, 2, 3), format_func=lambda x: {0:"0: Normal", 1:"1: Mild-to-moderate", 2:"2: Severe aphasia", 3:"3: Global aphasia/Mute"}[x])
                n10 = st.radio("10. Dysarthria (Speech Clarity):", (0, 1, 2), format_func=lambda x: {0:"0: Normal", 1:"1: Mild-to-moderate", 2:"2: Severe"}[x])
                n11 = st.radio("11. Extinction and Inattention (Neglect):", (0, 1, 2), format_func=lambda x: {0:"0: No neglect", 1:"1: Partial", 2:"2: Complete neglect"}[x])
                total_nihss = n1a + n1b + n1c + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 + n11
                nihss_calculated = True
                st.metric("Total Calculated NIHSS Score", total_nihss)

    with col_action:
        st.markdown("<div class='section-header'>⚡ 3. Decision Support & Treatment Protocols</div>", unsafe_allow_html=True)
        sbp = st.number_input("Systolic Blood Pressure (SBP mmHg):", min_value=50, max_value=260, value=160, key="stroke_sbp")
        dbp = st.number_input("Diastolic Blood Pressure (DBP mmHg):", min_value=30, max_value=180, value=95, key="stroke_dbp")
        
        if "Hemorrhagic" in imaging_type:
            st.error("🔴 HEMORRHAGIC STROKE CRITICAL PATHWAY ACTIVATED. Target SBP: 130-140 mmHg. Reverse coagulopathy.")
        else:
            if not nihss_calculated:
                st.warning("⏳ Please complete the NIHSS calculation in the left panel to unlock treatment protocols.")
            else:
                cta_result = st.radio("CT Angiography (CTA) / LVO Status:", ("Pending / Not Done", "Confirmed LVO (ICA, MCA-M1/M2, Basilar)", "No LVO"), key="stroke_cta")
                tpa_eligible = (onset_time <= 4.5 and sbp <= 185 and dbp <= 110 and total_nihss <= 22 and total_nihss > 0)
                evt_eligible = ("Confirmed LVO" in cta_result and onset_time <= 24.0 and total_nihss >= 6)

                treatment_path = st.radio("Select Definitive Treatment Pathway:", ("Thrombolysis / Intervention Path (Patient received/is receiving tPA or EVT)", "Non-Interventional Conservative Path (Pure Medical Management / Antiplatelets)"), key="stroke_path")
                
                if "Thrombolysis" in treatment_path:
                    st.success("🟢 **INTERVENTION PATHWAY ACTIVATED**")
                    if tpa_eligible:
                        total_dose = min(p_weight * 0.9, 90.0)
                        st.write(f"💉 **IV tPA Dose:** Total: {total_dose:.1f} mg | Bolus: {total_dose*0.1:.1f} mg | Infusion: {total_dose*0.9:.1f} mg over 60 mins.")
                    st.error("🚫 **ANTI-PLATELET SAFEGUARD:** Post-tPA/EVT. Hold ALL Antiplatelets/Anticoagulants for the first 24 hours until repeat CT rules out hemorrhage.")
                else:
                    st.warning("🟡 **CONSERVATIVE MEDICAL PATHWAY ACTIVATED**")
                    if total_nihss <= 3:
                        st.success("🟢 **Minor Stroke Protocol:** Start DAPT (Aspirin 162-325mg + Clopidogrel 300mg load) for 21 days.")
                    else:
                        st.error("⚠️ **Moderate-Severe Stroke:** High bleeding risk! No DAPT. Single Antiplatelet Only (Aspirin).")

# ==============================================================================
# MODULE 2: AKI & RENAL DOSING ENGINE (WITH NEW ADVANCED FEATURES)
# ==============================================================================
elif current_module == "⚡ AKI & Renal Dosing Engine (KDIGO)":
    st.markdown("<div class='main-title'>⚡ Acute Kidney Injury (AKI) & Renal Dosing Center</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Local Adaptive Protocol & Drug Dosing Engine for Al-Ahli Hospital Ward Protocols</div>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='branding-bar'>
        <div class='branding-text'>
            <strong>Clinical Lead:</strong> Dr. Ihab Abbass Abu Hilail<br>
            <strong>Specialty:</strong> Evidence-Based Nephrology Management & Resident Support Systems<br>
            <strong>Framework:</strong> 2012 KDIGO Clinical Practice Guidelines for Acute Kidney Injury
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_input, col_output = st.columns([1, 1.2])

    with col_input:
        st.markdown("<div class='section-header'>🧪 1. Patient Renal Metrics & Function</div>", unsafe_allow_html=True)
        
        with st.expander("👤 Patient Vital Parameters", expanded=True):
            age = st.number_input("Age (Years):", min_value=18, max_value=110, value=60, key="aki_age")
            gender = st.radio("Gender:", ("Male", "Female"), key="aki_gender")
            weight = st.number_input("Actual Body Weight (kg):", min_value=35, max_value=220, value=75, key="aki_weight")
            
        with st.expander("📊 Creatinine Kinetics (KDIGO Staging)", expanded=True):
            baseline_cr = st.number_input("Baseline Serum Creatinine (mg/dL) - *Prior stable value*:", min_value=0.3, max_value=12.0, value=1.0, step=0.1)
            current_cr = st.number_input("Current Serum Creatinine (mg/dL):", min_value=0.3, max_value=12.0, value=2.2, step=0.1)
            urine_output = st.radio("Urine Output History over the last 6-24 hours:",
                                    ("Normal (> 0.5 mL/kg/h)", "< 0.5 mL/kg/h for 6 - 12 hours", "< 0.5 mL/kg/h for ≥ 12 hours", "Anuria / Severe Oliguria (< 0.3 mL/kg/h) for ≥ 24h or Anuria ≥ 12h"))

        # Calculate CrCl using Cockcroft-Gault Equation
        if gender == "Male":
            crcl = ((140 - age) * weight) / (72 * current_cr)
        else:
            crcl = (((140 - age) * weight) / (72 * current_cr)) * 0.85

        # HIGHLY POWERFUL ADDITION: DYNAMIC FENA & FEUREA CALCULATOR
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
            "Select Antibiotic to Calculate Renal Dose大 Adjustment:",
            ["Tazocin (Piperacillin/Tazobactam)", "Meropenem (Meronem)", "Vancomycin", "Ceftriaxone (Rocephin)"]
        )

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
        elif kdigo_stage == 3: st.error("💥 **CRITICAL: ACUTE KIDNEY INJURY - KDIGO STAGE 3** (High Risk of Hemodialysis!)")

        st.metric(label="Calculated Current Creatinine Clearance (CrCl):", value=f"{crcl:.1f} mL/min")

        # Process FeNa / FeUrea Analytics
        if u_na > 0 and u_cr > 0:
            st.markdown("#### 🧬 Dynamic Nephrology Diagnostics Output:")
            fena = (u_na * p_cr) / (p_na * u_cr) * 100
            
            if is_on_diuretic == "Yes" and u_urea > 0 and p_urea > 0:
                feurea = (u_urea * p_cr) / (p_urea * u_cr) * 100
                st.write(f"📊 **Calculated FeUrea:** {feurea:.1f}% *(Preferred index: Patient is on a diuretic)*")
                if feurea < 35:
                    st.success("🟢 **Diagnostic Impression:** Consistent with **Pre-renal Azotemia** (Hypoperfusion). Fluids indicated.")
                else:
                    st.error("🔴 **Diagnostic Impression:** Consistent with **Intrinsic Renal Injury / ATN**.")
            else:
                st.write(f"📊 **Calculated FeNa:** {fena:.1f}%")
                if is_on_diuretic == "Yes":
                    st.warning("⚠️ *Warning: FeNa is unreliable because patient is taking diuretics. Please input Urine Urea to compute FeUrea instead.*")
                
                if fena < 1.0:
                    st.success("🟢 **Diagnostic Impression:** Consistent with **Pre-renal Azotemia** (FeNa < 1%).")
                else:
                    st.error("🔴 **Diagnostic Impression:** Consistent with **Intrinsic Renal Injury / ATN** (FeNa > 2%).")

        # ------------------------------------------------------------------
        # RENAL DOSING OUTPUT ENGINE
        # ------------------------------------------------------------------
        st.markdown("---")
        st.markdown("<div class='section-header'>📋 5. Adjusted Pharmacokinetic Dosing Guide</div>", unsafe_allow_html=True)
        st.write(f"### 🧪 Targeted Drug: **{selected_abx}**")

        if selected_abx == "Tazocin (Piperacillin/Tazobactam)":
            if crcl > 40:      st.success("🟢 **No Adjustment Needed:** 4.5 g IV every 6 hours.")
            elif 20 <= crcl <= 40: st.warning("⚠️ **Renal Adjusted Dose:** 3.375 g IV every 6 hours.")
            else:              st.error("🚨 **Severe Renal Dosing:** 2.25 g IV every 6 hours.")
        elif selected_abx == "Meropenem (Meronem)":
            if crcl > 50:      st.success("🟢 **No Adjustment Needed:** 1 g IV every 8 hours.")
            elif 26 <= crcl <= 50: st.warning("⚠️ **Renal Adjusted Dose:** 1 g IV every 12 hours.")
            elif 10 <= crcl <= 25: st.warning("⚠️ **Renal Adjusted Dose:** 500 mg IV every 12 hours.")
            else:              st.error("🚨 **Severe Renal Dosing:** 500 mg IV every 24 hours.")
        elif selected_abx == "Vancomycin":
            load_dose = min(round((weight * 20) / 250) * 250, 2000)
            st.success(f"💉 **Stat Loading Dose:** Administer **{load_dose} mg IV once** slowly over 2 hours.")
            if crcl > 60:       st.write("🔄 **Maintenance Interval:** 15 mg/kg every 12 hours.")
            elif 40 <= crcl <= 60:  st.write("🔄 **Maintenance Interval:** 15 mg/kg every 24 hours.")
            elif 20 <= crcl <= 39:  st.write("🔄 **Maintenance Interval:** 15 mg/kg every 48 hours.")
            else:               st.error("🚨 **Severe Renal Failure (<20):** Pulse dose only based on pre-dose random levels!")
        elif selected_abx == "Ceftriaxone (Rocephin)":
            st.success("🟢 **No Adjustment Required for Renal Impairment Alone:** Give 1 g to 2 g IV every 24 hours safely.")

        # ------------------------------------------------------------------
        # HIGHLY POWERFUL ADDITION: DYNAMIC INTERACTIVE BOARD MCQ GENERATOR
        # ------------------------------------------------------------------
        st.markdown("---")
        st.markdown("<div class='section-header'>📚 6. Dynamic Board Review Challenge (Randomized Hub)</div>", unsafe_allow_html=True)
        
        # Define a pool of high-yield board questions
        questions_pool = [
            {
                "id": 1,
                "case": "A 72-year-old male with severe diarrhea for 3 days has a BP of 95/55 mmHg. Labs: Creatinine 2.1 mg/dL (Baseline 0.9), BUN 62 mg/dL. Urine Sodium is 12 mEq/L. He takes Furosemide daily for heart failure.",
                "question": "Which parameter is most reliable to confirm a pre-renal state in this specific patient?",
                "options": ["A) FeNa < 1%", "B) FeUrea < 35%", "C) Urine Osmolality < 350 mOsm/kg", "D) Muddy brown granular casts on urinalysis"],
                "correct": "B) FeUrea < 35%",
                "explanation": "Because the patient is on a loop diuretic, sodium excretion is falsely elevated, making FeNa unreliable. Fractional Excretion of Urea (FeUrea < 35%) bypasses diuretic effects and confirms a pre-renal state."
            },
            {
                "id": 2,
                "case": "An 58-year-old female undergoes a contrast CT angiography. 48 hours later, her serum creatinine rises from 1.0 mg/dL to 1.9 mg/dL. Urinalysis reveals no cells but a FeNa of 0.8% and high urine specific gravity.",
                "question": "What is the most likely pathophysiological mechanism during this early phase of Contrast-Induced Nephropathy (CIN)?",
                "options": ["A) Acute allergic interstitial inflammation", "B) Intrenal vasoconstriction and medullary ischemia", "C) Direct mechanical tubular obstruction by crystals", "D) Immune-complex deposition in the glomerulus"],
                "correct": "B) Intrenal vasoconstriction and medullary ischemia",
                "explanation": "Early contrast nephropathy characteristically behaves like a 'pre-renal' mimic with a FeNa < 1% due to intense renal afferent arteriolar vasoconstriction causing ischemia, alongside direct tubular cytotoxicity."
            },
            {
                "id": 3,
                "case": "A 45-year-old patient is treated for severe Pseudomonas bacteremia with Piperacillin/Tazobactam and Tobramycin. On day 7, creatinine rises from 0.8 to 2.4 mg/dL. Urinalysis reveals muddy brown casts and a FeNa of 2.4%.",
                "question": "What is the most definitive diagnosis for this patient's renal failure?",
                "options": ["A) Acute Interstitial Nephritis (AIN)", "B) Pre-renal volume depletion", "C) Aminoglycoside-Induced Acute Tubular Necrosis (ATN)", "D) Post-renal obstruction"],
                "correct": "C) Aminoglycoside-Induced Acute Tubular Necrosis (ATN)",
                "explanation": "Aminoglycosides (Tobramycin) accumulate in proximal tubule epithelial cells causing direct toxicity. This results in ATN, characteristically causing a loss of tubular sodium reabsorption capacity (FeNa > 2%) and classic muddy brown casts."
            }
        ]

        # Use Streamlit session state to lock the selected question until the user clicks refresh
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
