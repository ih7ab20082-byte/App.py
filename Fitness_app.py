import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Al-Ahli Perioperative Fitness Engine v3",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Advanced Medical UI Theme Styling
st.markdown("""
    <style>
    .main-title { font-size:28px !important; font-weight: bold; color: #0F766E; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:14px !important; color: #4B5563; text-align: center; margin-bottom: 20px; font-style: italic; }
    .branding-bar { background-color: #F0FDFA; padding: 15px; border-radius: 10px; border-left: 6px solid #0F766E; margin-bottom: 25px; }
    .section-header { font-size:20px !important; font-weight: bold; color: #0F766E; margin-top: 25px; margin-bottom: 15px; border-bottom: 2px solid #0F766E; padding-bottom: 5px; }
    .status-box { padding: 14px; border-radius: 6px; margin-bottom: 12px; border: 1px solid #E5E7EB; background-color: #F9FAFB; color: #1F2937; }
    .danger-box { padding: 14px; border-radius: 6px; margin-bottom: 12px; border: 1px solid #DC2626; background-color: #FEF2F2; color: #991B1B; font-size: 14px; }
    .info-box { padding: 14px; border-radius: 6px; margin-bottom: 12px; border: 1px solid #2563EB; background-color: #EFF6FF; color: #1E40AF; }
    .workup-box { padding: 14px; border-radius: 6px; margin-bottom: 12px; border: 1px solid #D97706; background-color: #FFFBEB; color: #92400E; }
    .specialty-box { padding: 14px; border-radius: 6px; margin-bottom: 12px; border: 1px solid #7C3AED; background-color: #F5F3FF; color: #5B21B6; }
    </style>
""", unsafe_allow_html=True)

# 3. Department Header & Branding
st.markdown("<div class='main-title'>🏥 Al-Ahli Hospital Comprehensive Perioperative Medical Fitness Engine</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Advanced Automation Decision Matrix for Surgical Clearance & Multi-System Comorbidity Optimization</div>", unsafe_allow_html=True)

st.markdown("""
<div class='branding-bar'>
    <div style='color: #1F2937; font-size: 14px; line-height: 1.6;'>
        <strong>Project Director:</strong> Dr. Ihab Abbass Abu Hilail &nbsp;|&nbsp; 
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital<br>
        <strong>Clinical Benchmarks:</strong> ACC/AHA Perioperative Cardiac Updates, ARISCAT Pulmonary Matrix, ADA Diabetes Guidelines, ATA Thyroid Frameworks
    </div>
</div>
""", unsafe_allow_html=True)

# 4. Main App Tabs Configuration
tabs = st.tabs([
    "👤 Patient Profile & Vitals",
    "🩺 Clinical Exam & Cardiopulmonary Labs",
    "🧠 Metabolic & Endocrine Specialty Focus",
    "⚡ Device Interruption (Pacemaker/ICD)",
    "📋 Comprehensive Final Clearance Dashboard"
])

