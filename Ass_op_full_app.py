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
    .main-title { font-size:28px !important; font-weight: bold; color: #0F766E; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:14px !important; color: #4B5563; text-align: center; margin-bottom: 20px; font-style: italic; }
    .branding-bar { background-color: #F0FDFA; padding: 15px; border-radius: 10px; border-left: 6px solid #0F766E; margin-bottom: 20px; }
    .section-header { font-size:18px !important; font-weight: bold; color: #0F766E; margin-top: 15px; margin-bottom: 15px; border-bottom: 2px solid #E5E7EB; padding-bottom: 5px; }
    .status-box { padding: 12px; border-radius: 6px; margin-bottom: 12px; border: 1px solid #E5E7EB; background-color: #F9FAFB; color: #1F2937; }
    .danger-box { padding: 12px; border-radius: 6px; margin-bottom: 12px; border: 1px solid #DC2626; background-color: #FEF2F2; color: #991B1B; }
    .info-box { padding: 12px; border-radius: 6px; margin-bottom: 12px; border: 1px solid #2563EB; background-color: #EFF6FF; color: #1E40AF; }
    .workup-box { padding: 12px; border-radius: 6px; margin-bottom: 12px; border: 1px solid #D97706; background-color: #FFFBEB; color: #92400E; }
    </style>
""", unsafe_allow_html=True)

# 3. Header & Department Branding
st.markdown("<div class='main-title'>🏥 Al-Ahli Hospital Comprehensive Perioperative Medical Fitness Engine</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Advanced Decision-Support Matrix for Surgical Clearance & Multi-System Comorbidity Optimization</div>", unsafe_allow_html=True)

st.markdown("""
<div class='branding-bar'>
    <div style='color: #1F2937; font-size: 14px; line-height: 1.5;'>
        <strong>Project Director:</strong> Dr. Ihab Abbass Abu Hilail &nbsp;|&nbsp; 
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital<br>
        <strong>Clinical Guidelines:</strong> ACC/AHA Perioperative Cardiac Updates, ARISCAT Matrix, ASA Classification, HRS/ASA Device Consensus
    </div>
</div>
""", unsafe_allow_html=True)

# 4. Create App Tabs
tabs = st.tabs([
    "👤 Patient Profile & Vitals",
    "🩺 Clinical Exam & Investigations",
    "📊 Risk Stratification Models",
    "🧬 Comorbidity Optimization Matrix",
    "💊 Perioperative Medication Stewardship",
    "📋 Global Risk Summary"
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

    # Immediate Alert System
    st.markdown("<div class='section-header'>Immediate Clinical Triggers</div>", unsafe_allow_html=True)
    vitals_alerts = []
    if spo2 < 92:
        vitals_alerts.append(f"🔴 CRITICAL HYPOXEMIA DETECTED: Preoperative SpO2 is dangerously low ({spo2}%). Secure airway and oxygenate immediately.")
    if sbp >= 180 or dbp >= 110:
        vitals_alerts.append(f"🔴 CRITICAL HYPERTENSION DETECTED: Blood pressure is severely elevated ({sbp}/{dbp} mmHg). Delay elective surgeries.")
    if sbp < 90:
        vitals_alerts.append(f"🔴 CRITICAL HYPOTENSION DETECTED: Systolic blood pressure is dangerously low ({sbp} mmHg). Risk of hypoperfusion.")
    if temp >= 38.0:
        vitals_alerts.append(f"🔴 PREOPERATIVE PYREXIA / FEVER: Patient temperature is {temp}°C. Active infection must be ruled out.")
    if hr >= 120 or hr < 40:
        vitals_alerts.append(f"🔴 CRITICAL ARRHYTHMIA WARNING: Heart rate is abnormal ({hr} bpm). Obtain emergency 12-lead ECG.")
        
    if vitals_alerts:
        for alert in vitals_alerts:
            st.markdown(f"<div class='danger-box'>{alert}</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='status-box' style='border-left: 5px solid #16A34A;'>🟢 Vital Signs Baseline: Hemodynamic and oxygenation variables are stable.</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 2: CLINICAL EXAMINATION & INVESTIGATIONS
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
        echo_done = st.radio("Echocardiogram (ECHO) Status:", ["Available", "Not Done / Not Clinically Indicated"])
        
        ef_val = 55
        echo_valvular = "None / Mild Regular Regurgitation"
        if echo_done == "Available":
            ef_val = st.number_input("Left Ventricular Ejection Fraction (LVEF %):", min_value=10, max_value=85, value=55)
            echo_valvular = st.selectbox("Valvular Pathologies:", ["None / Mild Regular Regurgitation", "Severe Aortic Stenosis", "Severe Mitral Regurgitation", "Other Moderate-to-Severe Valvular Disease"])
            
        cxr_findings = st.selectbox("Chest X-Ray (CXR) Findings:", ["Clear Lung Fields", "Cardiomegaly", "Pulmonary Congestion / Cephalization", "Consolidation / Focal Infiltrate", "Hyperinflation"])

    # Chronic Kidney Disease Dashboard
    st.markdown("<div class='section-header'>🧬 Chronic Kidney Disease (CKD) Specialty Dashboard</div>", unsafe_allow_html=True)
    is_ckd = st.checkbox("Does this patient have known Chronic Kidney Disease (CKD)?")
    col_ckd1, col_ckd2, col_ckd3 = st.columns(3)
    ckd_stage = "N/A"
    baseline_creat = 0.9
    on_hd = "No"
    
    if is_ckd:
        with col_ckd1:
            baseline_creat = st.number_input("Patient's Baseline Serum Creatinine (mg/dL):", value=1.5, step=0.1)
        with col_ckd2:
            on_hd = st.radio("Is the patient undergoing chronic Hemodialysis?", ["No", "Yes"])
        with col_ckd3:
            ckd_stage = st.selectbox("CKD Stage Baseline:", ["Stage 3a (eGFR 45-59)", "Stage 3b (eGFR 30-44)", "Stage 4 (eGFR 15-29)", "Stage 5 (eGFR < 15)"])

    # Specialty Lab tracking for Thyroid and Epilepsy
    st.markdown("<div class='section-header'>🔬 Specialty Disease Panel Laboratory Input</div>", unsafe_allow_html=True)
    col_th1, col_th2, col_th3 = st.columns(3)
    with col_th1:
        tsh_level = st.number_input("Thyroid Stimulating Hormone (TSH) Level (µIU/mL):", value=2.0, step=0.01, help="Normal reference range: 0.45 - 4.5 µIU/mL")
    with col_th2:
        ft4_level = st.number_input("Free T4 (FT4) Level (ng/dL):", value=1.2, step=0.01, help="Normal reference range: 0.8 - 1.8 ng/dL")
    with col_th3:
        ft3_level = st.number_input("Free T3 (FT3) Level (pg/mL):", value=3.0, step=0.01, help="Normal reference range: 2.3 - 4.2 pg/mL")

    st.markdown("---")
    last_seizure = st.selectbox("Time Window of Last Documented Epileptic Seizure:", ["No seizures for > 6 months", "Seizure within the last 6 months", "Seizure within the last 30 days"])

    # Preoperative Laboratory Dashboard
    st.markdown("<h4 style='color:#0F766E; margin-top:20px;'>Preoperative Laboratory Dashboard (Complete Panel)</h4>", unsafe_allow_html=True)
    col_lab1, col_lab2, col_lab3 = st.columns(3)
    with col_lab1:
        hb = st.number_input("Current Hemoglobin (g/dL):", value=13.5, step=0.1)
        wbc = st.number_input("White Blood Cells (x10^3/µL):", value=7.5, step=0.1)
    with col_lab2:
        scr = st.number_input("Current Serum Creatinine (mg/dL):", value=0.9, step=0.1)
        potassium = st.number_input("Serum Potassium (mEq/L):", value=4.2, step=0.1)
    with col_lab3:
        plt = st.number_input("Platelet Count (x10^3/µL):", value=250)
        inr_val = st.number_input("INR Level:", value=1.0, step=0.1)

# ==============================================================================
# TAB 3: RISK STRATIFICATION MODELS
# ==============================================================================
with tabs[2]:
    st.markdown("<div class='section-header'>Objective Risk Scoring Frameworks</div>", unsafe_allow_html=True)
    col_r1, col_r2 = st.columns(2)
    
    with col_r1:
        st.markdown("<h4 style='color:#0F766E; margin-top:0px;'>1. Revised Cardiac Risk Index (RCRI)</h4>", unsafe_allow_html=True)
        rcri_1 = st.checkbox("High-risk surgery criteria met", value=("High Risk" in op_type))
        rcri_2 = st.checkbox("History of Ischemic Heart Disease", value=(ecg_findings == "Pathological Q Waves / Ischemic ST-T Changes"))
        rcri_3 = st.checkbox("History of Congestive Heart Failure", value=(ef_val < 40 or cxr_findings == "Pulmonary Congestion / Cephalization"))
        rcri_4 = st.checkbox("History of Cerebrovascular Disease")
        rcri_5 = st.checkbox("Preoperative Insulin Therapy")
        rcri_6 = st.checkbox("Preoperative Serum Creatinine > 2.0 mg/dL", value=(scr > 2.0))
        
        st.markdown("<h5 style='color:#0F766E; margin-top:15px;'>Functional Capacity Evaluation</h5>", unsafe_allow_html=True)
        mets_capacity = st.radio("Can the patient complete activities ≥ 4 METs?", ["Yes (≥ 4 METs)", "No (< 4 METs)"])

        rcri_score = sum([rcri_1, rcri_2, rcri_3, rcri_4, rcri_5, rcri_6])
        risk_mapping = {0: "0.4% (Low Risk)", 1: "1.0% (Moderate Risk)", 2: "2.4% (High Risk)", 3: "5.4+% (Critical Risk)"}
        estimated_risk = risk_mapping.get(rcri_score, "5.4+% (Critical Risk)")
        
    with col_r2:
        st.markdown("<h4 style='color:#0F766E; margin-top:0px;'>2. ARISCAT Pulmonary Risk Framework</h4>", unsafe_allow_html=True)
        p_resp = st.checkbox("Active respiratory infection within the past 4 weeks?")
        p_anemia = st.checkbox("Preoperative anemia status?", value=(hb <= 10.0))
        
        p_spo2_str = "≥ 96%"
        if 91 <= spo2 <= 95: p_spo2_str = "91 - 95%"
        elif spo2 <= 90: p_spo2_str = "≤ 90%"
            
        p_site_str = "Peripheral"
        if "Intermediate Risk" in op_type: p_site_str = "Upper Abdominal"
        elif "High Risk" in op_type: p_site_str = "Intrathoracic"

        p_score = 0
        if 51 <= patient_age <= 80: p_score += 3
        elif patient_age > 80: p_score += 11
        p_score += {"≥ 96%": 0, "91 - 95%": 8, "≤ 90%": 24}.get(p_spo2_str, 0)
        p_score += 17 if p_resp else 0
        p_score += 11 if p_anemia else 0
        p_score += {"Peripheral": 0, "Upper Abdominal": 15, "Intrathoracic": 24}.get(p_site_str, 0)
        p_score += 16 if op_duration > 3.0 else 0
        p_score += 8 if is_emergency else 0
        
        if p_score >= 45: ppc_class = "High Pulmonary Risk (≥40% PPC)"
        elif 26 <= p_score <= 44: ppc_class = "Moderate Pulmonary Risk"
        else: ppc_class = "Low Pulmonary Risk"

        st.markdown("<h4 style='color:#0F766E; margin-top:20px;'>3. ASA Physical Status Designation</h4>", unsafe_allow_html=True)
        asa_class = st.selectbox("Assign Global ASA Class:", [
            "ASA Class I: A normal healthy patient",
            "ASA Class II: A patient with mild systemic disease",
            "ASA Class III: A patient with severe systemic disease",
            "ASA Class IV: A patient with severe systemic disease that is a constant threat to life"
        ])

# ==============================================================================
# TAB 4: COMORBIDITY OPTIMIZATION MATRIX
# ==============================================================================
with tabs[3]:
    st.markdown("<div class='section-header'>Chronic Disease Management Protocols & Target End-Points</div>", unsafe_allow_html=True)
    selected_comorb = st.multiselect("Select Active Comorbidities to Review Optimization Steps:", [
        "Diabetes Mellitus", "Hypertension", "Chronic Kidney Disease / ESRD",
        "COPD / Chronic Bronchial Asthma", "Ischemic Heart Disease / Chronic Heart Failure",
        "Chronic Systemic Glucocorticoid / Steroid Use",
        "Thyroid Disorder (Hypo/Hyperthyroidism)", "Epilepsy / Seizure Disorder",
        "Cardiac Pacemaker", "Implantable Cardioverter-Defibrillator (ICD)"
    ])
    
    if "Diabetes Mellitus" in selected_comorb:
        st.markdown("<div class='info-box'><strong>Sugar Control Protocol:</strong> Target: 100 - 180 mg/dL perioperatively. Defer elective surgeries if HbA1c > 8-9% to prevent wound infection and poor healing.</div>", unsafe_allow_html=True)
    if "Hypertension" in selected_comorb:
        st.markdown("<div class='info-box'><strong>Blood Pressure Strategy:</strong> Postpone strictly if SBP ≥ 180 or DBP ≥ 110 mmHg. Prevent intensive intraoperative hypotension during anesthesia induction.</div>", unsafe_allow_html=True)
    if "Chronic Kidney Disease / ESRD" in selected_comorb or is_ckd:
        st.markdown("<div class='info-box'><strong>Renal Function Stewardship:</strong> Hemodialysis should be scheduled 12-24 hours prior to surgery. Check Potassium immediately pre-op (Must be < 5.5 mEq/L). Strictly avoid post-operative NSAIDs.</div>", unsafe_allow_html=True)
    if "COPD / Chronic Bronchial Asthma" in selected_comorb:
        st.markdown("<div class='info-box'><strong>Pulmonary Optimization Protocol:</strong> Ensure patient is free of active wheezing. Consider short pre-op course of oral Prednisone 40mg for 3-5 days if baseline mechanics are poor.</div>", unsafe_allow_html=True)
    if "Ischemic Heart Disease / Chronic Heart Failure" in selected_comorb:
        st.markdown("<div class='info-box'><strong>Myocardial & Volume Optimization:</strong> Elective surgeries are contraindicated within 6 months of acute ACS/MI. Patient must be strictly euvolemic without pulmonary rales.</div>", unsafe_allow_html=True)
    if "Chronic Systemic Glucocorticoid / Steroid Use" in selected_comorb:
        st.markdown("<div class='danger-box' style='background-color: #FFFBEB; border-color: #D97706; color: #92400E;'><strong>🛡️ Perioperative Glucocorticoid Stress Dosing Protocol (Adrenal Protection):</strong><br>• Minor Surgical Stress: Take regular home morning steroid dose orally.<br>• Moderate Surgical Stress: Administer 50 mg Hydrocortisone IV before induction, followed by 25 mg IV q8h for 24h.<br>• Major Surgical Stress: Administer 100 mg Hydrocortisone IV before induction, followed by 50 mg IV q8h for 24-48h.</div>", unsafe_allow_html=True)
    
    # Advanced Thyroid Management Matrix (Hypo vs Hyper Evaluation)
    if "Thyroid Disorder (Hypo/Hyperthyroidism)" in selected_comorb:
        st.markdown("<h4 style='color:#06B6D4;'>🦋 Specialty Thyroid Optimization Approach</h4>", unsafe_allow_html=True)
        thyroid_variant = st.radio("Specify Active Clinical Classification State:", ["Hypothyroidism (Underactive)", "Hyperthyroidism (Overactive)"])
        
        if thyroid_variant == "Hypothyroidism (Underactive)":
            st.markdown(f"""
            <div class='info-box' style='border-left: 5px solid #06B6D4;'>
                <strong>📉 Hypothyroidism Surgical Risk Mapping:</strong><br>
                • <b>Current Panel Summary:</b> TSH: {tsh_level} µIU/mL | FT4: {ft4_level} ng/dL.<br>
                • <b>Mild/Moderate Hypothyroidism:</b> (TSH elevated but FT4 stable/normal) Patient can safely proceed to surgery. No elevated risk of cardiovascular complications.<br>
                • <b>Severe Hypothyroidism / Myxedema:</b> (TSH severely elevated, clinical macroglossia, hypothermia, bradycardia, or low FT4). Elective surgeries <b>MUST</b> be cancelled. High clinical risk of intraoperative cardiovascular collapse, refractory hypotension, and delayed anesthetic emergence.
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class='danger-box' style='background-color: #ECFEFF; border-color: #06B6D4; color: #083344; border-left: 5px solid #083344;'>
                <strong>📈 Hyperthyroidism & Thyroid Storm High-Risk Warning:</strong><br>
                • <b>Current Panel Summary:</b> TSH: {tsh_level} µIU/mL | FT4: {ft4_level} ng/dL | FT3: {ft3_level} pg/mL.<br>
                • <b>Surgical Status:</b> Overt, uncontrolled hyperthyroidism is an <b>absolute contraindication</b> for elective surgeries due to the high risk of triggering a lethal, intraoperative <b>Thyroid Storm</b> (severe hyperthermia, tachyarrhythmias, heart failure).<br>
                • <b>Target End-Point:</b> Postpone elective procedures until patient achieves a definitive biochemically verified euthyroid window. 
            </div>
            """, unsafe_allow_html=True)

    # Epilepsy Matrix
    if "Epilepsy / Seizure Disorder" in selected_comorb:
        st.markdown(f"""
        <div class='info-box' style='border-left: 5px solid #6366F1;'>
            <strong>🧠 Epilepsy / Seizure Management Protocol:</strong><br>
            • <b>Current Window Control:</b> Status is documented as: <i>{last_seizure}</i>.<br>
            • <b>Seizure Prevention:</b> Breakthrough events under anesthesia are triggered by sleep loss, intense hyperventilation, or omission of home medications.<br>
            • <b>Management Strategy:</b> Maintain therapeutic neural thresholds. If NPO condition is prolonged post-surgery, immediately bridge with equivalent <b>intravenous (IV) formulations</b>.
        </div>
        """, unsafe_allow_html=True)

    # Pacemaker & ICD Matrix
    if "Cardiac Pacemaker" in selected_comorb:
        st.markdown("<div class='status-box'><b>📟 Cardiac Pacemaker Strategy:</b> Ensure interrogation was performed within 12 months. Prepare sterile magnet in OR if monopolar cautery is intended above the umbilicus.</div>", unsafe_allow_html=True)
    if "Implantable Cardioverter-Defibrillator (ICD)" in selected_comorb:
        st.markdown("<div class='danger-box' style='background-color: #FFF7ED; border-color: #EA580C; color: #7C2D12;'><b>⚡ ICD Anti-Shock Deactivation Protocol:</b> Inactivate tachyarrhythmia therapies immediately before incision. Place external transcutaneous patches. Continuous mechanical pulse monitoring is mandatory.</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 5: PERIOPERATIVE MEDICATION STEWARDSHIP
# ==============================================================================
with tabs[4]:
    st.markdown("<div class='section-header'>Critical Perioperative Medication Stewardship Matrix</div>", unsafe_allow_html=True)
    
    # Detailed Epilepsy Meds Checklist Entry
    if "Epilepsy / Seizure Disorder" in selected_comorb:
        st.markdown("<h4 style='color:#6366F1;'>💊 Epilepsy Patient Medication Selector & Clinical Stewardship Rulebook</h4>", unsafe_allow_html=True)
        selected_aeds = st.multiselect("Identify the specific Antiepileptic Drugs (AEDs) the patient is actively taking:", [
            "Levetiracetam (Keppra)", "Sodium Valproate (Depakine)", "Carbamazepine (Tegretol)", "Lamotrigine (Lamictal)", "Phenytoin (Epanutin)"
        ])
        
        for aed in selected_aeds:
            if "Levetiracetam" in aed:
                st.info("🧠 <b>Levetiracetam (Keppra) Protocol:</b> GIVE regular home dose on the morning of surgery with a sip of water. If patient remains NPO post-operatively, convert to <b>IV Keppra</b> at a 1:1 total daily dose ratio (e.g., 500mg PO BID becomes 500mg IV BID infused over 15 mins).")
            if "Sodium Valproate" in aed:
                st.info("🧠 <b>Sodium Valproate (Depakine) Protocol:</b> GIVE regular home dose on the morning of surgery. If NPO post-op, convert to <b>IV Depakine</b> 1:1 ratio. Note: Valproate can rarely cause transient thrombocytopenia or platelet dysfunction; check pre-op platelet count meticulously.")
            if "Carbamazepine" in aed:
                st.warning("🧠 <b>Carbamazepine (Tegretol) Protocol:</b> GIVE regular morning dose. Note: There is NO direct IV formulation available for Carbamazepine. If prolonged NPO status is expected, consult neurology immediately to bridge with <b>IV Levetiracetam or Phenytoin</b> to maintain seizure coverage.")
            if "Lamotrigine" in aed:
                st.info("🧠 <b>Lamotrigine (Lamictal) Protocol:</b> GIVE morning dose. No direct IV formulation is available. However, because Lamotrigine has an extremely long half-life (~25-30 hours), missing doses for 24 hours is rarely catastrophic, but oral therapy must be resumed as soon as bowel sounds return.")
            if "Phenytoin" in aed:
                st.markdown("<div class='danger-box' style='background-color:#FEF2F2; border-color:#DC2626; color:#991B1B;'>🧠 <b>Phenytoin (Epanutin) Protocol:</b> GIVE regular morning dose. If NPO, convert to <b>IV Phenytoin</b> 1:1 ratio. <i>Critical Safety:</i> IV Phenytoin must be infused slowly (<50 mg/min) and only in normal saline to avoid precipitation and cardiotoxicity/arrhythmias.</div>", unsafe_allow_html=True)

    # Detailed Thyroid Meds Checklist Entry
    if "Thyroid Disorder (Hypo/Hyperthyroidism)" in selected_comorb:
        st.markdown("<h4 style='color:#06B6D4;'>💊 Thyroid Disease Home Medication Stewardship System</h4>", unsafe_allow_html=True)
        selected_thyroid_meds = st.multiselect("Identify active home medications prescribed to this patient:", [
            "Levothyroxine (Euthyrox / Synthroid)", "Carbimazole", "Propylthiouracil (PTU)"
        ])
        
        for t_med in selected_thyroid_meds:
            if "Levothyroxine" in t_med:
                st.info("🦋 <b>Levothyroxine Protocol:</b> <b>CONTINUE ABSOLUTELY</b> on the morning of surgery with a tiny sip of water. Levothyroxine has a massive biological half-life (~7 days). Skipping it on the day of surgery causes no acute crisis, but giving it ensures optimal cardiac contractility and avoids intraoperative bradycardia triggers.")
            if "Carbimazole" in t_med or "Propylthiouracil" in t_med:
                st.markdown(f"<div class='workup-box'>🦋 <b>{t_med} Stewardship Action:</b> <b>GIVE</b> regular dose on the morning of surgery. Maintaining systemic anti-thyroid levels is mandatory to prevent intraoperative thyroid hormone escape or surge during intense physical surgical stress.</div>", unsafe_allow_html=True)

    med_cat = st.radio("Select General Pharmacological Classification for Review:", ["Oral Antiplatelets & Anticoagulants", "Diabetes Mellitus Therapies", "Antihypertensives"])
    if "Antiplatelets" in med_cat:
        st.markdown("<div class='status-box'>• <b>Aspirin:</b> Continue for stented patients unless high closed-cavity risk.<br>• <b>Clopidogrel:</b> Hold for 5 full days prior to elective surgery.</div>", unsafe_allow_html=True)
    elif "Diabetes" in med_cat:
        st.markdown("<div class='status-box'>• <b>Metformin:</b> Hold 24 hours prior.<br>• <b>SGLT2 Inhibitors:</b> Hold 3-4 days prior due to severe perioperative Euglycemic DKA risk.</div>", unsafe_allow_html=True)
    elif "Antihypertensives" in med_cat:
        st.markdown("<div class='status-box'>• <b>ACEIs/ARBs:</b> Hold on the morning of surgery.<br>• <b>Beta-Blockers:</b> Continue strictly to avoid rebound tachycardia.</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 6: GLOBAL RISK SUMMARY DASHBOARD (Pure Automated Validation Core)
# ==============================================================================
with tabs[5]:
    st.markdown("<div class='section-header'>📋 Comprehensive Perioperative Consultation Summary</div>", unsafe_allow_html=True)
    
    st.subheader("Patient Clearance Summary Report")
    st.caption("Al-Ahli Hospital Internal Medicine Department")
    
    st.info(f"👤 **Patient:** {patient_name}  |  🎂 **Age:** {patient_age} yrs  |  🚀 **Procedure:** {op_type}  |  🫁 **Oxygen Baseline:** {spo2}% SpO2 on RA")
    
    st.markdown("### Risk Assessment Parameters")
    m_col1, m_col2, m_col3 = st.columns(3)
    with m_col1:
        st.metric(label="RCRI Score", value=f"{rcri_score} Points", delta=estimated_risk, delta_color="inverse")
        st.write(f"**Functional Capacity:** {mets_capacity}")
    with m_col2:
        st.metric(label="ARISCAT Score", value=f"{p_score} Points", delta=ppc_class, delta_color="inverse")
    with m_col3:
        st.metric(label="Global ASA Class", value=f"Class {asa_class.split(':')[0][-3:]}")
        st.write(f"**Hemoglobin:** {hb} g/dL | **K+:** {potassium} mEq/L")

    # Documented Renal Baseline Block
    if is_ckd:
        st.markdown("### 🧬 Documented Renal Baseline")
        if scr >= (baseline_creat + 0.3) or scr >= (baseline_creat * 1.5):
            st.markdown("<div class='danger-box'>⚠️ <b>ACUTE KIDNEY INJURY (AKI) ALERT:</b> Current creatinine has jumped significantly from baseline! Postpone elective cases immediately.</div>", unsafe_allow_html=True)

    # --- ADVANCED DYNAMIC AUTOMATION APPROACH & LAB VALIDATION MATRIX ---
    st.markdown("<div class='section-header'>⚠️ Active Clinical Issues & Mandatory Workups Matrix</div>", unsafe_allow_html=True)
    
    clinical_issues = []
    recommended_workups = []
    
    # Lab Panel Triggers
    if hb < 11.0:
        clinical_issues.append(f"<b>Preoperative Anemia (Hb: {hb} g/dL):</b> Low tissue oxygen carriage capability.")
        recommended_workups.append("🧪 <b>Anemia Optimization:</b> If Hb < 7-8 g/dL or symptomatic, crossmatch and transfuse Packed Red Blood Cells (PRBCs) pre-op.")
    if wbc > 11.0 or wbc < 4.0:
        clinical_issues.append(f"<b>Abnormal White Blood Cell Count (WBC: {wbc} x10^3/µL):</b> Systemic index abnormality.")
        recommended_workups.append("🧪 <b>Infectious Screen:</b> Rule out acute infection or bacterial triggers.")
    if plt < 150:
        clinical_issues.append(f"<b>Thrombocytopenia (Platelets: {plt} x10^3/µL):</b> Increased microvascular surgical hemorrhage risk.")
        if plt < 50:
            recommended_workups.append("🧪 <b>CRITICAL Platelet Rescue Plan:</b> Secure 1-2 therapeutic apheresis platelet pools for immediate intraoperative administration.")
        else:
            recommended_workups.append("🧪 <b>Platelet Advisory:</b> Safe for open surgery, avoid neuraxial/spinal anesthetic approaches if platelets < 80-100.")
    if inr_val > 1.2:
        clinical_issues.append(f"<b>Coagulopathy Alert (INR: {inr_val}):</b> Impaired primary/secondary hemostasis.")
        recommended_workups.append("🧪 <b>Coagulation Reversal Strategy:</b> Administer oral/IV Vitamin K or order Prothrombin Complex Concentrate (PCC) if urgent reversal is indicated.")
    if potassium > 5.2 or potassium < 3.5:
        clinical_issues.append(f"<b>Electrolyte Imbalance (Potassium: {potassium} mEq/L):</b> Critical arrhythmia threat.")
        recommended_workups.append("🧪 <b>Potassium Correction:</b> Complete cardiac shift protocols or IV replacement before theater transfer.")

    # Vitals Triggers
    if sbp >= 180 or dbp >= 110:
        clinical_issues.append(f"<b>Severe Uncontrolled Hypertension ({sbp}/{dbp} mmHg):</b> Severe hemodynamic instability risk.")
        recommended_workups.append("🧪 <b>Hypertension Emergency Strategy:</b> Postpone surgery, initiate IV Labetalol/GTN titration.")
    if spo2 < 92:
        clinical_issues.append(f"<b>Critical Hypoxemia ({spo2}%):</b> Intolerable tissue oxygen desaturation barrier.")
        recommended_workups.append("🧪 <b>Hypoxemia Emergency Workup:</b> Immediate ABG, CXR, and high flow O2 mapping.")

    # --- COMPLETE ADVANCED THYROID AUTOMATION ARCHITECTURE ---
    if "Thyroid Disorder (Hypo/Hyperthyroidism)" in selected_comorb:
        clinical_issues.append(f"<b>Co-existing Thyroid Disease Profile:</b> Current Values -> TSH: {tsh_level} | FT4: {ft4_level} | FT3: {ft3_level}")
        
        # 1. Biochemical Hyperthyroidism Rule (TSH < 0.45 accompanied by elevated FT4 or FT3)
        if tsh_level < 0.45 and (ft4_level > 1.8 or ft3_level > 4.2):
            recommended_workups.append(f"❌ <b>CRITICAL HYPERTHYROIDISM ALERT:</b> Overt, uncontrolled overactive state documented! Elective surgery <b>MUST BE DEFERRED</b>. High imminent threat of <b>Thyroid Storm</b> under surgical stress. <b>Action Required:</b> Consult Endocrinology to optimize anti-thyroid drugs (Carbimazole) and initiate strict Beta-blockade (Propranolol) to safely reduce heart rate below 80 bpm before clearing.")
        
        # 2. Biochemical Severe Hypothyroidism Rule (TSH > 10.0 accompanied by low FT4 < 0.8)
        elif tsh_level > 4.5 and ft4_level < 0.8:
            recommended_workups.append(f"❌ <b>CRITICAL HYPOTHYROIDISM ALERT:</b> Severe underactive/Myxedema state identified! Elective surgery <b>MUST BE DEFERRED</b>. Patient is highly vulnerable to cardiac depression, severe intraoperative bradycardia, hypothermia, and drug clearance arrest. <b>Action Required:</b> Initiate structured oral or IV Levothyroxine replacement and delay surgery until clinical mechanics normalize.")
        
        # 3. Subclinical / Well Controlled Stable States (Triggers when values are acceptable or subclinical)
        else:
            recommended_workups.append("🟢 <b>Thyroid Status Optimized:</b> Patient is biochemically stable or subclinical. <b>Proceed with planned surgery</b>. Ensure the patient receives their morning dose of Levothyroxine or anti-thyroid medication with a tiny sip of water.")

    # Epilepsy Automation Approach Validation
    if "Epilepsy / Seizure Disorder" in selected_comorb:
        clinical_issues.append(f"<b>Co-existing Epilepsy / Seizure Disorder (Last Event: {last_seizure}):</b> Susceptible to intraoperative breakthrough events.")
        if last_seizure in ["Seizure within the last 6 months", "Seizure within the last 30 days"]:
            recommended_workups.append(f"🧠 <b>Mandatory Epilepsy Workup Triggered:</b> Seizure history is unstable! <b>Order serum antiepileptic drug levels</b> immediately. Ensure <b>IV Benzodiazepines</b> are drawn in the OR suite.")
        else:
            recommended_workups.append("🧠 <b>Epilepsy Action Plan:</b> Stable control window. Administer full morning AED oral dose on the day of surgery. Bridge with IV routes post-operatively if NPO state extends.")

    # Devices & Steroids Validation
    if "Cardiac Pacemaker" in selected_comorb:
        recommended_workups.append("📟 <b>Pacemaker Protocol:</b> Verify interrogation window < 12 months. Prepare sterile magnet or program to asynchronous mode if high EMI above the umbilicus is anticipated.")
    if "Implantable Cardioverter-Defibrillator (ICD)" in selected_comorb:
        recommended_workups.append("⚡ <b>ICD Crucial Security Plan:</b> Deactivate automatic shock therapies immediately prior to incision. Secure external transcutaneous defibrillator pads on skin and position a magnet inside the OR.")
    if "Chronic Systemic Glucocorticoid / Steroid Use" in selected_comorb:
        recommended_workups.append("🛡️ <b>Adrenal Protection Workup:</b> Administer IV Hydrocortisone stress dosing pre-induction based on surgical severity matrix.")

    # Render Conflict Results Summary
    if clinical_issues:
        st.markdown("<div class='danger-box'><strong>⚠️ Detected Clinical Issues & Laboratory Derangements:</strong></div>", unsafe_allow_html=True)
        for issue in clinical_issues:
            st.markdown(f"• {issue}", unsafe_allow_html=True)
            
        st.markdown("<div class='workup-box'><strong>📋 Required Preoperative Workups & Diagnostic Interventions:</strong></div>", unsafe_allow_html=True)
        for workup in recommended_workups:
            st.markdown(f"{workup}", unsafe_allow_html=True)
    else:
        st.markdown("<div class='status-box' style='border-left: 5px solid #16A34A; background-color: #F0FDFA;'>🟢 <b>No clinical abnormalities or severe physiological conflicts detected.</b> Patient is optimized based on current entry criteria.</div>", unsafe_allow_html=True)

    # Final Decision Verdict Summary
    st.markdown("#### Final Clearance Decision Status")
    # Defers if critical thyroid warnings or other severe clinical indicators are generated
    if any("❌" in w or "CRITICAL" in w for w in recommended_workups) or clinical_issues or (rcri_score >= 1 and mets_capacity == "No (< 4 METs)"):
        st.error("❌ CLEARANCE STATUS: CONDITIONAL HOLD / HIGH RISK - Elective surgery must be deferred until all listed active workups and clinical parameters are fully optimized and stabilized.")
    else:
        st.success("🟢 CLEARANCE STATUS: CLEARED FOR SURGERY WITH STANDARD PRECAUTIONS - Stable from an Internal Medicine perspective. Proceed with the planned procedure.")

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 11px;'>Al-Ahli Hospital Internal Medicine CDSS Platforms © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
