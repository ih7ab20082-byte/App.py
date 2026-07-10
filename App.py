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
    .alert-box { padding: 15px; border-radius: 8px; margin-bottom: 15px; }
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
# RIGHT COLUMN: Clinical Evaluation, Imaging & Patient Data
# ==============================================================================
with col_eval:
    st.markdown("<div class='section-header'>📋 1. Patient Demographics & Time Metrics</div>", unsafe_allow_html=True)
    
    with st.expander("👤 Quick Patient Profile", expanded=True):
        p_name = st.text_input("Patient Name / Initials (Optional):", placeholder="e.g., John Doe")
        p_age = st.number_input("Age:", min_value=1, max_value=120, value=65)
        p_sex = st.radio("Gender:", ("Male", "Female"))
        p_id = st.text_input("Medical Record Number (MRN):")
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

    # Mandatory NIHSS Section for Ischemic Stroke
    nihss_calculated = False
    total_nihss = 0
    
    if "Ischemic" in imaging_type or "Diffusion" in imaging_type:
        with st.expander("📝 Mandatory NIHSS Calculator", expanded=True):
            st.caption("AHA/ASA Requirement: Complete all items to unlock treatment recommendations.")
            
            n1 = st.radio("1a. Level of Consciousness (LOC):", (0, 1, 2, 3), format_func=lambda x: {0:"0: Alert", 1:"1: Somnolent", 2:"2: Obtunded", 3:"3: Comatose"}[x])
            n2 = st.radio("1b. LOC Questions (Month & Age):", (0, 1, 2), format_func=lambda x: {0:"0: Both correct", 1:"1: One correct", 2:"2: Neither correct"}[x])
            n3 = st.radio("1c. LOC Commands (Eyes & Grip):", (0, 1, 2), format_func=lambda x: {0:"0: Both correct", 1:"1: One correct", 2:"2: Neither correct"}[x])
            n4 = st.radio("2. Best Gaze (Horizontal Movements):", (0, 1, 2), format_func=lambda x: {0:"0: Normal", 1:"1: Partial gaze palsy", 2:"2: Forced deviation"}[x])
            n5 = st.radio("3. Visual Fields:", (0, 1, 2, 3), format_func=lambda x: {0:"0: No loss", 1:"1: Partial", 2:"2: Complete", 3:"3: Bilateral"}[x])
            n6 = st.radio("4. Facial Palsy:", (0, 1, 2, 3), format_func=lambda x: {0:"0: Normal", 1:"1: Minor", 2:"2: Partial", 3:"3: Complete"}[x])
            n7 = st.radio("5. Motor Arm (Worst Limb):", (0, 1, 2, 3, 4), format_func=lambda x: {0:"0: No drift", 1:"1: Drift", 2:"2: Some effort against gravity", 3:"3: No effort against gravity", 4:"4: No movement"}[x])
            n8 = st.radio("6. Motor Leg (Worst Limb):", (0, 1, 2, 3, 4), format_func=lambda x: {0:"0: No drift", 1:"1: Drift", 2:"2: Some effort against gravity", 3:"3: No effort against gravity", 4:"4: No movement"}[x])
            n9 = st.radio("7. Limb Ataxia (Coordination):", (0, 1, 2), format_func=lambda x: {0:"0: Absent", 1:"1: Present in 1 limb", 2:"2: Present in 2+ limbs"}[x])
            n10 = st.radio("8. Sensory (Pinprick):", (0, 1, 2), format_func=lambda x: {0:"0: Normal", 1:"1: Mild loss", 2:"2: Severe loss"}[x])
            n11 = st.radio("9. Best Language (Aphasia):", (0, 1, 2, 3), format_func=lambda x: {0:"0: No aphasia", 1:"1: Mild aphasia", 2:"2: Severe aphasia", 3:"3: Global"}[x])
            n12 = st.radio("10. Dysarthria (Speech Clarity):", (0, 1, 2), format_func=lambda x: {0:"0: Normal", 1:"1: Mild", 2:"2: Severe"}[x])
            n13 = st.radio("11. Extinction/Inattention (Neglect):", (0, 1, 2), format_func=lambda x: {0:"0: No neglect", 1:"1: Partial", 2:"2: Complete"}[x])
            
            total_nihss = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 + n11 + n12 + n13
            nihss_calculated = True
            
            st.metric("Calculated NIHSS Score", total_nihss)
            if total_nihss > 22:
                st.error("⚠️ CRITICAL WARNING: High NIHSS (> 22) indicates massive hemispheric stroke. Severe risk of post-tPA Hemorrhagic Transformation! Consider EVT over systemic lysis.")

