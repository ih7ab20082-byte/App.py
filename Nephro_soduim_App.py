import streamlit as st
import random

# Page Configuration
st.set_page_config(
    page_title="Al-Ahli Hospital Nephrology & Sodium Management Center",
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

# Everlasting Professional Credit
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Clinical Project Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Core Engine:</strong> Safe Sodium Correction Protocols & Kinetic Renal Function Tracking Matrix
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Navigation Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🔍 Phase 1: Hyponatremia Diagnostic Matrix", 
    "🧪 Phase 2: Precision Sodium Correction Calculator", 
    "📟 Phase 3: AKI Staging & Fluid Balance Tracker",
    "📚 Phase 4: Nephrology Board Review Challenge"
])

# ==============================================================================
# TAB 1: HYPONATREMIA DIAGNOSTIC MATRIX
# ==============================================================================
with tab1:
    col_in1, col_out1 = st.columns([1.1, 1.2])
    
    with col_in1:
        st.markdown("<div class='section-header'>🧪 Baseline Chemistry Inputs</div>", unsafe_allow_html=True)
        serum_na = st.number_input("Serum Sodium (mEq/L):", min_value=100, max_value=180, value=118)
        serum_osmo = st.selectbox("Serum Osmolality Status:", ["Hypotonic (< 275 mOsm/kg)", "Isotonic (275-295 mOsm/kg - Pseudohyponatremia)", "Hypertonic (> 295 mOsm/kg - Hyperglycemia/Mannitol)"])
        
        st.markdown("<div class='section-header'>🩺 Clinical Fluid Volume Status (Bedside Exam)</div>", unsafe_allow_html=True)
        vol_status = rel_status = st.radio(
            "Assess Patient's Extracellular Fluid (ECF) Volume:",
            ("Hypovolemic (Dry mucous membranes, poor skin turgor, tachycardia, hypotension)",
             "Euvolemic (No signs of fluid overload, no signs of dehydration, moist membranes)",
             "Hypervloemic (Peripheral edema, ascites, JVD present)")
        )
        
        st.markdown("<div class='section-header'> urine Urine Studies (Spot Check)</div>", unsafe_allow_html=True)
        urine_na = st.number_input("Urine Sodium Concentration (mEq/L):", min_value=5, max_value=150, value=42)
        urine_osmo = st.number_input("Urine Osmolality (mOsm/kg):", min_value=50, max_value=1200, value=350)

    with col_out1:
        st.markdown("<div class='section-header'>🧠 Diagnostic Synthesis & Pathophysiology</div>", unsafe_allow_html=True)
        
        if "Hypotonic" in serum_osmo:
            st.success(f"🟢 **True Hypotonic Hyponatremia Confirmed (Na+: {serum_na} mEq/L).** Proceeding to volume status differentiation...")
            
            if "Hypovolemic" in vol_status:
                if urine_na < 20:
                    st.warning("""
                    💥 **Diagnosis: Extra-renal Volume Depletion**
                    * **Mechanisms:** GI losses (severe vomiting, diarrhea), third-spacing, or remote sweating.
                    * **Pathophysiology:** Low effective circulating volume triggers massive non-osmotic ADH release, forcing water retention over sodium preservation.
                    * **First-line Therapy:** Resuscitate with Normal Saline (0.9% NaCl) to restore volume, which will shut off ADH secretion.
                    """)
                else:
                    st.error("""
                    💥 **Diagnosis: Renal Volume Depletion / Salt Wasting**
                    * **Mechanisms:** Active Diuretic use (Thiazides are notorious), Mineralocorticoid deficiency (Addison's), or Salt-Wasting Nephropathy.
                    * **Pathophysiology:** Kidneys are inappropriately losing sodium (Urine Na > 20) despite systematic hypovolemia.
                    """)
                    
            elif "Euvolemic" in vol_status:
                if urine_osmo > 100 and urine_na > 30:
                    st.error("""
                    💥 **Diagnosis: Syndrome of Inappropriate ADH Secretion (SIADH)**
                    * **Mechanisms:** Malignancy (Small cell lung cancer), CNS disorders, Pulmonary infections, or Medications (SSRIs, Carbamazepine).
                    * **Diagnostic Criteria:** Concentrated urine (Urine Osmo > 100) and high urine sodium (>30) despite normal volume status.
                    * **First-line Therapy:** Fluid restriction (< 800-1000 mL/day), oral salt tablets, or loop diuretics.
                    """)
                else:
                    st.info("💥 **Diagnosis: Primary Polydipsia / Beer Potomania**\n* **Mechanism:** Excess water intake overloading the kidney's maximum diluting capacity (Urine Osmo will be maximally dilute, typically < 100).")
                    
            elif "Hypervloemic" in vol_status:
                st.error("""
                💥 **Diagnosis: Hypervolemic Hyponatremia (Dilutional States)**
                * **Primary Suspects:** Congestive Heart Failure (CHF), Liver Cirrhosis, or Advanced Nephrotic Syndrome.
                * **Pathophysiology:** Decreased effective arterial blood volume causes paradoxical proximal water reabsorption and ADH activation despite full total body volume overload.
                * **First-line Therapy:** Strict fluid restriction, aggressive loop diuretics (Lasix).
                """)
        else:
            st.error(f"⚠️ **Caution:** This is {serum_osmo}. It is NOT true hypotonic hyponatremia. Ensure you correct sodium for hyperglycemia if glucose is markedly high.")

