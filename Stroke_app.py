import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Al-Ahli Hospital Advanced Stroke Platform",
    page_icon="🧠",
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
st.markdown("<div class='main-title'>🧠 Al-Ahli Hospital Advanced Stroke Command Center</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Comprehensive Clinical Decision Support System (CDSS) - Based on AHA/ASA Guidelines</div>", unsafe_allow_html=True)

# Professional Badge
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Project Founder & Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Scope:</strong> Evidence-Based Clinical Protocols & Medical Education
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Main Layout: Split Screen
col_eval, col_action = st.columns([1.2, 1])

# ==============================================================================
# LEFT COLUMN: Clinical Evaluation, Imaging & Patient Data
# ==============================================================================
with col_eval:
    st.markdown("<div class='section-header'>📋 1. Patient Demographics & Time Metrics</div>", unsafe_allow_html=True)
    
    with st.expander("👤 Quick Patient Profile", expanded=True):
        p_name = st.text_input("Patient Name / Initials (Optional):", placeholder="e.g., John Doe")
        p_age = st.number_input("Age:", min_value=1, max_value=120, value=65)
        p_sex = st.radio("Gender:", ("Male", "Female"))
        p_weight = st.number_input("Patient Weight (kg):", min_value=30, max_value=200, value=70)
        p_creatinine = st.number_input("Serum Creatinine (mg/dL):", min_value=0.3, max_value=10.0, value=1.2, step=0.1)

    with st.expander("⏱️ Door-to-Needle Quality Timer", expanded=True):
        onset_time = st.number_input("Time since symptom onset (Hours):", min_value=0.0, max_value=168.0, value=2.0, step=0.5)
        door_time = st.number_input("ED Arrival to Imaging Completion (Minutes):", min_value=1, max_value=180, value=25)
        
    st.markdown("---")
    st.markdown("<div class='section-header'>🔬 2. Neuroimaging Modality & NIHSS Assessment</div>", unsafe_allow_html=True)
    
    imaging_type = st.radio("Select Initial Imaging & Findings:", 
                       ("Non-Contrast CT: Ischemic Stroke Path (No acute hemorrhage)", 
                        "Diffusion MRI (DWI): Confirmed Acute Ischemic Infarct",
                        "Non-Contrast CT: Hemorrhagic Stroke Path (Acute ICH)"))

    # Full NIHSS Protocol Section
    nihss_calculated = False
    total_nihss = 0
    
    if "Ischemic" in imaging_type or "Diffusion" in imaging_type:
        with st.expander("📝 Comprehensive NIHSS Calculator (AHA/ASA Standard)", expanded=True):
            st.caption("Complete all 11 standardized clinical items below to view therapeutic recommendations:")
            
            n1a = st.radio("1a. Level of Consciousness (LOC):", (0, 1, 2, 3), 
                           format_func=lambda x: {0:"0: Alert (Keenly responsive)", 1:"1: Somnolent (Arousable by minor stimulation)", 2:"2: Obtunded (Requires repeated or painful stimuli)", 3:"3: Comatose (Unresponsive or reflex motor only)"}[x])
            
            n1b = st.radio("1b. LOC Questions (Current Month & Age):", (0, 1, 2), 
                           format_func=lambda x: {0:"0: Answers both questions correctly", 1:"1: Answers one question correctly", 2:"2: Answers neither question correctly (or intubated/aphasic)"}[x])
            
            n1c = st.radio("1c. LOC Commands (Open/Close Eyes & Grip/Release Hand):", (0, 1, 2), 
                           format_func=lambda x: {0:"0: Performs both commands correctly", 1:"1: Performs one command correctly", 2:"2: Performs neither command correctly"}[x])
            
            n2 = st.radio("2. Best Gaze (Horizontal Eye Movements):", (0, 1, 2), 
                          format_func=lambda x: {0:"0: Normal horizontal eye movements", 1:"1: Partial gaze palsy (Gaze is abnormal in one or both eyes)", 2:"2: Forced deviation (Total gaze paresis not overcome by oculocephalic maneuver)"}[x])
            
            n3 = st.radio("3. Visual Fields (Upper/Lower Quadrants via Confrontation):", (0, 1, 2, 3), 
                          format_func=lambda x: {0:"0: No visual field loss", 1:"1: Partial hemianopia", 2:"2: Complete hemianopia", 3:"3: Bilateral hemianopia (Blindness/Cortical blindness)"}[x])
            
            n4 = st.radio("4. Facial Palsy (Show Teeth, Raise Eyebrows, Close Eyes):", (0, 1, 2, 3), 
                          format_func=lambda x: {0:"0: Normal symmetric movement", 1:"1: Minor paralysis (Flattening of nasolabial fold, asymmetry on smiling)", 2:"2: Partial paralysis (Total or near-total paralysis of lower face)", 3:"3: Complete paralysis (Absence of facial movement in upper and lower face)"}[x])
            
            n5 = st.radio("5. Motor Arm (Drift Assessment - Holds 90° or 45° for 10 seconds):", (0, 1, 2, 3, 4), 
                          format_func=lambda x: {0:"0: No drift (Limb holds position for full 10s)", 1:"1: Drift (Limb holds but drifts down before 10s without hitting bed)", 2:"2: Some effort against gravity (Limb falls to bed, but can raise against gravity)", 3:"3: No effort against gravity (Limb falls, no resistance, drifts laterally)", 4:"4: No movement at all"}[x])
            
            n6 = st.radio("6. Motor Leg (Drift Assessment - Holds 30° in supine for 5 seconds):", (0, 1, 2, 3, 4), 
                          format_func=lambda x: {0:"0: No drift (Limb holds position for full 5s)", 1:"1: Drift (Limb drifts down before 5s without hitting bed)", 2:"2: Some effort against gravity (Limb falls to bed, but has muscle contraction)", 3:"3: No effort against gravity (Limb falls immediately, cannot lift)", 4:"4: No movement at all"}[x])
            
            n7 = st.radio("7. Limb Ataxia (Finger-to-Nose & Heel-to-Shin Testing):", (0, 1, 2), 
                          format_func=lambda x: {0:"0: Absent (No dysmetria or coordination defect)", 1:"1: Present in one limb", 2:"2: Present in two or more limbs"}[x])
            
            n8 = st.radio("8. Sensory (Pinprick response on face, arms, trunk, legs):", (0, 1, 2), 
                           format_func=lambda x: {0:"0: Normal; no sensory loss", 1:"1: Mild-to-moderate loss (Patient feels pinprick but it is less sharp)", 2:"2: Severe or total loss (Patient is unaware of being touched)"}[x])
            
            n9 = st.radio("9. Best Language (Naming objects, describing pictures, reading sentences):", (0, 1, 2, 3), 
                           format_func=lambda x: {0:"0: Normal; no aphasia", 1:"1: Mild-to-moderate aphasia (Some loss of fluency or comprehension)", 2:"2: Severe aphasia (Communication is fragmented, heavily reliant on inference)", 3:"3: Global aphasia/Mute (No usable speech or auditory comprehension)"}[x])
            
            n10 = st.radio("10. Dysarthria (Articulation of standard words):", (0, 1, 2), 
                           format_func=lambda x: {0:"0: Normal articulation and clarity", 1:"1: Mild-to-moderate dysarthria (Slurring of some words, but understood)", 2:"2: Severe dysarthria (Speech is completely unintelligible or mute)"}[x])
            
            n11 = st.radio("11. Extinction and Inattention (Visual, tactile, or spatial neglect):", (0, 1, 2), 
                           format_func=lambda x: {0:"0: No inattention/neglect", 1:"1: Partial inattention (Visual/tactile extinction to simultaneous bilateral stimuli)", 2:"2: Complete hemi-inattention / Neglect (Unaware of more than one modality)"}[x])
            
            total_nihss = n1a + n1b + n1c + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 + n11
            nihss_calculated = True
            
            st.metric("Total Calculated NIHSS Score", total_nihss)
            if total_nihss > 22:
                st.error("⚠️ CRITICAL WARNING: High NIHSS (> 22) indicates massive hemispheric stroke. Severe risk of post-tPA Hemorrhagic Transformation! Consider EVT over systemic lysis.")

