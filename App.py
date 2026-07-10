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
col_eval, col_action = st.columns([1.3, 1])

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
    st.markdown("<div class='section-header'>🔬 2. Neuroimaging Modality & NIHSS</div>", unsafe_allow_html=True)
    
    imaging_type = st.radio("Select Initial Imaging & Findings:", 
                       ("Non-Contrast CT: Ischemic Stroke Path (No acute hemorrhage)", 
                        "Diffusion MRI (DWI): Confirmed Acute Ischemic Infarct",
                        "Non-Contrast CT: Hemorrhagic Stroke Path (Acute ICH)"))

    # NIHSS Section with descriptions
    if "Ischemic" in imaging_type or "Diffusion" in imaging_type:
        with st.expander("📝 Comprehensive NIHSS Calculator", expanded=True):
            st.caption("Rate the patient across the 11 clinical items (Text descriptions included below):")
            
            n1 = st.radio("1a. Level of Consciousness (LOC):", (0, 1, 2, 3), 
                          format_func=lambda x: {0:"0: Alert", 1:"1: Not alert; somnolent", 2:"2: Not alert; obtunded", 3:"3: Comatose"}[x])
            
            n2 = st.radio("1b. LOC Questions (Month & Age):", (0, 1, 2), 
                          format_func=lambda x: {0:"0: Answers both correctly", 1:"1: Answers one correctly", 2:"2: Answers neither correctly"}[x])
            
            n3 = st.radio("1c. LOC Commands (Open/Close eyes & grip):", (0, 1, 2), 
                          format_func=lambda x: {0:"0: Performs both correctly", 1:"1: Performs one correctly", 2:"2: Performs neither correctly"}[x])
            
            n4 = st.radio("2. Best Gaze (Horizontal Eye Movements):", (0, 1, 2), 
                          format_func=lambda x: {0:"0: Normal", 1:"1: Partial gaze palsy", 2:"2: Forced deviation"}[x])
            
            n5 = st.radio("3. Visual Fields:", (0, 1, 2, 3), 
                          format_func=lambda x: {0:"0: No visual loss", 1:"1: Partial hemianopia", 2:"2: Complete hemianopia", 3:"3: Bilateral hemianopia"}[x])
            
            n6 = st.radio("4. Facial Palsy:", (0, 1, 2, 3), 
                          format_func=lambda x: {0:"0: Normal symmetric movement", 1:"1: Minor paralysis", 2:"2: Partial paralysis", 3:"3: Complete paralysis"}[x])
            
            n7 = st.radio("5. Motor Arm (Worst Limb):", (0, 1, 2, 3, 4), 
                          format_func=lambda x: {0:"0: No drift (holds 90° for 10s)", 1:"1: Drift before 10s", 2:"2: Some effort against gravity", 3:"3: No effort against gravity", 4:"4: No movement"}[x])
            
            n8 = st.radio("6. Motor Leg (Worst Limb):", (0, 1, 2, 3, 4), 
                          format_func=lambda x: {0:"0: No drift (holds 30° for 5s)", 1:"1: Drift before 5s", 2:"2: Some effort against gravity", 3:"3: No effort against gravity", 4:"4: No movement"}[x])
            
            n9 = st.radio("7. Limb Ataxia (Coordination):", (0, 1, 2), 
                          format_func=lambda x: {0:"0: Absent", 1:"1: Present in one limb", 2:"2: Present in two or more limbs"}[x])
            
            n10 = st.radio("8. Sensory (Pinprick response):", (0, 1, 2), 
                           format_func=lambda x: {0:"0: Normal", 1:"1: Mild-to-moderate loss", 2:"2: Severe or total loss"}[x])
            
            n11 = st.radio("9. Best Language (Aphasia):", (0, 1, 2, 3), 
                           format_func=lambda x: {0:"0: Normal; no aphasia", 1:"1: Mild-to-moderate aphasia", 2:"2: Severe aphasia", 3:"3: Global aphasia/mute"}[x])
            
            n12 = st.radio("10. Dysarthria (Speech Clarity):", (0, 1, 2), 
                           format_func=lambda x: {0:"0: Normal", 1:"1: Mild-to-moderate dysarthria", 2:"2: Severe dysarthria"}[x])
            
            n13 = st.radio("11. Extinction and Inattention (Neglect):", (0, 1, 2), 
                           format_func=lambda x: {0:"0: No neglect", 1:"1: Partial neglect", 2:"2: Complete neglect"}[x])
            
            total_nihss = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 + n11 + n12 + n13
            
            st.metric("Current NIHSS Score", total_nihss)
            if total_nihss > 22:
                st.error("⚠️ CRITICAL WARNING: High NIHSS (> 22) indicates massive hemispheric stroke. Severe risk of post-tPA Hemorrhagic Transformation! Consider EVT over systemic lysis.")
    else:
        total_nihss = 0

