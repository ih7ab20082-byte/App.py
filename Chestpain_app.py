import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Al-Ahli Acute Chest Pain Stratifier",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for Emergency and Cardiology Rigor
st.markdown("""
    <style>
    .main-title { font-size:30px !important; font-weight: bold; color: #1E3A8A; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:15px !important; color: #4B5563; text-align: center; margin-bottom: 25px; font-style: italic; }
    .branding-bar { background-color: #EFF6FF; padding: 20px; border-radius: 10px; border-left: 6px solid #1E3A8A; margin-bottom: 25px; }
    .branding-bar strong { color: #1E3A8A !important; font-weight: bold; }
    .branding-text { color: #1F2937 !important; font-size: 15px !important; line-height: 1.6; }
    .section-header { font-size:20px !important; font-weight: bold; color: #1E3A8A; margin-top: 15px; margin-bottom: 15px; border-bottom: 2px solid #E5E7EB; padding-bottom: 5px; }
    .status-box { padding: 15px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #E5E7EB; background-color: #F9FAFB; }
    .board-header { font-size:22px !important; font-weight: bold; color: #D97706; margin-top: 30px; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<div class='main-title'>🫀 Al-Ahli Hospital Acute Chest Pain Stratifier</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Advanced Decision Support System for Clinical Risk Phenotyping & Dynamic Troponin Kinetics</div>", unsafe_allow_html=True)

# Professional Branding Block
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Project Founder & Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Clinical Core:</strong> HEART Score Stratification, ESC Troponin Algorithm (0/3h Protocols), Sgarbossa Ischemic Screens
    </div>
</div>
""", unsafe_allow_html=True)

# Layout Split
col_input, col_dashboard = st.columns([1.1, 1.1])

# ==============================================================================
# LEFT COLUMN: HEART SCORE & TROPONIN INPUT PANEL
# ==============================================================================
with col_input:
    st.markdown("<div class='section-header'>📋 1. HEART Score Clinical Inputs</div>", unsafe_allow_html=True)
    
    # H - History
    history = st.radio(
        "History - Clinical Suspicion Intensity:",
        [0, 1, 2],
        format_func=lambda x: {
            0: "0 points: Slightly suspicious history",
            1: "1 point: Moderately suspicious history",
            2: "2 points: Highly suspicious history (Classic radiating pressure)"
        }[x]
    )
    
    # E - ECG
    ecg = st.radio(
        "ECG Interpretation:",
        [0, 1, 2],
        format_func=lambda x: {
            0: "0 points: Normal or non-specific repolarization",
            1: "1 point: Significant repolarization abnormalities / LBBB / Pacemaker",
            2: "2 points: ST depression or elevation transient (not clear STEMI)"
        }[x]
    )
    
    # A - Age
    age_input = st.number_input("Patient Actual Age (Years):", min_value=18, max_value=110, value=55)
    age_points = 0 if age_input < 45 else (1 if age_input < 65 else 2)
    
    # R - Risk Factors
    risk_factors = st.multiselect(
        "Cardiovascular Risk Factors Present:",
        ["HTN", "Diabetes Mellitus", "Hyperlipidemia / Dyslipidemia", "Active Smoker", "Family History of CAD", "Obesity (BMI ≥ 30)", "Known Atherosclerotic Stroke / PAD"]
    )
    rf_count = len(risk_factors)
    rf_points = 0 if rf_count == 0 else (1 if rf_count <= 2 else 2)

    st.markdown("<div class='section-header'>🧪 2. Kinetic Troponin Guard Panel</div>", unsafe_allow_html=True)
    
    # Troponin dynamic calculator inputs
    trop_baseline = st.number_input("Baseline High-Sensitivity Troponin (ng/L) [0-Hour]:", min_value=0.0, max_value=50000.0, value=12.0, step=1.0)
    trop_serial = st.number_input("Serial High-Sensitivity Troponin (ng/L) [3-Hour]:", min_value=0.0, max_value=50000.0, value=45.0, step=1.0)
    
    # T - Initial Troponin points for HEART score
    # Approximating standard institutional cuts
    trop_points = 0 if trop_baseline <= 14 else (1 if trop_baseline <= 42 else 2)

    # Calculate Total HEART Score
    total_heart_score = history + ecg + age_points + rf_points + trop_points
    
    # Calculate Dynamic Delta Troponin
    delta_absolute = trop_serial - trop_baseline
    delta_relative = (delta_absolute / trop_baseline * 100) if trop_baseline > 0 else 0

    st.markdown("<div class='section-header'>🛑 3. Safety Checkboxes</div>", unsafe_allow_html=True)
    has_lbbb = st.checkbox("Patient has a Left Bundle Branch Block (LBBB) on ECG", value=False)
    active_bleeding = st.checkbox("Suspected or Active Internal Bleeding / Severe Coagulopathy", value=False)

