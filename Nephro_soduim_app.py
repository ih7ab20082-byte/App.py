import streamlit as st
import random

# Page Configuration
st.set_page_config(
    page_title="Al-Ahli Nephrology & Sodium Management Center",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Medical Theme and Styling
st.markdown("""
    <style>
    .main-title { font-size:32px !important; font-weight: bold; color: #065F46; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:16px !important; color: #4B5563; text-align: center; margin-bottom: 25px; font-style: italic; }
    .branding-bar { background-color: #F0FDF4; padding: 20px; border-radius: 10px; border-left: 6px solid #059669; margin-bottom: 25px; }
    .branding-bar strong { color: #047857 !important; font-weight: bold; }
    .branding-text { color: #1F2937 !important; font-size: 16px !important; line-height: 1.6; }
    .section-header { font-size:22px !important; font-weight: bold; color: #065F46; margin-top: 15px; margin-bottom: 15px; }
    .safety-alert { background-color: #FEF2F2; padding: 18px; border-radius: 8px; border-left: 6px solid #EF4444; margin-top: 10px; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<div class='main-title'>🩸 Advanced Electrolyte & Acute Kidney Injury (AKI) Lifecycle Engine</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Precision Hyponatremia Correction, Adrogué-Madias Infusion Titrator, and KDIGO AKI Staging Platform</div>", unsafe_allow_html=True)

# Professional Credit
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Clinical Project Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Core Engine:</strong> Safe Sodium Correction Protocols & Kinetic Renal Function Tracking Matrix
    </div>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🔍 Phase 1: Hyponatremia Diagnostic Matrix", 
    "🧪 Phase 2: Precision Sodium Correction Calculator", 
    "📟 Phase 3: AKI Staging & Fluid Balance Tracker",
    "📚 Phase 4: Nephrology Board Review Challenge"
])

# ==============================================================================
# TAB 1: DIAGNOSTIC
# ==============================================================================
with tab1:
    col_in1, col_out1 = st.columns([1.1, 1.2])
    with col_in1:
        st.markdown("<div class='section-header'>🧪 Baseline Chemistry Inputs</div>", unsafe_allow_html=True)
        serum_na = st.number_input("Serum Sodium (mEq/L):", 100, 180, 118)
        serum_osmo = st.selectbox("Serum Osmolality Status:", ["Hypotonic (< 275 mOsm/kg)", "Isotonic", "Hypertonic (> 295 mOsm/kg)"])
        vol_status = st.radio("Patient Volume Status:", ("Hypovolemic", "Euvolemic", "Hypervolemic"))
        urine_na = st.number_input("Urine Sodium (mEq/L):", 5, 150, 42)
        urine_osmo = st.number_input("Urine Osmolality (mOsm/kg):", 50, 1200, 350)
    
    with col_out1:
        st.markdown("<div class='section-header'>🧠 Diagnostic Synthesis</div>", unsafe_allow_html=True)
        if "Hypotonic" in serum_osmo:
            if "Hypovolemic" in vol_status:
                st.write("Diagnosis: Extra-renal Volume Depletion (GI losses) if Urine Na < 20, or Salt Wasting if Urine Na > 20.")
            elif "Euvolemic" in vol_status:
                st.write("Diagnosis: SIADH if Urine Osmo > 100, or Polydipsia if Urine Osmo < 100.")
            else:
                st.write("Diagnosis: Hypervolemic (CHF/Cirrhosis) - Dilutional Hyponatremia.")

# ==============================================================================
# TAB 2: SODIUM CALCULATOR (THE WEIGHT FIX)
# ==============================================================================
with tab2:
    st.markdown("<div class='section-header'>🧪 Adrogué-Madias Calculation Panel</div>", unsafe_allow_html=True)
    col_calc_in, col_calc_out = st.columns([1.1, 1.2])
    with col_calc_in:
        weight = st.number_input("Patient Weight (kg):", 30.0, 200.0, 70.0) # الوزن الذي سبب الخطأ
        pt_gender = st.radio("Sex:", ("Male", "Female"))
        current_na = st.number_input("Current Sodium (mEq/L):", 100, 150, 115)
        target_na_24h = st.number_input("Target Sodium in 24h:", 105, 160, 123)
        infusate_na = st.selectbox("Infusate Na Concentration:", [513, 154, 130], format_func=lambda x: f"{x} mEq/L")
    
    with col_calc_out:
        factor = 0.6 if pt_gender == "Male" else 0.5
        tbw = weight * factor
        delta_na = (infusate_na - current_na) / (tbw + 1)
        st.write(f"Predicted Sodium rise per 1L: {delta_na:.2f} mEq/L")
        if (target_na_24h - current_na) > 8:
            st.markdown("<div class='safety-alert'>🚨 Danger: Over-correction risk (>8 mEq/L/24h)!</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 3: AKI TRACKER
# ==============================================================================
with tab3:
    st.markdown("<div class='section-header'>📟 AKI & Fluid Balance</div>", unsafe_allow_html=True)
    baseline_scr = st.number_input("Baseline Cr (mg/dL):", 0.3, 15.0, 1.0)
    current_scr = st.number_input("Current Cr (mg/dL):", 0.3, 15.0, 2.4)
    weight_val = st.number_input("Weight (kg):", 30.0, 200.0, 70.0, key="aki_weight")
    daily_intake = st.number_input("Daily Intake (mL):", 0, 10000, 3000)
    daily_output = st.number_input("Daily Output (mL):", 0, 10000, 500)
    
    if st.button("Calculate Staging"):
        ratio = current_scr / baseline_scr
        st.write(f"Stage: {'Stage 3' if ratio >= 3.0 else 'Stage 2' if ratio >= 2.0 else 'Stage 1' if ratio >= 1.5 else 'No AKI'}")
        st.write(f"Net Balance: {daily_intake - daily_output} mL")

# ==============================================================================
# TAB 4: BOARD REVIEW
# ==============================================================================
with tab4:
    st.markdown("<div class='section-header'>📚 Nephrology Board Review</div>", unsafe_allow_html=True)
    st.info("Q: What is the risk of rapid Na correction? A: Osmotic Demyelination Syndrome.")

# Footer
st.markdown("---")
st.markdown("Al-Ahli Hospital Nephrology App © 2026 • Curated by Dr. Ihab Abbass Abu Hilail")
