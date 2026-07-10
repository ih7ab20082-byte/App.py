import streamlit as st

# Page Configuration for the Ultimate Sodium Command Center
st.set_page_config(
    page_title="Al-Ahli Hospital Comprehensive Sodium Engine",
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
    .dx-box { background-color: #F9FAFB; padding: 20px; border-radius: 8px; border: 1px solid #E5E7EB; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<div class='main-title'>🧪 Al-Ahli Hospital Sodium Diagnostic & Fluid Engine</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Advanced Decision Support Tool: Multi-Lab Osmolality Mapping & Safe Adrogue-Madias Calculator</div>", unsafe_allow_html=True)

# Professional Badge
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Project Founder & Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Core Safety:</strong> Prevention of Central Pontine Myelinolysis & Cerebral Edema
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Layout Split
col_input, col_protocol = st.columns([1, 1.2])

# ==============================================================================
# LEFT COLUMN: Patient Metrics & Expanded Lab Profiles (Serum + Urine)
# ==============================================================================
with col_input:
    st.markdown("<div class='section-header'>📋 1. Patient Demographics & Full Lab Profiles</div>", unsafe_allow_html=True)
    
    p_age = st.number_input("Patient Age:", min_value=1, max_value=120, value=65)
    p_sex = st.radio("Gender:", ("Male", "Female"))
    p_weight = st.number_input("Patient Weight (kg):", min_value=30, max_value=200, value=70)
    
    st.markdown("---")
    st.subheader("A) Core Serum Labs")
    current_na = st.number_input("Serum Sodium (Na+ mEq/L):", min_value=100, max_value=180, value=118)
    target_na = st.number_input("Target Sodium Level (First 24 Hours - mEq/L):", min_value=100, max_value=180, value=124)
    
    fluid_choice = st.selectbox(
        "Select Infusate Fluid type to utilize:",
        ["Hypertonic Saline (3% NaCl) - [513 mEq/L]", 
         "Normal Saline (0.9% NaCl) - [154 mEq/L]", 
         "Half-Normal Saline (0.45% NaCl) - [77 mEq/L]", 
         "Dextrose 5% in Water (D5W) - [0 mEq/L]"]
    )

    st.markdown("---")
    st.subheader("B) Advanced Osmolality & Urine Panel")
    s_osmolality = st.number_input("Serum Osmolality (mOsm/kg) [Normal: 275-295]:", min_value=150, max_value=400, value=250)
    
    urine_labs_active = st.checkbox("Are Urine Labs available? (Highly Recommended)")
    if urine_labs_active:
        u_osmolality = st.number_input("Urine Osmolality (mOsm/kg):", min_value=50, max_value=1200, value=450)
        u_sodium = st.number_input("Urine Sodium Concentration (mEq/L):", min_value=5, max_value=150, value=45)
        vol_status = st.radio("Clinical Volume Status Estimation:", ("Hypovolemic (Dehydrated/Dry)", "Euvolemic (Normal Fluid Volume)", "Hypervolemic (Fluid Overload/Edema)"))
    else:
        u_osmolality, u_sodium, vol_status = None, None, None

    # Physiological Constants for TBW
    if p_age < 65:
        tbw_coeff = 0.6 if p_sex == "Male" else 0.5
    else:
        tbw_coeff = 0.5 if p_sex == "Male" else 0.45
    tbw = p_weight * tbw_coeff
    
    # Map fluid concentration
    infusate_na = 513 if "3%" in fluid_choice else (154 if "0.9%" in fluid_choice else (77 if "0.45%" in fluid_choice else 0))

    st.markdown("---")
    st.markdown("<div class='section-header'>📊 Calculated Physiological Metrics</div>", unsafe_allow_html=True)
    st.metric("Estimated Total Body Water (TBW)", f"{tbw:.1f} Liters")

# ==============================================================================
# RIGHT COLUMN: The Diagnostic Approach Mapping & Adrogue-Madias Fluid Engine
# ==============================================================================
with col_protocol:
    st.markdown("<div class='section-header'>⚡ 2. Diagnostic Mapping & Targeted Management</div>", unsafe_allow_html=True)

    target_change = target_na - current_na

    # ------------------------------------------------------------------
    # MAIN BRANCH A: HYPONATREMIA DIAGNOSTIC & TREATMENT ENGINE
    # ------------------------------------------------------------------
    if current_na < 135:
        st.warning("🔵 CLINICAL PATHWAY: HYPONATREMIA DETECTED")
        
        st.markdown("<div class='dx-box'>", unsafe_allow_html=True)
        st.markdown("### 🔍 Step A: Diagnostic Reasoning (Serum Osmolality Split)")
        
        # 1. Hypertonic Hyponatremia
        if s_osmolality > 295:
            st.markdown("🎯 **Etiology:** **Hypertonic Hyponatremia (Translocational)**")
            st.markdown("💡 *Reasoning:* Serum Osmolality is high. This is typically driven by profound **Hyperglycemia (DKA/HHS)** or Mannitol. Sodium drops artificially because water shifts from the intracellular space to dilute the serum.")
            st.markdown("📋 **Next Clinical Steps:** Check Blood Glucose immediately! Use the corrected sodium formula for hyperglycemia: *Corrected Na = Measured Na + 1.6 * (Glucose - 100)/100*.")
        
        # 2. Isotonic Hyponatremia
        elif 275 <= s_osmolality <= 295:
            st.markdown("🎯 **Etiology:** **Isotonic Hyponatremia (Pseudohyponatremia)**")
            st.markdown("💡 *Reasoning:* Normal Serum Osmolality in the presence of low sodium. This is a lab artifact caused by severe **Hyperlipidemia** or **Hyperproteinemia** (e.g., Multiple Myeloma).")
            st.markdown("📋 **Next Clinical Steps:** Order a Lipid Profile and Total Serum Protein with SPEP to rule out laboratory artifact.")
        
        # 3. True Hypotonic Hyponatremia
        else:
            st.markdown("🎯 **Etiology:** **True Hypotonic Hyponatremia**")
            st.markdown("💡 *Reasoning:* Serum Osmolality is appropriately low ($<275\ mOsm/kg$), confirming a true excess of free water relative to solute.")
            
            if urine_labs_active:
                st.markdown("---")
                st.markdown("#### 🧪 Advanced Urine Analysis Integration:")
                
                if u_osmolality < 100:
                    st.markdown("📌 **Diagnosis:** **Primary Polydipsia** or **Beer Potomania**")
                    st.markdown("💡 *Reasoning:* Urine Osmolality is maximally suppressed ($<100$). This proves the kidneys are working perfectly, trying to dump free water, but the patient's oral intake has overwhelmed renal capacity.")
                else:
                    st.markdown("📌 **Urine Osmolality > 100 mOsm/kg:** Inappropriate ADH activity is present. Evaluating via volume status and urine sodium:")
                    
                    if vol_status == "Hypovolemic (Dehydrated/Dry)":
                        if u_sodium < 20:
                            st.markdown("👉 **Cause:** **Extra-renal Volume Loss** (Vomiting, severe Diarrhea, or remote third-spacing). The kidneys are appropriately holding onto sodium ($<20$) and water.")
                        else:
                            st.markdown("👉 **Cause:** **Renal Volume Loss / Diuretics** (Thiazide Diuretic abuse or Mineralocorticoid Deficiency / Addison's disease). The kidneys are failing to conserve sodium despite volume depletion.")
                            
                    elif vol_status == "Euvolemic (Normal Fluid Volume)":
                        if u_sodium > 40:
                            st.markdown("👉 **Cause:** **SIADH (Syndrome of Inappropriate ADH)**")
                            st.markdown("💡 *Reasoning:* Euvolemic patient + Concentrated urine ($>100$) + High urine sodium ($>40$). This fits the explicit diagnostic criteria for SIADH.")
                            st.markdown("📋 **Next Steps for SIADH:** Strict Fluid Restriction ($<1000\ mL/\text{day}$). Look for triggers: Medications (SSRIs, Carbamazepine), CNS pathologies, or Small Cell Lung Cancer.")
                        else:
                            st.markdown("👉 **Cause:** Consider Secondary Hypothyroidism or Glucocorticoid Deficiency.")
                            
                    elif vol_status == "Hypervolemic (Fluid Overload/Edema)":
                        st.markdown("👉 **Cause:** **Edematous States (Heart Failure, Liver Cirrhosis, or Nephrotic Syndrome)**")
                        st.markdown("💡 *Reasoning:* Decreased effective arterial blood volume triggers secondary hyperaldosteronism and massive ADH release, forcing the kidneys to avidly retain sodium ($Urine\ Na < 20$) and water.")
            else:
                st.info("🧪 *To unlock full etiology identification (SIADH vs. Hypovolemic loss), please check the Urine Labs box on the left.*")
                
        st.markdown("</div>", unsafe_allow_html=True)

        # Fluid Calculation Integration
        st.markdown("### 💊 Step B: Quantified Adrogue-Madias Calculation")
        delta_na_per_liter = (infusate_na - current_na) / (tbw + 1)
        
        # Speed Limit Check
        if target_change > 8:
            st.error(f"🚫 **DANGER: OVERCORRECTION DETECTED!** Attempting to raise sodium by **{target_change} mEq/L** in 24 hours breaches the absolute safety limit (**6-8 mEq/L/24h**). Risk of **Osmotic Demyelination (Central Pontine Myelinolysis)** is high! Reduce target input!")
        else:
            st.success(f"✅ **Safe Correction Rate Approved:** Rate is {target_change} mEq/L/24h (Limit < 8).")
            
        if delta_na_per_liter > 0:
            required_ml = (target_change / delta_na_per_liter) * 1000
            rate_ml_hr = required_ml / 24
            st.write(f"Using **{fluid_choice}**:")
            st.write(f"* 1 Liter will raise serum sodium by **{delta_na_per_liter:.2f} mEq/L**.")
            st.success(f"💉 **Order Injection Pump Rate:** Run infusion at **{rate_ml_hr:.1f} mL/hour** for 24 hours (Total: {required_ml:.0f} mL).")

    # ------------------------------------------------------------------
    # MAIN BRANCH B: HYPERNATREMIA DIAGNOSTIC & TREATMENT ENGINE
    # ------------------------------------------------------------------
    elif current_na > 145:
        st.error("🔴 CLINICAL PATHWAY: HYPERNATREMIA EVALUATION")
        
        st.markdown("<div class='dx-box'>", unsafe_allow_html=True)
        st.markdown("### 🔍 Step A: Diagnostic Reasoning (Free Water Deficit Mapping)")
        
        if urine_labs_active:
            if u_osmolality > 600:
                st.markdown("🎯 **Etiology:** **Extra-renal Free Water Loss** (Insensible losses, severe sweating, or poor oral access to water).")
                st.markdown("💡 *Reasoning:* High serum sodium with maximally concentrated urine ($>600\ mOsm/kg$) proves the kidneys are intact and responding correctly by conserving every drop of water.")
            elif u_osmolality < 300:
                st.markdown("🎯 **Etiology:** **Diabetes Insipidus (DI)**")
                st.markdown("💡 *Reasoning:* Hypernatremia with dilute urine ($<300\ mOsm/kg$) indicates a complete failure to concentrate urine due to lack of ADH (Central DI) or renal resistance to ADH (Nephrogenic DI).")
                st.markdown("📋 **Next Step:** Perform a Water Deprivation Test followed by Desmopressin (DDAVP) administration to differentiate Central from Nephrogenic DI.")
        else:
            st.info("ℹ️ Check Urine Osmolality to rule out Diabetes Insipidus versus simple insensible losses.")
        st.markdown("</div>", unsafe_allow_html=True)

        # Free Water Deficit calculation
        water_deficit = tbw * ((current_na / 140) - 1)
        st.markdown("### 💧 Step B: Free Water Deficit Quantified")
        st.write(f"The absolute Free Water Deficit is **{water_deficit:.2f} Liters**.")
        
        if abs(target_change) > 10:
            st.error(f"🚫 **DANGER: SPEED LIMIT VIOLATION!** Lowering sodium by {abs(target_change)} mEq/L/24h is too fast and risks causing **Cerebral Edema**, herniation, and seizures. Limit reduction to ≤ 10 mEq/L per 24 hours.")
        else:
            st.success(f"✅ **Safe Rate Approved:** Planned drop of {abs(target_change)} mEq/L/24h is safe.")
            if "D5W" in fluid_choice:
                d5w_rate = (water_deficit * 1000) / 48
                st.success(f"💉 **Free Water Infusion Command:** Run **D5W IV** at **{d5w_rate:.1f} mL/hour** safely over 48 hours.")

    else:
        st.success("✅ Patient's sodium level is within normal homeostatic boundaries.")

# ==============================================================================
# BOTTOM SECTION: High-Yield Board Review Questions & Explanations
# ==============================================================================
st.markdown("---")
st.markdown("<div class='board-header'>🎓 3. High-Yield Board-Level Case Review (SIADH vs. Pseudohyponatremia Trap)</div>", unsafe_allow_html=True)

with st.expander("❓ Click to Reveal the Board Question & Scientific Rationale"):
    st.markdown("""
    **Clinical Scenario:** A 68-year-old male with a history of small cell lung cancer is evaluated due to progressive confusion. His laboratory results demonstrate a Serum Sodium of **120 mEq/L**. The resident immediately assumes SIADH and orders strict fluid restriction. However, the comprehensive metabolic profile returns showing a **Serum Osmolality of 290 mOsm/kg** (Normal range). 
    
    **What is the most appropriate next step in managing this patient?**
    
    * **A)** Change therapy to 3% Hypertonic Saline infusion immediately.
    * **B)** **Correct.** Cancel fluid restriction, order a Serum Lipid Panel and Serum Protein Electrophoresis.
    * **C)** Administer IV Desmopressin (DDAVP) to halt free water clearance.
    * **D)** Confirm the diagnosis of SIADH since small cell lung cancer is a classic trigger.
    
    ---
    
    ### 📝 Comprehensive Scientific Evidence-Based Explanation:
    * **The Correct Answer is B.** This case highlights the dangerous "SIADH Trap." While small cell lung cancer is a classic trigger for true SIADH, the **Serum Osmolality is 290 mOsm/kg (Normal/Isotonic)**. 
    * True hyponatremia caused by SIADH *must* be hypotonic (Serum Osmolality $<275\ mOsm/kg$). A normal osmolality in the presence of low sodium confirms **Pseudohyponatremia**, which is a laboratory artifact commonly resulting from extreme hyperlipidemia or hyperproteinemia. 
    * **Clinical Action:** Restricting fluids or giving hypertonic saline to this patient is an error and could cause severe dehydration. You must investigate the serum proteins and lipids to identify the underlying cause of the lab artifact!
    """)

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 12px;'>Al-Ahli Hospital Internal Medicine CDSS Platforms © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
