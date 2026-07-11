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
    st.markdown("<div class='section-header'>🔬 Specialty Disease Laboratory Input</div>", unsafe_allow_html=True)
    col_th1, col_th2 = st.columns(2)
    with col_th1:
        tsh_level = st.number_input("Thyroid Stimulating Hormone (TSH) Level (µIU/mL):", value=2.0, step=0.01, help="Normal reference range typically: 0.45 - 4.5 µIU/mL")
    with col_th2:
        last_seizure = st.selectbox("Time Window of Last Documented Epileptic Seizure:", ["No seizures for > 6 months", "Seizure within the last 6 months", "Seizure within the last 30 days"])

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
    
    # Thyroid Matrix
    if "Thyroid Disorder (Hypo/Hyperthyroidism)" in selected_comorb:
        st.markdown(f"""
        <div class='info-box' style='border-left: 5px solid #06B6D4;'>
            <strong>🦋 Thyroid Disorder Comprehensive Management Matrix:</strong><br>
            • <b>Current Profile Status:</b> Patient's inputted TSH is <b>{tsh_level} µIU/mL</b>.<br>
            • <b>Clinical Objective:</b> Achieve clinical and biochemical euthyroid state. Avoid surgery in uncontrolled manifest hyperthyroidism due to high risk of <b>Thyroid Storm</b>.<br>
            • <b>Severe Hypothyroidism:</b> Severe untreated Myxedema coma requires definitive case cancellation; mild-to-moderate forms can safely proceed.
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

    # Pacemaker Matrix
    if "Cardiac Pacemaker" in selected_comorb:
        st.markdown("""
        <div class='danger-box' style='background-color: #F8FAFC; border-color: #475569; color: #1E293B; border-left: 5px solid #475569;'>
            <strong>📟 Cardiac Pacemaker Comprehensive Approach:</strong><br>
            • <b>Device Interrogation:</b> Confirm pacing dependency and battery life. Device must be interrogated within the last 12 months.<br>
            • <b>Electrosurgery Risks:</b> Monopolar Bovie cautery usage above the umbilicus releases Electromagnetic Interference (EMI) which can cause pacing inhibition.<br>
            • <b>Action Strategy:</b> If the patient is entirely pacing-dependent, program to an asynchronous mode (VOO/DOO) or have a valid sterile cardiac magnet inside the OR suite.
        </div>
        """, unsafe_allow_html=True)

    # ICD Matrix
    if "Implantable Cardioverter-Defibrillator (ICD)" in selected_comorb:
        st.markdown("""
        <div class='danger-box' style='background-color: #FFF7ED; border-color: #EA580C; color: #7C2D12; border-left: 5px solid #EA580C;'>
            <strong>⚡ Implantable Cardioverter-Defibrillator (ICD) High-Risk Management:</strong><br>
            • <b>Interrogation Window:</b> Safety and configuration check must be verified within 6 months prior to surgery.<br>
            • <b>Fatal Cautery Artifacts:</b> Surgical monopolar cautery above the umbilicus can be misread by the ICD as Ventricular Fibrillation (VF), triggering catastrophic intraoperative shocks.<br>
            • <b>Stewardship Action Plan:</b> Inactivate tachyarrhythmia shock features immediately before skin incision. Place continuous ECG/Pulse monitoring, ensure a <b>magnet is physically inside the OR</b>, and secure external defibrillator pads pre-induction. Reactivate immediately in the PACU.
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# TAB 5: PERIOPERATIVE MEDICATION STEWARDSHIP (WITH DETAILED EPILEPSY DRUGS)
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
                st.danger_box("🧠 <b>Phenytoin (Epanutin) Protocol:</b> GIVE regular morning dose. If NPO, convert to <b>IV Phenytoin</b> 1:1 ratio. <i>Critical Safety:</i> IV Phenytoin must be infused slowly (<50 mg/min) and only in normal saline to avoid precipitation and cardiotoxicity/arrhythmias.")

    med_cat = st.radio("Select General Pharmacological Classification for Review:", ["Oral Antiplatelets & Anticoagulants", "Diabetes Mellitus Therapies", "Antihypertensives", "Thyroid Medications"])
    
    if "Antiplatelets" in med_cat:
        st.markdown("<div class='status-box'>• <b>Aspirin:</b> Continue for stented patients unless high closed-cavity risk.<br>• <b>Clopidogrel:</b> Hold for 5 full days prior to elective surgery.<br>• <b>Warfarin:</b> Hold 5 days prior. Bridge with LMWH only if high-embolic risk criteria met.<br>• <b>DOACs:</b> Hold for 24-48 hours based on bleeding severity and computed GFR. No routine bridging.</div>", unsafe_allow_html=True)
    elif "Diabetes" in med_cat:
        st.markdown("<div class='status-box'>• <b>Metformin:</b> Hold 24 hours prior to minimize anesthesia hypoperfusion Lactic Acidosis risk.<br>• <b>SGLT2 Inhibitors:</b> Hold 3-4 days prior due to severe perioperative Euglycemic DKA risk.<br>• <b>Long-Acting Insulin:</b> Reduce dose to 75-80% on the night before or day of surgery. Do not hold completely.</div>", unsafe_allow_html=True)
    elif "Antihypertensives" in med_cat:
        st.markdown("<div class='status-box'>• <b>ACEIs/ARBs:</b> Hold on the morning of surgery to avoid refractory intraoperative hypotension.<br>• <b>Beta-Blockers:</b> Continue strictly on the morning of surgery to prevent rebound tachycardia and ischemia.<br>• <b>Diuretics:</b> Hold on the morning of surgery.</div>", unsafe_allow_html=True)
    elif "Thyroid" in med_cat:
        st.markdown("""
        <div class='status-box' style='border-left: 5px solid #0F766E;'>
            <strong>💊 Thyroid Morning-Of Administration Rules:</strong><br><br>
            • <b>Levothyroxine (T4):</b> <b>CONTINUE ABSOLUTELY</b> on the morning of surgery with a tiny sip of water. Long half-life ensures cardiac stability and avoids hypothyroid myocardial bradycardia.<br>
            • <b>Antithyroid Drugs (Carbimazole / Propylthiouracil):</b> <b>CONTINUE</b> on the morning of surgery to prevent perioperative thyroid hormone escape.
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# TAB 6: GLOBAL RISK SUMMARY DASHBOARD (Automated Verification Core)
# ==============================================================================
with tabs[5]:
    st.markdown("<div class='section-header'>📋 Comprehensive Perioperative Consultation Summary</div>", unsafe_allow_html=True)
    
    st.subheader("Patient Clearance Summary Report")
    st.caption("Al-Ahli Hospital Internal Medicine Department")
    
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
            st.markdown("<div class='danger-box'>⚠️ <b>ACUTE KIDNEY INJURY (AKI) ALERT:</b> Current creatinine has jumped significantly from baseline! Postpone elective cases immediately.</div>", unsafe_allow_html=True)

    # --- ADVANCED DYNAMIC AUTOMATION APPROACH & LAB VALIDATION MATRIX ---
    st.markdown("<div class='section-header'>⚠️ Active Clinical Issues & Mandatory Workups Matrix</div>", unsafe_allow_html=True)
    
    clinical_issues = []
    recommended_workups = []
    
    # 1. Automated Lab Desynchronization & Trigger Validation Rules
    if hb < 11.0:
        clinical_issues.append(f"<b>Preoperative Anemia (Hb: {hb} g/dL):</b> Diminished oxygen carrying capacity.")
        recommended_workups.append("🧪 <b>Anemia Optimization:</b> Work up underlying causes. If Hb < 7-8 g/dL or patient is symptomatic/high-cardiac-risk, crossmatch and transfuse Packed Red Blood Cells (PRBCs) prior to incision.")
    if wbc > 11.0 or wbc < 4.0:
        clinical_issues.append(f"<b>Abnormal White Blood Cell Count (WBC: {wbc} x10^3/µL):</b> Out of physiological limits.")
        recommended_workups.append("🧪 <b>Infectious Workup:</b> Rule out active bacterial infection or occult sepsis. Postpone elective cases if acute systemic infection is verified.")
    if plt < 150:
        clinical_issues.append(f"<b>Thrombocytopenia (Platelets: {plt} x10^3/µL):</b> Elevated risk of intraoperative surgical hemorrhage.")
        if plt < 50:
            recommended_workups.append("🧪 <b>CRITICAL Platelet Workup:</b> Severe bleeding risk! Arrange for immediate platelet apheresis transfusion units to be available inside the operating suite.")
        else:
            recommended_workups.append("🧪 <b>Mild/Moderate Platelet Workup:</b> Avoid neuraxial/epidural anesthesia triggers if platelets are < 80-100; consult hematology if cause is unknown.")
    if inr_val > 1.2:
        clinical_issues.append(f"<b>Coagulopathy Alert (INR: {inr_val}):</b> Prolonged clotting profile.")
        recommended_workups.append("🧪 <b>Coagulation Workup:</b> Hold anticoagulants. If emergency surgery is mandatory, consider reversal with Vitamin K or Prothrombin Complex Concentrate (PCC).")
    if potassium > 5.2 or potassium < 3.5:
        clinical_issues.append(f"<b>Electrolyte Imbalance (Potassium: {potassium} mEq/L):</b> High risk for cardiac arrhythmias.")
        recommended_workups.append("🧪 <b>Electrolyte Optimization:</b> For hyperkalemia, administer shift therapy (Insulin-Dextrose + Calcium Gluconate). For hypokalemia, initiate controlled IV/PO Potassium replacement.")

    # Vitals Validation Triggers
    if sbp >= 180 or dbp >= 110:
        clinical_issues.append(f"<b>Severe Uncontrolled Hypertension ({sbp}/{dbp} mmHg):</b> Target-organ vascular risk.")
        recommended_workups.append("🧪 <b>Hypertension Management:</b> Initiate acute IV Labetalol or Glyceryl Trinitrate titration; postpone elective cases.")
    if spo2 < 92:
        clinical_issues.append(f"<b>Critical Hypoxemia ({spo2}% on Room Air):</b> Severe tissue desaturation hazard.")
        recommended_workups.append("🧪 <b>Pulmonary Hypoxemia Workup:</b> Obtain emergency ABG, Chest X-ray, and rule out acute PE or decompensated heart failure.")

    # 2. FIXED: Strict Thyroid Automation Approach Validation
    if "Thyroid Disorder (Hypo/Hyperthyroidism)" in selected_comorb:
        clinical_issues.append(f"<b>Active Thyroid Pathology History (Current TSH: {tsh_level} µIU/mL):</b> Requires tight metabolic monitoring.")
        # If TSH is abnormal (Outside 0.45 - 4.5 µIU/mL)
        if tsh_level > 4.5 or tsh_level < 0.45:
            recommended_workups.append(f"🦋 <b>Mandatory Thyroid Workup Triggered:</b> The TSH value of <b>{tsh_level}</b> is outside the safe reference range! <b>Order urgent Free T4 and Free T3</b> to rule out overt hyperthyroidism (high Thyroid Storm risk) or severe clinical Myxedema.")
        else:
            recommended_workups.append("🦋 <b>Thyroid Action Plan:</b> Biochemical TSH is stable. Ensure <b>Levothyroxine/Antithyroid medications are given</b> on the morning of surgery with a tiny sip of water.")

    # 3. FIXED: Epilepsy Automation Approach Validation
    if "Epilepsy / Seizure Disorder" in selected_comorb:
        clinical_issues.append(f"<b>Active Epilepsy / Seizure Disorder (Last Event: {last_seizure}):</b> Susceptible to intraoperative breakthrough events.")
        if last_seizure in ["Seizure within the last 6 months", "Seizure within the last 30 days"]:
            recommended_workups.append(f"🧠 <b>Mandatory Epilepsy Workup Triggered:</b> Due to a recent seizure event ({last_seizure}), you must <b>order statutory serum therapeutic drug levels</b> (e.g., Valproate, Phenytoin levels). Optimize anticonvulsant dosing and ensure <b>IV Benzodiazepines</b> are drawn and ready in the OR.")
        else:
            recommended_workups.append("🧠 <b>Epilepsy Action Plan:</b> Disease is stable. <b>Administer home AEDs on the morning of surgery</b>. Ensure immediate transition to IV formulations post-operatively if NPO status is prolonged.")

    # 4. Pacemaker Validation
    if "Cardiac Pacemaker" in selected_comorb:
        clinical_issues.append("<b>Cardiac Pacemaker implanted:</b> Risk of Electromagnetic Interference (EMI).")
        recommended_workups.append("📟 <b>Pacemaker Protocol:</b> Verify pacing dependency and ensure interrogation was completed within 12 months. If surgery is above the umbilicus using monopolar Bovie, have a cardiac magnet inside the OR suite or program device to VOO/DOO mode.")

    # 5. ICD Validation
    if "Implantable Cardioverter-Defibrillator (ICD)" in selected_comorb:
        clinical_issues.append("<b>ICD Device Present:</b> Extremely critical risk of inappropriate intraoperative shocks.")
        recommended_workups.append("⚡ <b>ICD Mandatory Safety Plan:</b> Deactivate shock/tachyarrhythmia therapy immediately before skin incision. Place external transcutaneous defibrillator pads on the patient, secure a <b>magnet inside the OR suite</b>, and reactivate the device immediately post-op in the PACU.")

    # 6. Glucocorticoid Validation
    if "Chronic Systemic Glucocorticoid / Steroid Use" in selected_comorb:
        clinical_issues.append("<b>Exogenous Chronic Cortisone Therapy:</b> Risk of adrenal suppression.")
        recommended_workups.append("🛡️ <b>Adrenal Protection Workup:</b> Give IV Hydrocortisone stress dosing pre-induction (50mg for moderate stress, 100mg for major surgical stress) followed by q8h scheduled dosing.")

    # Render Conflict Results
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
    if clinical_issues or (rcri_score >= 1 and mets_capacity == "No (< 4 METs)"):
        st.error("❌ CLEARANCE STATUS: CONDITIONAL HOLD / HIGH RISK - Elective surgery must be deferred until all listed active workups and clinical parameters are fully optimized and stabilized.")
    else:
        st.success("🟢 CLEARANCE STATUS: CLEARED FOR SURGERY WITH STANDARD PRECAUTIONS - Stable from an Internal Medicine perspective. Proceed with the planned procedure.")

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 11px;'>Al-Ahli Hospital Internal Medicine CDSS Platforms © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
