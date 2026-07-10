import streamlit as st
import math

# Page Configuration for a clean, professional medical look
st.set_page_config(
    page_title="Al-Ahli Inpatient Fluid & Kinetic GFR Tracker",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling to match your high clinical standards
st.markdown("""
    <style>
    .main-title { font-size:30px !important; font-weight: bold; color: #1E3A8A; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:15px !important; color: #4B5563; text-align: center; margin-bottom: 25px; font-style: italic; }
    .branding-bar { background-color: #EFF6FF; padding: 20px; border-radius: 10px; border-left: 6px solid #1E3A8A; margin-bottom: 25px; }
    .branding-bar strong { color: #1E3A8A !important; font-weight: bold; }
    .branding-text { color: #1F2937 !important; font-size: 15px !important; line-height: 1.6; }
    .section-header { font-size:20px !important; font-weight: bold; color: #1E3A8A; margin-top: 15px; margin-bottom: 15px; border-bottom: 2px solid #E5E7EB; padding-bottom: 5px; }
    .status-box { background-color: #F9FAFB; padding: 15px; border-radius: 8px; border: 1px solid #E5E7EB; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# App Header & Signature
st.markdown("<div class='main-title'>🧪 Al-Ahli Hospital Inpatient Fluid & Kinetic GFR Tracker</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Advanced Inpatient Decision Support System (CDSS) for Dynamic AKI & Fluid Stewardship</div>", unsafe_allow_html=True)

st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Project Founder & Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Clinical Core:</strong> Kinetic GFR (kGFR) Chen Equation, Dynamic Fluid Balance with Insensible Loss Integration
    </div>
</div>
""", unsafe_allow_html=True)

# Main Grid Split - Fixed variable names here
col_input, col_protocol = st.columns([1, 1.2])

# ==============================================================================
# LEFT COLUMN: INPUT PARAMETERS (Vitals, Fluids, Sequential Creatinines)
# ==============================================================================
with col_input:
    st.markdown("<div class='section-header'>📋 1. Patient Parameters & Baseline</div>", unsafe_allow_html=True)
    
    # Baseline Demographics
    p_weight = st.number_input("Patient Weight (kg):", min_value=30.0, max_value=250.0, value=75.0, step=0.5)
    p_age = st.number_input("Age (Years):", min_value=18, max_value=110, value=65)
    p_sex = st.radio("Gender:", ("Male", "Female"))
    p_temp = st.number_input("Maximum Body Temperature (°C):", min_value=35.0, max_value=43.0, value=37.0, step=0.1)

    st.markdown("<div class='section-header'>💧 2. 24-Hour Fluid Stewardship Input</div>", unsafe_allow_html=True)
    
    # Fluid Intakes
    st.subheader("A) Total Intake")
    iv_fluids = st.number_input("IV Fluids / Medications / Blood Products (mL/24h):", min_value=0, max_value=10000, value=1500, step=50)
    oral_intake = st.number_input("Oral Intake / NG Feed (mL/24h):", min_value=0, max_value=10000, value=500, step=50)
    
    # Fluid Outputs
    st.subheader("B) Total Output")
    urine_output = st.number_input("Total Urine Output (mL/24h):", min_value=0, max_value=12000, value=1200, step=50)
    other_output = st.number_input("Gastrointestinal / Drains / Vomiting (mL/24h):", min_value=0, max_value=5000, value=0, step=50)

    st.markdown("<div class='section-header'>📈 3. Kinetic GFR Tracker (Sequential Creatinines)</div>", unsafe_allow_html=True)
    
    # Time-variant creatinine inputs
    cr_baseline = st.number_input("Patient Baseline Creatinine (mg/dL) [Steady State]:", min_value=0.3, max_value=12.0, value=1.2, step=0.1)
    cr_initial = st.number_input("Initial Creatinine (mg/dL) [e.g., Yesterday]:", min_value=0.3, max_value=12.0, value=2.1, step=0.1)
    cr_current = st.number_input("Current Creatinine (mg/dL) [e.g., Today]:", min_value=0.3, max_value=12.0, value=2.6, step=0.1)
    time_delta = st.number_input("Time Interval Between Initial & Current Creatinine (Hours):", min_value=4, max_value=72, value=24, step=1)

    # ==========================================================================
    # AUTOMATED MATHEMATICAL RUNTIME ENGINES
    # ==========================================================================
    # 1. Kinetic GFR (kGFR) Engine using Chen Equation
    gender_factor = 0.85 if p_sex == "Female" else 1.0
    baseline_crcl = ((140 - p_age) * p_weight) / (72 * cr_baseline) * gender_factor
    
    delta_cr = cr_current - cr_initial
    mean_cr = (cr_initial + cr_current) / 2
    
    kgfr_multiplier = 1 - ((24 * delta_cr) / (time_delta * (mean_cr * 1.5)))
    kgfr = baseline_crcl * (cr_baseline / mean_cr) * max(0.0, kgfr_multiplier)
    
    # 2. Advanced Fluid Balance Calculations (Integrating Insensible Losses & Fever)
    fever_degree = max(0.0, p_temp - 37.0)
    base_insensible = p_weight * 11.0
    fever_insensible = base_insensible * (0.12 * fever_degree)
    total_insensible_loss = base_insensible + fever_insensible
    
    total_intake = iv_fluids + oral_intake
    total_measured_output = urine_output + other_output
    net_fluid_balance = total_intake - (total_measured_output + total_insensible_loss)

    st.markdown("---")
    st.markdown("<div class='section-header'>📊 Automated Calculations</div>", unsafe_allow_html=True)
    st.metric("Dynamic Kinetic GFR", f"{kgfr:.1f} mL/min")
    st.metric("Net Daily Fluid Balance", f"{net_fluid_balance:+.0f} mL")

# ==============================================================================
# RIGHT COLUMN: REAL-TIME CLINICAL DECISION SUPPORT DASHBOARD
# ==============================================================================
with col_protocol:
    st.markdown("<div class='section-header'>⚡ Real-Time Clinical Decision Support Dashboard</div>", unsafe_allow_html=True)
    
    # TABS FOR ANALYTICS
    tab_kgfr, tab_fluid = st.tabs(["🧬 Dynamic Kinetic GFR Analytics", "🌊 Fluid Stewardship & Diuretic Control"])
    
    with tab_kgfr:
        st.markdown("### 🔍 Kinetic vs. Steady-State Clearance Analytics")
        
        static_crcl = ((140 - p_age) * p_weight) / (72 * cr_current) * gender_factor
        
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.metric("Kinetic GFR (kGFR - Dynamic)", f"{kgfr:.1f} mL/min", 
                      delta=f"{kgfr - static_crcl:.1f} vs Static" if (kgfr-static_crcl) != 0 else None,
                      delta_color="normal")
        with col_m2:
            st.metric("Standard Static CrCl (Today's Cr)", f"{static_crcl:.1f} mL/min")
            
        st.markdown("<div class='status-box'>", unsafe_allow_html=True)
        if cr_current > cr_initial:
            st.error("🚨 **ALERT: Active / Worsening Acute Kidney Injury (AKI)**")
            st.markdown(f"""
            * **Pathophysiology:** Creatinine is currently in an upward trajectory. Standard static clearance equations **overestimate** the patient's actual renal function right now.
            * **Dosing Safety:** Your **True kGFR ({kgfr:.1f} mL/min)** is lower than standard calculations. You must adjust critical ward medications (e.g., *Meropenem, Piperacillin/Tazobactam, Low-Molecular-Weight Heparin*) based on the **kGFR** to avoid severe drug toxicities.
            """)
        elif cr_current < cr_initial:
            st.success("🟢 **NOTICE: Renal Function is Recovering**")
            st.markdown(f"""
            * **Pathophysiology:** Creatinine is down-trending. Static equations **underestimate** current clearance.
            * **Dosing Safety:** The **True kGFR ({kgfr:.1f} mL/min)** indicates that the kidneys are clearing drugs better than today's absolute creatinine suggests. Avoid under-dosing vital antibiotics.
            """)
        else:
            st.info("⚪ **Renal Function is Currently in a Steady State**")
            st.write("The kinetic GFR matches standard static calculations. Maintain standard renal dosing protocols.")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("### 💊 Adjusted Ward Drug Dosing Map (Based on kGFR)")
        if kgfr < 15:
            st.markdown("* **Piperacillin/Tazobactam:** Max 2.25 g IV q6h or 3.375 g IV q8h.\n* **Meropenem:** 500 mg IV q24h.\n* **Enoxaparin (Therapeutic):** Avoid completely. Use Unfractionated Heparin.")
        elif 15 <= kgfr < 30:
            st.markdown("* **Piperacillin/Tazobactam:** 2.25 g IV q6h.\n* **Meropenem:** 500 mg IV q12h.\n* **Enoxaparin (Prophylactic):** Reduce to 30 mg SC once daily.")
        elif 30 <= kgfr < 50:
            st.markdown("* **Piperacillin/Tazobactam:** 3.375 g IV q6h.\n* **Meropenem:** 1 g IV q12h.\n* **Enoxaparin (Therapeutic):** Reduce dose to 1 mg/kg SC once daily.")
        else:
            st.markdown("🟢 **Normal Range Dosing:** Clearance is stable enough for standard empiric dosing.")

    with tab_fluid:
        st.markdown("### 🌊 Fluid Compartment Balance & Stewardship")
        
        col_f1, col_f2, col_f3 = st.columns(3)
        with col_f1:
            st.metric("Total Intake", f"{total_intake} mL")
        with col_f2:
            st.metric("Insensible Loss (Calc.)", f"{total_insensible_loss:.0f} mL")
        with col_f3:
            st.metric("Net Daily Fluid Balance", f"{net_fluid_balance:+.0f} mL")
            
        st.markdown("<div class='status-box'>", unsafe_allow_html=True)
        hourly_urine_output = urine_output / (p_weight * 24)
        st.write(f"📊 **Calculated Urine Output:** `{hourly_urine_output:.2f} mL/kg/hour`")
        
        if hourly_urine_output < 0.5:
            st.error("🚨 **CRITICAL: Patient meets KDIGO Oliguria Criteria ($< 0.5\\ mL/kg/h$)!**")
        
        if net_fluid_balance > 500:
            st.error("⚠️ **Significant Positive Fluid Accumulation:**")
            st.markdown(f"""
            * **Clinical Evaluation:** High risk for **Fluid Overload / Pulmonary Congestion**, especially dangerous in AKI/CKD with low kGFR.
            * **Stewardship Action:** Consider initiating or intensifying **IV Furosemide Loop Diuretics** (e.g., 40 mg to 80 mg IV bolus) and minimize maintenance IV fluid rates immediately.
            """)
        elif net_fluid_balance < -500:
            st.warning("🍂 **Significant Negative Fluid Balance (Dehydration Risk):**")
            st.markdown(f"""
            * **Clinical Evaluation:** Patient is in a deficit. If the dynamic **kGFR** is dropping simultaneously, this AKI could be **Pre-renal** secondary to intravascular volume depletion.
            * **Stewardship Action:** Assess perfusion markers. Consider gentle volume resuscitation or decreasing diuretic dosages.
            """)
        else:
            st.success("🟢 **Fluid Balance Optimized:** The patient is within a safe net-neutral fluid homeostasis zone.")
        st.markdown("</div>", unsafe_allow_html=True)

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 11px;'>Al-Ahli Hospital Internal Medicine CDSS Platforms © 2026 • Platform Design curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