# ==============================================================================
# RIGHT COLUMN: REAL-TIME MANAGEMENT DASHBOARD & DECISION TREES
# ==============================================================================
with col_dashboard:
    st.markdown("<div class='section-header'>⚡ Automated Cardiac Stratification Output</div>", unsafe_allow_html=True)
    
    # 1. ECG Safety Alert Block (Sgarbossa Reminder)
    if has_lbbb:
        st.warning("⚠️ **ECG GUARD: LBBB Present (Activate Sgarbossa Screening Criteria):**")
        st.markdown("""
        * Look for **Concordant ST-elevation $\ge 1\ mm$** in leads with a positive QRS complex (5 points).
        * Look for **Concordant ST-depression $\ge 1\ mm$** in leads V1, V2, or V3 (3 points).
        * If points $\ge 3$, suspect an acute myocardial infarction hidden behind the block!
        """)
        st.markdown("---")

    # 2. HEART Score Evaluation Display
    st.markdown(f"### Calculated HEART Score: `{total_heart_score} / 10`")
    
    if total_heart_score <= 3:
        heart_color = "#F0FDF4"
        heart_border = "#15803D"
        heart_text = "🟢 **LOW RISK PATIENT (Score 0-3):**\n* **MACE Risk:** ~1.7% chance of adverse cardiac events within 6 weeks.\n* **Guideline:** Candidate for safe and accelerated discharge if serial troponins are completely flat."
    elif 4 <= total_heart_score <= 6:
        heart_color = "#FFFBEB"
        heart_border = "#D97706"
        heart_text = "⚠️ **INTERMEDIATE RISK PATIENT (Score 4-6):**\n* **MACE Risk:** ~12-17% chance of adverse cardiac events.\n* **Guideline:** Admit to the medical ward/observation unit. Continue serial biomarker tracking and consider a non-invasive cardiac stress test / CT coronary angiography."
    else:
        heart_color = "#FEF2F2"
        heart_border = "#991B1B"
        heart_text = "🚨 **HIGH RISK PATIENT (Score 7-10):**\n* **MACE Risk:** $> 50\%$ chance of imminent adverse cardiac events.\n* **Guideline:** Immediate stabilization. Initiate active medical therapy (Dual Antiplatelet Therapy - DAPT, Heparin protocol). Consult Cardiology for early invasive coronary angiography (Cath Lab)."

    st.markdown(f"""
    <div class='status-box' style='background-color: {heart_color}; border-left: 5px solid {heart_border};'>
        {heart_text}
    </div>
    """, unsafe_allow_html=True)

    # 3. Dynamic Troponin Kinetics Tab Area
    tab_kinetics, tab_contra = st.tabs(["📉 Dynamic Troponin Delta Analysis", "🚫 Antithrombotics Safety Matrix"])
    
    with tab_kinetics:
        st.markdown("### 📊 ESC-Directed Biomarker Velocity Calculations")
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.metric("Absolute Delta Troponin", f"{delta_absolute:.1f} ng/L")
        with col_m2:
            st.metric("Percentage Relative Shift", f"{delta_relative:.1f} %")
            
        st.markdown("<div class='status-box'>", unsafe_allow_html=True)
        st.write("📋 **Kinetic Interpretation & Decision Rule:**")
        
        # Checking ESC delta criteria (Standard limits: Absolute rise of 5-7 ng/L or >20% relative rise indicates acute injury)
        if delta_absolute >= 7.0 or delta_relative >= 20.0:
            st.error("🚨 **RULE-IN CRITERIA MET (Acute Myocardial Injury Velocity):**")
            st.markdown(f"""
            * **Kinetic Status:** The troponin has shifted significantly (Absolute: **{delta_absolute:.1f} ng/L**, Relative: **{delta_relative:.1f}%**).
            * **Diagnosis:** Consistent with an **Acute NSTEMI / Type 1 Myocardial Infarction** or severe acute myocardial stress.
            * **Order Set:** Start Full-Dose Anticoagulation unless contraindicated. Notify Cardiology for Cath Lab evaluation.
            """)
        elif delta_absolute == 0 and trop_baseline <= 14:
            st.success("🟢 **RULE-OUT MET:** Biomarker values are flat and below upper reference limits. Stable chronic margins.")
        else:
            st.warning("🌗 **OBSERVATION ZONE:** Small indeterminate fluctuations. Check a third sample in 3 hours if clinical suspicion remains high.")
        st.markdown("</div>", unsafe_allow_html=True)

    with tab_contra:
        st.markdown("### 🚫 Absolute & Relative Contraindications Panel")
        if active_bleeding:
            st.error("❌ **CRITICAL CONTRAINDICATION TRIGGERED:** Active bleeding or coagulopathy is present! Hold all heavy therapeutic anticoagulation (e.g., LMWH therapeutic infusion) and immediately balance risk/benefit with senior consultant input.")
        else:
            st.success("🟢 No absolute bleeding contraindications checked. Standard ACS management algorithms may proceed with cautious monitoring.")

