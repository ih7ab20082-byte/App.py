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
    .summary-card { padding: 20px; border-radius: 12px; border: 1px solid #0F766E; background-color: #FAFAFA; margin-bottom: 20px; }
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
        st.markdown("<h4 style='color:#0F766E;'>Admission Vital Signs</h4>", unsafe_allow_html=True)
        sbp = st.number_input("Systolic Blood Pressure (mmHg):", value=130)
        dbp = st.number_input("Diastolic Blood Pressure (mmHg):", value=80)
        hr = st.number_input("Heart Rate (bpm):", value=75)
        spo2 = st.slider("Preoperative SpO2 on Room Air (%):", min_value=50, max_value=100, value=97)
        temp = st.number_input("Temperature (°C):", value=36.7, step=0.1)

    # Immediate Alert System (Fixed Oxygenation & Hemodynamic Logic)
    st.markdown("<div class='section-header'>Immediate Clinical Triggers</div>", unsafe_allow_html=True)
    trigger_active = False
    
    if spo2 < 92:
        st.markdown(f"<div class='danger-box'>🔴 CRITICAL HYPOXEMIA DETECTED: Preoperative SpO2 is dangerously low ({spo2}%). Elective surgery is strictly contraindicated. Assess for acute pulmonary edema, severe COPD/Asthma exacerbation, or PE. Secure airway and oxygenate immediately.</div>", unsafe_allow_html=True)
        trigger_active = True
        
    if sbp >= 180 or dbp >= 110:
        st.markdown(f"<div class='danger-box'>🔴 CRITICAL HYPERTENSION DETECTED: Blood pressure is severely elevated ({sbp}/{dbp} mmHg). Delay elective surgeries until stabilized. For urgent cases, coordinate with anesthesia for immediate IV antihypertensives.</div>", unsafe_allow_html=True)
        trigger_active = True
        
    if hr >= 120 or hr < 40:
        st.markdown(f"<div class='danger-box'>🔴 CRITICAL ARRHYTHMIA WARNING: Heart rate is abnormal ({hr} bpm). High risk for perioperative myocardial ischemia or acute heart failure. Obtain emergency 12-lead ECG.</div>", unsafe_allow_html=True)
        trigger_active = True
        
    if not trigger_active:
        st.markdown("<div class='status-box' style='border-left: 5px solid #16A34A;'>🟢 Vital Signs Baseline: Hemodynamic and oxygenation variables are within acceptable limits for safe perioperative transition.</div>", unsafe_allow_html=True)

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
        
        ef_val = 55
        echo_valvular = "None / Mild Regular Regurgitation"
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

    # Automated Holistic Synthesis Engine
    st.markdown("<div class='section-header'>Clinical Integration Summary</div>", unsafe_allow_html=True)
    synthesis_alerts = []
    
    if hb < 7.0:
        synthesis_alerts.append("⚠️ CRITICAL ANEMIA (Hb < 7 g/dL): High risk of intraoperative tissue hypoxia. Transfusion of Packed Red Blood Cells (PRBCs) is recommended prior to surgical incision.")
    if cv_ausc == "Severe Aortic Stenosis" or cv_ausc == "Systolic Murmur (Possible Aortic Stenosis)" or echo_valvular == "Severe Aortic Stenosis":
        synthesis_alerts.append("⚠️ POSSIBLE SEVERE AORTIC STENOSIS: High risk for sudden hemodynamic collapse during induction. Delay elective surgery until formal ECHO quantifies the valve area.")
    if echo_done == "Available" and ef_val < 40:
        synthesis_alerts.append("⚠️ SEVERE VENTRICULAR DYSFUNCTION: LVEF is below 40%. High risk for perioperative decompensated heart failure. Avoid aggressive fluid boluses.")
    if chest_ausc == "Basal Bilateral Crepitations (Rales)" or jvp == "Elevated JVP (Sign of Volume Overload)" or cxr_findings == "Pulmonary Congestion / Cephalization":
        synthesis_alerts.append("⚠️ ACTIVE PULMONARY CONGESTION: Clinical markers indicate hypervolemia. Consider administering IV Diuretics (Furosemide) preoperatively.")
    if potassium > 5.2 or potassium < 3.5:
        synthesis_alerts.append("⚠️ ELECTROLYTE IMBALANCE: Potassium must be tightly corrected to a safe range (3.5 - 5.0 mEq/L) to prevent intraoperative arrhythmias.")
        
    if synthesis_alerts:
        for alert in synthesis_alerts:
            st.markdown(f"<div class='danger-box'>{alert}</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='status-box' style='border-left: 5px solid #16A34A;'>🟢 Holistic Examination Baseline: No immediate decompensated cardiopulmonary or laboratory emergency signals detected.</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 3: RISK STRATIFICATION MODELS (RCRI & ARISCAT & ASA)
# ==============================================================================
with tabs[2]:
    st.markdown("<div class='section-header'>Objective Risk Scoring Frameworks</div>", unsafe_allow_html=True)
    col_r1, col_r2 = st.columns(2)
    
    with col_r1:
        st.markdown("<h4 style='color:#0F766E;'>1. Revised Cardiac Risk Index (RCRI)</h4>", unsafe_allow_html=True)
        rcri_1 = st.checkbox("High-risk surgery criteria met", value=("High Risk" in op_type))
        rcri_2 = st.checkbox("History of Ischemic Heart Disease", value=(ecg_findings == "Pathological Q Waves / Ischemic ST-T Changes"))
        rcri_3 = st.checkbox("History of Congestive Heart Failure", value=(ef_val < 40 or cxr_findings == "Pulmonary Congestion / Cephalization"))
        rcri_4 = st.checkbox("History of Cerebrovascular Disease")
        rcri_5 = st.checkbox("Preoperative Insulin Therapy")
        rcri_6 = st.checkbox("Preoperative Serum Creatinine > 2.0 mg/dL", value=(scr > 2.0))
        
        st.markdown("<h5 style='color:#0F766E; margin-top:15px;'>Functional Capacity Evaluation</h5>", unsafe_allow_html=True)
        mets_capacity = st.radio("Can the patient complete activities ≥ 4 METs?", ["Yes (≥ 4 METs)", "No (< 4 METs)"])

        rcri_score = sum([rcri_1, rcri_2, rcri_3, rcri_4, rcri_5, rcri_6])
        risk_mapping = {0: "0.4% (Low Risk)", 1: "1.0% (Moderate Risk)", 2: "2.4% (High Risk)", 3: "5.4% or greater (Critical Risk)"}
        estimated_risk = risk_mapping.get(rcri_score, "5.4% or greater (Critical Risk)")
        
    with col_r2:
        st.markdown("<h4 style='color:#0F766E;'>2. ARISCAT Postoperative Pulmonary Complications (PPC) Index</h4>", unsafe_allow_html=True)
        p_resp = st.checkbox("Active respiratory infection within the past 4 weeks?")
        p_anemia = st.checkbox("Preoperative anemia status?", value=(hb <= 10.0))
        
        p_spo2_str = "≥ 96% (0 pts)"
        if 91 <= spo2 <= 95: p_spo2_str = "91 - 95% (8 pts)"
        elif spo2 <= 90: p_spo2_str = "≤ 90% (24 pts)"
            
        p_site_str = "Peripheral (0 pts)"
        if "Intermediate Risk" in op_type: p_site_str = "Upper Abdominal (15 pts)"
        elif "High Risk" in op_type: p_site_str = "Intrathoracic (24 pts)"

        p_score = 0
        if 51 <= patient_age <= 80: p_score += 3
        elif patient_age > 80: p_score += 11
        p_score += {"≥ 96% (0 pts)": 0, "91 - 95% (8 pts)": 8, "≤ 90% (24 pts)": 24}[p_spo2_str]
        p_score += 17 if p_resp else 0
        p_score += 11 if p_anemia else 0
        p_score += {"Peripheral (0 pts)": 0, "Upper Abdominal (15 pts)": 15, "Intrathoracic (24 pts)": 24}[p_site_str]
        p_score += 16 if op_duration > 3.0 else 0
        p_score += 8 if is_emergency else 0
        
        if p_score >= 45: ppc_class = "High Pulmonary Risk (≥40% complication rate)"
        elif 26 <= p_score <= 44: ppc_class = "Moderate Pulmonary Risk"
        else: ppc_class = "Low Pulmonary Risk"

        st.markdown("<h4 style='color:#0F766E; margin-top:20px;'>3. ASA Physical Status Designation</h4>", unsafe_allow_html=True)
        asa_class = st.selectbox("Assign Global ASA Class:", [
            "ASA Class I: A normal healthy patient",
            "ASA Class II: A patient with mild systemic disease",
            "ASA Class III: A patient with severe systemic disease",
            "ASA Class IV: A patient with severe systemic disease that is a constant threat to life"
        ])

    st.info("Scoring matrices completed. Please verify the 'Global Risk Summary' tab for the final structured text output.")

# ==============================================================================
# TAB 4: COMORBIDITY OPTIMIZATION MATRIX (WITH STEROID DOSE PROTOCOL)
# ==============================================================================
with tabs[3]:
    st.markdown("<div class='section-header'>Chronic Disease Management Protocols & Target End-Points</div>", unsafe_allow_html=True)
    selected_comorb = st.multiselect("Select Active Comorbidities to Review Optimization Steps:", [
        "Diabetes Mellitus", "Hypertension", "Chronic Kidney Disease / End-Stage Renal Disease",
        "COPD / Chronic Bronchial Asthma", "Ischemic Heart Disease / Chronic Heart Failure",
        "Chronic Systemic Glucocorticoid / Steroid Use"
    ])
    
    if "Diabetes Mellitus" in selected_comorb:
        st.markdown("<div class='info-box'><strong>Sugar Control Protocol:</strong><br>• Target: 100 - 180 mg/dL perioperatively.<br>• Defer elective surgeries if HbA1c > 8-9% to prevent wound infection and poor healing.</div>", unsafe_allow_html=True)
    if "Hypertension" in selected_comorb:
        st.markdown("<div class='info-box'><strong>Blood Pressure Strategy:</strong><br>• Postpone strictly if SBP ≥ 180 or DBP ≥ 110 mmHg. Prevent intensive intraoperative hypotension during anesthesia induction.</div>", unsafe_allow_html=True)
    if "Chronic Kidney Disease / End-Stage Renal Disease" in selected_comorb:
        st.markdown("<div class='info-box'><strong>Renal Function Stewardship:</strong><br>• Hemodialysis should be scheduled 12-24 hours prior to surgery. Check Potassium immediately pre-op (Must be < 5.5 mEq/L). Strictly avoid post-operative NSAIDs.</div>", unsafe_allow_html=True)
    if "COPD / Chronic Bronchial Asthma" in selected_comorb:
        st.markdown("<div class='info-box'><strong>Pulmonary Optimization Protocol:</strong><br>• Ensure patient is free of active wheezing or acute exacerbation. Consider a short pre-op course of oral Prednisone 40mg for 3-5 days if baseline respiratory mechanics are poor.</div>", unsafe_allow_html=True)
    if "Ischemic Heart Disease / Chronic Heart Failure" in selected_comorb:
        st.markdown("<div class='info-box'><strong>Myocardial & Volume Optimization:</strong><br>• Elective surgeries are contraindicated within 6 months of an acute ACS/MI event. Patient must be strictly euvolemic without pulmonary rales.</div>", unsafe_allow_html=True)
    if "Chronic Systemic Glucocorticoid / Steroid Use" in selected_comorb:
        st.markdown("""
        <div class='danger-box' style='background-color: #FFFBEB; border-color: #D97706; color: #92400E;'>
            <strong>Perioperative Glucocorticoid Stress Dosing (Adrenal Suppression Protection):</strong><br>
            Indicated for any patient receiving a systemic dose equivalent to ≥ 5 mg Prednisone for more than 3 weeks:<br>
            • Minor Surgical Stress: Take regular home morning steroid dose orally. No extra IV coverage required.<br>
            • Moderate Surgical Stress (e.g., Cholecystectomy, Arthroplasty): Administer 50 mg Hydrocortisone IV immediately before induction, followed by 25 mg IV every 8 hours for a total of 24 hours.<br>
            • Major Surgical Stress (e.g., Aortic/Vascular Reconstruction, Whipple): Administer 100 mg Hydrocortisone IV before induction, followed by 50 mg IV every 8 hours for 24 to 48 hours, then taper rapidly to home maintenance baseline.
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# TAB 5: PERIOPERATIVE MEDICATION STEWARDSHIP
# ==============================================================================
with tabs[4]:
    st.markdown("<div class='section-header'>Critical Perioperative Medication Stewardship Matrix</div>", unsafe_allow_html=True)
    med_cat = st.radio("Select Pharmacological Classification:", ["Oral Antiplatelets & Anticoagulants", "Diabetes Mellitus Therapies", "Antihypertensives"])
    
    if "Antiplatelets" in med_cat:
        st.markdown("<div class='status-box'>• Aspirin: Continue for stented patients unless high closed-cavity risk (e.g., spinal/neurosurgery).<br>• Clopidogrel: Hold for 5 full days prior to elective surgery.<br>• Warfarin: Hold 5 days prior. Bridge with LMWH only if high-embolic risk criteria met.<br>• DOACs (Apixaban/Rivaroxaban): Hold for 24-48 hours based on bleeding severity and computed GFR. No routine bridging.</div>", unsafe_allow_html=True)
    elif "Diabetes" in med_cat:
        st.markdown("<div class='status-box'>• Metformin: Hold 24 hours prior to minimize anesthesia hypoperfusion Lactic Acidosis risk.<br>• SGLT2 Inhibitors: Hold 3-4 days prior due to severe perioperative Euglycemic DKA risk.<br>• Long-Acting Insulin: Reduce dose to 75-80% on the night before or day of surgery. Do not hold completely.<br>• Short-Acting Insulin: Hold while NPO; manage in-hospital with sliding scale checks.</div>", unsafe_allow_html=True)
    elif "Antihypertensives" in med_cat:
        st.markdown("<div class='status-box'>• ACEIs/ARBs: Hold on the morning of surgery to avoid refractory intraoperative hypotension.<br>• Beta-Blockers: Continue strictly on the morning of surgery to prevent rebound tachycardia and ischemia.<br>• Diuretics: Hold on the morning of surgery.</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 6: GLOBAL RISK SUMMARY DASHBOARD (المستند الشامل)
# ==============================================================================
with tabs[5]:
    st.markdown("<div class='section-header'>📋 Comprehensive Perioperative Consultation Summary</div>", unsafe_allow_html=True)
    st.write("This tab compiles all system data into a single scannable clearance document, ideal for insertion into the patient clinical file.")
    
    st.markdown(f"""
    <div class='summary-card'>
        <h3 style='color:#0F766E; margin-top:0px;'>Patient Clearance Summary Report</h3>
        <hr style='margin-top:5px; margin-bottom:15px;'>
        <p><strong>Patient Identifier:</strong> {patient_name} | <strong>Age:</strong> {patient_age} years old</p>
        <p><strong>Scheduled Procedure:</strong> {op_type} ({op_duration} hours expected duration)</p>
        <p><strong>Preoperative Oxygenation Baseline:</strong> SpO2 {spo2}% on Room Air</p>
        <hr style='border-top: 1px dashed #E5E7EB;'>
        
        <h4 style='color:#0F766E;'>1. Cardiovascular Risk Status</h4>
        <p>• <strong>Revised Cardiac Risk Index (RCRI) Score:</strong> {rcri_score} Points</p>
        <p>• <strong>Estimated Risk of MACE:</strong> {estimated_risk}</p>
        <p>• <strong>Functional Capacity (METs):</strong> {mets_capacity}</p>
        
        <h4 style='color:#0F766E;'>2. Pulmonary Risk Status</h4>
        <p>• <strong>ARISCAT Score:</strong> {p_score} Points</p>
        <p>• <strong>Stratification Tier:</strong> {ppc_class}</p>
        
        <h4 style='color:#0F766E;'>3. Anesthesia & Systemic Baseline</h4>
        <p>• <strong>Assigned Global Status:</strong> {asa_class}</p>
        <p>• <strong>Preoperative Hemoglobin:</strong> {hb} g/dL | <strong>Serum Potassium:</strong> {potassium} mEq/L</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Conditional Final Clearance Text Recommendation
    st.markdown("<h4 style='color:#0F766E;'>Final Medical Fitness Recommendation</h4>", unsafe_allow_html=True)
    if spo2 < 92 or sbp >= 180 or (rcri_score >= 1 and mets_capacity == "No (< 4 METs)") or potassium > 5.2 or potassium < 3.5 or hb < 7.0:
        st.markdown("<div class='danger-box'>❌ <strong>CLEARANCE STATUS: CONDITIONAL HOLD / HIGH RISK</strong><br>The patient presents with severe clinical deviations (Critical Hypoxemia, Severe Hypertension, Electrolyte Imbalance, or Elevated MACE with Poor METs). Elective surgery should be deferred until optimization parameters detailed in previous tabs are fully instituted.</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='status-box' style='border-left: 5px solid #16A34A; background-color: #F0FDFA;'>🟢 <strong>CLEARANCE STATUS: CLEARED FOR SURGERY WITH STANDARD PRECAUTIONS</strong><br>The patient is optimized from an Internal Medicine perspective. Proceed with the planned procedure. Ensure specific home medications are held/continued as outlined in the Medication Stewardship protocol.</div>", unsafe_allow_html=True)

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 11px;'>Al-Ahli Hospital Internal Medicine CDSS Platforms © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
