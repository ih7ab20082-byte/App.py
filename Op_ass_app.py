import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Al-Ahli Perioperative Fitness Engine",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Enhanced CSS for Professional Clinical Interface
st.markdown("""
    <style>
    .main-title { font-size:30px !important; font-weight: bold; color: #0F766E; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:15px !important; color: #4B5563; text-align: center; margin-bottom: 25px; font-style: italic; }
    .branding-bar { background-color: #F0FDFA; padding: 18px; border-radius: 12px; border-left: 6px solid #0F766E; margin-bottom: 25px; }
    .section-header { font-size:20px !important; font-weight: bold; color: #0F766E; margin-top: 15px; margin-bottom: 15px; border-bottom: 2px solid #E5E7EB; padding-bottom: 5px; }
    .status-box { padding: 15px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #E5E7EB; background-color: #F9FAFB; line-height: 1.6; color: #1F2937; }
    .danger-box { padding: 15px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #DC2626; background-color: #FEF2F2; color: #991B1B; line-height: 1.6; }
    .info-box { padding: 15px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #2563EB; background-color: #EFF6FF; color: #1E40AF; line-height: 1.6; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<div class='main-title'>🏥 Al-Ahli Hospital Comprehensive Perioperative Medical Fitness Engine</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Advanced Holistic Decision-Support Matrix for Surgical Clearance & Multi-System Comorbidity Optimization</div>", unsafe_allow_html=True)

# Professional Branding Block
st.markdown(f"""
<div class='branding-bar'>
    <div style='color: #1F2937; font-size: 15px; line-height: 1.6;'>
        <strong>Project Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Core Standards:</strong> ACC/AHA Perioperative Guidelines, ARISCAT Pulmonary Risk, ASA Classification
    </div>
</div>
""", unsafe_allow_html=True)

# Main Application Tabs
tabs = st.tabs([
    "👤 Patient Profile & Vitals",
    "🩺 Clinical Examination & Investigations",
    "📊 Risk Stratification Models (RCRI & ARISCAT)",
    "🧬 Comorbidity Optimization Matrix",
    "💊 Perioperative Medication Stewardship"
])

# ==============================================================================
# TAB 1: PATIENT PROFILE, SURGERY DETAILS & VITALS
# ==============================================================================
with tabs[0]:
    st.markdown("<div class='section-header'>Patient Profile and Surgical Procedure Metadata</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        patient_name = st.text_input("Patient Name / ID Number:")
        patient_age = st.number_input("Patient Age:", min_value=18, max_value=110, value=60)
        op_type = st.selectbox("Type of Scheduled Surgery (Inherent Risk Classification):", [
            "Low Risk (Cataract, Superficial Surgery, Upper/Lower GI Endoscopy)",
            "Intermediate Risk (Orthopedic Major Joint, Cholecystectomy, Prostatectomy, Uncomplicated Hernia)",
            "High Risk (Major Vascular, Open Aortic Surgery, Thoracoabdominal Thoracotomy, Total Cystectomy)"
        ])
        op_duration = st.number_input("Expected Duration of Surgery (in Hours):", min_value=0.5, max_value=12.0, value=2.0, step=0.5)
        is_emergency = st.checkbox("Is this an emergency or urgent surgical procedure?")
        
    with col2:
        st.markdown("<h4 style='color:#0F766E;'>Admission Vital Signs</h4>", unsafe_allow_html=True)
        sbp = st.number_input("Systolic Blood Pressure (mmHg):", value=130)
        dbp = st.number_input("Diastolic Blood Pressure (mmHg):", value=80)
        hr = st.number_input("Heart Rate (bpm):", value=75)
        spo2 = st.slider("Preoperative SpO2 on Room Air (%):", min_value=70, max_value=100, value=97)
        temp = st.number_input("Temperature (°C):", value=36.7, step=0.1)

    # Immediate Alert System based on Vitals & Urgency
    st.markdown("<div class='section-header'>Immediate Clinical Triggers</div>", unsafe_allow_html=True)
    if sbp >= 180 or dbp >= 110:
        st.markdown("<div class='danger-box'>CRITICAL HYPERTENSION DETECTED: Blood pressure is severely elevated (≥ 180/110 mmHg). Delay elective surgeries until blood pressure is controlled. For urgent surgeries, coordinate immediately with anesthesia for IV titratable antihypertensives.</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='status-box' style='border-left: 5px solid #16A34A;'>Hemodynamic Status: Blood pressure is within acceptable limits for safe perioperative transition.</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 2: CLINICAL EXAMINATION & INVESTIGATIONS (ECG, ECHO, CXR, LABS)
# ==============================================================================
with tabs[1]:
    st.markdown("<div class='section-header'>Comprehensive Clinical Evaluation and Diagnostic Diagnostics</div>", unsafe_allow_html=True)
    
    col_ex1, col_ex2 = st.columns(2)
    with col_ex1:
        st.markdown("<h4 style='color:#0F766E;'>Targeted Physical Examination Findings</h4>", unsafe_allow_html=True)
        chest_ausc = st.selectbox("Chest Auscultation:", ["Clear Lung Fields", "Diffuse Wheezing", "Basal Bilateral Crepitations (Rales)", "Decreased Air Entry / Dullness"])
        cv_ausc = st.selectbox("Cardiovascular Auscultation:", ["Normal S1 S2, No Murmurs", "Systolic Murmur (Possible Aortic Stenosis)", "Diastolic Murmur", "S3 Gallop Rhythm Present"])
        jvp = st.radio("Jugular Venous Pressure (JVP):", ["Normal / Not Elevated", "Elevated JVP (Sign of Volume Overload)"])
        edema = st.checkbox("Bilateral Lower Limb Pitting Edema Present")
        
    with col_ex2:
        st.markdown("<h4 style='color:#0F766E;'>Cardiopulmonary Diagnostics (ECG, ECHO, CXR)</h4>", unsafe_allow_html=True)
        ecg_findings = st.selectbox("Electrocardiogram (ECG) Report:", ["Normal Sinus Rhythm", "Sinus Tachycardia / Bradycardia", "Atrial Fibrillation with Controlled VR", "Atrial Fibrillation with Rapid VR", "Pathological Q Waves / Ischemic ST-T Changes", "Left Bundle Branch Block (LBBB)"])
        echo_done = st.radio("Echocardiogram (ECHO) Status:", ["Available", "Not Done / Not Clinically Indicated"])
        
        ef_val = 50
        if echo_done == "Available":
            ef_val = st.number_input("Left Ventricular Ejection Fraction (LVEF %):", min_value=10, max_value=85, value=55)
            echo_valvular = st.selectbox("Valvular Pathologies:", ["None / Mild Regular Regurgitation", "Severe Aortic Stenosis", "Severe Mitral Regurgitation", "Other Moderate-to-Severe Valvular Disease"])
            
        cxr_findings = st.selectbox("Chest X-Ray (CXR) Findings:", ["Clear Lung Fields", "Cardiomegaly", "Pulmonary Congestion / Cephalization", "Consolidation / Focal Infiltrate", "Hyperinflation"])

    # Laboratory Panel Integration
    st.markdown("<h4 style='color:#0F766E; margin-top:20px;'>Preoperative Laboratory Dashboard</h4>", unsafe_allow_html=True)
    col_lab1, col_lab2, col_lab3 = st.columns(3)
    with col_lab1:
        hb = st.number_input("Hemoglobin (g/dL):", value=13.5, step=0.1)
        wbc = st.number_input("White Blood Cells (x10^3/µL):", value=7.5, step=0.1)
    with col_lab2:
        scr = st.number_input("Serum Creatinine (mg/dL):", value=0.9, step=0.1)
        potassium = st.number_input("Serum Potassium (mEq/L):", value=4.2, step=0.1)
    with col_lab3:
        plt = st.number_input("Platelet Count (x10^3/µL):", value=250)
        inr_val = st.number_input("INR Level:", value=1.0, step=0.1)

    # Automated Synthesis of Physical Exam and Diagnostics
    st.markdown("<div class='section-header'>Clinical Integration Summary</div>", unsafe_allow_html=True)
    synthesis_alerts = []
    if cv_ausc == "Systolic Murmur (Possible Aortic Stenosis)":
        synthesis_alerts.append("POSSIBLE SEVERE AORTIC STENOSIS: High risk for sudden hemodynamic collapse during induction. Delay surgery if elective until formal ECHO quantifies the valve area and gradient.")
    if echo_done == "Available" and ef_val < 40:
        synthesis_alerts.append("SEVERE VENTRICULAR DYSFUNCTION: LVEF is below 40%. High risk for perioperative decompensated heart failure. Avoid aggressive fluid boluses and optimize preload/afterload.")
    if chest_ausc == "Basal Bilateral Crepitations (Rales)" or jvp == "Elevated JVP (Sign of Volume Overload)" or cxr_findings == "Pulmonary Congestion / Cephalization":
        synthesis_alerts.append("ACTIVE PULMONARY CONGESTION: Clinical markers indicate the patient is hypervolemic. Consider administering IV Diuretics (Furosemide) preoperatively to reach euvolemic baseline.")
    if potassium > 5.2 or potassium < 3.5:
        synthesis_alerts.append("ELECTROLYTE IMBALANCE: Potassium must be tightly corrected to a safe range (3.5 - 5.0 mEq/L) to prevent lethal intraoperative arrhythmias.")
        
    if synthesis_alerts:
        for alert in synthesis_alerts:
            st.markdown(f"<div class='danger-box'>{alert}</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='status-box' style='border-left: 5px solid #16A34A;'>Holistic Examination Baseline: No immediate decompensated cardiopulmonary, physical, or laboratory signals detected. Proceeding to scoring matrices.</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 3: RISK STRATIFICATION MODELS (RCRI & ARISCAT)
# ==============================================================================
with tabs[2]:
    st.markdown("<div class='section-header'>Objective Risk Scoring Frameworks</div>", unsafe_allow_html=True)
    col_r1, col_r2 = st.columns(2)
    
    with col_r1:
        st.markdown("<h4 style='color:#0F766E;'>1. Revised Cardiac Risk Index (RCRI) Configuration</h4>", unsafe_allow_html=True)
        rcri_1 = st.checkbox("High-risk surgery criteria met (Intrathoracic, intra-abdominal, or suprainguinal vascular)", value=("High Risk" in op_type))
        rcri_2 = st.checkbox("History of Ischemic Heart Disease (IHD / CAD / Prior MI / Pathological Q waves on ECG)", value=(ecg_findings == "Pathological Q Waves / Ischemic ST-T Changes"))
        rcri_3 = st.checkbox("History of Congestive Heart Failure (CHF / Pulmonary Congestion / LVEF < 40%)", value=(echo_done == "Available" and ef_val < 40 or cxr_findings == "Pulmonary Congestion / Cephalization"))
        rcri_4 = st.checkbox("History of Cerebrovascular Disease (Prior Stroke or TIA)")
        rcri_5 = st.checkbox("Preoperative Insulin Therapy for Diabetes Mellitus")
        rcri_6 = st.checkbox("Preoperative Serum Creatinine > 2.0 mg/dL (177 µmol/L)", value=(scr > 2.0))
        
        # METs Assessment linked to cardiac pathway
        st.markdown("<h5 style='color:#0F766E; margin-top:15px;'>Functional Capacity Evaluation</h5>", unsafe_allow_html=True)
        mets_capacity = st.radio("Can the patient complete activities ≥ 4 METs without limiting symptoms? (e.g., climb two flights of stairs, walk up a steep hill)", ["Yes (≥ 4 METs)", "No (< 4 METs)"])

        # RCRI Calculations
        rcri_score = sum([rcri_1, rcri_2, rcri_3, rcri_4, rcri_5, rcri_6])
        risk_mapping = {0: "0.4% (Low Risk Index)", 1: "1.0% (Moderate Risk Index)", 2: "2.4% (High Risk Index)", 3: "5.4% or greater (Critical Risk Index)"}
        estimated_risk = risk_mapping.get(rcri_score, "5.4% or greater (Critical Risk Index)")
        
        st.markdown(f"<h5>Total RCRI Score: <code>{rcri_score} Points</code></h5>", unsafe_allow_html=True)
        st.markdown(f"<div class='status-box'>Estimated Risk of Major Adverse Cardiac Events (MACE): <strong>{estimated_risk}</strong> during the perioperative timeline.</div>", unsafe_allow_html=True)
        
        if rcri_score >= 1 and mets_capacity == "No (< 4 METs)":
            st.markdown("<div class='danger-box'>ACC/AHA CLINICAL TRIGGER: Elevated risk score combined with poor functional capacity (< 4 METs). If the procedure is non-urgent, withhold automatic clearance and secure a Cardiology Consultation for non-invasive risk testing (Echocardiogram or Stress Test).</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='status-box' style='border-left: 5px solid #16A34A;'>Cardiac Pathway Cleared: Patient meets stable criteria to bypass advanced functional stress testing. Maintain home cardiopulmonary optimizations.</div>", unsafe_allow_html=True)

    with col_r2:
        st.markdown("<h4 style='color:#0F766E;'>2. ARISCAT Postoperative Pulmonary Complications (PPC) Index</h4>", unsafe_allow_html=True)
        p_resp = st.checkbox("Active respiratory infection within the past 4 weeks?")
        p_anemia = st.checkbox("Preoperative anemia status?", value=(hb <= 10.0))
        
        # Map parameters from profile
        p_spo2_str = "≥ 96% (0 pts)"
        if 91 <= spo2 <= 95: p_spo2_str = "91 - 95% (8 pts)"
        elif spo2 <= 90: p_spo2_str = "≤ 90% (24 pts)"
            
        p_site_str = "Peripheral (0 pts)"
        if "Intermediate Risk" in op_type: p_site_str = "Upper Abdominal (15 pts)"
        elif "High Risk" in op_type: p_site_str = "Intrathoracic (24 pts)"

        # Score Compilation
        p_score = 0
        if 51 <= patient_age <= 80: p_score += 3
        elif patient_age > 80: p_score += 11
        
        p_score += {"≥ 96% (0 pts)": 0, "91 - 95% (8 pts)": 8, "≤ 90% (24 pts)": 24}[p_spo2_str]
        p_score += 17 if p_resp else 0
        p_score += 11 if p_anemia else 0
        p_score += {"Peripheral (0 pts)": 0, "Upper Abdominal (15 pts)": 15, "Intrathoracic (24 pts)": 24}[p_site_str]
        p_score += 16 if op_duration > 3.0 else 0
        p_score += 8 if is_emergency else 0
        
        st.markdown(f"<h5>Calculated ARISCAT Score: <code>{p_score} Points</code></h5>", unsafe_allow_html=True)
        if p_score >= 45:
            st.markdown(f"<div class='danger-box'>HIGH PULMONARY RISK (Score {p_score} ≥ 45): Predicts a >40% incidence of severe postoperative pulmonary events (Atelectasis, Hypoxemia, Respiratory Failure). Mandate intensive pre-op incentive spirometry and schedule post-op bronchodilator nebulization.</div>", unsafe_allow_html=True)
        elif 26 <= p_score <= 44:
            st.markdown(f"<div class='status-box' style='border-left: 5px solid #D97706;'>MODERATE PULMONARY RISK (Score {p_score}): Intermediate probability of clinical PPC. Avoid intraoperative fluid volume overload and facilitate early post-operative mobilization.</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='status-box' style='border-left: 5px solid #16A34A;'>LOW PULMONARY RISK: Standard baseline respiratory optimization is sufficient.</div>", unsafe_allow_html=True)

        # Unified ASA Classification Tag
        st.markdown("<h4 style='color:#0F766E; margin-top:20px;'>3. ASA Physical Status Designation</h4>", unsafe_allow_html=True)
        asa_class = st.selectbox("Assign Global ASA Class:", [
            "ASA Class I: A normal healthy patient",
            "ASA Class II: A patient with mild systemic disease (controlled DM/HTN)",
            "ASA Class III: A patient with severe systemic disease (stable CAD, CKD on dialysis)",
            "ASA Class IV: A patient with severe systemic disease that is a constant threat to life"
        ])
        if "ASA Class III" in asa_class or "ASA Class IV" in asa_class:
            st.markdown("<div class='danger-box'>ADVANCED SYSTEMIC IMPAIRMENT: Patient falls into a high ASA tier. High anesthetic complexity is anticipated. Confirm postoperative intensive care unit (ICU) or high dependency unit (HDU) backup bed availability.</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 4: COMORBIDITY OPTIMIZATION MATRIX
# ==============================================================================
with tabs[3]:
    st.markdown("<div class='section-header'>Chronic Disease Management Protocols & Target End-Points</div>", unsafe_allow_html=True)
    st.write("Select the patient's specific underlying medical comorbidities to unlock specialized pre-surgical optimization directives:")
    
    selected_comorb = st.multiselect("Select Active Comorbidities:", [
        "Diabetes Mellitus",
        "Hypertension",
        "Chronic Kidney Disease / End-Stage Renal Disease",
        "COPD / Chronic Bronchial Asthma",
        "Ischemic Heart Disease / Chronic Heart Failure",
        "Chronic Systemic Glucocorticoid / Steroid Use"
    ])
    
    if "Diabetes Mellitus" in selected_comorb:
        st.markdown("""
        <div class='info-box'>
            <strong>Sugar Control Protocol:</strong><br>
            • Clinical Target End-Point: Maintain perioperative blood glucose tightly between 100 - 180 mg/dL.<br>
            • Elective Threshold: Postpone major elective procedures if HbA1c is severely uncontrolled (> 8-9%) to prevent severe postoperative wound infection and impaired healing.<br>
            • Action Plan: Transition oral medications to scheduled sliding scales or continuous intravenous insulin infusions on the day of surgery.
        </div>
        """, unsafe_allow_html=True)
        
    if "Hypertension" in selected_comorb:
        st.markdown("""
        <div class='info-box'>
            <strong>Blood Pressure Strategy:</strong><br>
            • Safe Surgical Window: Do not delay essential surgery for mild or moderate hypertension. Delay is strictly warranted if Systolic BP ≥ 180 mmHg or Diastolic BP ≥ 110 mmHg.<br>
            • Anesthetic Goal: Prevent severe intraoperative hypotension during induction. Ensure specialized vasoactive classes are managed according to the Medication Stewardship tab.
        </div>
        """, unsafe_allow_html=True)
        
    if "Chronic Kidney Disease / End-Stage Renal Disease" in selected_comorb:
        st.markdown("""
        <div class='info-box'>
            <strong>Renal Function Stewardship:</strong><br>
            • Maintenance Dialysis Patients: Schedule maintenance hemodialysis exactly 12 - 24 hours prior to the operative incision to ensure optimal volume status and electrolyte normalization.<br>
            • Serum Potassium Mandate: Check serum potassium immediately prior to operating room entry. If potassium is > 5.5 mEq/L, delay until medical shifting therapies or emergency dialysis is performed.<br>
            • Analgesic Restrictions: Strictly avoid post-operative Non-Steroidal Anti-Inflammatory Drugs (NSAIDs) to safeguard residual nephron function.
        </div>
        """, unsafe_allow_html=True)

    if "COPD / Chronic Bronchial Asthma" in selected_comorb:
        st.markdown("""
        <div class='info-box'>
            <strong>Pulmonary Optimization Protocol:</strong><br>
            • Fitness Goal: Ensure the patient is at their personal clinical baseline, free of active wheezing, severe dyspnea, or productive sputum changes.<br>
            • Exacerbation Management: For patients with significant residual airway obstruction or recent flare-ups, prescribe a short preoperative course of oral Prednisone (40 mg daily) for 3 to 5 days prior to surgery.
        </div>
        """, unsafe_allow_html=True)

    if "Ischemic Heart Disease / Chronic Heart Failure" in selected_comorb:
        st.markdown("""
        <div class='info-box'>
            <strong>Myocardial & Volume Optimization:</strong><br>
            • Recent Myocardial Infarction (MI): Elective, non-urgent surgeries are strictly contraindicated within 6 months of an acute coronary syndrome event due to exceptionally high re-infarction rates.<br>
            • Heart Failure Stability: Patient must be strictly euvolemic. Defer surgery if there is clinical evidence of right or left-sided fluid accumulation (ascites, peripheral congestion, pulmonary rales).
        </div>
        """, unsafe_allow_html=True)

    if "Chronic Systemic Glucocorticoid / Steroid Use" in selected_comorb:
        st.markdown("""
        <div class='danger-box' style='background-color: #FFFBEB; border-color: #D97706; color: #92400E;'>
            <strong>Perioperative Glucocorticoid Stress Dosing (Adrenal Protection):</strong><br>
            Indicated for any patient receiving a systemic dose equivalent to ≥ 5 mg Prednisone for more than 3 weeks, due to secondary hypothalamic-pituitary-adrenal (HPA) axis suppression:<br>
            • Minor Surgical Stress (e.g., Local skin procedures): Take regular home morning steroid dose orally. No extra IV coverage needed.<br>
            • Moderate Surgical Stress (e.g., Open Cholecystectomy, Total Joint Arthroplasty): Administer 50 mg Hydrocortisone IV immediately before induction, followed by 25 mg IV every 8 hours for a total of 24 hours.<br>
            • Major Surgical Stress (e.g., Major Whipple, Cardiothoracic, Vascular Reconstruction): Administer 100 mg Hydrocortisone IV before induction, followed by 50 mg IV every 8 hours for 24 to 48 hours, then taper rapidly to regular home maintenance doses.
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# TAB 5: PERIOPERATIVE MEDICATION STEWARDSHIP
# ==============================================================================
with tabs[4]:
    st.markdown("<div class='section-header'>Critical Perioperative Medication Stewardship Matrix</div>", unsafe_allow_html=True)
    
    med_cat = st.radio("Select Pharmacological Classification to Review Hold / Resume Directives:", [
        "Oral Antiplatelets & Anticoagulants (Antithrombotic Core)",
        "Diabetes Mellitus Therapies & Insulin Regimens",
        "Antihypertensives & Vasoactive Medications"
    ])
    
    if "Antithrombotic" in med_cat:
        st.markdown("""
        <div class='status-box'>
            <strong>Antithrombotic Discontinuation Timelines:</strong><br>
            • Aspirin (Monotherapy): Continue uninterrupted for patients with coronary stents undergoing non-neurological/non-spinal procedures. Discontinue 7 days before if surgery is in a closed anatomical cavity.<br>
            • Clopidogrel (Plavix): Hold strictly for 5 full days prior to elective operative timelines.<br>
            • Warfarin (Coumadin): Discontinue 5 days prior to surgery. Utilize Heparin Bridging (therapeutic LMWH/Enoxaparin) strictly in high-embolic risk groups (e.g., older mechanical mitral valves, acute VTE < 3 months).<br>
            • Direct Oral Anticoagulants (DOACs - Apixaban, Rivaroxaban): Hold for 24 to 48 hours before surgery based on surgical bleeding severity and the computed glomerular filtration rate (GFR). Routine bridging is not indicated.
        </div>
        """, unsafe_allow_html=True)
        
    elif "Diabetes" in med_cat:
        st.markdown("""
        <div class='status-box'>
            <strong>Antidiabetic Agent Adjustment Rules:</strong><br>
            • Metformin: Hold 24 hours prior to surgery to minimize risks of anesthesia-induced tissue hypoperfusion and subsequent Lactic Acidosis.<br>
            • SGLT2 Inhibitors (Empagliflozin, Dapagliflozin): Discontinue 3 to 4 days before major surgery due to the pronounced risk of perioperative Euglycemic Diabetic Ketoacidosis (DKA).<br>
            • Long-Acting Basal Insulin (Glargine / Lantus): Reduce the evening dose before or the morning dose on the day of surgery to 75% - 80% of the patient's standard calculation. Do not hold completely.<br>
            • Short-Acting Nutritional Insulin: Hold completely while the patient is NPO (Nil Per Os). Monitor fingerstick blood sugar every 6 hours and manage with a regular sliding scale regimen.
        </div>
        """, unsafe_allow_html=True)
        
    elif "Antihypertensives" in med_cat:
        st.markdown("""
        <div class='status-box'>
            <strong>Vasoactive & Blood Pressure Medication Directives:</strong><br>
            • ACE Inhibitors & ARBs (Enalapril, Valsartan, Lisinopril): Hold on the morning of the surgical procedure. Continuing these agents poses a severe risk of refractory intraoperative hypotension that resists traditional vasopressor reversal.<br>
            • Beta-Blockers (Metoprolol, Carvedilol, Bisoprolol): Continue strictly on the morning of surgery with a minimal sip of water. Abrupt withdrawal causes rebound sympathetic activity, severe tachycardia, and silent myocardial ischemia.<br>
            • Calcium Channel Blockers: Continue uninterrupted through the perioperative window.<br>
            • Diuretics (Furosemide / Lasix): Hold on the morning of surgery to limit profound intraoperative hypovolemia and acute electrolyte shifting under general anesthesia.
        </div>
        """, unsafe_allow_html=True)

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 11px;'>Al-Ahli Hospital Internal Medicine CDSS Platforms © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
