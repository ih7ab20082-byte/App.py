import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Al-Ahli Perioperative Fitness Engine",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS Styles
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
# TAB 2: CLINICAL EXAMINATION & INVESTIGATIONS (WITH CKD & NEW MODULES)
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

    # New Module Specific Inputs (Thyroid & Epilepsy Lab tracking)
    st.markdown("<div class='section-header'>🔬 New Modules Preoperative Lab Tracking</div>", unsafe_allow_html=True)
    col_th1, col_th2 = st.columns(2)
    with col_th1:
        tsh_level = st.number_input("TSH Level (µIU/mL) [Leave 2.0 if normal or untested]:", value=2.0, step=0.1)
    with col_th2:
        last_seizure = st.selectbox("Time Since Last Epileptic Seizure:", ["No seizures for > 6 months", "Seizure within the last 6 months", "Seizure within the last 30 days"])

    # Preoperative Laboratory Dashboard
    st.markdown("<h4 style='color:#0F766E; margin-top:20px;'>Preoperative Laboratory Dashboard</h4>", unsafe_allow_html=True)
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
# TAB 3: RISK STRATIFICATION MODELS (RCRI & ARISCAT & ASA)
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
# TAB 4: COMORBIDITY OPTIMIZATION MATRIX (WITH EXPLICIT THYROID, SEIZURE & CIED)
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
    
    # 1. New Thyroid Matrix
    if "Thyroid Disorder (Hypo/Hyperthyroidism)" in selected_comorb:
        st.markdown("""
        <div class='info-box' style='border-left: 5px solid #06B6D4;'>
            <strong>🦋 Thyroid Disorder Optimization Approach:</strong><br>
            • <b>Clinical Objective:</b> Achieve clinical euthyroid state. Avoid surgery in manifest, uncontrolled overt hyperthyroidism due to high risk of life-threatening intraoperative <b>Thyroid Storm</b>.<br>
            • <b>Biochemical Monitoring:</b> Check pre-op TSH / Free T4. Overt hyperthyroidism requires delay of elective cases.<br>
            • <b>Severe Hypothyroidism Risk:</b> Untreated severe Myxedema coma requires cancellation; mild/moderate hypothyroidism can proceed with standard precautions.
        </div>
        """, unsafe_allow_html=True)

    # 2. New Epilepsy Matrix
    if "Epilepsy / Seizure Disorder" in selected_comorb:
        st.markdown("""
        <div class='info-box' style='border-left: 5px solid #6366F1;'>
            <strong>🧠 Epilepsy / Seizure Management Protocol:</strong><br>
            • <b>Clinical Objective:</b> Ensure complete seizure freedom. Perioperative seizure triggers include sleep deprivation, pain, and drug omissions.<br>
            • <b>Pre-Op Workup:</b> Document baseline seizure frequency and last dose. If patient has recent breakout seizures, order therapeutic serum Antiepileptic Drug (AED) levels (e.g., Phenytoin, Valproate).<br>
            • <b>Intraoperative / Post-Op Strategy:</b> If NPO post-surgery, arrange immediate transition to equivalent intravenous (IV) anti-seizure formulations to maintain stable brain therapeutic thresholds.
        </div>
        """, unsafe_allow_html=True)

    # 3. New Pacemaker Matrix
    if "Cardiac Pacemaker" in selected_comorb:
        st.markdown("""
        <div class='danger-box' style='background-color: #F8FAFC; border-color: #475569; color: #1E293B; border-left: 5px solid #475569;'>
            <strong>📟 Cardiac Pacemaker Comprehensive Approach:</strong><br>
            • <b>Device Verification:</b> Identify device model, indication, battery longevity, and current programming. Interrogate within 12 months for pacemakers.<br>
            • <b>Electrosurgery (Monopolar Bovie) Risk:</b> Monopolar electrocautery above the umbilicus causes Electromagnetic Interference (EMI), potentially inducing pacing inhibition or device resetting.<br>
            • <b>Management Strategy:</b> If patient is pacing-dependent and high EMI is expected, program the device to an asynchronous pacing mode (e.g., VOO/DOO) or have a temporary magnet available in the operating room.
        </div>
        """, unsafe_allow_html=True)

    # 4. New ICD Matrix
    if "Implantable Cardioverter-Defibrillator (ICD)" in selected_comorb:
        st.markdown("""
        <div class='danger-box' style='background-color: #FFF7ED; border-color: #EA580C; color: #7C2D12; border-left: 5px solid #EA580C;'>
            <strong>⚡ Implantable Cardioverter-Defibrillator (ICD) High-Risk Management:</strong><br>
            • <b>Interrogation Window:</b> Strict interrogation and safety verification required within 6 months prior to scheduled surgery.<br>
            • <b>EMI Fatal Risk:</b> Surgical monopolar cautery can be misinterpreted by the ICD as ventricular fibrillation (VF), causing catastrophic, inappropriate intraoperative shocks.<br>
            • <b>Stewardship Action Plan:</b> Inactivate tachyarrhythmia detection/shock features immediately prior to surgical incision. Ensure continuous ECG and pulse monitoring are active. <b>A magnet must be physically in the OR</b>, and emergency external defibrillation pads must be placed on the patient before induction. Reactivate the device immediately post-op.
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# TAB 5: PERIOPERATIVE MEDICATION STEWARDSHIP (WITH NEW PHARMA ENTRIES)
# ==============================================================================
with tabs[4]:
    st.markdown("<div class='section-header'>Critical Perioperative Medication Stewardship Matrix</div>", unsafe_allow_html=True)
    med_cat = st.radio("Select Pharmacological Classification:", ["Oral Antiplatelets & Anticoagulants", "Diabetes Mellitus Therapies", "Antihypertensives", "Thyroid & Antiepileptic Medications"])
    
    if "Antiplatelets" in med_cat:
        st.markdown("<div class='status-box'>• <b>Aspirin:</b> Continue for stented patients unless high closed-cavity risk.<br>• <b>Clopidogrel:</b> Hold for 5 full days prior to elective surgery.<br>• <b>Warfarin:</b> Hold 5 days prior. Bridge with LMWH only if high-embolic risk criteria met.<br>• <b>DOACs:</b> Hold for 24-48 hours based on bleeding severity and computed GFR. No routine bridging.</div>", unsafe_allow_html=True)
    elif "Diabetes" in med_cat:
        st.markdown("<div class='status-box'>• <b>Metformin:</b> Hold 24 hours prior to minimize anesthesia hypoperfusion Lactic Acidosis risk.<br>• <b>SGLT2 Inhibitors:</b> Hold 3-4 days prior due to severe perioperative Euglycemic DKA risk.<br>• <b>Long-Acting Insulin:</b> Reduce dose to 75-80% on the night before or day of surgery. Do not hold completely.</div>", unsafe_allow_html=True)
    elif "Antihypertensives" in med_cat:
        st.markdown("<div class='status-box'>• <b>ACEIs/ARBs:</b> Hold on the morning of surgery to avoid refractory intraoperative hypotension.<br>• <b>Beta-Blockers:</b> Continue strictly on the morning of surgery to prevent rebound tachycardia and ischemia.<br>• <b>Diuretics:</b> Hold on the morning of surgery.</div>", unsafe_allow_html=True)
    elif "Thyroid" in med_cat:
        st.markdown("""
        <div class='status-box' style='border-left: 5px solid #0F766E;'>
            <strong>💊 Thyroid & Antiepileptic Drug (AED) Morning-Of Administration Rules:</strong><br><br>
            • <b>Levothyroxine (T4):</b> <b>CONTINUE</b> on the morning of surgery with a tiny sip of water. Long half-life ensures stability, avoiding hypothyroid myocardial bradycardia.<br>
            • <b>Antithyroid Drugs (Carbimazole / Propylthiouracil):</b> <b>CONTINUE</b> on the morning of surgery to minimize risk of intraoperative thyroid escape or storm.<br>
            • <b>Antiepileptic Drugs (AEDs - Levetiracetam, Carbamazepine, Valproate, Lamotrigine):</b> <b>CONTINUE ABSOLUTELY</b> on the morning of surgery. Skipping a dose severely drops the seizure threshold during anesthetic induction. If the patient is strictly NPO post-operatively, convert to IV route immediately.
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# TAB 6: GLOBAL RISK SUMMARY DASHBOARD (Pure Native Layout - 100% Fixed & Complete)
# ==============================================================================
with tabs[5]:
    st.markdown("<div class='section-header'>📋 Comprehensive Perioperative Consultation Summary</div>", unsafe_allow_html=True)
    
    st.subheader("Patient Clearance Summary Report")
    st.caption("Al-Ahli Hospital Internal Medicine Department")
    
    # Identification Block
    st.info(f"👤 **Patient:** {patient_name}  |  🎂 **Age:** {patient_age} yrs  |  🚀 **Procedure:** {op_type} ({op_duration} hrs duration)  |  🫁 **Oxygen Baseline:** {spo2}% SpO2 on RA")
    
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
        k_col1, k_col2, k_col3 = st.columns(3)
        with k_col1: st.write(f"**Baseline Creatinine:** {baseline_creat} mg/dL")
        with k_col2: st.write(f"**Current Creatinine:** {scr} mg/dL")
        with k_col3: st.write(f"**Hemodialysis Dependent:** {on_hd}")
        
        if scr >= (baseline_creat + 0.3) or scr >= (baseline_creat * 1.5):
            st.markdown("<div class='danger-box'>⚠️ <b>ACUTE KIDNEY INJURY (AKI) ALERT:</b> Current creatinine has jumped significantly from baseline. Postpone elective cases immediately.</div>", unsafe_allow_html=True)

    # 5. Dynamic Diagnostics, Workup & Recommendations Engine (With the 4 New Additions)
    st.markdown("<div class='section-header'>⚠️ Active Clinical Issues & Mandatory Workups Matrix</div>", unsafe_allow_html=True)
    
    clinical_issues = []
    recommended_workups = []
    
    # Baseline Vitals & Labs Logic
    if sbp >= 180 or dbp >= 110:
        clinical_issues.append(f"<b>Severe Uncontrolled Hypertension ({sbp}/{dbp} mmHg):</b> Crucial hemodynamic vulnerability.")
        recommended_workups.append("🧪 <b>Hypertension Workup:</b> Order continuous IV Glyceryl Trinitrate or Labetalol titration; request stat 12-lead ECG.")
    if sbp < 90:
        clinical_issues.append(f"<b>Severe Cardiovascular Hypotension ({sbp} mmHg):</b> Absolute circulatory perfusion defect.")
        recommended_workups.append("🧪 <b>Hypotension Workup:</b> Draw urgent Serum Lactate, Central Venous Pressure (CVP) analysis, Blood Cultures x2, and initiate intensive crystaloid resuscitation.")
    if temp >= 38.0:
        clinical_issues.append(f"<b>Preoperative Pyrexia / Active Fever ({temp}°C):</b> High risk of worsening systemic infection.")
        recommended_workups.append("🧪 <b>Fever Workup:</b> Order urgent CBC with differential, C-Reactive Protein (CRP), Chest X-ray, Urinalysis, and Blood/Urine Cultures.")
    if spo2 < 92:
        clinical_issues.append(f"<b>Critical Hypoxemia ({spo2}% on Room Air):</b> Severe oxygen transport barrier.")
        recommended_workups.append("🧪 <b>Hypoxemia Workup:</b> Stat Arterial Blood Gas (ABG) analysis, CT Pulmonary Angiography (CTPA) to rule out PE, and initiate high-flow oxygen.")
    if hr >= 120 or hr < 40:
        clinical_issues.append(f"<b>Hemodynamic Heart Rate Derangement ({hr} bpm):</b> Arrhythmia risk.")
        recommended_workups.append("🧪 <b>Arrhythmia Workup:</b> Order emergency 12-lead ECG, check Serum Magnesium/Potassium panel, and consider continuous telemetry monitoring.")
    if hb < 7.0:
        clinical_issues.append(f"<b>Severe Preoperative Anemia (Hb: {hb} g/dL):</b> Critical tissue hypoxia hazard.")
        recommended_workups.append("🧪 <b>Anemia Workup:</b> Crossmatch and transfuse 2 units of Packed Red Blood Cells (PRBCs) immediately.")
    if potassium > 5.2 or potassium < 3.5:
        clinical_issues.append(f"<b>Electrolyte Imbalance (Potassium: {potassium} mEq/L):</b> Threat of malignant intraoperative arrhythmia.")
        recommended_workups.append("🧪 <b>Potassium Workup:</b> If high, give Calcium Gluconate 10% IV + Insulin-Dextrose infusion. If low, initiate urgent peripheral/central KCl replacement.")
    if cv_ausc in ["Severe Aortic Stenosis", "Systolic Murmur (Possible Aortic Stenosis)"] or echo_valvular == "Severe Aortic Stenosis":
        clinical_issues.append("<b>Suspected/Confirmed Critical Severe Aortic Stenosis:</b> Extremely high risk of sudden cardiac death on induction.")
        recommended_workups.append("🧪 <b>Aortic Stenosis Workup:</b> Urgent Echocardiography mapping is mandatory to calculate aortic valve area (AVA) before any surgical consideration.")

    # 1. New Thyroid Automation Approach Triggers
    if "Thyroid Disorder (Hypo/Hyperthyroidism)" in selected_comorb:
        clinical_issues.append("<b>Co-existing Thyroid Disorder:</b> Potential hazard for metabolic instability or Thyroid Storm.")
        if tsh_level > 10.0 or tsh_level < 0.1:
            recommended_workups.append(f"🦋 <b>Thyroid Workup Required:</b> Pre-op TSH is abnormal ({tsh_level} µIU/mL). Order a fresh <b>Free T4 and Free T3 panel</b>. If overt clinical hyperthyroidism is documented, postpone elective surgery and start anti-thyroid therapy + Beta-blockade immediately.")
        else:
            recommended_workups.append("🦋 <b>Thyroid Action Plan:</b> Patient biochemical TSH window is stable. <b>Continue home Levothyroxine or anti-thyroid drugs</b> on the morning of surgery with a minimal sip of water.")

    # 2. New Epilepsy Automation Approach Triggers
    if "Epilepsy / Seizure Disorder" in selected_comorb:
        clinical_issues.append("<b>Co-existing Epilepsy / Seizure Disorder:</b> Inherent risk of intraoperative breakthrough seizures.")
        if last_seizure in ["Seizure within the last 6 months", "Seizure within the last 30 days"]:
            recommended_workups.append(f"🧠 <b>Epilepsy Workup Required:</b> Patient had a recent breakthrough seizure ({last_seizure}). <b>Order therapeutic serum drug levels</b> (Phenytoin/Valproate/Carbamazepine). Optimize doses immediately and ensure availability of <b>IV Benzodiazepines (Diazepam/Lorazepam)</b> in the operating theater.")
        else:
            recommended_workups.append("🧠 <b>Epilepsy Action Plan:</b> Seizures are historically well-controlled. Ensure the patient <b>receives their full morning oral antiepileptic drug dose</b> on the day of surgery. Coordinate for immediate post-op IV AED formulation if NPO status extends.")

    # 3. New Pacemaker Automation Approach Triggers
    if "Cardiac Pacemaker" in selected_comorb:
        clinical_issues.append("<b>Presence of Permanent Cardiac Pacemaker:</b> Vulnerable to Electromagnetic Interference (EMI) from electrocautery.")
        recommended_workups.append("📟 <b>Pacemaker Safety Workup:</b> Verify indication and pacing dependency. Obtain formal interrogation report (valid within 12 months). If high-power monopolar cautery is expected above the umbilicus, coordinate with anesthesia to program to <b>asynchronous pacing mode (VOO/DOO)</b> or place a magnet securely over the device.")

    # 4. New ICD Automation Approach Triggers
    if "Implantable Cardioverter-Defibrillator (ICD)" in selected_comorb:
        clinical_issues.append("<b>Presence of Implantable Cardioverter-Defibrillator (ICD):</b> CRITICAL hazard for inappropriate shock delivery.")
        recommended_workups.append("⚡ <b>ICD High-Risk Safety Workup:</b> Device interrogation is mandatory within 6 months. <b>Tachyarrhythmia therapy and automatic shocks must be disabled</b> immediately prior to incision. You must apply <b>external transcutaneous pacing/defibrillator pads</b> pre-induction, keep a <b>physical magnet inside the OR suite</b>, and reactivate the device shock capabilities in the PACU immediately after closure.")

    # Glucocorticoid trigger
    if "Chronic Systemic Glucocorticoid / Steroid Use" in selected_comorb:
        clinical_issues.append("<b>Active Long-term Exogenous Cortisone Therapy:</b> High risk for secondary adrenal crisis under anesthesia stress.")
        recommended_workups.append("🛡️ <b>Steroid Action Plan:</b> Mandatory administration of IV Hydrocortisone stress dosing prior to anesthesia induction as outlined in the Optimization tab.")

    # Render Conflict Results
    if clinical_issues:
        st.markdown("<div class='danger-box'><strong>⚠️ Detected Clinical Issues:</strong></div>", unsafe_allow_html=True)
        for issue in clinical_issues:
            st.markdown(f"• {issue}")
            
        st.markdown("<div class='workup-box'><strong>📋 Required Preoperative Workups & Diagnostic Interventions:</strong></div>", unsafe_allow_html=True)
        for workup in recommended_workups:
            st.markdown(f"{workup}", unsafe_allow_html=True)
    else:
        st.markdown("<div class='status-box' style='border-left: 5px solid #16A34A; background-color: #F0FDFA;'>🟢 <b>No clinical abnormalities or severe physiological conflicts detected.</b> Patient is optimized based on current entry criteria.</div>", unsafe_allow_html=True)

    # 6. Final Decision Verdict Summary
    st.markdown("#### Final Clearance Decision Status")
    if clinical_issues or (rcri_score >= 1 and mets_capacity == "No (< 4 METs)"):
        st.error("❌ CLEARANCE STATUS: CONDITIONAL HOLD / HIGH RISK - Elective surgery must be deferred until all listed active workups and clinical parameters are fully optimized and stabilized.")
    else:
        st.success("🟢 CLEARANCE STATUS: CLEARED FOR SURGERY WITH STANDARD PRECAUTIONS - Stable from an Internal Medicine perspective. Proceed with the planned procedure.")

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 11px;'>Al-Ahli Hospital Internal Medicine CDSS Platforms © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
