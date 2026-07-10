import streamlit as st

# Page Configuration for the Ultimate Calcium Command Center
st.set_page_config(
    page_title="Al-Ahli Hospital Comprehensive Calcium Engine",
    page_icon="🦴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Medical Branding Styles
st.markdown("""
    <style>
    .main-title { font-size:32px !important; font-weight: bold; color: #1E3A8A; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:16px !important; color: #4B5563; text-align: center; margin-bottom: 25px; font-style: italic; }
    .branding-bar { background-color: #F0F4F8; padding: 20px; border-radius: 10px; border-left: 6px solid #1E3A8A; margin-bottom: 25px; }
    .branding-bar strong { color: #1E3A8A !important; font-weight: bold; }
    .branding-text { color: #1F2937 !important; font-size: 16px !important; line-height: 1.6; }
    .section-header { font-size:22px !important; font-weight: bold; color: #1E3A8A; margin-top: 15px; margin-bottom: 15px; }
    .board-header { font-size:20px !important; font-weight: bold; color: #D97706; margin-top: 15px; }
    .dx-box { background-color: #F9FAFB; padding: 20px; border-radius: 8px; border: 1px solid #E5E7EB; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<div class='main-title'>🦴 Al-Ahli Hospital Comprehensive Calcium Diagnostic Engine</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Advanced Decision Support System: PICO & Evidence-Based Architecture</div>", unsafe_allow_html=True)

# Professional Badge
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Project Founder & Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Clinical Features:</strong> Automated FEca Calculator, PTHrP Tumor Tracker & Next-Step Checklist
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Layout Split
col_input, col_protocol = st.columns([1, 1.2])

# ==============================================================================
# LEFT COLUMN: Full Lab Panel (Serum + Urine + Specialized)
# ==============================================================================
with col_input:
    st.markdown("<div class='section-header'>🧪 1. Comprehensive Laboratory Input Panel</div>", unsafe_allow_html=True)
    
    st.subheader("A) Baseline Serum Panel")
    measured_ca = st.number_input("Measured Serum Total Calcium (mg/dL):", min_value=3.0, max_value=20.0, value=11.2, step=0.1)
    albumin = st.number_input("Serum Albumin (g/dL):", min_value=1.0, max_value=6.0, value=3.2, step=0.1)
    creatinine = st.number_input("Serum Creatinine (mg/dL):", min_value=0.3, max_value=15.0, value=1.0, step=0.1)
    
    st.markdown("---")
    st.subheader("B) Advanced Endocrine & Tumor Panel")
    pth_level = st.number_input("Intact PTH Level (pg/mL) [Normal: 15-65]:", min_value=1.0, max_value=1500.0, value=75.0, step=1.0)
    
    pthrh_available = st.checkbox("Is PTHrP (PTH-related Peptide) result available?")
    if pthrh_available:
        pthrp_status = st.radio("PTHrP Status:", ("Elevated / Positive", "Normal / Suppressed"))
    else:
        pthrp_status = "Not Checked"
        
    phosphorus = st.number_input("Serum Phosphorus (mg/dL):", min_value=0.5, max_value=15.0, value=2.2, step=0.1)
    magnesium = st.number_input("Serum Magnesium (mg/dL):", min_value=0.2, max_value=5.0, value=1.8, step=0.1)

    st.markdown("---")
    st.subheader("C) 24-Hour Urine Panel (For Hypercalcemia Differentiation)")
    urine_labs_available = st.checkbox("Are 24-Hour Urine Calcium/Creatinine available?")
    if urine_labs_available:
        u_calcium = st.number_input("24-Hour Urine Calcium (mg/24h):", min_value=10.0, max_value=1000.0, value=250.0, step=10.0)
        u_creatinine = st.number_input("24-Hour Urine Creatinine (mg/24h):", min_value=200.0, max_value=3000.0, value=1000.0, step=50.0)
    
    # 1. Corrected Calcium Math
    if albumin < 4.0:
        corrected_ca = measured_ca + 0.8 * (4.0 - albumin)
    else:
        corrected_ca = measured_ca

    # 2. FEca Calculation Math (if urine inputs are active)
    feca = None
    if urine_labs_available and u_creatinine > 0 and measured_ca > 0:
        # FEca Formula: (Urine Ca * Serum Cr) / (Serum Ca * Urine Cr)
        feca = (u_calcium * creatinine) / (measured_ca * u_creatinine)

    st.markdown("---")
    st.markdown("<div class='section-header'>📊 Homeostatic Baseline</div>", unsafe_allow_html=True)
    st.metric("Corrected Total Calcium", f"{corrected_ca:.2f} mg/dL")
    if feca is not None:
        st.metric("Fractional Excretion of Calcium (FEca)", f"{feca*100:.2f}%")

# ==============================================================================
# RIGHT COLUMN: The Algorithmic Approach & Differential Mapping
# ==============================================================================
with col_protocol:
    st.markdown("<div class='section-header'>⚡ 2. Diagnostic Approach & Verification</div>", unsafe_allow_html=True)

    # ------------------------------------------------------------------
    # MAIN BRANCH A: HYPERCALCEMIA
    # ------------------------------------------------------------------
    if corrected_ca > 10.5:
        st.error("🔴 CLINICAL PATHWAY: HYPERCALCEMIA EVALUATION")
        
        st.markdown("<div class='dx-box'>", unsafe_allow_html=True)
        st.markdown("### 🔍 Algorithmic Etiology Engine:")
        
        # Scenario 1: High PTH (PHPT vs FHH Trap)
        if pth_level > 55:
            st.markdown("#### 🧬 PTH-Dependent Pattern Detected (PTH is High/Inappropriate)")
            
            if urine_labs_available and feca is not None:
                if feca < 0.01:
                    st.markdown("🎯 **Definitive Diagnosis:** **Familial Hypocalciuric Hypercalcemia (FHH)**")
                    st.markdown("💡 *Evidence-Based Reasoning:* High serum calcium and high PTH, but a **FEca < 1%** confirms the kidneys are reabsorbing calcium aberrantly due to a CASR gene mutation. **This is a benign condition.**")
                    st.markdown("📋 **CRITICAL NEXT STEP:**")
                    st.error("🚫 **DO NOT REFER TO SURGERY.** Cancel any planned parathyroidectomy. Reassure the patient and screen first-degree relatives.")
                elif feca > 0.02:
                    st.markdown("🎯 **Definitive Diagnosis:** **Primary Hyperparathyroidism (PHPT)**")
                    st.markdown("💡 *Evidence-Based Reasoning:* High serum calcium, high PTH, low phosphorus, and a **FEca > 2%** confirms renal dumping of calcium, typical of an autonomous parathyroid adenoma.")
                    st.markdown("📋 **RECOMMENDED NEXT STEPS:**")
                    st.write("* [ ] Order a **Parathyroid Sestamibi Scan** and Neck Ultrasound for adenoma localization.")
                    st.write("* [ ] Evaluate for surgical criteria (Age <50, T-score <-2.5, or GFR <60).")
                else:
                    st.warning("⚠️ **Borderline FEca (1% - 2%):** Non-diagnostic zone. Review 24-hour total urine volume, vitamin D status, or repeat the clearance panel.")
            else:
                st.info("ℹ️ **Differential Pending:** PTH is high. This could be **Primary Hyperparathyroidism** OR **FHH**. To avoid unnecessary surgical neck exploration, you must calculate the FEca.")
                st.markdown("📋 **MANDATORY NEXT STEP:**")
                st.warning("🧪 Please check the box on the left and enter **24-Hour Urine Calcium and Creatinine** to unlock the differential logic.")

        # Scenario 2: Suppressed PTH (Malignancy Focus)
        elif pth_level < 20:
            st.markdown("#### 🦀 PTH-Independent Pattern Detected (PTH is Suppressed)")
            
            if pthrp_status == "Elevated / Positive":
                st.markdown("🎯 **Definitive Diagnosis:** **Humoral Hypercalcemia of Malignancy (HHM)**")
                st.markdown("💡 *Evidence-Based Reasoning:* Suppressed PTH with an **elevated PTHrP** confirms ectopic secretion of parathyroid hormone-related peptide by a tumor.")
                st.markdown("📋 **RECOMMENDED NEXT STEPS:**")
                st.write("* [ ] Urgent **CT Scan of the Chest, Abdomen, and Pelvis** to evaluate for solid tumors (e.g., Lung Squamous Cell, Renal Cell, or Ovarian Ca).")
                st.write("* [ ] Start immediate aggressive IV hydration and schedule **IV Bisphosphonates (Zoledronic Acid 4mg)**.")
            elif pthrp_status == "Normal / Suppressed":
                st.markdown("🎯 **Suspected Etiology:** **Local Osteolytic Hypercalcemia or Hematologic Malignancy**")
                st.markdown("💡 *Evidence-Based Reasoning:* PTH is suppressed and PTHrP is normal. This rules out humoral mechanisms and points toward direct bone destruction or other systemic pathways.")
                st.markdown("📋 **RECOMMENDED NEXT STEPS:**")
                st.write("* [ ] Order **SPEP / UPEP with Immunofixation** immediately to evaluate for **Multiple Myeloma**.")
                st.write("* [ ] Order a Skeletal Survey or Bone Scan to search for lytic/blastic lesions.")
            else:
                st.markdown("🎯 **Differential Diagnosis:** Malignancy vs. Granulomatous Disease.")
                st.markdown("📋 **MANDATORY NEXT STEP:**")
                st.warning("🔬 Check the **PTHrP** status on the left panel once results return to differentiate Humoral Malignancy from Multiple Myeloma / Sarcoidosis.")

        st.markdown("</div>", unsafe_allow_html=True)

    # ------------------------------------------------------------------
    # MAIN BRANCH B: HYPOCALCEMIA
    # ------------------------------------------------------------------
    elif corrected_ca < 8.5:
        st.warning("🔵 CLINICAL PATHWAY: HYPOCALCEMIA EVALUATION")
        
        st.markdown("<div class='dx-box'>", unsafe_allow_html=True)
        st.markdown("### 🔍 Algorithmic Etiology Engine:")
        
        if magnesium < 1.4:
            st.markdown("🎯 **Definitive Etiology:** **Hypomagnesemia-Induced Hypocalcemia**")
            st.markdown("💡 *Evidence-Based Reasoning:* Serum Magnesium is critically low ($<1.4\ mg/dL$). This paralyzes parathyroid function, inducing both PTH resistance and secretory failure.")
            st.markdown("📋 **MANDATORY NEXT STEP:**")
            st.error("💊 **STOP! Correct Magnesium first.** Order **Magnesium Sulfate 2g IV** over 1-2 hours. Calcium levels will remain completely refractory until magnesium homeostasis is restored!")
        elif pth_level < 15:
            st.markdown("🎯 **Most Probable Etiology:** **Primary Hypoparathyroidism**")
            st.markdown("💡 *Reasoning:* Hypocalcemia with failure of the parathyroid gland to secrete PTH.")
            st.markdown("📋 **RECOMMENDED NEXT STEPS:**")
            st.write("* [ ] Check for previous neck or thyroid surgery history.")
            st.write("* [ ] Prescribe oral Calcium + active **Calcitriol**.")
        else:
            st.markdown("🎯 **Most Probable Etiology:** **Secondary Hyperparathyroidism** (e.g., Vitamin D deficiency or advanced CKD).")
            st.markdown("📋 **RECOMMENDED NEXT STEPS:**")
            st.write("* [ ] Check Vitamin D (25-OH) and evaluate renal function.")

        st.markdown("</div>", unsafe_allow_html=True)

    else:
        st.success("✅ Calcium homeostasis is normal. No workup required.")

# ==============================================================================
# BOTTOM SECTION: High-Yield Board Review
# ==============================================================================
st.markdown("---")
st.markdown("<div class='board-header'>🎓 3. High-Yield Board-Level Case Review (FHH vs PHPT Surgery Trap)</div>", unsafe_allow_html=True)

with st.expander("❓ Click to Reveal the Board Question & Scientific Rationale"):
    st.markdown("""
    **Clinical Scenario:** A 32-year-old completely asymptomatic male is found to have a Serum Calcium of **11.4 mg/dL** during a routine insurance physical. His baseline Albumin is 4.0 g/dL, and Serum Creatinine is 0.9 mg/dL. An Intact PTH level is checked and returns elevated at **78 pg/mL**. The intern immediately schedules the patient for a neck ultrasound and a parathyroidectomy consultation. However, a 24-hour urine collection reveals a Urine Calcium of 60 mg/24h and Urine Creatinine of 1200 mg/24h.
    
    **What is the most appropriate management strategy for this patient?**
    
    * **A)** Proceed with urgent parathyroidectomy to prevent nephrolithiasis.
    * **B)** Start oral Cinacalcet to suppress parathyroid hormone secretion.
    * **C)** **Correct.** Cancel the surgery and reassure the patient; this is a benign genetic condition (FHH).
    * **D)** Administer high-dose IV Zoledronic Acid to protect bone mineral density.
    
    ---
    
    ### 📝 Comprehensive Scientific Evidence-Based Explanation:
    * **The Correct Answer is C.** This patient has **Familial Hypocalciuric Hypercalcemia (FHH)**. 
    * **The Math Breakdown:** Calculating the FEca for this patient:
      $$FEca = \frac{60 \times 0.9}{11.4 \times 1200} = \frac{54}{13680} = 0.0039\ \rightarrow\ \mathbf{0.39\%}$$
      Since the **FEca is significantly less than 1% (<0.01)**, it definitively rules out Primary Hyperparathyroidism (which typically features a FEca > 2%) and confirms FHH.
    * **The Clinical Lesson:** FHH is caused by an inactivating mutation in the Calcium-Sensing Receptor ($CASR$), meaning the body requires higher serum calcium levels to feel "normal." It is benign, does not cause target-organ damage, and **does not respond to surgery**. Performing a parathyroidectomy here is a major medical error!
    """)

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 12px;'>Al-Ahli Hospital Internal Medicine CDSS Platforms © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