# ==============================================================================
# LEFT COLUMN: Decision Support & Strict Pathway Separation
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

            # ------------------------------------------------------------------
            # CLINICAL FORK: CHOOSE THE ACTUAL INTERVENTION PATHWAY
            # ------------------------------------------------------------------
            st.markdown("### 🛠️ Select Final Clinical Pathway Decisions:")
            treatment_path = st.radio(
                "Based on clinical eligibility above, what is the definitive plan?",
                ("Thrombolysis / Intervention Path (Patient received/is receiving tPA or EVT)", 
                 "Non-Interventional Conservative Path (Pure Medical Management)")
            )

            # PATHWAY 1: INTERVENTIONAL (tPA/EVT)
            if "Thrombolysis" in treatment_path:
                st.success("🟢 **INTERVENTION PATHWAY ACTIVATED**")
                
                if tpa_eligible:
                    total_dose = min(p_weight * 0.9, 90.0)
                    st.write(f"💉 **IV tPA Dose:** Total: **{total_dose:.1f} mg** | Bolus (10%): **{total_dose*0.1:.1f} mg** | Infusion: **{total_dose*0.9:.1f} mg** over 60 mins.")
                
                if evt_eligible and tpa_eligible:
                    st.warning("🧠 **BRIDGING MANDATE ACTIVE:** Patient satisfies criteria for both tPA and EVT. **Start tPA immediately and transfer to Angio-Suite simultaneously.** Do NOT delay EVT to wait for tPA results.")
                elif evt_eligible and not tpa_eligible:
                    st.info("🎯 **Direct Mechanical Thrombectomy (EVT):** Outside tPA window but eligible for extended EVT (up to 24h). Activate Cath Lab.")

                # ABSOLUTE CONTRAINDICATION FOR ANTIPLATELETS IN FIRST 24H
                st.error("🚫 **ANTI-PLATELET CONTRAINDICATION:** Patient is post-tPA/EVT. **Hold ALL Antiplatelets (Aspirin/Clopidogrel) and Anticoagulants for the first 24 hours.**")
                st.info("ℹ️ *Antiplatelets can only be initiated after a Repeat Non-Contrast CT Brain at 24 hours safely rules out Hemorrhagic Transformation.*")

            # PATHWAY 2: CONSERVATIVE (PURE MEDICAL MANAGEMENT)
            else:
                st.warning("🟡 **CONSERVATIVE MEDICAL PATHWAY ACTIVATED (No tPA/EVT)**")
                st.markdown("### 💊 Acute Antiplatelet Strategy:")
                if total_nihss <= 3 and total_nihss > 0:
                    st.success("🟢 **Minor Stroke (NIHSS ≤ 3) Protocol:** Safe for **Dual Antiplatelet Therapy (DAPT)**. Initiate Aspirin 162-325mg stat + Clopidogrel 300mg loading dose, then continue DAPT for 21 days (POINT/CHANCE Trials).")
                elif total_nihss > 3:
                    st.error("⚠️ **Moderate-to-Severe Stroke (NIHSS > 3) Protocol:** High risk of bleeding transformation! **Do NOT use DAPT**. Restrict treatment strictly to Single Antiplatelet Therapy (**Aspirin Only**).")

            # ------------------------------------------------------------------
            # 📋 COMPREHENSIVE STROKE WORKUP MANDATES
            # ------------------------------------------------------------------
            st.markdown("---")
            st.markdown("<div class='section-header'>📋 4. Mandatory Stroke Workup Checklist</div>", unsafe_allow_html=True)
            with st.expander("🔬 View Complete Diagnostic & Secondary Prevention Workup", expanded=True):
                st.markdown("""
                **1. Immediate Emergency Lab Orders:**
                * [ ] **Random Blood Sugar (RBS):** Rule out hypoglycemia (Essential mimic).
                * [ ] **Coagulation Profile:** PT, INR, aPTT (Critical if patient is on baselines).
                * [ ] **Complete Blood Count (CBC):** Check platelets (Must be > 100,000 for tPA).
                * [ ] **Renal Function Tests:** Serum Creatinine & Electrolytes (Needed for CTA/DOACs).
                * [ ] **Cardiac Enzymes:** Troponin level to rule out concurrent Type 2 Myocardial Infarction.
                
                **2. Secondary Etiology & Cardiac Evaluation (Within 24-48h):**
                * [ ] **12-Lead ECG:** Check immediately for Occult Atrial Fibrillation or acute ischemic changes.
                * [ ] **Echocardiography (TTE/TEE):** Assess for cardiac thrombus, patent foramen ovale (PFO), or ejection fraction.
                * [ ] **Carotid & Vertebral Doppler / CTA Neck:** Rule out significant large artery atherosclerosis/stenosis (>50% or >70%).
                * [ ] **Extended Cardiac Holter Monitoring:** Indicated if embolic stroke of undetermined source (ESUS) is highly suspected.
                
                **3. Metabolic & Fasting Labs (Next Morning):**
                * [ ] **Fasting Lipid Profile:** Target LDL < 70 mg/dL (or < 55 mg/dL if recurrent vascular events).
                * [ ] **HbA1c:** Optimize long-term glycemic control.
                """)

            # ------------------------------------------------------------------
            # 🔬 5. CARDIOEMBOLIC AF: TIMING GUIDE & GFR-BASED NOAC DOSING ENGINE
            # ------------------------------------------------------------------
            st.markdown("---")
            st.markdown("<div class='section-header'>🔬 5. Cardioembolic AF: Anticoagulation Timing & Dosing</div>", unsafe_allow_html=True)
            
            # Part A: Anticoagulation Timing Rule based strictly on calculated NIHSS
            with st.expander("⏱️ When to Start Oral Anticoagulation (DOACs) Post-Stroke:", expanded=True):
                st.caption("Dynamic advice based on the patient's calculated NIHSS score:")
                if total_nihss <= 3:
                    st.info("🟢 **Day 1 to 3 Initiation (Minor Stroke):** Safe to start oral anticoagulation early, provided a follow-up head CT rules out any microhemorrhage.")
                elif total_nihss <= 15:
                    st.warning("🟡 **Day 6 Initiation (Moderate Stroke):** Delay oral anticoagulation until Day 6. Ensure stability with an updated Non-Contrast CT prior to administration.")
                else:
                    st.error("🔴 **Day 12 to 14 Initiation (Severe Stroke):** High danger of hemorrhagic expansion. Hold anticoagulation for 12-14 days. Re-image via CT before first dose.")

            # Part B: GFR / CrCl Engine
            if p_sex == "Male":
                crcl = ((140 - p_age) * p_weight) / (72 * p_creatinine)
            else:
                crcl = (((140 - p_age) * p_weight) / (72 * p_creatinine)) * 0.85
                
            st.metric(label="Calculated Creatinine Clearance (CrCl):", value=f"{crcl:.1f} mL/min")
            
            # Part C: Targeted NOAC Dosing Guidelines
            with st.expander("💊 GFR-Based NOAC Dosing Adjustments:", expanded=True):
                st.markdown(f"**Current Renal Status:** CrCl = {crcl:.1f} mL/min")
                
                st.markdown("#### 🔹 Apixaban (Eliquis):")
                apixaban_criteria = 0
                if p_age >= 80: apixaban_criteria += 1
                if p_weight <= 60: apixaban_criteria += 1
                if p_creatinine >= 1.5: apixaban_criteria += 1
                
                if crcl < 15:
                    st.error("❌ Apixaban is Contraindicated (CrCl < 15 mL/min).")
                elif apixaban_criteria >= 2:
                    st.warning("⚠️ **Dose Reduced:** Give **2.5 mg BID**.")
                else:
                    st.success("🟢 **Standard Dose:** Give **5 mg BID**.")
                    
                st.markdown("#### 🔹 Rivaroxaban (Xarelto):")
                if crcl < 15:
                    st.error("❌ Rivaroxaban is Contraindicated (CrCl < 15 mL/min).")
                elif 15 <= crcl <= 50:
                    st.warning("⚠️ **Dose Reduced for Renal Impairment:** Give **15 mg Once Daily**.")
                else:
                    st.success("🟢 **Standard Dose:** Give **20 mg Once Daily**.")

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 12px;'>Al-Ahli Hospital Stroke Command Center App © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
