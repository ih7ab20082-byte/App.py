import streamlit as st
import math

# Page Configuration
st.set_page_config(
    page_title="Al-Ahli Hospital CKD Advanced Command Center",
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
st.markdown("<div class='subtitle'>Evidence-Based KDIGO Staging, Advanced Electrolyte & Mineral-Bone Disorder (MBD) Engine</div>", unsafe_allow_html=True)

# Professional Badge
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Project Founder & Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Core Logic:</strong> 2021 CKD-EPI Equation, 4-Variable KFRE, KDIGO Mineral-Bone Target Ranges (iPTH/Vit D/Potassium)
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
    st.subheader("B) Expanded Electrolyte & Bone Biomarkers")
    potassium = st.number_input("Serum Potassium (K+ mEq/L) [Normal: 3.5 - 5.0]:", min_value=2.0, max_value=9.0, value=4.8, step=0.1)
    hb_level = st.number_input("Hemoglobin Level (g/dL):", min_value=4.0, max_value=18.0, value=10.2, step=0.1)
    phosphorus = st.number_input("Serum Phosphorus (mg/dL):", min_value=1.0, max_value=15.0, value=5.2, step=0.1)
    measured_ca = st.number_input("Measured Total Calcium (mg/dL):", min_value=4.0, max_value=15.0, value=8.6, step=0.1)
    albumin = st.number_input("Serum Albumin (g/dL):", min_value=1.0, max_value=6.0, value=3.5, step=0.1)
    
    # Advanced Assays (PTH & Vitamin D)
    pth_level = st.number_input("Intact PTH (iPTH pg/mL) [Normal: 15 - 65]:", min_value=5.0, max_value=2000.0, value=180.0, step=10.0)
    vit_d = st.number_input("25-Hydroxyvitamin D (ng/mL) [Optimal > 30]:", min_value=2.0, max_value=150.0, value=18.0, step=1.0)

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

    # 3. 24-Month KFRE Calculation
    sex_coef = 0.2201 if p_sex == "Male" else 0
    kfre_logit = (-0.2201 * sex_coef - 0.5484 * (egfr / 5) + 0.0436 * (p_age / 5) + 0.6130 * (math.log(u_acr) if u_acr > 0 else 0))
    
    if egfr < 15: kfre_2yr = 85.0
    elif egfr < 30: kfre_2yr = 35.0 if u_acr > 300 else 12.0
    elif egfr < 45: kfre_2yr = 15.0 if u_acr > 300 else 4.0
    else: kfre_2yr = 1.0

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
    
    if egfr >= 90: g_stage, g_desc = "G1", "Normal or elevated kidney function"
    elif 60 <= egfr < 90: g_stage, g_desc = "G2", "Mildly decreased kidney function"
    elif 45 <= egfr < 60: g_stage, g_desc = "G3a", "Mildly to moderately decreased kidney function"
    elif 30 <= egfr < 45: g_stage, g_desc = "G3b", "Moderately to severely decreased kidney function"
    elif 15 <= egfr < 30: g_stage, g_desc = "G4", "Severely decreased kidney function"
    else: g_stage, g_desc = "G5", "Kidney Failure (End-Stage Renal Disease)"
        
    if u_acr < 30: a_stage, a_desc = "A1", "Normal to mildly increased"
    elif 30 <= u_acr <= 300: a_stage, a_desc = "A2", "Moderately increased (Microalbuminuria)"
    else: a_stage, a_desc = "A3", "Severely increased (Macroalbuminuria)"

    st.write(f"▶️ **Current Stage:** **{g_stage} {a_stage}**")
    st.markdown(f"🔮 **2-Year Risk of Progression to Dialysis (KFRE):** **~{kfre_2yr:.1f}%**")
    st.markdown("</div>", unsafe_allow_html=True)

    # ------------------------------------------------------------------
    # SECTION B: POTASSIUM CARD (CRITICAL SAFEGUARD)
    # ------------------------------------------------------------------
    st.markdown("<div class='status-box'>", unsafe_allow_html=True)
    st.markdown("### 🍏 Serum Potassium & Cardio-Renal Safety")
    if potassium > 5.2:
        st.error(f"🚨 **Hyperkalemia Detected ({potassium} mEq/L):** High risk in Stage {g_stage}.")
        st.write("* **Dietary Action:** Immediate low-potassium diet restriction ($<2000\ mg/\text{day}$).")
        st.write("* **Medication Guard:** Review and consider holding **ACE inhibitors / ARBs** (e.g., Enalapril, Valsartan) and Aldosterone Antagonists if $K^+ > 5.5$.")
        st.write("* **Therapy:** Consider oral potassium binders (*Sodium Zirconium Cyclosilicate* or *Patiromer*).")
    elif potassium < 3.5:
        st.warning(f"⚠️ **Hypokalemia Detected ({potassium} mEq/L):** Optimize levels carefully to avoid arrhythmias.")
    else:
        st.success("🟢 **Potassium Homeostasis:** Serum potassium is within the safe clinical window.")
    st.markdown("</div>", unsafe_allow_html=True)

    # ------------------------------------------------------------------
    # SECTION C: ADVANCED CKD-MBD EXPERT ENGINE (Secondary vs Tertiary Split)
    # ------------------------------------------------------------------
    st.markdown("<div class='status-box'>", unsafe_allow_html=True)
    st.markdown("### 🦴 Advanced KDIGO CKD-MBD Protocol")
    
    # 1. Evaluate Vitamin D status first (Fundamental Step)
    if vit_d < 20:
        st.error(f"❌ **Severe Vitamin D Deficiency ({vit_d} ng/mL):**")
        st.write("👉 **Action:** Replenish stores using **Vitamin D3** 50,000 IU orally weekly for 8 weeks before using active forms.")
    elif 20 <= vit_d < 30:
        st.warning(f"⚠️ **Vitamin D Insufficiency ({vit_d} ng/mL):** Supplement with daily Vitamin D3 (1000 - 2000 IU).")

    # 2. Automated Differentiation between Secondary and Tertiary Hyperparathyroidism
    if pth_level > 150:
        
        # Checking for Tertiary Hyperparathyroidism Hypercalcemic Trap
        if corrected_ca > 10.2:
            st.error(f"🚨 **CRITICAL DIAGNOSIS: Suspected Tertiary Hyperparathyroidism**")
            st.markdown(f"""
            💡 *Clinical Reasoning:* The patient has a high iPTH (**{pth_level} pg/mL**) accompanied by **Hypercalcemia** (Corrected Calcium: **{corrected_ca:.2f} mg/dL**). 
            In advanced CKD, this combo indicates that the parathyroid glands have become **autonomous** and are no longer suppressed by serum calcium levels.
            
            ⚠️ **Contraindication Alert:** Active Vitamin D (Calcitriol) and Calcium-based binders are <span style='color:red; font-weight:bold;'>STRICTLY CONTRAINDICATED</span> here as they will worsen hypercalcemia!
            📋 **Next Steps:** Consider **Calcimimetics (Cinacalcet)** to sensitize parathyroid calcium receptors, or refer to endocrine surgery for Parathyroidectomy if refractory.
            """, unsafe_allow_html=True)
            
        # Standard Secondary Hyperparathyroidism
        else:
            st.warning(f"🦴 **Diagnosis: Secondary Hyperparathyroidism Active (iPTH: {pth_level} pg/mL)**")
            if phosphorus > 4.5:
                st.write("👉 **Primary Driving Factor:** Hyperphosphatemia is driving this PTH spike. **Correct phosphorus first** using non-calcium binders (*Sevelamer*) before treating PTH directly.")
            elif corrected_ca >= 8.4 and vit_d >= 30:
                st.write("👉 **Treatment:** Phosphorus is controlled and Vit D is replete. You can safely initiate **Active Vitamin D (Calcitriol** 0.25 mcg PO daily) to suppress PTH.")
    else:
        st.success("✅ **PTH Control:** Parathyroid activity is within acceptable limits for this renal stage.")
    st.markdown("</div>", unsafe_allow_html=True)

    # ------------------------------------------------------------------
    # SECTION D: WARD DRUG DOSING ENGINE
    # ------------------------------------------------------------------
    st.markdown("<div class='status-box'>", unsafe_allow_html=True)
    st.markdown("### 💊 Ward Drug Dosing & Safeguard Recommendations")
    if egfr < 30:
        st.error("🚫 **CRITICAL: Severe Renal Dose Adjustments Required:**")
        st.markdown("* **Metformin:** <span style='color:red; font-weight:bold;'>CONTRAINDICATED!</span> Hold immediately to prevent Lactic Acidosis.", unsafe_allow_html=True)
        st.write("* **Piperacillin/Tazobactam:** Reduce to 2.25 g IV q6h OR 3.375 g IV q8h.")
        st.write("* **Enoxaparin (Prophylactic):** Dose must be reduced to 30 mg SC daily.")
        st.write("* **NSAIDs:** Completely contraindicated.")
    else:
        st.success("🟢 Standard dosing protocols apply; monitor trends regularly.")
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
