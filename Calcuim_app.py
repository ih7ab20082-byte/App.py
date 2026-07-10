import streamlit as st

# Page Configuration for a dedicated Calcium disorder tool
st.set_page_config(
    page_title="Al-Ahli Hospital Calcium Disorders Protocol",
    page_icon="🦴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Medical Branding Styles
st.markdown("""
    <style>
    .main-title { font-size:32px !important; font-weight: bold; color: #4338CA; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:16px !important; color: #4B5563; text-align: center; margin-bottom: 25px; font-style: italic; }
    .branding-bar { background-color: #EEF2FF; padding: 20px; border-radius: 10px; border-left: 6px solid #4F46E5; margin-bottom: 25px; }
    .branding-bar strong { color: #4338CA !important; font-weight: bold; }
    .branding-text { color: #1F2937 !important; font-size: 16px !important; line-height: 1.6; }
    .section-header { font-size:22px !important; font-weight: bold; color: #4338CA; margin-top: 15px; margin-bottom: 15px; }
    .board-header { font-size:20px !important; font-weight: bold; color: #D97706; margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<div class='main-title'>🦴 Al-Ahli Hospital Calcium Disorders Command Center</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Interactive Diagnostic Approach & Advanced Treatment Protocols</div>", unsafe_allow_html=True)

# Professional Badge
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Project Founder & Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Focus:</strong> Corrected Calcium Math, PTH-Driven Algorithms & Emergency Therapeutics
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Layout Split
col_input, col_protocol = st.columns([1, 1.2])

# ==============================================================================
# LEFT COLUMN: Lab Inputs & Calcium Correction Math
# ==============================================================================
with col_input:
    st.markdown("<div class='section-header'>🧪 1. Serum Laboratory Inputs</div>", unsafe_allow_html=True)
    
    measured_ca = st.number_input("Measured Serum Total Calcium (mg/dL):", min_value=3.0, max_value=20.0, value=11.5, step=0.1)
    albumin = st.number_input("Serum Albumin (g/dL):", min_value=1.0, max_value=6.0, value=3.0, step=0.1)
    
    st.markdown("---")
    st.markdown("**Endocrine & Renals (Crucial for Etiology / Diagnostic Approach):**")
    pth_level = st.number_input("Intact PTH Level (pg/mL) [Normal: 15-65]:", min_value=1.0, max_value=1500.0, value=95.0, step=1.0)
    creatinine = st.number_input("Serum Creatinine (mg/dL):", min_value=0.3, max_value=15.0, value=1.1, step=0.1)
    ecg_changes = st.radio("ECG Findings:", ("Normal QT Interval", "Shortened QT Interval (Hypercalcemia)", "Prolonged QT Interval / Torsades Risk (Hypocalcemia)"))

    # 1. Corrected Calcium Calculation Formula
    # Formula: Corrected Ca = Measured Ca + 0.8 * (4.0 - Albumin)
    if albumin < 4.0:
        corrected_ca = measured_ca + 0.8 * (4.0 - albumin)
    else:
        corrected_ca = measured_ca

    st.markdown("---")
    st.markdown("<div class='section-header'>📊 Corrected Calcium Result</div>", unsafe_allow_html=True)
    
    if corrected_ca > 10.5:
        status_text = "Hypercalcemia"
        delta_color = "Elevated"
    elif corrected_ca < 8.5:
        status_text = "Hypocalcemia"
        delta_color = "Low"
    else:
        status_text = "Normal Calcium Range"
        delta_color = "Normal"
        
    st.metric("Corrected Total Calcium", f"{corrected_ca:.2f} mg/dL", delta=delta_color)
    st.caption("📝 Rationale: Always base clinical decisions on Corrected Calcium to rule out pseudohypo/hypercalcemia caused by abnormal albumin levels.")

# ==============================================================================
# RIGHT COLUMN: Diagnostic Algorithm & Treatment Protocols
# ==============================================================================
with col_protocol:
    st.markdown("<div class='section-header'>⚡ 2. Diagnostic Approach & Management</div>", unsafe_allow_html=True)

    # ------------------------------------------------------------------
    # BRANCH A: HYPERCALCEMIA PATHWAY
    # ------------------------------------------------------------------
    if corrected_ca > 10.5:
        st.error(f"🔴 PATHWAY ACTIVATED: HYPERCALCEMIA MANAGEMENT")
        
        # Severity
        if corrected_ca >= 14.0:
            st.markdown("**Severity:** <span style='color:red; font-weight:bold;'>Hypercalcemic Crisis (Severe)</span>", unsafe_allow_html=True)
        else:
            st.markdown("**Severity:** <span style='color:orange; font-weight:bold;'>Mild-to-Moderate Hypercalcemia</span>", unsafe_allow_html=True)
            
        st.markdown("---")
        st.markdown("### 🔍 Step A: Diagnostic Approach (Etiology Finder)")
        
        if pth_level > 65:
            st.info("🧬 **PTH-Dependent Hypercalcemia:** Intact PTH is elevated. The most probable diagnosis is **Primary Hyperparathyroidism** (e.g., parathyroid adenoma) or Tertiary Hyperparathyroidism if renal failure is advanced.")
        elif pth_level < 20:
            st.warning("🦀 **PTH-Independent Hypercalcemia:** PTH is appropriately suppressed. **High Suspicion of Malignancy!** Workup should prioritize: PTHrP (Malignancy of squamous cells), Serum Protein Electrophoresis (SPEP for Multiple Myeloma), and Vitamin D toxicities/Granulomatous diseases (Sarcoidosis, TB).")
        else:
            st.caption("Inappropriate or borderline PTH level. Evaluate for Familial Hypocalciuric Hypercalcemia (FHH) using a 24-hour urine calcium collection.")

        st.markdown("---")
        st.markdown("### 💊 Step B: Immediate Treatment Protocol")
        st.markdown("""
        1. **Aggressive Fluid Resuscitation (First Line):** Start **0.9% Normal Saline at 200-500 mL/hr** immediately to restore volume and promote renal calcium excretion. (Maintain urine output ~100-150 mL/hr).
        2. **Calcitonin Injection (For Rapid Correction):** Administer **4-8 units/kg IM or SC every 12 hours**. *Works within 4-6 hours (Tachyphylaxis develops after 48h).*
        3. **Bisphosphonates (For Sustained Control):** Give **Zoledronic Acid 4 mg IV infusion over 15 mins** OR **Pamidronate 60-90 mg IV over 2-4 hours**. *Takes 2-4 days to reach peak effect; mandatory for malignancy-induced hypercalcemia.*
        4. **Avoid Loop Diuretics (Furosemide):** Do NOT give routine Furosemide unless the patient develops frank volume overload / heart failure during fluid resuscitation.
        """)

    # ------------------------------------------------------------------
    # BRANCH B: HYPOCALCEMIA PATHWAY
    # ------------------------------------------------------------------
    elif corrected_ca < 8.5:
        st.warning(f"🔵 PATHWAY ACTIVATED: HYPOCALCEMIA MANAGEMENT")
        st.markdown("---")
        st.markdown("### 🔍 Step A: Diagnostic Approach (Etiology Finder)")
        
        if pth_level < 15:
            st.info("🧬 **Hypoparathyroidism Detected:** Low PTH indicates primary failure of parathyroid glands (e.g., post-neck surgery, autoimmune destruction, or severe magnesium deficiency).")
        else:
            st.info("🥛 **Secondary Hyperparathyroidism Detected:** High PTH is a reactive response. Differential diagnosis: **Vitamin D Deficiency**, Chronic Kidney Disease (CKD), or Hyperphosphatemia/Tumor Lysis Syndrome.")

        st.markdown("---")
        st.markdown("### 💊 Step B: Emergency Treatment Protocol")
        
        if ecg_changes == "Prolonged QT Interval / Torsades Risk (Hypocalcemia)" or corrected_ca < 7.0:
            st.error("🚨 EMERGENCY REFLEX: SYMPTOMATIC / SEVERE HYPOCALCEMIA")
            st.markdown("""
            * **First-line Rescue Stat:** Give **1-2 grams of Calcium Gluconate IV** (10-20 mL of 10% Calcium Gluconate solution) diluted in 50-100 mL of D5W or NS, infused over **10 to 20 minutes**.
            * **Safety Alert:** *Prefer Calcium Gluconate over Calcium Chloride in peripheral IV lines to prevent severe tissue necrosis/thrombophlebitis if extravasation occurs.*
            * **Continuous Infusion if Refractory:** Mix 10 ampules of 10% Calcium Gluconate in 1L of D5W or NS and run at 50-100 mL/hour.
            * **Check Magnesium:** Always measure and replace **Magnesium** if low ($<1.5\ mg/dL$), because hypomagnesemia induces parathyroid gland resistance and impairs PTH release, making hypocalcemia refractory to calcium replacement!
            """)
        else:
            st.success("🟢 **Asymptomatic / Mild Protocol:** Manage with **Oral Calcium Carbonate / Citrate** (1-3 g/day) + active **Vitamin D (Calcitriol)** supplementation.")

    else:
        st.success("✅ Patient's calcium homeostasis is completely normal. No therapeutic intervention required.")

# ==============================================================================
# BOTTOM SECTION: High-Yield Board Review Questions & Explanations
# ==============================================================================
st.markdown("---")
st.markdown("<div class='board-header'>🎓 3. High-Yield Board-Level Case Review (Calcium Homeostasis Focus)</div>", unsafe_allow_html=True)
st.caption("High-yield clinical vignette testing the intersection of electrolyte corrections and endocrine logic.")

with st.expander("❓ Click to Reveal the Board Question & Scientific Rationale"):
    st.markdown("""
    **Clinical Scenario:** A 64-year-old female with advanced breast cancer is admitted to the medical floor due to severe constipation, confusion, and generalized muscle weakness. Baseline labs reveal: Total Serum Calcium **14.2 mg/dL**, Albumin **2.5 g/dL**, Serum Creatinine **1.8 mg/dL**, and Intact PTH **6 pg/mL**. ECG demonstrates a notably shortened QT interval. 
    
    **What is the most appropriate initial combination of therapies to implement for this patient?**
    
    * **A)** Start IV Furosemide boluses immediately followed by oral Alendronate.
    * **B)** **Correct.** Initiation of high-volume 0.9% Normal Saline infusion, SC Calcitonin, and IV Zoledronic Acid.
    * **C)** Administer 10% Calcium Gluconate IV to stabilize the cardiac membrane.
    * **D)** High-dose oral Vitamin D3 (Cholecalciferol) replacement and emergency hemodialysis.
    
    ---
    
    ### 📝 Comprehensive Scientific Evidence-Based Explanation:
    * **The Correct Answer is B.** This patient is in a **Hypercalcemic Crisis** (Corrected Calcium = $14.2 + 0.8 \times (4.0 - 2.5) = 15.4\ mg/dL$) with suppressed PTH ($<20$), classic for Hypercalcemia of Malignancy. 
    * **Therapeutic Rationale:** 1. **Saliene Hydration** is the critical first step to correct volume depletion and induce calciuresis.
        2. **Calcitonin** is added for a rapid reduction in calcium levels within hours.
        3. **IV Zoledronic Acid** (bisphosphonate) provides long-term control by inhibiting osteoclast activity, though it takes 48-72 hours to start working.
    * **The Diuretic Trap (Critique of A):** Loop diuretics should *never* be given before full volume status is restored, as they can worsen volume contraction and reduce the renal clearance of calcium, exacerbating the crisis. Oral bisphosphonates (Alendronate) have no role in acute crisis management.
    * **Cardiac Membrane Stabilization (Critique of C):** Calcium gluconate is used to protect the heart against *hyperkalemia* or *hypocalcemia*, giving it here would be giving fuel to the fire.
    """)

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 12px;'>Al-Ahli Hospital Internal Medicine CDSS Platforms © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