# ==============================================================================
# LEFT COLUMN: Adaptive Management Protocols & Core Decisions
# ==============================================================================
with col_action:
    st.markdown("<div class='section-header'>⚡ 3. Decision Support & Treatment Protocols</div>", unsafe_allow_html=True)
    
    sbp = st.number_input("Systolic Blood Pressure (SBP mmHg):", min_value=50, max_value=260, value=160)
    dbp = st.number_input("Diastolic Blood Pressure (DBP mmHg):", min_value=30, max_value=180, value=95)
    
    if "Hemorrhagic" in imaging_type:
        st.error("🔴 HEMORRHAGIC STROKE CRITICAL PATHWAY ACTIVATED")
        st.markdown("Target SBP: **130 - 140 mmHg**. Initiate aggressive IV Labetalol titration. Reverse coagulopathy immediately.")
    else:
        cta_result = st.radio("CT Angiography (CTA) / LVO Status:", 
                              ("Pending / Not Done", "Confirmed LVO (ICA, MCA-M1/M2, Basilar)", "No LVO"))
        
        tpa_eligible = (onset_time <= 4.5 and sbp <= 185 and dbp <= 110 and total_nihss <= 22)
        evt_eligible = ("Confirmed LVO" in cta_result and onset_time <= 24.0 and total_nihss >= 6)

        if tpa_eligible:
            total_dose = min(p_weight * 0.9, 90.0)
            st.success(f"💉 **IV tPA (Alteplase) Dose Commands:** Total: **{total_dose:.1f} mg** | Bolus (10%): **{total_dose*0.1:.1f} mg** | Infusion (90%): **{total_dose*0.9:.1f} mg** over 60 mins.")
        
        st.markdown("### 💊 Acute Antiplatelet Strategy:")
        if total_nihss <= 3 and total_nihss > 0:
            st.info("🟢 **Minor Stroke (NIHSS ≤ 3) Protocol:** Safe for **Dual Antiplatelet Therapy (DAPT)**. Initiate Aspirin 162-325mg + Clopidogrel 300mg load, then continue DAPT for 21 days.")
        elif total_nihss > 3:
            st.warning("⚠️ **Moderate-to-Severe Stroke (NIHSS > 3) Protocol:** High risk of bleeding transformation! **Do NOT use DAPT**. Restrict to Single Antiplatelet Therapy (**Aspirin Only**).")

        st.markdown("### ⏱️ 4. Post-Intervention Ward Protocols (First 24h)")
        with st.sidebar:
            st.markdown("### 🚨 Post-tPA & EVT Nursing Mandates:")
            st.markdown("""
            * **Neurological Checks:** Every 15 mins for 2 hours, then every 30 mins for 6 hours, then hourly for 16 hours.
            * **Blood Pressure Targets:** Maintain strictly **< 180/105 mmHg**.
            * **Follow-up Imaging:** Order a repeat **Non-Contrast CT Brain at 24 hours** post-procedure. *Antiplatelets or anticoagulants must NOT be started until this scan rules out hemorrhage.*
            """)
        st.caption("👈 See side panel for detailed post-procedure nursing orders.")

        # ==============================================================================
        # 5. CARDIOEMBOLIC AF: TIMING GUIDE & GFR-BASED NOAC DOSING ENGINE
        # ==============================================================================
        st.markdown("---")
        st.markdown("<div class='section-header'>🔬 5. Cardioembolic AF: Anticoagulation Timing & Dosing</div>", unsafe_allow_html=True)
        
        # Part A: Anticoagulation Timing Rule (1-3-6-12 Day Rule)
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
