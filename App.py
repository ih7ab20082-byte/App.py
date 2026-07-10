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
    .main-title { font-size:38px !important; font-weight: bold; color: #1E3A8A; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:18px !important; color: #4B5563; text-align: center; margin-bottom: 25px; font-style: italic; }
    .branding-bar { background-color: #F3F4F6; padding: 15px; border-radius: 10px; border-left: 5px solid #2563EB; margin-bottom: 20px; }
    .section-header { font-size:22px !important; font-weight: bold; color: #1E3A8A; margin-top: 15px; margin-bottom: 15px; }
    .pearl-box { background-color: #FEF3C7; padding: 15px; border-radius: 8px; border-left: 5px solid #D97706; margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

# App Header & Branding
st.markdown("<div class='main-title'>🧠 Al-Ahli Hospital Advanced Stroke Command Center</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Comprehensive Clinical Decision Support System (CDSS) - Based on AHA/ASA Guidelines</div>", unsafe_allow_html=True)

# Your Professional Badge / Signature
st.markdown(f"""
<div class='branding-bar'>
    <strong>Project Founder & Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
    <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
    <strong>Scope:</strong> Evidence-Based Clinical Protocols & Medical Education
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Main Layout: Split Screen
col_eval, col_action = st.columns([1.3, 1])

# ==============================================================================
# RIGHT COLUMN: Clinical Evaluation, Calculators, Scale Systems
# ==============================================================================
with col_eval:
    st.markdown("<div class='section-header'>📋 1. Patient Demographics & Time Metrics</div>", unsafe_allow_html=True)
    
    with st.expander("👤 Quick Patient Profile", expanded=True):
        p_name = st.text_input("Patient Name / Initials (Optional):", placeholder="e.g., John Doe")
        p_age = st.number_input("Age:", min_value=1, max_value=120, value=65)
        p_id = st.text_input("Medical Record Number (MRN):")
        p_weight = st.number_input("Patient Weight (kg) - *Crucial for dosing*", min_value=30, max_value=200, value=70)

    with st.expander("⏱️ Door-to-Needle Quality Timer", expanded=True):
        st.caption("Tracks clinical efficiency milestones in the emergency department.")
        onset_time = st.number_input("Time since symptom onset (Hours):", min_value=0.0, max_value=168.0, value=2.0, step=0.5)
        door_time = st.number_input("Emergency Department Arrival to CT Scan Completion (Minutes):", min_value=1, max_value=180, value=25)
        target_tpa_time = st.number_input("Estimated Door-to-Needle Time (Minutes):", min_value=1, max_value=180, value=45)
        
        if target_tpa_time <= 60:
            st.success(f"⚡ Target Met: Door-to-Needle is within the gold standard (< 60 minutes). Efficiency Optimal!")
        else:
            st.error(f"⚠️ Target Delayed: Expected Door-to-Needle exceeds 60 mins. Streamline CT reading and lab processing immediately!")

    st.markdown("---")
    st.markdown("<div class='section-header'>🔬 2. Diagnostic Neuroimaging & Metrics</div>", unsafe_allow_html=True)
    
    ct_type = st.radio("Initial Non-Contrast CT Brain Finding:", 
                       ("Ischemic Stroke Path (No acute hemorrhage/large hypodensity)", 
                        "Hemorrhagic Stroke Path (Acute Intracerebral Hemorrhage - ICH)"))

    # A. PATHWAY 1: ISCHEMIC STROKE (NIHSS + ASPECTS)
    if ct_type == "Ischemic Stroke Path (No acute hemorrhage/large hypodensity)":
        
        with st.expander("📐 ASPECTS Calculator (Alberta Stroke Program Early CT Score)", expanded=True):
            st.caption("Deduct 1 point for any early ischemic change in the MCA territories below (Default is 10):")
            aspects_deductions = st.multiselect(
                "Select affected MCA regions on CT:",
                ["Caudate", "Lentiform", "Internal Capsule", "Insular Cortex", "M1 (Anterior MCA)", "M2 (Lateral MCA)", "M3 (Posterior MCA)", "M4 (Anterior Superior MCA)", "M5 (Lateral Superior MCA)", "M6 (Posterior Superior MCA)"]
            )
            aspects_score = 10 - len(aspects_deductions)
            st.metric("Final ASPECTS Score", aspects_score)
            if aspects_score < 6:
                st.warning("⚠️ Low ASPECTS (< 6): Indicates large established infarction. High risk of Hemorrhagic Transformation if tPA or EVT is attempted.")

        with st.expander("📝 Comprehensive NIHSS Calculator", expanded=False):
            st.caption("Rate the patient across the 11 clinical items:")
            n1 = st.radio("1a. Level of Consciousness (LOC):", (0, 1, 2, 3), format_func=lambda x: {0:"0: Alert", 1:"1: Not alert; somnolent", 2:"2: Not alert; obtunded", 3:"3: Comatose"}[x])
            n2 = st.radio("1b. LOC Questions (Month & Age):", (0, 1, 2), format_func=lambda x: {0:"0: Answers both correctly", 1:"1: Answers one correctly", 2:"2: Answers neither correctly"}[x])
            n3 = st.radio("1c. LOC Commands (Open/Close eyes & grip):", (0, 1, 2), format_func=lambda x: {0:"0: Performs both correctly", 1:"1: Performs one correctly", 2:"2: Performs neither correctly"}[x])
            n4 = st.radio("2. Best Gaze (Horizontal Eye Movements):", (0, 1, 2), format_func=lambda x: {0:"0: Normal", 1:"1: Partial gaze palsy", 2:"2: Forced deviation"}[x])
            n5 = st.radio("3. Visual Fields:", (0, 1, 2, 3), format_func=lambda x: {0:"0: No visual loss", 1:"1: Partial hemianopia", 2:"2: Complete hemianopia", 3:"3: Bilateral hemianopia"}[x])
            n6 = st.radio("4. Facial Palsy:", (0, 1, 2, 3), format_func=lambda x: {0:"0: Normal symmetric movement", 1:"1: Minor paralysis (flattened nasolabial fold)", 2:"2: Partial paralysis (lower face)", 3:"3: Complete paralysis (upper & lower face)"}[x])
            n7 = st.radio("5. Motor Arm (Worst Limb):", (0, 1, 2, 3, 4), format_func=lambda x: {0:"0: No drift (holds 90° for 10s)", 1:"1: Drift before 10s", 2:"2: Some effort against gravity", 3:"3: No effort against gravity", 4:"4: No movement"}[x])
            n8 = st.radio("6. Motor Leg (Worst Limb):", (0, 1, 2, 3, 4), format_func=lambda x: {0:"0: No drift (holds 30° for 5s)", 1:"1: Drift before 5s", 2:"2: Some effort against gravity", 3:"3: No effort against gravity", 4:"4: No movement"}[x])
            n9 = st.radio("7. Limb Ataxia (Coordination):", (0, 1, 2), format_func=lambda x: {0:"0: Absent", 1:"1: Present in one limb", 2:"2: Present in two or more limbs"}[x])
            n10 = st.radio("8. Sensory (Pinprick response):", (0, 1, 2), format_func=lambda x: {0:"0: Normal", 1:"1: Mild-to-moderate loss", 2:"2: Severe or total loss"}[x])
            n11 = st.radio("9. Best Language (Aphasia):", (0, 1, 2, 3), format_func=lambda x: {0:"0: Normal; no aphasia", 1:"1: Mild-to-moderate aphasia", 2:"2: Severe aphasia", 3:"3: Global aphasia/mute"}[x])
            n12 = st.radio("10. Dysarthria (Speech Clarity):", (0, 1, 2), format_func=lambda x: {0:"0: Normal", 1:"1: Mild-to-moderate dysarthria", 2:"2: Severe dysarthria/unintelligible"}[x])
            n13 = st.radio("11. Extinction and Inattention (Neglect):", (0, 1, 2), format_func=lambda x: {0:"0: No neglect", 1:"1: Partial neglect", 2:"2: Complete neglect"}[x])
            total_nihss = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 + n11 + n12 + n13
            st.metric("Current NIHSS Score", total_nihss)

    # B. PATHWAY 2: HEMORRHAGIC STROKE (ICH SCORE)
    else:
        with st.expander("📊 ICH Score Calculator (Intracerebral Hemorrhage Mortality Predictor)", expanded=True):
            st.caption("Calculate the risk profile for hemorrhagic stroke cases:")
            ich_gcs = st.radio("Initial GCS Score:", (0, 1, 2), format_func=lambda x: {0:"GCS 3-4 (2 points)", 1:"GCS 5-12 (1 point)", 2:"GCS 13-15 (0 points)"}[x])
            ich_vol = st.radio("ICH Volume on CT Scan:", (0, 1), format_func=lambda x: {0:">= 30 cm³ (1 point)", 1:"< 30 cm³ (0 points)"}[x])
            ich_ivh = st.radio("Intraventricular Hemorrhage (IVH) Extension:", (0, 1), format_func=lambda x: {0:"Yes (1 point)", 1:"No (0 points)"}[x])
            ich_infra = st.radio("Infratentorial Origin of Hemorrhage:", (0, 1), format_func=lambda x: {0:"Yes (1 point)", 1:"No (0 points)"}[x])
            ich_age = st.radio("Patient Age:", (0, 1), format_func=lambda x: {0:">= 80 Years Old (1 point)", 1:"< 80 Years Old (0 points)"}[x])
            
            # GCS score maps backwards for points calculation
            gcs_pts = 2 if ich_gcs == 0 else (1 if ich_gcs == 1 else 0)
            vol_pts = 1 if ich_vol == 0 else 0
            ivh_pts = 1 if ich_ivh == 0 else 0
            infra_pts = 1 if ich_infra == 0 else 0
            age_pts = 1 if ich_age == 0 else 0
            
            total_ich_score = gcs_pts + vol_pts + ivh_pts + infra_pts + age_pts
            st.metric("Total ICH Score", total_ich_score)

# ==============================================================================
# LEFT COLUMN: Adaptive Decision Trees, Treatment Protocols, & Post-Workup
# ==============================================================================
with col_action:
    st.markdown("<div class='section-header'>⚡ 3. Decision Support & Management Protocols</div>", unsafe_allow_html=True)
    
    sbp = st.number_input("Systolic Blood Pressure (SBP mmHg):", min_value=50, max_value=260, value=160)
    dbp = st.number_input("Diastolic Blood Pressure (DBP mmHg):", min_value=30, max_value=180, value=95)
    
    # --- IF HEMORRHAGIC PATHWAY IS ACTIVE ---
    if ct_type == "Hemorrhagic Stroke Path (Acute Intracerebral Hemorrhage - ICH)":
        st.error("🔴 HEMORRHAGIC STROKE CRITICAL PATHWAY ACTIVATED")
        st.markdown(f"""
        ### 🎯 Acute Blood Pressure Targets (INTERACT-2 / ATACH-2):
        * **Target SBP:** Maintain strictly between **130 - 140 mmHg** to limit hematoma expansion.
        * **Current SBP Status:** {"🔴 Elevated! Start aggressive IV titration." if sbp > 140 else "🟢 Within optimal targets."}
        
        ### 💊 Emergent Medical Management:
        1. **Anticoagulation Reversal:** If patient is on Warfarin, give Prothrombin Complex Concentrate (PCC) + Vitamin K 10mg IV. If on DOACs (Apixaban/Rivaroxaban), consider *Andexanet Alfa*.
        2. **ICP Management:** Elevate head of bed to 30°, maintain normothermia, and administer Mannitol 20% (0.5-1 g/kg IV) or Hypertonic Saline if signs of herniation appear.
        3. **Neurosurgery Consult:** Emergent contact for clot evacuation if cerebellar hemorrhage is present or worsening mass effect.
        """)
        
    # --- IF ISCHEMIC PATHWAY IS ACTIVE ---
    else:
        cta_result = st.radio("CT Angiography (CTA) / Large Vessel Occlusion (LVO) Status:", 
                              ("Pending / Not Done", 
                               "Confirmed LVO (ICA, MCA-M1/M2, Basilar)", 
                               "No LVO / Small Vessel Occlusion Only"))
        
        tpa_eligible = False
        evt_eligible = False
        medical_only = False
        
        if aspects_score < 6:
            st.error("❌ High Risk: Fibrinolysis/EVT contraindicated due to massive early ischemic changes (ASPECTS < 6). Rely on Medical Treatment.")
            medical_only = True
        else:
            if onset_time <= 4.5:
                tpa_eligible = True
                st.success(f"🟢 Within IV tPA Window (< 4.5 hrs from onset).")
                if sbp > 185 or dbp > 110:
                    st.warning("⚠️ BP Contraindication: SBP must be reduced below 185/110 mmHg using Labetalol before tPA initialization.")
                    tpa_eligible = False
            else:
                st.info(f"🟠 Outside IV tPA window ({onset_time} hrs). Assessing for Endovascular Thrombectomy.")
                
            if "Confirmed LVO" in cta_result and onset_time <= 24.0 and total_nihss >= 6:
                evt_eligible = True
                st.success("🎯 Endovascular Thrombectomy (EVT) Candidate! Emergent activation of Angio-Suite required (DAWN/DEFUSE 3 criteria).")
            elif "No LVO" in cta_result or onset_time > 24.0:
                medical_only = True

        # tPA Dosing Calculator Output
        if tpa_eligible:
            total_dose = min(p_weight * 0.9, 90.0)
            bolus = total_dose * 0.10
            infusion = total_dose * 0.90
            
            st.markdown(f"""
            ### 💉 IV Alteplase (tPA) Dosing Commands:
            * **Total Calculated Dose:** **{total_dose:.1f} mg**
            * 🧪 **IV Bolus (10%):** Give **{bolus:.1f} mg** IV push over **1 minute**.
            * 💧 **IV Infusion (90%):** Infuse remaining **{infusion:.1f} mg** over **60 minutes** via electronic pump.
            """)
            if evt_eligible:
                st.warning("🧠 **Bridging Therapy:** Begin IV tPA infusion immediately and transfer to the cath lab simultaneously without waiting for clinical response!")

        # Medical Treatment Path
        if medical_only or (onset_time > 4.5 and not evt_eligible):
            st.markdown("""
            ### 💊 Acute Medical Management Protocol:
            1. **Antiplatelets (Aspirin):** Start **Aspirin 162-325 mg** immediately. If minor non-cardioembolic stroke (NIHSS ≤ 3), initiate **Dual Antiplatelet Therapy (DAPT)**: Aspirin + Clopidogrel 300mg loading dose, then daily for 21 days (CHANCE/POINT trials).
            2. **Permissive Hypertension:** Allow SBP up to **220/120 mmHg** unless target-organ damage exists, to optimize perfusion to the ischemic penumbra. Deduct BP by 15% only if it spikes over threshold.
            3. **Neuroprotection:** Keep oxygen saturation > 94%, control glucose (140-180 mg/dL), and keep core temperature normal.
            """)

    # ==============================================================================
    # 4. STEP-DOWN INPATIENT WORKUP & ANTICOAGULATION TIMING
    # ==============================================================================
    st.markdown("---")
    st.markdown("<div class='section-header'>🔬 4. Inpatient Workup & Long-Term Management</div>", unsafe_allow_html=True)
    
    with st.expander("📊 Secondary Prevention & Etiology Workup (TOAST Criteria)", expanded=False):
        st.markdown("""
        * **Carotid Doppler:** Evaluate for severe internal carotid artery stenosis. If > 70% ipsilateral stenosis is found, prepare for Carotid Endarterectomy (CEA) or stenting within 14 days.
        * **Transthoracic/Transesophageal Echocardiogram (TTE/TEE):** Rule out cardiac thrombus, severe wall akinesia, or Patent Foramen Ovale (PFO).
        * **24-48h continuous Holter Monitoring:** Essential to capture Paroxysmal Atrial Fibrillation (AF). If verified, discontinue antiplatelets and transition to Oral Anticoagulation (DOACs).
        * **Lipid Management:** Start **Atorvastatin 80 mg** immediately. Target *LDL-C* threshold must be **< 55 mg/dL**.
        """)

    with st.expander("⏱️ Cardioembolic AF Anticoagulation Timing Guide", expanded=False):
        st.caption("When to initiate oral anticoagulation (DOACs) post-ischemic stroke caused by Atrial Fibrillation:")
        af_nihss = st.slider("Select Patient Baseline NIHSS for AF timing:", 0, 42, int(total_nihss if ct_type.startswith("Ischemic") else 10))
        
        if af_nihss <= 3:
            st.info("🟢 **Day 1 to 3 Initiation:** Minor stroke. Safe to start DOAC (Apixaban/Rivaroxaban) early once hemorrhagic transformation is ruled out by follow-up CT.")
        elif af_nihss <= 15:
            st.warning("🟡 **Day 6 Initiation:** Moderate stroke. Postpone initiation until day 6. Confirm stability with an updated CT scan prior to dosing.")
        else:
            st.error("🔴 **Day 12 to 14 Initiation:** Severe stroke. High bleeding risk. Delay anticoagulation for 12-14 days. Perform a repeat Non-Contrast CT to guarantee safety.")

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 12px;'>Al-Ahli Hospital Stroke Command Center App © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
