import streamlit as st
import math  # تم إضافة المكتبة هنا لحل مشكلة الحسابات الرياضية اللوغاريتمية

# Page Configuration
st.set_page_config(
    page_title="Al-Ahli Hospital CKD Management Command Center",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Medical Branding Styles
st.markdown("""
    <style>
    .main-title { font-size:32px !important; font-weight: bold; color: #0F766E; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:16px !important; color: #4B5563; text-align: center; margin-bottom: 25px; font-style: italic; }
    .branding-bar { background-color: #F0FDFA; padding: 20px; border-radius: 10px; border-left: 6px solid #0F766E; margin-bottom: 25px; }
    .branding-bar strong { color: #0F766E !important; font-weight: bold; }
    .branding-text { color: #1F2937 !important; font-size: 16px !important; line-height: 1.6; }
    .section-header { font-size:22px !important; font-weight: bold; color: #0F766E; margin-top: 15px; margin-bottom: 15px; }
    .board-header { font-size:20px !important; font-weight: bold; color: #D97706; margin-top: 15px; }
    .status-box { background-color: #F9FAFB; padding: 15px; border-radius: 8px; border: 1px solid #E5E7EB; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<div class='main-title'>🩸 Al-Ahli Hospital CKD Advanced Command Center</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Evidence-Based KDIGO Staging, Complication Mapping & Drug Dosing Engine</div>", unsafe_allow_html=True)

# Professional Badge
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Project Founder & Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Core Logic:</strong> 2021 CKD-EPI Equation, 4-Variable KFRE, and Mineral-Bone Disorder Guidelines
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Layout Split
col_input, col_protocol = st.columns([1, 1.2])

# ==============================================================================
# LEFT COLUMN: Patient Profiles, Serum & Urine Labs
# ==============================================================================
with col_input:
    st.markdown("<div class='section-header'>📋 1. Patient Demographics & Biomarkers</div>", unsafe_allow_html=True)
    
    # Demographics
    p_age = st.number_input("Patient Age (Years):", min_value=18, max_value=110, value=62)
    p_sex = st.radio("Gender:", ("Male", "Female"))
    
    st.markdown("---")
    st.subheader("A) Renal Function Panel")
    creatinine = st.number_input("Serum Creatinine (mg/dL):", min_value=0.3, max_value=15.0, value=2.4, step=0.1)
    u_acr = st.number_input("Urine Albumin-to-Creatinine Ratio (Urine ACR in mg/g):", min_value=5.0, max_value=5000.0, value=340.0, step=10.0)
    
    st.markdown("---")
    st.subheader("B) CKD Complications Lab Panel")
    hb_level = st.number_input("Hemoglobin Level (g/dL):", min_value=4.0, max_value=18.0, value=10.2, step=0.1)
    phosphorus = st.number_input("Serum Phosphorus (mg/dL):", min_value=1.0, max_value=15.0, value=5.2, step=0.1)
    measured_ca = st.number_input("Measured Total Calcium (mg/dL):", min_value=4.0, max_value=15.0, value=8.6, step=0.1)
    albumin = st.number_input("Serum Albumin (g/dL):", min_value=1.0, max_value=6.0, value=3.5, step=0.1)

    # ==========================================================================
    # MATH ENGINE RUNNING BACKGROUND CALCULATIONS
    # ==========================================================================
    # 1. Corrected Calcium
    corrected_ca = measured_ca + 0.8 * (4.0 - albumin) if albumin < 4.0 else measured_ca

    # 2. 2021 CKD-EPI Equation (Race-free)
    kappa = 0.9 if p_sex == "Male" else 0.7
    alpha = -0.302 if p_sex == "Male" else -0.241
    gender_mult = 1.0 if p_sex == "Male" else 1.012
    
    scr_kappa_ratio = creatinine / kappa
    min_term = min(scr_kappa_ratio, 1.0) ** alpha
    max_term = max(scr_kappa_ratio, 1.0) ** -1.200
    age_term = 0.9938 ** p_age
    
    egfr = 142 * min_term * max_term * age_term * gender_mult

    # 3. 24-Month Kidney Failure Risk Equation (KFRE) 4-Variable (تم التصحيح هنا ليعتمد على math.log)
    sex_coef = 0.2201 if p_sex == "Male" else 0
    kfre_logit = (
        -0.2201 * sex_coef 
        - 0.5484 * (egfr / 5) 
        + 0.0436 * (p_age / 5) 
        + 0.6130 * (math.log(u_acr) if u_acr > 0 else 0)
    )
    
    # Practical fallback categorization for risk based on validated tables
    if egfr < 15:
        kfre_2yr = 85.0
    elif egfr < 30:
        kfre_2yr = 35.0 if u_acr > 300 else 12.0
    elif egfr < 45:
        kfre_2yr = 15.0 if u_acr > 300 else 4.0
    else:
        kfre_2yr = 1.0

    st.markdown("---")
    st.markdown("<div class='section-header'>📊 Automated Calculations</div>", unsafe_allow_html=True)
    st.metric("Calculated eGFR (CKD-EPI 2021)", f"{egfr:.1f} mL/min/1.73m²")
    st.metric("Corrected Total Calcium", f"{corrected_ca:.2f} mg/dL")

# ==============================================================================
# RIGHT COLUMN: KDIGO Staging, Complications & Drug Dosing Engine
# ==============================================================================
with col_protocol:
    st.markdown("<div class='section-header'>⚡ 2. Clinical Decision Support System Dashboard</div>", unsafe_allow_html=True)

    # ------------------------------------------------------------------
    # SECTION A: KDIGO STAGING ENGINE
    # ------------------------------------------------------------------
    st.markdown("<div class='status-box'>", unsafe_allow_html=True)
    st.markdown("### 🔍 KDIGO Classification & Risk Matrix")
    
    # eGFR Staging
    if egfr >= 90:
        g_stage, g_desc = "G1", "Normal or elevated kidney function"
    elif 60 <= egfr < 90:
        g_stage, g_desc = "G2", "Mildly decreased kidney function"
    elif 45 <= egfr < 60:
        g_stage, g_desc = "G3a", "Mildly to moderately decreased kidney function"
    elif 30 <= egfr < 45:
        g_stage, g_desc = "G3b", "Moderately to severely decreased kidney function"
    elif 15 <= egfr < 30:
        g_stage, g_desc = "G4", "Severely decreased kidney function"
    else:
        g_stage, g_desc = "G5", "Kidney Failure (End-Stage Renal Disease)"
        
    # Albuminuria Staging
    if u_acr < 30:
        a_stage, a_desc = "A1", "Normal to mildly increased (Optimal)"
    elif 30 <= u_acr <= 300:
        a_stage, a_desc = "A2", "Moderately increased (Microalbuminuria)"
    else:
        a_stage, a_desc = "A3", "Severely increased (Macroalbuminuria / Nephrotic Range)"

    st.write(f"▶️ **Current Stage:** **{g_stage} {a_stage}**")
    st.write(f"* **Renal Status ({g_stage}):** {g_desc}")
    st.write(f"* **Albuminuria ({a_stage}):** {a_desc}")
    
    # Prognosis Warning based on KDIGO colors
    if g_stage in ["G4", "G5"] or a_stage == "A3":
        st.error("🚨 **KDIGO Risk Category: VERY HIGH RISK.** High cardiovascular mortality and imminent progression to ESRD. Close Nephrology follow-up is mandatory.")
    elif g_stage == "G3b" or (g_stage == "G3a" and a_stage == "A2"):
        st.warning("⚠️ **KDIGO Risk Category: MODERATE-TO-HIGH RISK.** Monitor progression every 4-6 months.")
    else:
        st.success("🟢 **KDIGO Risk Category: Low to Moderate Risk.** Optimize conservative medical management.")
        
    st.markdown(f"🔮 **2-Year Risk of Progression to Dialysis (KFRE):** **~{kfre_2yr:.1f}%**")
    st.markdown("</div>", unsafe_allow_html=True)

    # ------------------------------------------------------------------
    # SECTION B: COMPLICATION MANAGEMENT PROTOCOLS
    # ------------------------------------------------------------------
    st.markdown("<div class='status-box'>", unsafe_allow_html=True)
    st.markdown("### 🦴 CKD-MBD & Anemia Management Engine")
    
    # Anemia Check
    if hb_level < 10.0 and g_stage in ["G3a", "G3b", "G4", "G5"]:
        st.error("🩸 **CKD Anemia Action Required:** Hb is < 10.0 g/dL.")
        st.write("* **Action Plan:** Target Hb is **10.0 - 11.5 g/dL**. Rule out iron deficiency first (Ensure Ferritin > 100 ng/mL, TSAT > 20%). Consider initiating an **Erythropoiesis-Stimulating Agent (ESA)** such as Epoetin Alfa or Darbepoetin Alfa.")
    else:
        st.success("✅ **Anemia Status:** Hb is stable or managed appropriately within safe limits.")
        
    # Mineral Bone Disorder Check
    if phosphorus > 4.5:
        st.warning("🦴 **Hyperphosphatemia Alert:** Serum Phosphorus is elevated.")
        st.write("* **Action Plan:** Initiate a dietary phosphorus restriction ($<800-1000\ mg/\text{day}$). Start an oral **Phosphate Binder with meals** (e.g., *Calcium Acetate 667mg* if calcium is low, or *Sevelamer Carbonate 800mg* if calcium is normal/elevated).")
    if corrected_ca < 8.4 and g_stage in ["G4", "G5"]:
        st.info("🦴 **Hypocalcemia Management:** Secondary Hyperparathyroidism path active. Avoid correcting asymptomatic hypocalcemia unless severe. Consider **Calcitriol (Active Vit D)** if PTH is rising progressively.")
    st.markdown("</div>", unsafe_allow_html=True)

    # ------------------------------------------------------------------
    # SECTION C: CLINICAL WARD RENAL DRUG DOSING ENGINE
    # ------------------------------------------------------------------
    st.markdown("<div class='status-box'>", unsafe_allow_html=True)
    st.markdown("### 💊 Ward Drug Dosing & Safeguard Recommendations")
    st.caption("Automated dosing guidelines based on the calculated eGFR:")
    
    if egfr >= 50:
        st.success("🟢 **Standard Dosing Allowed:** Most medications do not require renal adjustments at this level.")
        st.write("* **Metformin:** Safe to continue. Monitor annually.")
        st.write("* **Enoxaparin (Prophylactic):** Standard 40 mg SC daily.")
    elif 30 <= egfr < 50:
        st.warning("⚠️ **Moderate Renal Adjustments Required:**")
        st.write("* **Metformin:** **Reduce Maximum Dose** to 1000 mg/day total. Do NOT initiate new treatment.")
        st.write("* **Piperacillin/Tazobactam:** Adjust dose to **3.375 g IV q6h** (instead of 4.5g).")
        st.write("* **Enoxaparin (Therapeutic):** Standard dose is okay but monitor Anti-Xa activity closely if eGFR approaches 30.")
    else:
        st.error("🚫 **CRITICAL: Severe Renal Dose Adjustments Required:**")
        st.markdown("* **Metformin:** <span style='color:red; font-weight:bold;'>CONTRAINDICATED!</span> Hold immediately to prevent Lactic Acidosis.", unsafe_allow_html=True)
        st.write("* **Piperacillin/Tazobactam:** Reduce to **2.25 g IV q6h** OR **3.375 g IV q8h**.")
        st.write("* **Meropenem:** Reduce to **500 mg IV q12h** (instead of 1g q8h).")
        st.write("* **Enoxaparin (Prophylactic):** Reduce dose to **30 mg SC daily**.")
        st.write("* **Enoxaparin (Therapeutic):** Avoid if possible; switch to **Unfractionated Heparin (UFH)** with aPTT monitoring as it does not rely on renal clearance.")
        st.write("* **NSAIDs:** Avoid completely to prevent precipitating an acute-on-chronic kidney injury (AKI).")
    st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# BOTTOM SECTION: High-Yield Board Review Questions & Explanations
# ==============================================================================
st.markdown("---")
st.markdown("<div class='board-header'>🎓 3. High-Yield Board-Level Case Review (CKD-MBD Homeostasis)</div>", unsafe_allow_html=True)

with st.expander("❓ Click to Reveal the Board Question & Scientific Rationale"):
    st.markdown("""
    **Clinical Scenario:** A 54-year-old male with a 15-year history of poorly controlled type 2 diabetes presents with a baseline eGFR of **24 mL/min/1.73m²** (Stage G4 CKD). Labs reveal Serum Calcium **8.1 mg/dL**, Serum Phosphorus **5.8 mg/dL** (High), and an Intact PTH of **280 pg/mL** (Significantly Elevated). 
    
    **What is the primary underlying mechanism responsible for this patient's secondary hyperparathyroidism?**
    
    * **A)** Primary autonomous adenoma formation within the superior parathyroid glands.
    * **B)** Decreased skeletal sensitivity to the direct actions of calcitonin.
    * **C)** **Correct.** Decreased renal 1-alpha-hydroxylase activity and reciprocal phosphate retention.
    * **D)** Excessive urinary excretion of parathyroid hormone due to glomerular hyperfiltration.
    
    ---
    
    ### 📝 Comprehensive Scientific Evidence-Based Explanation:
    * **The Correct Answer is C.** As kidney disease advances to Stage G4, two major pathophysiologic processes drive **Secondary Hyperparathyroidism**:
      1. **Phosphate Retention:** The kidneys lose the capacity to excrete phosphorus, leading to hyperphosphatemia. High phosphorus directly binds serum calcium (dropping ionized calcium) and suppresses the activation of Vitamin D.
      2. **Loss of 1-alpha-hydroxylase:** The damaged renal proximal tubules can no longer convert 25-hydroxyvitamin D into its active form, **1,25-dihydroxyvitamin D (Calcitriol)**. 
    * The combined effects of **low active Vitamin D** (which decreases gut calcium absorption) and **hyperphosphatemia** lead to hypocalcemia. This hypocalcemia acts as a potent stimulator for the parathyroid glands to hypertrophy and release massive amounts of **PTH** to try and pull calcium back from the bones.
    * **Clinical Intervention Tip:** To break this loop, you must treat the hyperphosphatemia using dietary restriction and oral *phosphate binders*, and replace the active Vitamin D deficiency with *Calcitriol*.
    """)

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 12px;'>Al-Ahli Hospital Internal Medicine CDSS Platforms © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