# ==============================================================================
# HIGH-YIELD BOARD EXAM REVIEW MATERIAL (Created for the Scientific Club)
# ==============================================================================
st.markdown("---")
st.markdown("<div class='board-header'>🎓 High-Yield Board-Level Review (Al-Ahli Scientific Research Club)</div>", unsafe_allow_html=True)

with st.expander("❓ Click to Reveal the Board Question & Rationale"):
    st.markdown("""
    **Clinical Scenario:** A 62-year-old male with a history of hypertension and dyslipidemia presents to the Al-Ahli emergency department with a 2-hour history of retrosternal chest heaviness radiating to his left shoulder. His initial ECG reveals non-specific T-wave inversions in leads V4-V6. Initial high-sensitivity troponin at 0-hours is **12 ng/L** (Normal reference boundary $< 14\ ng/L$). A repeat sample obtained 3 hours later reveals a high-sensitivity troponin level of **22 ng/L**. 
    
    **Based on the European Society of Cardiology (ESC) guidelines and his kinetic biomarker shifts, which of the following represents the most accurate clinical interpretation?**
    
    * **A)** The patient is successfully ruled out from an acute myocardial infarction because both troponin levels are below the high mortality threshold.
    * **B)** The absolute increase of 10 ng/L over 3 hours fulfills the dynamic 'Rule-In' criteria for acute myocardial injury.
    * **C)** A coronary CT angiography should be ordered immediately as the next best step before starting any antiplatelet agents.
    * **D)** The troponin rise is negligible, and the patient should be discharged home with outpatient exercise stress testing.
    
    ---
    
    ### 📝 Comprehensive Scientific Rationale:
    * **The Correct Answer is B.** Even though the initial troponin was completely normal, the absolute kinetic delta over 3 hours is **10 ng/L** ($22 - 12$), which exceeds the guideline-directed threshold of an absolute rise of $\ge 5-7\ ng/L$ for high-sensitivity assays. This dynamic rise proves an active, ongoing myocardial necrosis process, confirming an **NSTEMI** despite the normal initial baseline. 
    * **Clinical Pearl for the Club:** Never rely on a single normal baseline troponin in patients with classic symptoms! The **Delta (Kinetics)** is what differentiates acute coronary syndrome from chronic stable elevation.
    """)

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 11px;'>Al-Ahli Hospital Internal Medicine CDSS Platforms © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