# ==============================================================================
# TAB 2: PRECISION SODIUM CORRECTION CALCULATOR
# ==============================================================================
with tab2:
    st.markdown("<div class='section-header'>🧪 Precision Adrogué-Madias Correction Panel</div>", unsafe_allow_html=True)
    
    col_calc_in, col_calc_out = st.columns([1.1, 1.2])
    
    with col_calc_in:
        st.write("### 👤 Patient Clinical Parameters")
        pt_gender = st.radio("Patient Sex:", ("Male", "Female"))
        pt_age_group = st.radio("Age Group Category:", ("Adult", "Elderly (>65 Years)"))
        current_na = st.number_input("Patient Current Sodium (mEq/L):", min_value=100, max_value=150, value=115, key="calc_curr_na")
        target_na_24h = st.number_input("Desired Target Sodium in 24 Hours (mEq/L):", min_value=105, max_value=160, value=123)
        
        infusate_type = st.selectbox(
            "Select the intended IV Infusate Solution:",
            ["Hypertonic Saline (3% NaCl - 513 mEq/L)",
             "Normal Saline (0.9% NaCl - 154 mEq/L)",
             "Ringer's Lactate (130 mEq/L)"]
        )
        
        sx_severity = st.radio("Clinical Neuro Symptoms Status:", ("Severe Symptoms (Seizures, Obtundation, Coma)", "Mild to Moderate / Asymptomatic"))

    with col_calc_out:
        st.write("### 📟 Kinetic Math & Safe Infusion Orders")
        
        # 1. Total Body Water (TBW) Calculation
        if pt_gender == "Male":
            factor = 0.6 if pt_age_group == "Adult" else 0.5
        else:
            factor = 0.5 if pt_age_group == "Adult" else 0.45
        tbw = weight * factor
        
        # 2. Infusate Sodium value mapping
        if "3%" in infusate_type: infusate_na = 513
        elif "0.9%" in infusate_type: infusate_na = 154
        else: infusate_na = 130
        
        # 3. Adrogue-Madias Equation
        delta_na_per_liter = (infusate_na - current_na) / (tbw + 1)
        
        # Calculate needed volume to hit target
        desired_change = target_na_24h - current_na
        liters_needed = desired_change / delta_na_per_liter if delta_na_per_liter > 0 else 0
        ml_needed_24h = liters_needed * 1000

        st.markdown(f"""
        <div style="background-color: #EFF6FF; padding: 15px; border-radius: 8px; border-left: 4px solid #3B82F6; margin-bottom: 15px;">
            • <strong>Calculated Total Body Water (TBW):</strong> {tbw:.1f} Liters<br>
            • <strong>Predicted Sodium Rise per 1 Liter of this fluid:</strong> {delta_na_per_liter:.2f} mEq/L
        </div>
        """, unsafe_allow_html=True)

        # Safety Limit Check
        if desired_change > 8:
            st.markdown(f"""
            <div class='safety-alert'>
                <strong style="color: #991B1B !important;">🚨 SAFETY WARP ALERT: OVER-CORRECTION RISK!</strong><br>
                <span style="color: #1F2937 !important; font-size: 14px;">Your requested change is <strong>{desired_change} mEq/L</strong>. Correcting sodium faster than <strong>8 mEq/L per 24 hours</strong> puts the patient at extreme risk of <strong>Osmotic Demyelination Syndrome (ODS)</strong>. The system has auto-capped the trajectory.</span>
            </div>
            """, unsafe_allow_html=True)
            safe_ml_24h = (8 / delta_na_per_liter) * 1000
            rate_ml_hr = safe_ml_24h / 24
        else:
            safe_ml_24h = ml_needed_24h
            rate_ml_hr = safe_ml_24h / 24

        # Emergency Bolus Protocol for Severe Symptoms
        if sx_severity == "Severe Symptoms (Seizures, Obtundation, Coma)" and "3%" in infusate_type:
            st.error(f"""
            🚨 **EMERGENCY ACTIVE PROMPT: SEVERE SYMPTOMATIC HYPONATREMIA**
            * Do not wait for a 24-hour slow infusion if the patient isactively seizing or comatose.
            * **Immediate Action Order:** Give a **100 mL bolus of Hypertonic Saline (3% NaCl) IV over 10-15 minutes**.
            * Repeat up to 2 times (Max 300 mL total) every 30 minutes if symptoms persist, checking a stat serum sodium between doses. 
            * **Goal:** Raise sodium rapidly by **4-6 mEq/L** to stop brain herniation, then arrest further aggressive correction.
            """)
        else:
            st.success(f"""
            📟 **Standard Safe Maintenance Infusion Plan (24-Hour Protocol):**
            * **Total Volume of Infusate Required:** **{safe_ml_24h:.0f} mL** over 24 hours.
            * **Continuous Infusion Rate:** Set the pump strictly at **{rate_ml_hr:.1f} mL/hour**.
            * **Monitoring Mandate:** Recheck serum sodium level every **4 to 6 hours** without exception. If sodium is rising faster than expected, stop the infusion and consider free water administration.
            """)

