import streamlit as st
import random

# Page Configuration
st.set_page_config(
    page_title="Al-Ahli Hospital Cardiorenal Command Center",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Branding and Signature Style
st.markdown("""
    <style>
    .main-title { font-size:32px !important; font-weight: bold; color: #1E3A8A; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:16px !important; color: #4B5563; text-align: center; margin-bottom: 25px; font-style: italic; }
    .branding-bar { background-color: #F3F4F6; padding: 20px; border-radius: 10px; border-left: 6px solid #3B82F6; margin-bottom: 25px; }
    .branding-bar strong { color: #1E3A8A !important; font-weight: bold; }
    .branding-text { color: #1F2937 !important; font-size: 16px !important; line-height: 1.6; }
    .section-header { font-size:22px !important; font-weight: bold; color: #1E3A8A; margin-top: 15px; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# App Header & Branding
st.markdown("<div class='main-title'>🫀 Acute Decompensated Heart Failure & Renal Follow-up Engine</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Local Protocol Guidelines & Decision Support Tool - Integrated Cardiorenal Syndrome Hub</div>", unsafe_allow_html=True)

# Professional Badge (The Everlasting Agreement)
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Clinical Project Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Core Framework:</strong> ESC/ACC Heart Failure Guidelines adapted to Local Resource Optimization & Board Review Criteria
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Layout Configuration: Split Screen
col_input, col_output = st.columns([1.1, 1.2])

# ==============================================================================
# LEFT COLUMN: Patient Clinical Status & Fluid/Renal Inputs
# ==============================================================================
with col_input:
    st.markdown("<div class='section-header'>🩺 1. Baseline Characteristics & Demographics</div>", unsafe_allow_html=True)
    with st.expander("👤 Demographics & Status", expanded=True):
        weight = st.number_input("Current Patient Weight (kg):", min_value=30, max_value=200, value=80, key="hf_weight")
        age = st.number_input("Age (Years):", min_value=18, max_value=100, value=65, key="hf_age")
        gender = st.radio("Gender:", ("Male", "Female"))

    st.markdown("<div class='section-header'>🌊 2. Hemodynamic & Congestion Profile</div>", unsafe_allow_html=True)
    with st.expander("🫁 Clinical Presentation", expanded=True):
        perfusion = st.radio("Peripheral Perfusion Status (Warm vs. Cold):", ("Warm (Well Perfused)", "Cold (Hypoperfused / Shock Signs)"))
        congestion = st.radio("Pulmonary/Systemic Congestion (Wet vs. Dry):", ("Wet (Crackles, JVD, Edema present)", "Dry (No signs of fluid overload)"))
        sbp = st.number_input("Systolic Blood Pressure (mmHg):", min_value=60, max_value=220, value=130)
        home_lasix = st.number_input("Patient's Chronic Home Oral Lasix Dose (mg/day):", min_value=0, max_value=250, value=40, step=20)

    st.markdown("<div class='section-header'>🧪 3. Renal Lab Panel & Strict 24h Fluid Log</div>", unsafe_allow_html=True)
    with st.expander("🔋 Labs & Strict I/O Balance", expanded=True):
        creatinine = st.number_input("Current Serum Creatinine (mg/dL):", min_value=0.3, max_value=12.0, value=1.4, step=0.1)
        baseline_creat = st.number_input("Baseline/Admission Creatinine (mg/dL):", min_value=0.3, max_value=12.0, value=1.0, step=0.1)
        potassium = st.number_input("Serum Potassium (mEq/L):", min_value=2.0, max_value=7.5, value=4.2, step=0.1)
        
        st.markdown("**Strict 24-Hour Fluid Balance Tracker:**")
        fluid_in = st.number_input("Total Intake (IV Meds, Oral Fluids, Flushes) - mL:", min_value=0, max_value=10000, value=1000, step=100)
        fluid_out = st.number_input("Total Output (Urine Volume, emesis, etc.) - mL:", min_value=0, max_value=10000, value=2500, step=100)
        urine_sodium = st.number_input("Spot Urinary Sodium (mEq/L) [If ordered for resistance check]:", min_value=0, max_value=150, value=45)

# ==============================================================================
# RIGHT COLUMN: Clinical Decision Algorithms, Fluid Status & Board Challenges
# ==============================================================================
with col_output:
    st.markdown("<div class='section-header'>🎯 4. Diagnostic Profiling & Kidney Calculations</div>", unsafe_allow_html=True)
    
    # 1. GFR Calculation using Cockcroft-Gault for bedside drug adjustments
    if gender == "Male":
        gfr = ((140 - age) * weight) / (72 * creatinine)
    else:
        gfr = (((140 - age) * weight) / (72 * creatinine)) * 0.85
        
    # 2. AKI Staging according to KDIGO
    creat_ratio = creatinine / baseline_creat
    aki_stage = "No AKI Criteria Met"
    if creat_ratio >= 3.0 or creatinine >= 4.0:
        aki_stage = "KDIGO Stage 3 AKI"
    elif 2.0 <= creat_ratio <= 2.9:
        aki_stage = "KDIGO Stage 2 AKI"
    elif (creat_ratio >= 1.5) or (creatinine - baseline_creat >= 0.3):
        aki_stage = "KDIGO Stage 1 AKI"

    # 3. Cardiorenal Syndrome Type Classification
    crs_type = "None"
    if "Wet" in congestion and "Stage" in aki_stage:
        crs_type = "Type 1 Cardiorenal Syndrome (Acute Heart failure driving Acute Kidney Injury)"

    # Display Hemodynamic Quadrant
    if "Warm" in perfusion and "Wet" in congestion:
        st.error("🚨 **Hemodynamic Profile: WARM & WET (Classic Congestive HF)**")
    elif "Cold" in perfusion and "Wet" in congestion:
        st.error("💥 **Hemodynamic Profile: COLD & WET (Cardiogenic Shock Pathophysiology!)**")
    elif "Warm" in perfusion and "Dry" in congestion:
        st.success("🟢 **Hemodynamic Profile: WARM & DRY (Compensated)**")
    elif "Cold" in perfusion and "Dry" in congestion:
        st.warning("⚠️ **Hemodynamic Profile: COLD & DRY (Hypovolemic / Low Output)**")

    # Metrics Layout
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.metric(label="Calculated Bedside GFR:", value=f"{gfr:.1f} mL/min")
    with col_m2:
        st.metric(label="Renal Injury Status:", value=aki_stage, delta="Watch Renal Perfusion" if "Stage" in aki_stage else "Stable")

    if crs_type != "None":
        st.info(f"🧬 **Cardiorenal Classification:** {crs_type}")

    # ------------------------------------------------------------------
    # LOCAL HOSPITAL PHARMACOPOEIA PROTOCOLS (ADHF & DIURETICS)
    # ------------------------------------------------------------------
    st.markdown("---")
    st.markdown("<div class='section-header'>💊 5. Interactive Guideline & Local Protocol Directives</div>", unsafe_allow_html=True)
    
    st.write("#### **Phase 1: Intravenous Diuretic Initialization**")
    if "Wet" in congestion:
        if home_lasix == 0:
            initial_lasix = 40
        else:
            initial_lasix = home_lasix * 2
        st.success(f"💉 **IV Lasix Target Dose:** Administer **{initial_lasix} mg IV Bolus** immediately (1-2x the home dose according to local Al-Ahli protocol).")
    else:
        st.write("Patient is clinically dry. High dose IV Loop diuretics are not indicated at this moment.")

    # Diuretic Resistance Assessment
    st.write("#### **Phase 2: Diuretic Resistance & Response Monitor**")
    net_balance = fluid_in - fluid_out
    
    st.markdown(f"""
    <div style="background-color: #F9FAFB; padding: 15px; border-radius: 8px; border-left: 5px solid #10B981; margin-bottom: 15px;">
        <p style="color: #1F2937 !important; font-weight: bold; margin-bottom: 5px;">24-Hour Net Fluid Status:</p>
        <ul style="color: #374151 !important; margin-left: 20px; font-size: 14px;">
            <li><strong>Net Balance:</strong> {net_balance} mL (Goal is negative balance for overloaded patients).</li>
            <li><strong>Spot Urinary Sodium Status:</strong> {urine_sodium} mEq/L.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    if "Wet" in congestion and fluid_out < 1200 and urine_sodium < 100:
        st.markdown(f"""
        <div style="background-color: #FEF2F2; padding: 18px; border-radius: 8px; border-left: 6px solid #EF4444;">
            <strong style="color: #991B1B !important;">⚠️ DIURETIC RESISTANCE DETECTED!</strong><br>
            <span style="color: #1F2937 !important; font-size: 14px;">Urine output is suboptimal and spot urinary Na is &lt; 100 mEq/L. Execute <strong>Sequential Nephron Blockade Protocol</strong>:</span>
            <ul style="color: #1F2937 !important; font-size: 14px; margin-left: 20px; margin-top: 5px;">
                <li><strong>Local Action:</strong> Double the IV Lasix dose to maximum capacity OR add <strong>Hydrochlorothiazide (25-50 mg PO)</strong> or Metolazone if available 30 minutes prior to the IV loop diuretic.</li>
                <li><strong>Safety Check:</strong> Closely monitor serum Potassium. Current K+ is <strong>{potassium} mEq/L</strong>.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # ------------------------------------------------------------------
    # DYNAMIC INTERACTIVE BOARD MCQ GENERATOR (ADHF & RENAL HUB)
    # ------------------------------------------------------------------
    st.markdown("---")
    st.markdown("<div class='section-header'>📚 6. High-Yield Cardiorenal Board Review Challenge</div>", unsafe_allow_html=True)
    
    cardio_pool = [
        {
            "id": 1,
            "case": "A 72-year-old male with severe ischemic cardiomyopathy presents with severe orthopnea and massive peripheral edema. Vital signs reveal SBP 145 mmHg. Baseline Creatinine was 1.1 mg/dL 3 months ago; today it is 1.9 mg/dL. He takes Lasix 40 mg PO daily at home. The resident decides to hold diuretics due to the fear of worsening the acute kidney injury.",
            "question": "What is the most appropriate next step in the clinical management of this patient?",
            "options": ["A) Maintain the hold on diuretics and give a 250 mL Normal Saline fluid challenge", "B) Administer IV Regular Insulin and Dextrose immediately to shield the kidneys", "C) Initiate aggressive intravenous loop diuretic therapy (e.g., IV Lasix 80 mg bolus)", "D) Prepare the patient for urgent renal replacement therapy (Dialysis)"],
            "correct": "C) Initiate aggressive intravenous loop diuretic therapy (e.g., IV Lasix 80 mg bolus)",
            "explanation": "This patient is suffering from Type 1 Cardiorenal Syndrome. The rise in creatinine is driven by severe renal venous congestion (back-pressure from heart failure) rather than true hypovolemia. Decreasing congestion via intravenous loop diuretics restores proper renal perfusion pressure, which often improves or stabilizes renal function."
        },
        {
            "id": 2,
            "case": "A 66-year-old female is admitted for acute decompensated heart failure. Despite receiving IV Furosemide 120 mg twice daily, her 6-hour urine output is only 150 mL, and a spot urinary sodium is measured at 55 mEq/L.",
            "question": "Which of the following pharmacological strategies is recommended next under local guidelines to break this loop diuretic resistance?",
            "options": ["A) Stop all loop diuretics entirely and switch to oral Spironolactone 100 mg", "B) Implement Sequential Nephron Blockade by adding a Thiazide or Thiazide-like diuretic", "C) Administer a rapid infusion of 20% Mannitol over 15 minutes", "D) Start an immediate continuous infusion of high-dose Norepinephrine"],
            "correct": "B) Implement Sequential Nephron Blockade by adding a Thiazide or Thiazide-like diuretic",
            "explanation": "Diuretic resistance is manifested by a spot urinary sodium < 100 mEq/L following loop diuretic administration. Adding a Thiazide diuretic (Sequential Nephron Blockade) shuts down the compensatory sodium reabsorption taking place in the distal convoluted tubule, restoring diuretic efficacy."
        }
    ]

    if 'hf_q' not in st.session_state:
        st.session_state.hf_q = random.choice(cardio_pool)
        
    if st.button("🔄 Generate Another Cardiorenal Board Question"):
        st.session_state.hf_q = random.choice(cardio_pool)
        
    current_hf_q = st.session_state.hf_q
    
    st.warning(f"**Clinical Scenario:** {current_hf_q['case']}")
    st.write(f"❓ **Question:** {current_hf_q['question']}")
    
    user_ans_hf = st.radio("Select your answer from below:", current_hf_q['options'], key=f"hf_q_{current_hf_q['id']}")
    
    if st.expander("🔑 Reveal Correct Answer & Dr. Ihab's Clinical Explanation"):
        if user_ans_hf == current_hf_q['correct']:
            st.success(f"🎯 **Correct!** The answer is {current_hf_q['correct']}")
        else:
            st.error(f"❌ **Incorrect Choice.** The correct answer is {current_hf_q['correct']}")
        st.markdown(f"**Explanation:** {current_hf_q['explanation']}")

# Footer Signature (The Unshakable Standard)
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 12px;'>Al-Ahli Hospital Cardiorenal Center App © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