# ==============================================================================
# TAB 1: PATIENT PROFILE, SURGERY METADATA & VITALS Panel
# ==============================================================================
with tabs[0]:
    st.markdown("<div class='section-header'>Patient Demographics & Surgical Risk Profile</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        patient_name = st.text_input("Patient Identifier Name / ID:", value="John Doe")
        patient_age = st.number_input("Patient Age (Years):", min_value=18, max_value=110, value=65)
        op_type = st.selectbox("Surgical Procedure Classification (Inherent Risk Group):", [
            "Low Risk (Cataract, Superficial / Breast Biopsy, Upper/Lower GI Endoscopy)",
            "Intermediate Risk (Orthopedic Major Joint, Cholecystectomy, Laparoscopic Ventral Hernia, Prostatectomy)",
            "High Risk (Major Vascular, Open Aortic Surgery, Whipple Procedure, Thoracoabdominal Lung Resection)"
        ])
        is_emergency = st.checkbox("This is an Urgent or Emergency Surgical Case")
        
    with col2:
        st.markdown("<h4 style='color:#0F766E; margin-top:0px;'>Perioperative Bedside Vitals Panel</h4>", unsafe_allow_html=True)
        sbp = st.number_input("Systolic Blood Pressure (mmHg):", value=130)
        dbp = st.number_input("Diastolic Blood Pressure (mmHg):", value=80)
        hr = st.number_input("Heart Rate (bpm):", value=78)
        rr = st.number_input("Respiratory Rate (breaths/min):", value=18, help="Crucial parameter for pulmonary score")
        spo2 = st.slider("Preoperative SpO2 on Room Air (%):", min_value=50, max_value=100, value=96)
        temp = st.number_input("Temperature (°C):", value=36.8, step=0.1)

    st.markdown("<div class='section-header'>Immediate Critical Vitals Alerts</div>", unsafe_allow_html=True)
    vitals_alerts = []
    if spo2 < 92: vitals_alerts.append(f"🔴 CRITICAL HYPOXEMIA: Baseline oxygen saturation is alarming ({spo2}%). Postpone elective theater.")
    if rr > 24: vitals_alerts.append(f"🔴 TACHYPNEA DETECTED: Respiratory rate is {rr}/min. Potential acute pulmonary congestion.")
    if sbp >= 180 or dbp >= 110: vitals_alerts.append(f"🔴 MALIGNANT HYPERTENSION CRITERIA: Blood pressure is {sbp}/{dbp} mmHg. Postpone elective cases immediately.")
    
    if vitals_alerts:
        for alert in vitals_alerts: st.markdown(f"<div class='danger-box'>{alert}</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='status-box' style='border-left: 5px solid #16A34A;'>🟢 Vital Signs Baseline: Stable. Hemodynamically sound for routine induction preparation.</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 2: DETAILED CLINICAL EXAMINATION & CARDIOPULMONARY LABS
# ==============================================================================
with tabs[1]:
    st.markdown("<div class='section-header'>Targeted Physical Examination Findings & Diagnostics</div>", unsafe_allow_html=True)
    col_ex1, col_ex2 = st.columns(2)
    with col_ex1:
        st.markdown("<h4 style='color:#0F766E; margin-top:0px;'>Clinical Physical Findings</h4>", unsafe_allow_html=True)
        chest_ausc = st.selectbox("Chest Auscultation Assessment:", [
            "Clear Lung Fields", 
            "Diffuse Expiratory Wheezing / Rhonchi", 
            "Basal Bilateral Crepitations (Rales)", 
            "Markedly Decreased Air Entry / Dullness"
        ])
        cv_ausc = st.selectbox("Cardiovascular Auscultation Findings:", [
            "Normal S1 S2, No Pathological Murmurs", 
            "Loud Systolic Murmur at Right Upper Sternal Border (Suspect Severe AS)", 
            "Diastolic Murmur at Apex", 
            "S3 Gallop Rhythm Present (Decompensated Heart Failure Indicator)"
        ])
        edema = st.checkbox("Bilateral Lower Limb Pitting Edema Present (Sign of Fluid Overload / Right HF)")
        
    with col_ex2:
        st.markdown("<h4 style='color:#0F766E; margin-top:0px;'>Cardiopulmonary Specialized Diagnostics</h4>", unsafe_allow_html=True)
        ecg_findings = st.selectbox("Electrocardiogram (ECG) Analysis:", [
            "Normal Sinus Rhythm", 
            "Sinus Tachycardia / Bradycardia", 
            "Atrial Fibrillation with Controlled Ventricular Response", 
            "Atrial Fibrillation with Uncontrolled Rapid Ventricular Response", 
            "Pathological Q Waves / Acute Ischemic ST-T Changes", 
            "New Onset Left Bundle Branch Block (LBBB)"
        ])
        ef_val = st.number_input("Left Ventricular Ejection Fraction (LVEF %):", min_value=10, max_value=85, value=50)
        cxr_findings = st.selectbox("Chest X-Ray (CXR) Core Report:", [
            "Clear Lung Fields, No Infiltrates", 
            "Cardiomegaly with Marked Pulmonary Congestion / Cephalization", 
            "Lobar Consolidation / Focal Active Infiltrate", 
            "Bilateral Pleural Effusion"
        ])

    st.markdown("<h4 style='color:#0F766E; margin-top:20px;'>Preoperative Routine Systemic Laboratory Dashboard</h4>", unsafe_allow_html=True)
    col_lab1, col_lab2, col_lab3 = st.columns(3)
    with col_lab1:
        hb = st.number_input("Current Hemoglobin Count (g/dL):", value=13.0, step=0.1)
        wbc = st.number_input("White Blood Cells (x10^3/µL):", value=7.0, step=0.1)
    with col_lab2:
        scr = st.number_input("Current Serum Creatinine Clearance (mg/dL):", value=1.0, step=0.1)
        potassium = st.number_input("Serum Potassium Balance (mEq/L):", value=4.0, step=0.1)
    with col_lab3:
        plt = st.number_input("Platelet Count Matrix (x10^3/µL):", value=220)
        inr_val = st.number_input("Coagulation INR Baseline:", value=1.1, step=0.1)

# ==============================================================================
# TAB 3: METABOLIC, GLYCEMIC & ENDOCRINE SPECIALTY FOCUS
# ==============================================================================
with tabs[2]:
    st.markdown("<div class='section-header'>🦋 1. Integrated Thyroid Status Strategy</div>", unsafe_allow_html=True)
    col_th1, col_th2, col_th3 = st.columns(3)
    with col_th1:
        tsh_level = st.number_input("Thyroid Stimulating Hormone (TSH) Level (µIU/mL):", value=2.0, step=0.1)
    with col_th2:
        ft4_level = st.number_input("Free T4 (FT4) Level (ng/dL):", value=1.2, step=0.01)
    with col_th3:
        ft3_level = st.number_input("Free T3 (FT3) Level (pg/mL):", value=3.0, step=0.01)

    st.markdown("##### 💊 Concurrent Thyroid Stewardship Home Medications")
    thyroid_meds = st.multiselect("Active Home Thyroid Therapeutics:", [
        "Levothyroxine (Euthyrox / Synthroid)", "Carbimazole", "Propylthiouracil (PTU)", "None"
    ], default=["None"])

    # --------------------------------------------------------------------------
    st.markdown("<div class='section-header'>🩸 2. Comprehensive Glycemic Control & Diabetic Stewardship Panel</div>", unsafe_allow_html=True)
    col_dm1, col_dm2 = st.columns(2)
    with col_dm1:
        hba1c = st.number_input("Hemoglobin A1c Percentage (HbA1c %):", value=7.0, step=0.1)
    with col_dm2:
        rbs = st.number_input("Random Blood Sugar at Admission (RBS mg/dL):", value=140)

    # Glycemic Smart Logic Block
    st.markdown("##### 🩺 Glycemic Perioperative Optimization Guidance:")
    if rbs > 180 or hba1c > 8.5:
        st.markdown(f"<div class='workup-box'><b>⚠️ POOR PERIOPERATIVE GLYCEMIC CONTROL (RBS: {rbs} mg/dL, HbA1c: {hba1c}%):</b><br>• <b>Surgical Risk:</b> High propensity for delayed deep surgical wound healing, surgical site infections (SSIs), and osmotic diuresis.<br>• <b>Action Protocol:</b> Initiate an inpatient **Sliding Scale Regular Insulin** regimen for current target of (140-180 mg/dL). Hold all oral hypoglycemic drugs (e.g., Metformin, SGLT2 inhibitors like Jardiance) 24 hours prior to surgery to avoid lactic acidosis or euglycemic DKA.</div>", unsafe_allow_html=True)
    elif rbs < 70:
        st.markdown(f"<div class='danger-box'><b>🚨 HYPOGLYCEMIA CRITICAL ALERT (RBS: {rbs} mg/dL):</b><br>• <b>Immediate Emergency Treatment:</b> Administer 100-150 mL of **10% Dextrose IV infusion** immediately or 1 ampoule of D50W. Recheck blood sugar every 15-30 minutes until securely above 100 mg/dL before anesthesia induction.</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='status-box' style='border-left: 5px solid #16A34A;'>🟢 Metabolic Baseline: Glycemic profile is optimized. Target parameters met.</div>", unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    st.markdown("<div class='section-header'>🧠 3. Integrated Epilepsy & Antiepileptic Drug (AED) Maintenance</div>", unsafe_allow_html=True)
    last_seizure = st.selectbox("Documented Seizure Recency Matrix:", [
        "Patient does NOT have Epilepsy", "Seizure-free for > 6 months", "Seizure within the last 6 months", "Seizure within the last 30 days"
    ])
    
    if last_seizure != "Patient does NOT have Epilepsy":
        selected_aeds = st.multiselect("Identify current home Antiepileptic Drugs (AEDs) to build IV Bridging:", [
            "Levetiracetam (Keppra)", "Sodium Valproate (Depakine)", "Carbamazepine (Tegretol)", "Lamotrigine (Lamictal)", "Phenytoin (Epanutin)"
        ])
        for aed in selected_aeds:
            if "Levetiracetam" in aed:
                st.markdown("<div class='specialty-box'>🧠 <b>Levetiracetam (Keppra) Protocol:</b> Give normal morning PO dose. If post-op NPO window is present, bridge with <b>IV Keppra 1:1 dosing equivalence</b> infused over 15 mins.</div>", unsafe_allow_html=True)
            if "Sodium Valproate" in aed:
                st.markdown("<div class='specialty-box'>🧠 <b>Sodium Valproate (Depakine) Protocol:</b> Give home dose morning of theater. If NPO, bridge with <b>IV Depakine 1:1</b>. *Strictly double check baseline platelets* as it may cause dysfunction.</div>", unsafe_allow_html=True)
            if "Carbamazepine" in aed:
                st.markdown("<div class='specialty-box' style='border-color: #B45309; background-color: #FFFBEB; color: #78350F;'>🧠 <b>Carbamazepine (Tegretol) Protocol:</b> Give PO dose on morning of surgery. ⚠️ <b>No IV formulation exists.</b> If NPO is prolonged (>24 hrs), immediately consult neurology to load with alternative coverage like IV Keppra.</div>", unsafe_allow_html=True)
            if "Phenytoin" in aed:
                st.markdown("<div class='danger-box' style='background-color: #FFF5F5; border-color: #E53E3E; color: #9B2C2C;'>🧠 <b>Phenytoin (Epanutin) Protocol:</b> Bridge with <b>IV Phenytoin 1:1 equivalence</b>. Infuse strictly at less than 50 mg/min and mix <b>ONLY with Normal Saline</b> to prevent precipitation. Run on continuous cardiac monitor.</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 4: ⚡ CARDIOVASCULAR IMPLANTABLE ELECTRONIC DEVICES (CIED) MANAGEMENT
# ==============================================================================
with tabs[3]:
    st.markdown("<div class='section-header'>⚡ Electrosurgical & CIED Interruption Strategy (Pacemaker / ICD)</div>", unsafe_allow_html=True)
    cied_status = st.radio("Does the patient have a Cardiac Implantable Electronic Device?", [
        "No Device Present", "Permanent Pacemaker (PPM)", "Implantable Cardioverter-Defibrillator (ICD)", "Combined CRTD / Pacemaker-Defibrillator Device"
    ])
    
    if cied_status != "No Device Present":
        st.markdown("### 📋 Mandatory Perioperative Device Interruption Protocol:")
        
        if "Defibrillator" in cied_status or "ICD" in cied_status:
            st.markdown("<div class='danger-box'><b>🚨 ICD DEACTIVATION REQUIRED PRIOR TO INCISION:</b><br>• <b>Rationale:</b> Surgical monopolar electrocautery (Bovie) causes electromagnetic interference (EMI) that the ICD will misinterpret as Ventricular Fibrillation, leading to **inappropriate intraoperative shocks**.<br>• <b>Plan:</b> Suspend/Deactivate the shock tachyarrhythmia therapy of the ICD right before the operation using a programmer magnet.<br>• <b>Mandatory Safety Catch:</b> Continuous ECG monitoring is mandatory. Defibrillator pads **MUST** be placed on the patient, and a standalone external defibrillator crash cart must be physically inside the Operating Room for immediate crash use. Re-activate device immediately in recovery.</div>", unsafe_allow_html=True)
        
        if "Pacemaker" in cied_status or "PPM" in cied_status:
            st.markdown("<div class='workup-box'><b>⚡ PACEMAKER STRATEGY (Pacing Dependent Patients):</b><br>• <b>Rationale:</b> Electrosurgery EMI can suppress pacemaking output, inducing acute severe intraoperative asystole or severe bradycardia.<br>• <b>Action:</b> If the patient is pacemaker-dependent or the surgery is superior to the umbilicus, program the device to an **Asynchronous Pacing Mode (DOO or VOO)** using a specialized magnet or cardiology review. This keeps pacing at a fixed rate, completely safe from EMI artifact suppression.</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 5: GLOBAL MEDICAL FITNESS COMPREHENSIVE RECONCILIATION DASHBOARD
# ==============================================================================
with tabs[4]:
    st.markdown("<div class='section-header'>📋 Final Multi-System Medical Clearance Reconciliation</div>", unsafe_allow_html=True)
    st.subheader("Patient Clinical Summary Decision Architecture Report")
    st.caption("Al-Ahli Hospital Internal Medicine Perioperative Consultation Unit")
    
    st.info(f"👤 **Patient:** {patient_name}  |  🎂 **Age:** {patient_age} Years Old  |  🚀 **Surgical Classification:** {op_type}")
    
    clinical_issues = []
    mandatory_actions = []
    
    # --- AUTOMATED HEART FAILURE RECONCILIATION ---
    is_hf = (edema or "Crepitations" in chest_ausc or "Cardiomegaly" in cxr_findings or "S3 Gallop" in cv_ausc or ef_val < 40)
    if is_hf:
        clinical_issues.append("<b>Heart Failure / Acute Volume Overload Congestion:</b> Documented presence of Lower Limb Edema, S3 Gallop, or Congested Chest X-Ray / Rales.")
        mandatory_actions.append("❌ <b>HOLD ELECTIVE SURGERY:</b> Decompensated Heart Failure carries catastrophic perioperative mortality. Order urgent <b>NT-proBNP</b>, consult Cardiology, and optimize with IV Diuretics (Furosemide) prior to any clearance.")

    # --- PERIOPERATIVE PULMONARY RISK ASSESSMENT LOGIC ---
    pulm_score = 0
    if patient_age > 60: pulm_score += 3
    if spo2 <= 95: pulm_score += 8
    if rr > 20: pulm_score += 4
    if "Wheezing" in chest_ausc or "Crepitations" in chest_ausc: pulm_score += 5
    if "Consolidation" in cxr_findings: pulm_score += 6
    if is_emergency: pulm_score += 8

    if pulm_score >= 45: pulm_tier = "🔴 HIGH Pulmonary Complication Risk Status"
    elif 26 <= pulm_score <= 44: pulm_tier = "🟡 MODERATE Pulmonary Complication Risk Status"
    else: pulm_tier = "🟢 LOW Pulmonary Complication Risk Status"

    clinical_issues.append(f"<b>Perioperative Pulmonary Risk Assessment (ARISCAT Scaffold):</b> Calculated Tier is: <b>{pulm_tier}</b> (Score: {pulm_score} points).")
    if pulm_score >= 26:
        mandatory_actions.append("🫁 Initiate aggressive pre-op chest physiotherapy, order incentive spirometry training, and schedule post-op bronchodilator nebulizers.")

    # --- GLYCEMIC RECONCILIATION ---
    if rbs > 200 or hba1c > 8.5:
        clinical_issues.append(f"Uncontrolled Diabetes Mellitus (RBS: {rbs} mg/dL, HbA1c: {hba1c}%).")
        mandatory_actions.append("🩸 Manage with short-acting IV or subcutaneous insulin scale. Cancel elective major cases if DKA or severe ketosis is suspected.")
    elif rbs < 70:
        clinical_issues.append(f"Acute Preoperative Hypoglycemia (RBS: {rbs} mg/dL).")
        mandatory_actions.append("🚨 Emergency correction with IV Dextrose infusion before induction.")

    # --- THYROID RECONCILIATION ---
    if tsh_level > 4.5:
        if ft4_level < 0.8:
            clinical_issues.append(f"Overt Hypothyroidism (TSH: {tsh_level}, Low FT4: {ft4_level}).")
            mandatory_actions.append("❌ <b>HOLD ELECTIVE SURGERY:</b> High risk of severe prolonged intraoperative bradycardia, myxedema coma, and poor cardiac lability.")
        else:
            clinical_issues.append(f"Subclinical Hypothyroidism (TSH: {tsh_level}, Normal FT4).")
            mandatory_actions.append("🟢 Safe for surgery. Ensure baseline home Levothyroxine is taken on the morning of surgery with a tiny sip of water.")

    # --- CARDIAC DEVICE SAFETY TRIGGER ---
    if cied_status != "No Device Present":
        clinical_issues.append(f"Cardiac Electronic Device Installed ({cied_status}).")
        mandatory_actions.append("⚡ Apply magnet intraoperatively for PPM, or suspend shock tracking on ICD with external pads physically applied to chest wall.")

    # ==============================================================================
    # 🚨 AUTOMATED POST-OPERATIVE DESTINATION TRIAGE MATRIX (ICU/CCU vs FLOOR)
    # ==============================================================================
    st.markdown("<div class='section-header'>🛏️ Automated Post-Operative Bed Triage Decision Matrix</div>", unsafe_allow_html=True)
    
    need_ccu = (ef_val < 35 or "Rapid Ventricular" in ecg_findings or "Ischemic ST-T" in ecg_findings or "S3 Gallop" in cv_ausc)
    need_icu = (pulm_score >= 45 or spo2 < 90 or "High Risk" in op_type or is_emergency)
    
    if need_ccu and is_hf:
        st.markdown("<div class='danger-box' style='border-left: 6px solid #B91C1C;'>🏥 <b>MANDATORY POST-OPERATIVE DESTINATION: CCU BED CORRIDOR (Critical Cardiac Care Unit)</b><br>• <b>Rationale:</b> Patient has critical cardiac triggers (Low LVEF, Decompensated Clinical HF Signs, or Acute Ischemia) and requires continuous arterial lines, central venous pressure monitoring, and potential active inotropic infusion post-theater. <b>DO NOT send to general ward.</b></div>", unsafe_allow_html=True)
    elif need_icu:
        st.markdown("<div class='danger-box' style='border-left: 6px solid #7C3AED; background-color: #FAF5FF; color: #6D28D9;'>🏥 <b>MANDATORY POST-OPERATIVE DESTINATION: MAIN ICU BED ALLOCATION (Intensive Care Unit)</b><br>• <b>Rationale:</b> Due to elevated ARISCAT Pulmonary scoring, high inherent vascular surgical trauma, or hypoxemic risks, the patient requires prolonged post-op elective mechanical ventilation or intensive respiratory monitoring. Secure ICU bed clearance prior to skin incision.</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='status-box' style='border-left: 5px solid #16A34A; background-color: #F0FDFA;'>🏥 <b>MANDATORY POST-OPERATIVE DESTINATION: REGULAR MEDICAL-SURGICAL FLOOR WARD</b><br>• <b>Rationale:</b> Multi-system metrics indicate standard postoperative recovery is satisfactory. Continuous high-dependency step-down care is not indicated.</div>", unsafe_allow_html=True)

    # ==============================================================================
    # FINAL RECONCILIATION DISPOSITION RENDER
    # ==============================================================================
    st.markdown("<div class='section-header'>🔬 Aggregated Multi-System Findings Log & Action Steps</div>", unsafe_allow_html=True)
    col_fin1, col_fin2 = st.columns(2)
    with col_fin1:
        st.markdown("##### ⚠️ Systemic Pathophysiological Findings:")
        for issue in clinical_issues: st.markdown(f"• {issue}", unsafe_allow_html=True)
    with col_fin2:
        st.markdown("##### 📋 Action Optimization Instructions:")
        for action in mandatory_actions: st.markdown(f"• {action}", unsafe_allow_html=True)

    st.markdown("#### Final Combined Medical Clearance Verdict Summary")
    if any("❌" in act or "HOLD" in act for act in mandatory_actions):
        st.error("❌ COMBINED DECISION: CLEARANCE DELAYED / CONDITIONAL HOLD - Severe acute active organ decompensation detected. Elective cases must be canceled until clinical stabilization targets are met.")
    else:
        st.success("🟢 COMBINED DECISION: MEDICAL FITNESS APPROVED / PROCEED TO INDUCTION - Patient is medically optimized with targeted perioperative maintenance parameters.")

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 11px;'>Al-Ahli Hospital Internal Medicine CDSS Platforms v3 • 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
