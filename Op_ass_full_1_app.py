import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Al-Ahli Perioperative Fitness Engine",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS Styles for Medical CDSS UI
st.markdown("""
    <style>
    .main-title { font-size:26px !important; font-weight: bold; color: #0F766E; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:13px !important; color: #4B5563; text-align: center; margin-bottom: 20px; font-style: italic; }
    .branding-bar { background-color: #F0FDFA; padding: 12px; border-radius: 10px; border-left: 6px solid #0F766E; margin-bottom: 20px; }
    .section-header { font-size:18px !important; font-weight: bold; color: #0F766E; margin-top: 15px; margin-bottom: 15px; border-bottom: 2px solid #E5E7EB; padding-bottom: 5px; }
    .status-box { padding: 12px; border-radius: 6px; margin-bottom: 12px; border: 1px solid #E5E7EB; background-color: #F9FAFB; color: #1F2937; }
    .danger-box { padding: 12px; border-radius: 6px; margin-bottom: 12px; border: 1px solid #DC2626; background-color: #FEF2F2; color: #991B1B; }
    .info-box { padding: 12px; border-radius: 6px; margin-bottom: 12px; border: 1px solid #2563EB; background-color: #EFF6FF; color: #1E40AF; }
    .workup-box { padding: 12px; border-radius: 6px; margin-bottom: 12px; border: 1px solid #D97706; background-color: #FFFBEB; color: #92400E; }
    .specialty-box { padding: 12px; border-radius: 6px; margin-bottom: 12px; border: 1px solid #7C3AED; background-color: #F5F3FF; color: #5B21B6; }
    </style>
""", unsafe_allow_html=True)

# 3. Header & Department Branding
st.markdown("<div class='main-title'>🏥 Al-Ahli Hospital Comprehensive Perioperative Medical Fitness Engine</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Advanced Automation Decision Matrix for Surgical Clearance & Multi-System Comorbidity Optimization</div>", unsafe_allow_html=True)

st.markdown("""
<div class='branding-bar'>
    <div style='color: #1F2937; font-size: 14px; line-height: 1.5;'>
        <strong>Project Director:</strong> Dr. Ihab Abbass Abu Hilail &nbsp;|&nbsp; 
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital<br>
        <strong>Clinical Guidelines:</strong> ACC/AHA Perioperative Cardiac Updates, ARISCAT Matrix, ASA Classification, ATA Thyroid Guidelines
    </div>
</div>
""", unsafe_allow_html=True)

# 4. Create App Tabs
tabs = st.tabs([
    "👤 Patient Profile & Vitals",
    "🩺 Clinical Exam & Labs Panel",
    "🧠 Epilepsy & Thyroid Specialty Focus",
    "📊 Risk Stratification Models",
    "📋 Global Clearance Summary Dashboard"
])

