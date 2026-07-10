import streamlit as st
import random

# Page Configuration
st.set_page_config(
    page_title="Al-Ahli Hospital DKA Command Center",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Branding and Signature Style
st.markdown("""
    <style>
    .main-title { font-size:32px !important; font-weight: bold; color: #1E3A8A; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:16px !important; color: #4B5563; text-align: center; margin-bottom: 25px; font-style: italic; }
    .branding-bar { background-color: #F3F4F6; padding: 20px; border-radius: 10px; border-left: 6px solid #10B981; margin-bottom: 25px; }
    .branding-bar strong { color: #065F46 !important; font-weight: bold; }
    .branding-text { color: #1F2937 !important; font-size: 16px !important; line-height: 1.6; }
    .section-header { font-size:22px !important; font-weight: bold; color: #065F46; margin-top: 15px; margin-bottom: 15px; }
    .critical-box { background-color: #FEF2F2; padding: 15px; border-radius: 8px; border-left: 5px solid #EF4444; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# App Header & Branding
st.markdown("<div class='main-title'>🩸 Al-Ahli Hospital Diabetic Ketoacidosis (DKA) Protocol</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Advanced Interactive Decision Support & Fluid Resuscitation Engine - ADA Guidelines</div>", unsafe_allow_html=True)

# Professional Badge
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Clinical Project Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Core Framework:</strong> American Diabetes Association (ADA) Hyperglycemic Crises Protocol
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Layout Configuration: Split Screen
col_input, col_output = st.columns([1.1, 1.2])

# ==============================================================================
# LEFT COLUMN: Patient Metrics, Fluid/Electrolyte Inputs
# ==============================================================================
with col_input:
    st.markdown("<div class='section-header'>🧪 1. Patient Presentation & Initial Labs</div>", unsafe_allow_html=True)
    
    with st.expander("👤 Patient Demographics", expanded=True):
        weight = st.number_input("Patient Actual Weight (kg):", min_value=30, max_value=200, value=70, key="dka_weight")
        age = st.number_input("Age (Years):", min_value=14, max_value=100, value=45, key="dka_age")

    with st.expander("🩸 Hyperglycemia & Acid-Base Metrics", expanded=True):
        glucose = st.number_input("Serum Glucose (mg/dL):", min_value=50, max_value=1500, value=450)
        ph = st.number_input("Arterial/Venous pH:", min_value=6.50, max_value=7.60, value=7.15, step=0.01)
        hco3 = st.number_input("Serum Bicarbonate (mEq/L):", min_value=1.0, max_value=40.0, value=12.0, step=0.5)
        ketones = st.radio("Urinary / Serum Ketones Status:", ("Positive / Elevated", "Negative / Trace"))

    st.markdown("---")
    st.markdown("<div class='section-header'>🧬 2. Electrolyte Profiles & Status</div>", unsafe_allow_html=True)
    with st.expander("🔋 Core Ions Assessment", expanded=True):
        sodium = st.number_input("Measured Serum Sodium (mEq/L):", min_value=100, max_value=170, value=132)
        potassium = st.number_input("Serum Potassium (mEq/L):", min_value=1.5, max_value=8.0, value=3.0, step=0.1)
        chloride = st.number_input("Serum Chloride (mEq/L):", min_value=70, max_value=140, value=98)

    st.markdown("---")
    st.markdown("<div class='section-header'>💉 3. Ongoing Treatment Status</div>", unsafe_allow_html=True)
    insulin_status = st.radio(
        "Current Insulin Infusion Administration Stage:",
        ("Not Started / Initial Phase", "Infusion ongoing - Glucose dropped < 250 mg/dL")
    )

# ==============================================================================
# RIGHT COLUMN: ADA Staging, Calculations, Safeguards & Questions
# ==============================================================================
with col_output:
    st.markdown("<div class='section-header'>🎯 4. ADA Staging & Diagnostic Calculations</div>", unsafe_allow_html=True)
    
    # 1. Anion Gap Calculation
    anion_gap = sodium - (chloride + hco3)
    
    # 2. Corrected Sodium Calculation
    corrected_sodium = sodium + (0.016 * (glucose - 100))
    
    # ADA Staging Logic
    dka_severity = "No DKA Criteria Met"
    is_dka = False
    
    if ketones == "Positive / Elevated" and glucose > 250:
        if ph < 7.00 or hco3 < 10.0 or anion_gap > 12:
            dka_severity = "SEVERE DKA"
            is_dka = True
        elif 7.00 <= ph <= 7.24 or 10.0 <= hco3 < 15.0:
            dka_severity = "MODERATE DKA"
            is_dka = True
        elif 7.25 <= ph <= 7.30 or 15.0 <= hco3 <= 18.0:
            dka_severity = "MILD DKA"
            is_dka = True

    if not is_dka:
        st.success("🟢 **Diagnostic Status: Patient does not explicitly fulfill ADA DKA criteria.**")
    else:
        if "MILD" in dka_severity: st.warning(f"⚠️ **ADA Classification: {dka_severity}**")
        elif "MODERATE" in dka_severity: st.error(f"🚨 **ADA Classification: {dka_severity}**")
        elif "SEVERE" in dka_severity: st.error(f"💥 **CRITICAL ADMISSION MANDATE: {dka_severity} (High ICU Shift Requirement!)**")

    # Metrics Display
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.metric(label="Calculated Anion Gap:", value=f"{anion_gap:.1f} mEq/L", delta="> 12 (Elevated)" if anion_gap > 12 else "Normal")
    with col_m2:
        st.metric(label="Corrected Sodium (for Hyperglycemia):", value=f"{corrected_sodium:.1f} mEq/L")

    # ------------------------------------------------------------------
    # FLUID RESUSCITATION ENGINE
    # ------------------------------------------------------------------
    st.markdown("---")
    st.markdown("<div class='section-header'>💧 5. Fluid Resuscitation & Infusion Fluids Blueprint</div>", unsafe_allow_html=True)
    
    st.write("#### **Phase 1: Emergent Volume expansion**")
    st.info(f"💉 Give **0.9% Normal Saline (NaCl):** Infuse 1000 - 1500 mL IV over the 1st hour to restore intravascular volume.")
    
    st.write("#### **Phase 2: Maintenance Hydration (Based on Corrected Sodium)**")
    if corrected_sodium < 135:
        st.success(f"🔹 **Hydration Choice:** Corrected Na is Low ({corrected_sodium:.1f}). Continue **0.9% Normal Saline** at 250 - 500 mL/hr (based on hydration status).")
    else:
        st.warning(f"🔸 **Hydration Choice:** Corrected Na is High/Normal ({corrected_sodium:.1f}). Switch to **0.45% Half-Normal Saline** at 250 - 500 mL/hr to safeguard against intracellular dehydration.")

    if "dropped < 250" in list(insulin_status):
        st.error("🔄 **CRITICAL FLUID SWITCH:** Glucose is < 250 mg/dL! **Add 5% Dextrose (D5 1/2 NS or D5 NS)** immediately to prevent hypoglycemia and allow continued insulin infusion to close the anion gap.")

    # ------------------------------------------------------------------
    # INSULIN & POTASSIUM SAFEGUARDS (FIXED CONTRAST & FULL DOSING PROTOCOL)
    # ------------------------------------------------------------------
    st.markdown("---")
    st.markdown("<div class='section-header'>🛑 6. Potassium Safeguards & Insulin Dosing</div>", unsafe_allow_html=True)
    
    if potassium < 3.3:
        st.markdown(f"""
        <div style="background-color: #FEF2F2; padding: 20px; border-radius: 8px; border-left: 6px solid #EF4444; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
            <p style="color: #991B1B !important; font-weight: bold; margin-bottom: 10px; font-size: 18px; display: flex; align-items: center;">
                🚫 ABSOLUTE INSULIN CONTRAINDICATION ACTIVE!
            </p>
            <p style="color: #1F2937 !important; font-size: 15px; margin-bottom: 8px; font-weight: bold;">
                Serum Potassium is critically low (<strong>{potassium} mEq/L</strong>).
            </p>
            <hr style="border: 0; border-top: 1px solid #FCA5A5; margin: 10px 0;">
            <ul style="color: #1F2937 !important; font-size: 14px; margin-left: 20px; line-height: 1.6; list-style-type: square;">
                <li style="color: #1F2937 !important; margin-bottom: 8px;">
                    <strong style="color: #B91C1C !important;">HOLD ALL INSULIN:</strong> Administering insulin now will drive K+ intracellularly, risking acute cardiovascular collapse and fatal cardiac arrhythmias (V-Fib).
                </li>
                <li style="color: #1F2937 !important; margin-bottom: 8px;">
                    <strong style="color: #065F46 !important;">CRITICAL K+ REPLACEMENT DOSING:</strong> Infuse <strong>20 - 30 mEq of Potassium Chloride (KCl) per hour IV</strong> (preferably via central line if >20 mEq/h, or split in peripheral lines) until serum K+ is corrected.
                </li>
                <li style="color: #1F2937 !important; margin-bottom: 5px;">
                    <strong style="color: #1E3A8A !important;">RECHECK WINDOW:</strong> Repeat serum potassium <strong>every 1 hour</strong>. Do NOT initiate the regular insulin infusion until potassium is strictly <strong>&ge; 3.3 mEq/L</strong>.
                </li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    elif 3.3 <= potassium <= 5.2:
        st.success(f"🟢 **Safe to Administer Insulin:** Serum Potassium is {potassium} mEq/L.")
        st.write(f"💉 **Insulin Infusion (Regular):** Give **0.1 units/kg/hr** continuous infusion (**{weight*0.1:.1f} units/hr**).")
        st.info(f"🔋 **Concomitant K+ Replacement:** Add **20-30 mEq of K+ to each liter of IV fluids** to maintain serum potassium between 4.0 and 5.0 mEq/L.")
    else:
        st.error(f"⚠️ **Hyperkalemia Detected ({potassium} mEq/L):** Hold potassium replacement. Start insulin infusion at 0.1 units/kg/hr. Recheck K+ every 2 hours.")

    # ------------------------------------------------------------------
    # DYNAMIC INTERACTIVE BOARD MCQ GENERATOR (DKA HUB)
    # ------------------------------------------------------------------
    st.markdown("---")
    st.markdown("<div class='section-header'>📚 7. Dynamic Board Review Challenge (DKA Specialist Hub)</div>", unsafe_allow_html=True)
    
    dka_pool = [
        {
            "id": 1,
            "case": "A 24-year-old female presents with DKA. Initial labs: Glucose 420 mg/dL, pH 7.12, Serum Potassium 3.1 mEq/L, Anion Gap 22. The medical resident is preparing to hang a regular insulin infusion.",
            "question": "What is the most appropriate next step in the management of this patient?",
            "options": ["A) Start regular insulin infusion at 0.1 units/kg/hr immediately", "B) Give 50 mEq of IV Sodium Bicarbonate push", "C) Hold insulin, initiate aggressive IV potassium replacement first", "D) Order a brain CT to rule out cerebral edema before therapy"],
            "correct": "C) Hold insulin, initiate aggressive IV potassium replacement first",
            "explanation": "According to ADA criteria, if serum potassium is < 3.3 mEq/L, insulin MUST be held. Administering insulin triggers rapid intracellular movement of potassium, which can crash the cardiovascular system into life-threatening arrhythmias (e.g., V-Fib)."
        },
        {
            "id": 2,
            "case": "An 18-year-old male with Type 1 Diabetes is being managed for severe DKA. Over 6 hours, his plasma glucose drops from 540 mg/dL to 230 mg/dL. His venous pH has improved from 6.95 to 7.18, but the anion gap remains elevated at 18.",
            "question": "Which clinical alteration is mandatory at this juncture?",
            "options": ["A) Stop the insulin infusion and transfer to subcutaneous basal insulin", "B) Add 5% Dextrose to the intravenous fluids and continue insulin infusion", "C) Double the rate of the insulin infusion to clear the remaining ketones", "D) Discontinue all IV fluids and allow the patient to clear the gap orally"],
            "correct": "B) Add 5% Dextrose to the intravenous fluids and continue insulin infusion",
            "explanation": "The resolution of DKA is defined by closure of the anion gap (<12) and pH >7.30, NOT by normal glucose. Because glucose dropped <250 but the gap is still open, Dextrose must be added to the IV fluids. This prevents hypoglycemia while allowing continuous insulin infusion to clear the systemic ketoacids."
        },
        {
            "id": 3,
            "case": "A 35-year-old female is admitted with severe DKA. Her initial serum sodium is reported as 128 mEq/L with a concurrent serum glucose of 700 mg/dL.",
            "question": "What is her true physiological (corrected) serum sodium status, and how does it alter management?",
            "options": ["A) 128 mEq/L; treat aggressively for severe hypotonic hyponatremia", "B) 137.6 mEq/L; use 0.45% Half-Normal Saline for maintenance hydration", "C) 134.2 mEq/L; continue 0.9% Normal Saline exclusively", "D) 142.0 mEq/L; start free water administration via nasogastric tube"],
            "correct": "B) 137.6 mEq/L; use 0.45% Half-Normal Saline for maintenance hydration",
            "explanation": "The corrected sodium formula is: Measured Na + [0.016 * (Glucose - 100)]. Here: 132 + [0.016 * 600] = 137.6 mEq/L. Because the corrected sodium is normal/high (>135), ADA guidelines recommend changing maintenance fluids to 0.45% NaCl to prevent severe cellular dehydration."
        }
    ]

    if 'dka_q' not in st.session_state:
        st.session_state.dka_q = random.choice(dka_pool)
        
    if st.button("🔄 Generate Another DKA Board Question"):
        st.session_state.dka_q = random.choice(dka_pool)
        
    current_dka_q = st.session_state.dka_q
    
    st.warning(f"**Clinical Scenario:** {current_dka_q['case']}")
    st.write(f"❓ **Question:** {current_dka_q['question']}")
    
    user_ans_dka = st.radio("Select your answer from below:", current_dka_q['options'], key=f"dka_q_{current_dka_q['id']}")
    
    if st.expander("🔑 Reveal Correct Answer & Dr. Ihab's Clinical Explanation"):
        if user_ans_dka == current_dka_q['correct']:
            st.success(f"🎯 **Correct!** The answer is {current_dka_q['correct']}")
        else:
            st.error(f"❌ **Incorrect Choice.** The correct answer is {current_dka_q['correct']}")
        st.markdown(f"**Explanation:** {current_dka_q['explanation']}")

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 12px;'>Al-Ahli Hospital DKA Command Center App © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