# ==============================================================================
# TAB 3: AKI STAGING & NEPHROLOGY FLUID TRACKER
# ==============================================================================
with tab3:
    st.markdown("<div class='section-header'>📟 KDIGO Acute Kidney Injury & Volume Analysis Panel</div>", unsafe_allow_html=True)
    
    col_aki_in, col_aki_out = st.columns([1.1, 1.2])
    
    with col_aki_in:
        st.write("### 🧪 Creatinine & Urine Kinetics")
        baseline_scr = st.number_input("Patient's Baseline Serum Creatinine (mg/dL):", min_value=0.3, max_value=15.0, value=1.0)
        current_scr = st.number_input("Current/Peak Serum Creatinine (mg/dL):", min_value=0.3, max_value=15.0, value=2.4)
        
        total_uop = st.number_input("Total Urine Output past 24 Hours (mL):", min_value=0, max_value=10000, value=400)
        hours_tracked = st.number_input("Urine Output Tracking Window (Hours):", min_value=6, max_value=24, value=24)
        
        st.write("### 💧 Comprehensive Daily Intake / Output Balance")
        daily_intake = st.number_input("Total 24-Hour Intake (IV Fluids + Oral Meds + Nutrition mL):", min_value=0, max_value=10000, value=3000)
        daily_output = total_uop + st.number_input("Insensible/Other Losses (Stool, Vomitus, Gastric drains mL):", min_value=0, max_value=5000, value=500)

    with col_aki_out:
        st.write("### 🧮 Renal Function Classification & Staging")
        
        # KDIGO Calculations
        scr_ratio = current_scr / baseline_scr
        uop_rate = (total_uop / weight) / hours_tracked
        
        # Determine Stage
        aki_stage = "No AKI"
        reason = "Creatinine rise and urine output are within normal boundaries."
        
        if scr_ratio >= 3.0 or current_scr >= 4.0 or uop_rate < 0.3:
            aki_stage = "Stage 3 AKI"
            reason = "Serum Creatinine increased &ge; 3.0 times baseline OR current value &ge; 4.0 mg/dL, OR anuria/severe oliguria present."
        elif scr_ratio >= 2.0 and scr_ratio < 3.0:
            aki_stage = "Stage 2 AKI"
            reason = "Serum Creatinine increased 2.0 to 2.9 times baseline values."
        elif scr_ratio >= 1.5 or (current_scr - baseline_scr) >= 0.3:
            aki_stage = "Stage 1 AKI"
            reason = "Serum Creatinine increased 1.5-1.9 times baseline OR absolute rise &ge; 0.3 mg/dL."

        # Net Balance and Overload
        net_balance = daily_intake - daily_output
        fluid_overload_pct = (net_balance / weight) * 100 if net_balance > 0 else 0

        if "No AKI" not in aki_stage:
            st.error(f"""
            🚨 **KDIGO STATUS: {aki_stage} DETECTED**
            * **Staging Logic:** {reason}
            * **Calculated Weight-Adjusted Urine Output:** **{uop_rate:.2f} mL/kg/hour** over the last {hours_tracked} hours.
            """)
        else:
            st.success("🟢 **Renal Function Status:** Normal. No active KDIGO AKI profile detected.")

        # Fluid Balance Visuals
        st.markdown(f"""
        <div style="background-color: #F8FAFC; padding: 18px; border-radius: 8px; border: 1px solid #CBD5E1;">
            <strong>💧 24-Hour Net Fluid Balance Matrix:</strong><br>
            • <strong>Net Balance:</strong> {'+' if net_balance > 0 else ''}{net_balance} mL (Positive Fluid Accumulation)<br>
            • <strong>Estimated Cumulative Fluid Overload Percentage:</strong> {fluid_overload_pct:.1f}%<br>
            <em>(Note: A cumulative Fluid Overload > 10% is independently associated with increased mortality in AKI patients).</em>
        </div>
        """, unsafe_allow_html=True)

        # Urgent Indications for Dialysis (AEIOU Mnemonic Reminder)
        st.markdown("""
        ### 🏥 Urgent Indications for Emergency Dialysis (AEIOU):
        1. **A - Acidosis:** Refractory Metabolic Acidosis (pH < 7.15) unresponsive to therapy.
        2. **E - Electrolytes:** Severe hyperkalemia (K > 6.5 mEq/L) or rapidly rising potassium with ECG changes.
        3. **I - Intoxication:** Toxic ingestions of dialyzable drugs (Lithium, Methanol, Ethylene glycol, Salicylates).
        4. **O - Overload:** Refractory fluid overload / pulmonary edema unresponsive to massive loop diuretic doses.
        5. **U - Uremia:** Uremic pericarditis, uremic encephalopathy, or asterixis.
        """)