# ==============================================================================
# TAB 1: PATIENT PROFILE, SURGERY DETAILS & VITALS
# ==============================================================================
with tabs[0]:
    st.markdown("<div class='section-header'>Patient Profile and Surgical Procedure Metadata</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        patient_name = st.text_input("Patient Name / ID Number:", value="John Doe")
        patient_age = st.number_input("Patient Age:", min_value=18, max_value=110, value=60)
        op_type = st.selectbox("Type of Scheduled Surgery (Inherent Risk Classification):", [
            "Low Risk (Cataract, Superficial Surgery, Upper/Lower GI Endoscopy)",
            "Intermediate Risk (Orthopedic Major Joint, Cholecystectomy, Prostatectomy, Uncomplicated Hernia)",
            "High Risk (Major Vascular, Open Aortic Surgery, Thoracoabdominal Thoracotomy, Total Cystectomy)"
        ])
        op_duration = st.number_input("Expected Duration of Surgery (in Hours):", min_value=0.5, max_value=12.0, value=2.0, step=0.5)
        is_emergency = st.checkbox("Is this an emergency or urgent surgical procedure?")
        
    with col2:
        st.markdown("<h4 style='color:#0F766E; margin-top:0px;'>Admission Vital Signs</h4>", unsafe_allow_html=True)
        sbp = st.number_input("Systolic Blood Pressure (mmHg):", value=130)
        dbp = st.number_input("Diastolic Blood Pressure (mmHg):", value=80)
        hr = st.number_input("Heart Rate (bpm):", value=75)
        spo2 = st.slider("Preoperative SpO2 on Room Air (%):", min_value=50, max_value=100, value=97)
        temp = st.number_input("Temperature (°C):", value=36.7, step=0.1)

    st.markdown("<div class='section-header'>Immediate Clinical Triggers</div>", unsafe_allow_html=True)
    vitals_alerts = []
    if spo2 < 92: vitals_alerts.append(f"🔴 CRITICAL HYPOXEMIA DETECTED: Preoperative SpO2 is low ({spo2}%).")
    if sbp >= 180 or dbp >= 110: vitals_alerts.append(f"🔴 CRITICAL HYPERTENSION DETECTED: ({sbp}/{dbp} mmHg). Delay elective cases.")
    if temp >= 38.0: vitals_alerts.append(f"🔴 PREOPERATIVE PYREXIA / FEVER: Patient temperature is {temp}°C.")
        
    if vitals_alerts:
        for alert in vitals_alerts: st.markdown(f"<div class='danger-box'>{alert}</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='status-box' style='border-left: 5px solid #16A34A;'>🟢 Vital Signs Baseline: Stable.</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 2: CLINICAL EXAMINATION & LABS PANEL
# ==============================================================================
with tabs[1]:
    st.markdown("<div class='section-header'>Comprehensive Clinical Evaluation and Diagnostic Diagnostics</div>", unsafe_allow_html=True)
    col_ex1, col_ex2 = st.columns(2)
    with col_ex1:
        st.markdown("<h4 style='color:#0F766E; margin-top:0px;'>Targeted Physical Examination Findings</h4>", unsafe_allow_html=True)
        chest_ausc = st.selectbox("Chest Auscultation:", ["Clear Lung Fields", "Diffuse Wheezing", "Basal Bilateral Crepitations (Rales)", "Decreased Air Entry / Dullness"])
        cv_ausc = st.selectbox("Cardiovascular Auscultation:", ["Normal S1 S2, No Murmurs", "Systolic Murmur (Possible Aortic Stenosis)", "Diastolic Murmur", "S3 Gallop Rhythm Present"])
        jvp = st.radio("Jugular Venous Pressure (JVP):", ["Normal / Not Elevated", "Elevated JVP (Sign of Volume Overload)"])
        edema = st.checkbox("Bilateral Lower Limb Pitting Edema Present")
        
    with col_ex2:
        st.markdown("<h4 style='color:#0F766E; margin-top:0px;'>Cardiopulmonary Diagnostics (ECG, ECHO, CXR)</h4>", unsafe_allow_html=True)
        ecg_findings = st.selectbox("Electrocardiogram (ECG) Report:", ["Normal Sinus Rhythm", "Sinus Tachycardia / Bradycardia", "Atrial Fibrillation with Controlled VR", "Atrial Fibrillation with Rapid VR", "Pathological Q Waves / Ischemic ST-T Changes", "Left Bundle Branch Block (LBBB)"])
        ef_val = st.number_input("Left Ventricular Ejection Fraction (LVEF %):", min_value=10, max_value=85, value=55)
        cxr_findings = st.selectbox("Chest X-Ray (CXR) Findings:", ["Clear Lung Fields", "Cardiomegaly", "Pulmonary Congestion / Cephalization", "Consolidation / Focal Infiltrate"])

    st.markdown("<h4 style='color:#0F766E; margin-top:20px;'>Preoperative Laboratory Dashboard (Complete Panel)</h4>", unsafe_allow_html=True)
    col_lab1, col_lab2, col_lab3 = st.columns(3)
    with col_lab1:
        hb = st.number_input("Current Hemoglobin (g/dL):", value=13.5, step=0.1)
        wbc = st.number_input("White Blood Cells (x10^3/µL):", value=7.5, step=0.1)
    with col_lab2:
        scr = st.number_input("Current Serum Creatinine (mg/dL):", value=0.9, step=0.1)
        potassium = mEq_val = st.number_input("Serum Potassium (mEq/L):", value=4.2, step=0.1)
    with col_lab3:
        plt = st.number_input("Platelet Count (x10^3/µL):", value=250)
        inr_val = st.number_input("INR Level:", value=1.0, step=0.1)

# ==============================================================================
# TAB 3:🧠 EPILEPSY & THYROID SPECIALTY FOCUS (NEW EXTENSIVE APPROACH)
# ==============================================================================
with tabs[2]:
    st.markdown("<div class='section-header'>🦋 1. Integrated Thyroid Status & Home Medication Approach</div>", unsafe_allow_html=True)
    
    col_th1, col_th2, col_th3 = st.columns(3)
    with col_th1:
        tsh_level = st.number_input("Thyroid Stimulating Hormone (TSH) Level (µIU/mL):", value=2.0, step=0.1, help="Normal: 0.45 - 4.5 µIU/mL")
    with col_th2:
        ft4_level = st.number_input("Free T4 (FT4) Level (ng/dL):", value=1.2, step=0.01, help="Normal: 0.8 - 1.8 ng/dL")
    with col_th3:
        ft3_level = st.number_input("Free T3 (FT3) Level (pg/mL):", value=3.0, step=0.01, help="Normal: 2.3 - 4.2 pg/mL")

    st.markdown("##### 💊 Active Home Thyroid Medications")
    thyroid_meds = st.multiselect("Select what thyroid medications the patient is currently taking:", [
        "Levothyroxine (Euthyrox / Synthroid)", "Carbimazole", "Propylthiouracil (PTU)", "None"
    ], default=["None"])

    # Live Analysis Logic for Thyroid
    is_thyroid_abnormal = (tsh_level > 4.5 or Tsh_level < 0.45 or ft4_level > 1.8 or ft4_level < 0.8)
    
    if is_thyroid_abnormal or "None" not in thyroid_meds:
        st.markdown("🗣️ **Thyroid Clinical Optimization Plan:**")
        if tsh_level > 4.5:
            if ft4_level < 0.8:
                st.markdown("<div class='danger-box'><b>Classification: Overt Hypothyroidism (Severe الخمول الحاد)</b><br>• <b>Surgical Recommendation:</b> Postpone all elective major operations. High risk of intraoperative cardiovascular collapse, severe bradycardia, and delayed awakening from general anesthesia.<br>• <b>Action:</b> Initiate or adjust Levothyroxine dose and recheck. Avoid clearance until patient is stable.</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='workup-box'><b>Classification: Subclinical Hypothyroidism (الخمول البسيط/الظاهري)</b><br>• <b>Surgical Recommendation:</b> Safe to proceed with surgery. No documented risk of excess surgical complications.<br>• <b>Action:</b> Continue home dose.</div>", unsafe_allow_html=True)
        elif tsh_level < 0.45:
            if ft4_level > 1.8 or ft3_level > 4.2:
                st.markdown("<div class='danger-box'><b>Classification: Overt Hyperthyroidism (Severe النشاط الحاد)</b><br>• <b>Surgical Recommendation:</b> ABSOLUTE CONTRAINDICATION for elective procedures. Extreme risk of life-threatening <b>Thyroid Storm (العاصفة الدرقية)</b>.<br>• <b>Action:</b> Postpone immediately. Control with Antithyroid drugs + Beta-blockers (Propranolol) to reach euthyroid status before surgery.</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='workup-box'><b>Classification: Subclinical Hyperthyroidism</b><br>• <b>Surgical Recommendation:</b> Proceed with caution. Monitor intraoperative heart rates carefully.</div>", unsafe_allow_html=True)
        
        # Thyroid Med Stewardship
        for med in thyroid_meds:
            if "Levothyroxine" in med:
                st.markdown("<div class='info-box'>📋 <b>Levothyroxine Stewardship:</b> GIVE the normal morning dose with a small sip of water on the day of surgery. (Long half-life of 7 days means missing one day won't cause immediate crisis, but maintaining steady serum levels prevents cardiac lability).</div>", unsafe_allow_html=True)
            if "Carbimazole" in med or "PTU" in med:
                st.markdown("<div class='info-box'>📋 <b>Anti-Thyroid Drug Stewardship:</b> GIVE normal home dose on the morning of surgery to prevent perioperative thyroid hormone escape under surgical stress.</div>", unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    st.markdown("<div class='section-header'>🧠 2. Integrated Epilepsy Status & Antiepileptic Drug (AED) Stewardship</div>", unsafe_allow_html=True)
    
    last_seizure = st.selectbox("Time Window of Last Documented Seizure:", [
        "Patient does NOT have Epilepsy", 
        "Seizure-free for > 6 months", 
        "Seizure within the last 6 months", 
        "Seizure within the last 30 days"
    ])
    
    if last_seizure != "Patient does NOT have Epilepsy":
        st.markdown("##### 💊 Active Antiepileptic Medications & IV Bridging Approach")
        selected_aeds = st.multiselect("Identify current home Antiepileptic Drugs (AEDs):", [
            "Levetiracetam (Keppra)", "Sodium Valproate (Depakine)", "Carbamazepine (Tegretol)", "Lamotrigine (Lamictal)", "Phenytoin (Epanutin)"
        ])
        
        # Display Approach for each Selected Seizure Drug
        for aed in selected_aeds:
            if "Levetiracetam" in aed:
                st.markdown("<div class='specialty-box'>🧠 <b>Levetiracetam (Keppra) Comprehensive Approach:</b><br>• <b>Morning of Surgery:</b> GIVE regular morning dose orally with a tiny sip of water.<br>• <b>NPO Bridging Phase:</b> If patient is NPO post-op, convert to <b>IV Keppra at a 1:1 ratio</b> (e.g., 500mg PO BID changes to 500mg IV BID infused over 15 minutes). Highly stable and preferred perioperatively.</div>", unsafe_allow_html=True)
            if "Sodium Valproate" in aed:
                st.markdown("<div class='specialty-box'>🧠 <b>Sodium Valproate (Depakine) Comprehensive Approach:</b><br>• <b>Morning of Surgery:</b> GIVE regular home dose.<br>• <b>NPO Bridging Phase:</b> Convert to <b>IV Depakine at a 1:1 ratio</b>. <i>Clinical Note:</i> Meticulously check preoperative platelet count as Valproate can cause transient dose-dependent thrombocytopenia or plate dysfunction.</div>", unsafe_allow_html=True)
            if "Carbamazepine" in aed:
                st.markdown("<div class='specialty-box' style='border-color: #B45309; background-color: #FFFBEB; color: #78350F;'>🧠 <b>Carbamazepine (Tegretol) Comprehensive Approach:</b><br>• <b>Morning of Surgery:</b> GIVE regular morning dose orally.<br>• <b>NPO Bridging Phase:</b> ⚠️ <b>No direct IV formulation is available for Carbamazepine.</b> If the patient will be NPO for more than 24 hours, you must consult neurology to bridge with an alternative IV drug such as <b>IV Levetiracetam (Keppra) or Phenytoin</b> to prevent therapeutic drop and breakthrough seizures.</div>", unsafe_allow_html=True)
            if "Lamotrigine" in aed:
                st.markdown("<div class='specialty-box'>🧠 <b>Lamotrigine (Lamictal) Comprehensive Approach:</b><br>• <b>Morning of Surgery:</b> GIVE morning dose.<br>• <b>NPO Bridging Phase:</b> ⚠️ <b>No direct IV formulation available.</b> However, Lamotrigine has a long half-life (~24-30 hrs). If NPO window is short (<24h), it can be restarted orally as soon as bowel sounds return. If prolonged NPO is expected, alternate seizure coverage is required.</div>", unsafe_allow_html=True)
            if "Phenytoin" in aed:
                st.markdown("<div class='danger-box' style='background-color: #FFF5F5; border-color: #E53E3E; color: #9B2C2C;'>🧠 <b>Phenytoin (Epanutin) Comprehensive Approach:</b><br>• <b>Morning of Surgery:</b> GIVE regular morning dose.<br>• <b>NPO Bridging Phase:</b> Convert to <b>IV Phenytoin at a 1:1 ratio</b>.<br>• ⚠️ <i>CRITICAL INFUSION SAFETY:</i> IV Phenytoin must be given slowly (maximum speed < 50 mg/min) and mixed **only** with Normal Saline (causes precipitation in Dextrose). Continuous ECG monitoring during infusion is recommended due to risks of bradycardia and arrhythmias.</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 4: RISK STRATIFICATION MODELS
# ==============================================================================
with tabs[3]:
    st.markdown("<div class='section-header'>Objective Risk Scoring Frameworks</div>", unsafe_allow_html=True)
    col_r1, col_r2 = st.columns(2)
    
    with col_r1:
        st.markdown("<h4 style='color:#0F766E; margin-top:0px;'>1. Revised Cardiac Risk Index (RCRI)</h4>", unsafe_allow_html=True)
        rcri_1 = st.checkbox("High-risk surgery criteria met", value=("High Risk" in op_type))
        rcri_2 = st.checkbox("History of Ischemic Heart Disease")
        rcri_3 = st.checkbox("History of Congestive Heart Failure")
        rcri_4 = st.checkbox("History of Cerebrovascular Disease")
        rcri_5 = st.checkbox("Preoperative Insulin Therapy")
        rcri_6 = st.checkbox("Preoperative Serum Creatinine > 2.0 mg/dL", value=(scr > 2.0))
        
        rcri_score = sum([rcri_1, rcri_2, rcri_3, rcri_4, rcri_5, rcri_6])
        risk_mapping = {0: "0.4% (Low Risk)", 1: "1.0% (Moderate Risk)", 2: "2.4% (High Risk)", 3: "5.4+% (Critical Risk)"}
        estimated_risk = risk_mapping.get(rcri_score, "5.4+% (Critical Risk)")
        st.metric("Estimated Perioperative MACE Risk:", estimated_risk)
        
    with col_r2:
        st.markdown("<h4 style='color:#0F766E; margin-top:0px;'>2. ARISCAT Pulmonary Risk Score</h4>", unsafe_allow_html=True)
        p_resp = st.checkbox("Active respiratory infection within past 4 weeks?")
        p_score = 10
        if patient_age > 60: p_score += 3
        if spo2 <= 95: p_score += 8
        if is_emergency: p_score += 8
        
        if p_score >= 45: ppc_class = "High Pulmonary Risk"
        elif 26 <= p_score <= 44: ppc_class = "Moderate Pulmonary Risk"
        else: ppc_class = "Low Pulmonary Risk"
        st.metric("Pulmonary Complication Risk Class:", ppc_class)

# ==============================================================================
# TAB 5: GLOBAL CLEARANCE SUMMARY DASHBOARD (AUTOMATED INTELLIGENCE)
# ==============================================================================
with tabs[4]:
    st.markdown("<div class='section-header'>📋 Comprehensive Perioperative Consultation Summary</div>", unsafe_allow_html=True)
    st.subheader("Patient Final Clearance Status Report")
    st.caption("Al-Ahli Hospital Internal Medicine Department")
    
    st.info(f"👤 **Patient:** {patient_name}  |  🎂 **Age:** {patient_age} yrs  |  🚀 **Procedure:** {op_type}")
    
    # Core Clinical Automation Aggregator
    clinical_issues = []
    mandatory_actions = []

    # --- AUTOMATED LAB VALIDATION TRIGGERS ---
    if hb < 10.0:
        clinical_issues.append(f"Anemia detected (Hb: {hb} g/dL).")
        mandatory_actions.append("🧪 Crossmatch 2 units PRBCs prior to theater if surgery is high-risk.")
    if plt < 100:
        clinical_issues.append(f"Thrombocytopenia present (Platelets: {plt} x10^3/µL).")
        mandatory_actions.append("🧪 Avoid neuraxial anesthesia/spinal block if platelets are under 80-100.")
    if potassium > 5.2 or potassium < 3.5:
        clinical_issues.append(f"Serum Potassium level out of range ({potassium} mEq/L).")
        mandatory_actions.append("🧪 Correct serum Potassium immediately to safe zone (3.5 - 5.0 mEq/L) to prevent arrhythmias.")

    # --- AUTOMATED THYROID TRIGGERS ---
    if tsh_level > 4.5:
        if ft4_level < 0.8:
            clinical_issues.append(f"Severe Overt Hypothyroidism (TSH: {tsh_level} µIU/mL, Low FT4: {ft4_level}).")
            mandatory_actions.append("❌ <b>HOLD ELECTIVE SURGERY:</b> Delay surgery until patient is clinically optimized on Levothyroxine to avoid refractory hypotension.")
        else:
            clinical_issues.append(f"Subclinical Hypothyroidism (TSH: {tsh_level} µIU/mL, Normal FT4).")
            mandatory_actions.append("🟢 Thyroid is stable enough for surgery. Administer routine home Levothyroxine on the morning of surgery.")
    elif tsh_level < 0.45 and (ft4_level > 1.8 or ft3_level > 4.2):
        clinical_issues.append(f"Overt Hyperthyroidism (TSH: {tsh_level} µIU/mL, High FT4/FT3).")
        mandatory_actions.append("❌ <b>HOLD ELECTIVE SURGERY:</b> Postpone immediately to prevent intraoperative <b>Thyroid Storm</b>. Achieve biochemical control first.")

    # --- AUTOMATED EPILEPSY TRIGGERS ---
    if last_seizure in ["Seizure within the last 6 months", "Seizure within the last 30 days"]:
        clinical_issues.append(f"Unstable Seizure Control (Last seizure window: {last_seizure}).")
        mandatory_actions.append("🧠 Order emergency serum AED drug levels. Ensure IV Benzodiazepines (Rescue therapy) are physically present in the OR.")
    elif last_seizure == "Seizure-free for > 6 months":
        clinical_issues.append("History of Controlled Epilepsy.")
        mandatory_actions.append("🧠 Maintain seizure threshold: Ensure morning oral AED dose is given. Utilize 1:1 IV bridging post-operatively if NPO status is prolonged.")

    # Render Conflict Results Summary
    if clinical_issues:
        st.markdown("<div class='danger-box'><strong>⚠️ Active Clinical Findings & Laboratory Concerns:</strong></div>", unsafe_allow_html=True)
        for issue in clinical_issues:
            st.markdown(f"• {issue}", unsafe_allow_html=True)
            
        st.markdown("<div class='workup-box'><strong>📋 Mandatory Action Plan & Optimization Steps:</strong></div>", unsafe_allow_html=True)
        for action in mandatory_actions:
            st.markdown(f"• {action}", unsafe_allow_html=True)
    else:
        st.markdown("<div class='status-box' style='border-left: 5px solid #16A34A; background-color: #F0FDFA;'>🟢 <b>No critical physiological abnormalities or endocrine conflicts detected.</b> Patient is optimized.</div>", unsafe_allow_html=True)

    # Final Decision Verdict Summary
    st.markdown("#### Final Clearance Status Decision Verdict")
    if any("❌" in act or "HOLD" in act for act in mandatory_actions):
        st.error("❌ CLEARANCE STATUS: CONDITIONAL HOLD / NOT CLEARED - Elective surgery must be deferred until parameters are fully corrected.")
    else:
        st.success("🟢 CLEARANCE STATUS: CLEARED WITH STANDARD SYSTEMIC PRECAUTIONS - Internally stable. Proceed with anesthesia care plan.")

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 11px;'>Al-Ahli Hospital Internal Medicine CDSS Platforms © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
