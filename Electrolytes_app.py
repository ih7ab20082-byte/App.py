import streamlit as st

# Page Configuration for a dedicated electrolyte tool
st.set_page_config(
    page_title="Al-Ahli Hospital Electrolyte Correction Protocol",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Medical Branding Styles
st.markdown("""
    <style>
    .main-title { font-size:32px !important; font-weight: bold; color: #1E3A8A; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:16px !important; color: #4B5563; text-align: center; margin-bottom: 25px; font-style: italic; }
    .branding-bar { background-color: #EFF6FF; padding: 20px; border-radius: 10px; border-left: 6px solid #3B82F6; margin-bottom: 25px; }
    .branding-bar strong { color: #1E3A8A !important; font-weight: bold; }
    .branding-text { color: #1F2937 !important; font-size: 16px !important; line-height: 1.6; }
    .section-header { font-size:22px !important; font-weight: bold; color: #1E3A8A; margin-top: 15px; margin-bottom: 15px; }
    .board-header { font-size:20px !important; font-weight: bold; color: #D97706; margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<div class='main-title'>🧪 Al-Ahli Hospital Electrolyte & Sodium Correction Platform</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Advanced Clinical Decision Support Tool & Dysnatremia Safety Engine</div>", unsafe_allow_html=True)

# Professional Badge
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Project Founder & Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Focus:</strong> Prevention of Osmotic Demyelination & Evidence-Based Math Modeling
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Layout Split
col_input, col_math = st.columns([1, 1.2])

# ==============================================================================
# LEFT COLUMN: Patient Metrics & Lab Inputs
# ==============================================================================
with col_input:
    st.markdown("<div class='section-header'>📋 1. Patient Profiles & Baseline Serum Labs</div>", unsafe_allow_html=True)
    
    p_age = st.number_input("Patient Age:", min_value=1, max_value=120, value=65)
    p_sex = st.radio("Gender:", ("Male", "Female"))
    p_weight = st.number_input("Patient Weight (kg):", min_value=30, max_value=200, value=70)
    
    st.markdown("---")
    st.markdown("**Core Electrolyte Panel:**")
    current_na = st.number_input("Current Serum Sodium (Na+ mEq/L):", min_value=100, max_value=180, value=118)
    target_na = st.number_input("Target Sodium Level (First 24 Hours - mEq/L):", min_value=100, max_value=180, value=124)
    
    fluid_choice = st.selectbox(
        "Select Infusate Fluid type to utilize:",
        ["Hypertonic Saline (3% NaCl) - [513 mEq/L]", 
         "Normal Saline (0.9% NaCl) - [154 mEq/L]", 
         "Half-Normal Saline (0.45% NaCl) - [77 mEq/L]", 
         "Dextrose 5% in Water (D5W) - [0 mEq/L]"]
    )

    # 1. Total Body Water (TBW) Calculation based on physiological constants
    if p_age < 65:
        tbw_coeff = 0.6 if p_sex == "Male" else 0.5
    else:
        tbw_coeff = 0.5 if p_sex == "Male" else 0.45
        
    tbw = p_weight * tbw_coeff
    
    # Map fluid concentration
    infusate_na = 513 if "3%" in fluid_choice else (154 if "0.9%" in fluid_choice else (77 if "0.45%" in fluid_choice else 0))

    st.markdown("---")
    st.markdown("<div class='section-header'>📊 Physiological Calculations</div>", unsafe_allow_html=True)
    st.metric("Estimated Total Body Water (TBW)", f"{tbw:.1f} Liters")

# ==============================================================================
# RIGHT COLUMN: Adrogue-Madias Formula & Speed Limit Safeguards (FIXED SYNTAX)
# ==============================================================================
with col_math:
    st.markdown("<div class='section-header'>⚡ 2. Quantified Correction Guide & Fluid Engine</div>", unsafe_allow_html=True)
    
    # Delta calculation using Adrogue-Madias Equation
    delta_na_per_liter = (infusate_na - current_na) / (tbw + 1)
    
    # Calculate total volume required to hit target
    target_change = target_na - current_na
    
    if delta_na_per_liter != 0:
        required_liters = target_change / delta_na_per_liter
        required_ml = required_liters * 1000
    else:
        required_ml = 0

    # ------------------------------------------------------------------
    # MEDICAL FORK A: HYPONATREMIA SAFETY CHECKS
    # ------------------------------------------------------------------
    if current_na < 135:
        st.warning("🔵 HYPONATREMIA MANAGEMENT DIRECTION DETECTED")
        
        # Absolute Correction Speed Limit Counter
        st.markdown("### 🚨 CRITICAL CRITICAL SAFEGUARD: Speed Limit Check")
        if target_change > 8:
            st.error(f"🚫 **DANGER: OVERCORRECTION DETECTED!** You are trying to raise sodium by **{target_change} mEq/L** in 24 hours. The absolute safety limit is **6-8 mEq/L/24h** to avoid Osmotic Demyelination. Please lower your target sodium input!")
        else:
            st.success(f"✅ **Safe Rate Approved:** Target correction is {target_change} mEq/L/24h, which stays within the safe guideline boundaries (<8 mEq/L).")

        st.markdown("---")
        st.markdown("### 💊 Infusion Delivery Commands:")
        st.write(f"Using **{fluid_choice}**:")
        st.write(f"* **1 Liter ($1000\ mL$) of this fluid will raise Serum Sodium by:** **{delta_na_per_liter:.2f} mEq/L**")
        
        if required_ml > 0:
            rate_ml_hr = required_ml / 24
            st.write(f"* **Total Infusate Volume needed over 24 hours:** **{required_ml:.0f} mL**")
            st.success(f"💉 **Order Injection Pump Rate:** Run infusion at **{rate_ml_hr:.1f} mL/hour** for 24 hours.")
        else:
            st.info("Target sodium is lower or equal to current sodium. No active replacement calculated.")

    # ------------------------------------------------------------------
    # MEDICAL FORK B: HYPERNATREMIA SAFETY CHECKS
    # ------------------------------------------------------------------
    elif current_na > 145:
        st.error("🔴 HYPERNATREMIA / FREE WATER DEFICIT DIRECTION DETECTED")
        
        # Calculate Free Water Deficit specifically
        water_deficit = tbw * ((current_na / 140) - 1)
        
        st.markdown("### 💧 Free Water Deficit Quantification:")
        st.write(f"The absolute physiological Free Water Deficit is **{water_deficit:.2f} Liters**.")
        
        # Speed limit checking for Hypernatremia (Max drop 10 mEq/L in 24 hours)
        if abs(target_change) > 10:
            st.error(f"🚫 **DANGER: SPEED LIMIT VIOLATION!** Lowering sodium by {abs(target_change)} mEq/L/24h is too fast and risks causing **Cerebral Edema** and seizures. Modify your target sodium to limit reduction to ≤ 10 mEq/L per 24 hours.")
        else:
            st.success(f"✅ **Safe Reduction Rate Approved:** Reduction of {abs(target_change)} mEq/L/24h is safe.")
            
        st.markdown("---")
        st.markdown("### 💊 Free Water Infusion Guide:")
        if "D5W" in fluid_choice:
            d5w_rate = (water_deficit * 1000) / 48
            st.write(f"* To replace this deficit safely over 48 hours, run **D5W IV** at **{d5w_rate:.1f} mL/hour**.")
            st.info("ℹ️ Alternatively, if the patient's GI tract is fully functional, Free Water can be given orally or via NGT (Plain Tap Water 200-250ml every 4-6 hours).")

    st.markdown("""
    ---
    **🔬 Mandatory Electrolyte Monitoring Schedule:**
    * [ ] Re-check Serum Sodium **every 4 to 6 hours** without exception.
    * [ ] If the rate of correction exceeds 0.5 mEq/L per hour, slow down or pause the infusion.
    * [ ] If overcorrection occurs accidentally, consult senior staff immediately regarding the initiation of rescue **D5W** or **DDAVP** to re-lower the sodium.
    """)

# ==============================================================================
# BOTTOM SECTION: High-Yield Board Review Questions & Explanations
# ==============================================================================
st.markdown("---")
st.markdown("<div class='board-header'>🎓 3. High-Yield Board-Level Case Review (Osmotic Demyelination Focus)</div>", unsafe_allow_html=True)
st.caption("A perfect instructional clinical vignette regarding the catastrophic danger of rapid hyponatremia correction.")

with st.expander("❓ Click to Reveal the Board Question & Scientific Rationale"):
    st.markdown("""
    **Clinical Scenario:** A 52-year-old female with severe chronic alcoholism is brought to the medical ward due to profound weakness and lethargy. Initial laboratory workup reveals a severe chronic hypotonic hyponatremia with a Serum Sodium of **108 mEq/L**. The intern immediately starts an aggressive infusion of 3% Hypertonic Saline. 12 hours later, a repeat metabolic panel shows a Serum Sodium of **124 mEq/L** (a rise of 16 mEq/L). The patient initially appears more alert, but 4 days later, she develops progressive quadriparesis, dysphagia, dysarthria, and pseudobulbar palsy. 
    
    **What is the underlying pathophysiology of this patient's new neurological deterioration?**
    
    * **A)** Acute ischemic stroke involving the middle cerebral artery territory.
    * **B)** Unmasked severe Wernicke-Korsakoff Encephalopathy due to thiamine deficiency alone.
    * **C)** **Correct.** Central Pontine Myelinolysis (Osmotic Demyelination Syndrome) caused by overly rapid correction of chronic hyponatremia.
    * **D)** Cerebral edema resulting from sudden intracellular water shifts into brain cells.
    
    ---
    
    ### 📝 Comprehensive Scientific Evidence-Based Explanation:
    * **The Correct Answer is C.** Chronic severe hyponatremia (>48 hours) allows the brain cells to adapt by pumping out intracellular organic osmolytes to prevent swelling. If hypertonic fluids correct this state too rapidly, the extracellular space becomes hypertonic relative to the adapted brain cells. Water is rapidly drawn out of the astrocytes and oligodendrocytes, triggering apoptosis and destruction of the myelin sheaths, particularly within the **pons**.
    * **High-Yield Core Limit:** For exams and safe clinical practice at Al-Ahli Hospital, remember: **\"Keep it slow!\"** The limit is a maximum rise of **8 mEq/L within any 24-hour window**, and ideally even slower (**4-6 mEq/L**) in high-risk patients such as alcoholics or malnourished individuals.
    * **Distinction Point:** Cerebral edema (Choice D) occurs when sodium *drops* too fast or when hypernatremia is *corrected* too rapidly, not during fast hyponatremia correction.
    """)

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 12px;'>Al-Ahli Hospital Internal Medicine CDSS Platforms © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