# ==============================================================================
# TAB 4: HIGH-YIELD NEPHROLOGY BOARD REVIEW CHALLENGE
# ==============================================================================
with tab4:
    st.markdown("<div class='section-header'>📚 High-Yield Nephrology Board Examination Challenge</div>", unsafe_allow_html=True)
    
    neph_pool = [
        {
            "id": 1,
            "case": "A 72-year-old female is admitted from a nursing home with confusion. Her serum sodium is 112 mEq/L. She is completely asymptomatic neurologically otherwise, with no seizures. The resident puts an aggressive order for 3% Hypertonic Saline, and her sodium rises to 128 mEq/L within the first 16 hours. On day 3, the patient develops spastic quadriparesis, pseudobulbar palsy, and loss of consciousness.",
            "question": "What is the underlying diagnosis for this devastating neurological complication?",
            "options": ["A) Acute Ischemic Stroke of the Middle Cerebral Artery", "B) Osmotic Demyelination Syndrome (Central Pontine Myelinolysis)", "C) Severe Uremic Encephalopathy due to unrecognized AKI", "D) Wernicke's Encephalopathy from vitamin depletion"],
            "correct": "B) Osmotic Demyelination Syndrome (Central Pontine Myelinolysis)",
            "explanation": "Rapid over-correction of chronic hyponatremia (>8-10 mEq/L in 24 hours) causes water to shift rapidly out of brain cells, leading to cellular dehydration and destruction of the myelin sheath in the pons, known as Osmotic Demyelination Syndrome. This classically presents with delayed pseudobulbar palsy and quadriparesis."
        },
        {
            "id": 2,
            "case": "A 62-year-old male with severe liver cirrhosis is admitted with ascites and a serum sodium of 122 mEq/L. His urine sodium is checked and is found to be 8 mEq/L (very low). His physical exam shows significant peripheral pitting edema and safe mucous membranes.",
            "question": "What is the mechanism and correct initial approach to this patient's hyponatremia?",
            "options": ["A) This is hypovolemic salt-wasting; infuse 2 Liters of Normal Saline immediately", "B) This is hypervolemic hyponatremia; initiate free water restriction and optimize loop diuretic therapy", "C) This is SIADH; start high-dose intravenous Desmopressin (DDAVP)", "D) This is pseudohyponatremia; no treatment is necessary"],
            "correct": "B) This is hypervolemic hyponatremia; initiate free water restriction and optimize loop diuretic therapy",
            "explanation": "In cirrhosis, splanchnic vasodilation causes a massive drop in effective arterial blood volume, activating ADH and aldosterone. This leads to total body fluid overload (edema/ascites) but with dilutional hyponatremia and avid renal sodium retention (Urine Na < 10). The correct management is fluid restriction and diuretics, not saline infusion."
        }
    ]

    if 'neph_q' not in st.session_state:
        st.session_state.neph_q = random.choice(neph_pool)
        
    if st.button("🔄 Generate Another Advanced Nephrology Question"):
        st.session_state.neph_q = random.choice(neph_pool)
        
    curr_neph_q = st.session_state.neph_q
    
    st.warning(f"**Clinical Scenario:** {curr_neph_q['case']}")
    st.write(f"❓ **Question:** {curr_neph_q['question']}")
    
    user_neph_ans = st.radio("Select your answer from below:", curr_neph_q['options'], key=f"nq_id_{curr_neph_q['id']}")
    
    if st.expander("🔑 Reveal Correct Answer & Dr. Ihab's Expert Explanation"):
        if user_neph_ans == curr_neph_q['correct']:
            st.success(f"🎯 **Correct!** The answer is {curr_neph_q['correct']}")
        else:
            st.error(f"❌ **Incorrect Choice.** The correct answer is {curr_neph_q['correct']}")
        st.markdown(f"**Explanation:** {curr_neph_q['explanation']}")

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 12px;'>Al-Ahli Hospital Nephrology & Sodium Management Engine © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