# ==============================================================================
# RIGHT COLUMN: Decision Support & Strict Pathway Separation
# ==============================================================================
with col_action:
    st.markdown("<div class='section-header'>⚡ 3. Decision Support & Treatment Protocols</div>", unsafe_allow_html=True)
    
    sbp = st.number_input("Systolic Blood Pressure (SBP mmHg):", min_value=50, max_value=260, value=160)
    dbp = st.number_input("Diastolic Blood Pressure (DBP mmHg):", min_value=30, max_value=180, value=95)
    
    if "Hemorrhagic" in imaging_type:
        st.error("🔴 HEMORRHAGIC STROKE CRITICAL PATHWAY ACTIVATED")
        st.markdown("Target SBP: **130 - 140 mmHg**. Initiate aggressive IV Labetalol titration. Reverse coagulopathy immediately.")
    
    else:
        if not nihss_calculated:
            st.warning("⏳ Please complete the NIHSS calculation in the left panel to unlock clinical decision recommendations.")
        else:
            cta_result = st.radio("CT Angiography (CTA) / LVO Status:", 
                                  ("Pending / Not Done", "Confirmed LVO (ICA, MCA-M1/M2, Basilar)", "No LVO"))
            
            tpa_eligible = (onset_time <= 4.5 and sbp <= 185 and dbp <= 110 and total_nihss <= 22 and total_nihss > 0)
            evt_eligible = ("Confirmed LVO" in cta_result and onset_time <= 24.0 and total_nihss >= 6)

            # Blood pressure check for tPA window
            if onset_time <= 4.5 and (sbp > 185 or dbp > 110):
                st.error("⚠️ BP CONTRAINDICATION: Blood pressure is above tPA thresholds (>185/110 mmHg). Lower SBP < 185 to unlock Thrombolysis eligibility.")

            # CLINICAL PATHWAY CHOOSER
            st.markdown("### 🛠️ Select Definitive Treatment Pathway:")
            treatment_path = st.radio(
                "Based on clinical workup, what is the chosen management strategy?",
                ("Thrombolysis / Intervention Path (Patient received/is receiving tPA or EVT)", 
                 "Non-Interventional Conservative Path (Pure Medical Management / Antiplatelets)")
            )

            # PATHWAY A: THROMBOLYSIS/EVT INTERVENTION
            if "Thrombolysis" in treatment_path:
                st.success("🟢 **INTERVENTION PATHWAY ACTIVATED**")
                
                if tpa_eligible:
                    total_dose = min(p_weight * 0.9, 90.0)
                    st.write(f"💉 **IV tPA (Alteplase) Dose Commands:** Total: **{total_dose:.1f} mg** | Bolus (10%): **{total_dose*0.1:.1f} mg** IV push | Infusion (90%): **{total_dose*0.9:.1f} mg** over 60 mins.")
                
                if evt_eligible and tpa_eligible:
                    st.warning("🧠 **AHA/ASA BRIDGING MANDATE ACTIVE:** Start tPA infusion immediately and transfer to Angio-Suite simultaneously. DO NOT wait.")
                elif evt_eligible and not tpa_eligible:
                    st.info("🎯 **Direct Mechanical Thrombectomy (EVT):** Outside tPA window but eligible for extended EVT (up to 24h). Activate Cath Lab immediately.")

                # ABSOLUTE POST-INTERVENTION CONTRAINDICATION
                st.error("🚫 **ANTI-PLATELET SAFEGUARD:** Patient is post-tPA/EVT. **Hold ALL Antiplatelets (Aspirin/Clopidogrel) and Anticoagulants for the first 24 hours.**")

            # PATHWAY B: PURE MEDICAL CONSERVATIVE MANAGEMENT
            else:
                st.warning("🟡 **CONSERVATIVE MEDICAL PATHWAY ACTIVATED (No tPA/EVT)**")
                st.markdown("### 💊 Acute Antiplatelet Strategy:")
                if total_nihss <= 3 and total_nihss > 0:
                    st.success("🟢 **Minor Stroke (NIHSS ≤ 3) Protocol:** Eligible for **Dual Antiplatelet Therapy (DAPT)**. Initiate Aspirin 162-325mg PO + Clopidogrel 300mg loading dose STAT, then continue DAPT for 21 days (POINT/CHANCE Trials).")
                elif total_nihss > 3:
                    st.error("⚠️ **Moderate-to-Severe Stroke (NIHSS > 3) Protocol:** High risk of bleeding transformation! **Do NOT use DAPT**. Restrict treatment strictly to Single Antiplatelet Therapy (**Aspirin Only 162-325mg daily**).")

            # ==============================================================================
            # 📋 MANDATORY WORKUP CHECKLIST (TIMELINE DRIVEN)
            # ==============================================================================
            st.markdown("---")
            st.markdown("<div class='section-header'>📋 4. Mandatory Stroke Workup Checklist</div>", unsafe_allow_html=True)
            with st.expander("🔬 View Complete Diagnostic & Secondary Prevention Workup", expanded=True):
                st.markdown("""
                **1. Hyperacute Stat Orders (Within 10 Minutes of Arrival):**
                * [ ] **Random Blood Sugar (RBS):** Rule out hypoglycemia (Essential mimic).
                * [ ] **Coagulation Profile (PT, INR, aPTT):** Critical if patient is on baseline anticoagulation.
                * [ ] **Complete Blood Count (CBC):** Check platelets (Must be > 100,000 cells/µL for tPA safety).
                * [ ] **Renal Function Tests:** Serum Creatinine & GFR (Needed for CTA contrast and DOACs).
                * [ ] **Cardiac Enzymes:** Troponin level to screen for silent or concurrent Type 2 MI.
                
                **2. Secondary Etiology Evaluation (Within 24-48 Hours):**
                * [ ] **12-Lead ECG:** Immediate screening for Occult Atrial Fibrillation.
                * [ ] **Transthoracic Echocardiography (TTE/TEE):** Rule out cardiac thrombus, PFO, or low EF.
                * [ ] **Carotid & Vertebral Doppler / CTA Neck:** Screen for large artery atherosclerosis/stenosis (>50% or >70%).
                * [ ] **Extended Holter Monitoring:** Indicated if embolic stroke of undetermined source (ESUS) is highly suspected.
                
                **3. Metabolic Panels (Next Morning Labs):**
                * [ ] **Fasting Lipid Profile:** Target LDL < 70 mg/dL.
                * [ ] **HbA1c & Fasting Glucose:** Optimize long-term glycemic control.
                """)

            # ==============================================================================
            # 5. CARDIOEMBOLIC AF: TIMING GUIDE & GFR-BASED NOAC DOSING ENGINE
            # ==============================================================================
            st.markdown("---")
            st.markdown("<div class='section-header'>🔬 5. Cardioembolic AF: Anticoagulation Timing & Dosing</div>", unsafe_allow_html=True)
            
            with st.expander("⏱️ When to Start Oral Anticoagulation (DOACs) Post-Stroke:", expanded=True):
                if total_nihss <= 3:
                    st.info("🟢 **Day 1 to 3 Initiation (Minor Stroke):** Safe to start oral anticoagulation early, provided a follow-up head CT rules out any microhemorrhage.")
                elif total_nihss <= 15:
                    st.warning("🟡 **Day 6 Initiation (Moderate Stroke):** Delay oral anticoagulation until Day 6. Ensure clinical stability with an updated Non-Contrast CT prior to administration.")
                else:
                    st.error("🔴 **Day 12 to 14 Initiation (Severe Stroke):** High danger of hemorrhagic expansion. Hold anticoagulation for 12-14 days. Re-image via CT before first dose.")

            if p_sex == "Male":
                crcl = ((140 - p_age) * p_weight) / (72 * p_creatinine)
            else:
                crcl = (((140 - p_age) * p_weight) / (72 * p_creatinine)) * 0.85
                
            st.metric(label="Calculated Creatinine Clearance (CrCl):", value=f"{crcl:.1f} mL/min")
            
            with st.expander("💊 GFR-Based NOAC Dosing Adjustments:", expanded=True):
                st.markdown(f"**Current Renal Status:** CrCl = {crcl:.1f} mL/min")
                st.markdown("#### 🔹 Apixaban (Eliquis):")
                apixaban_criteria = 0
                if p_age >= 80: apixaban_criteria += 1
                if p_weight <= 60: apixaban_criteria += 1
                if p_creatinine >= 1.5: apixaban_criteria += 1
                
                if crcl < 15: st.error("❌ Apixaban is Contraindicated (CrCl < 15 mL/min).")
                elif apixaban_criteria >= 2: st.warning("⚠️ **Dose Reduced:** Give **2.5 mg BID**.")
                else: st.success("🟢 **Standard Dose:** Give **5 mg BID**.")
                
                st.markdown("#### 🔹 Rivaroxaban (Xarelto):")
                if crcl < 15: st.error("❌ Rivaroxaban is Contraindicated (CrCl < 15 mL/min).")
                elif 15 <= crcl <= 50: st.warning("⚠️ **Dose Reduced for Renal Impairment:** Give **15 mg Once Daily**.")
                else: st.success("🟢 **Standard Dose:** Give **20 mg Once Daily**.")

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 12px;'>Al-Ahli Hospital Stroke Command Center App © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
