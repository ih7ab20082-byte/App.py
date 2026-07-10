import streamlit as st

# Page Configuration for a dedicated GI Bleeding tool
st.set_page_config(
    page_title="Al-Ahli Hospital Upper GI Bleeding Protocol",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Medical Branding Styles
st.markdown("""
    <style>
    .main-title { font-size:32px !important; font-weight: bold; color: #7F1D1D; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:16px !important; color: #4B5563; text-align: center; margin-bottom: 25px; font-style: italic; }
    .branding-bar { background-color: #FFF5F5; padding: 20px; border-radius: 10px; border-left: 6px solid #B91C1C; margin-bottom: 25px; }
    .branding-bar strong { color: #7F1D1D !important; font-weight: bold; }
    .branding-text { color: #1F2937 !important; font-size: 16px !important; line-height: 1.6; }
    .section-header { font-size:22px !important; font-weight: bold; color: #7F1D1D; margin-top: 15px; margin-bottom: 15px; }
    .board-header { font-size:20px !important; font-weight: bold; color: #D97706; margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<div class='main-title'>🩸 Al-Ahli Hospital Acute Upper GI Bleeding Platform</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Clinical Decision Support Tool & Risk Stratification Engine</div>", unsafe_allow_html=True)

# Professional Badge
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Project Founder & Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Focus:</strong> Variceal vs Non-Variceal Pathways & Glasgow-Blatchford Integration
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Layout Split
col_input, col_protocol = st.columns([1, 1.2])

# ==============================================================================
# LEFT COLUMN: Patient Demographics & Lab Inputs for GBS Scoring
# ==============================================================================
with col_input:
    st.markdown("<div class='section-header'>📋 1. Clinical Presentation & Lab Inputs</div>", unsafe_allow_html=True)
    
    # Vital Signs
    sbp = st.number_input("Systolic Blood Pressure (SBP mmHg):", min_value=50, max_value=220, value=105)
    hr = st.number_input("Heart Rate (bpm):", min_value=30, max_value=200, value=110)
    
    st.markdown("---")
    # Laboratory Values
    hb = st.number_input("Hemoglobin (g/dL):", min_value=3.0, max_value=18.0, value=8.5, step=0.1)
    bun = st.number_input("Blood Urea Nitrogen (BUN mg/dL):", min_value=5, max_value=150, value=35)
    
    st.markdown("---")
    # Clinical Presentations (GBS Components)
    presentation = st.multiselect(
        "Select Presentation Symptoms / Signs:",
        ["Melena (Black tarry stools)", "Syncope (Fainting / Collapse)"]
    )
    
    # Comorbidities (GBS Components)
    comorbidities = st.multiselect(
        "Known Comorbidities / Medical History:",
        ["Hepatic Disease / Cirrhosis", "Cardiac Failure / Heart Failure"]
    )

    # ------------------------------------------------------------------
    # GLASGOW-BLATCHFORD SCORE (GBS) CALCULATION ENGINE
    # ------------------------------------------------------------------
    gbs_score = 0
    
    # BUN Component
    if 18.2 <= bun < 28.0: gbs_score += 2
    elif 28.0 <= bun < 70.0: gbs_score += 3
    elif bun >= 70.0: gbs_score += 4
    
    # Hemoglobin Component
    if hb < 10.0: gbs_score += 6  # Simplified for general flow, standard accounts for gender
    elif 10.0 <= hb < 12.0: gbs_score += 3
    elif 12.0 <= hb < 13.0: gbs_score += 1
        
    # Systolic BP Component
    if sbp < 90: gbs_score += 3
    elif 90 <= sbp < 100: gbs_score += 2
    elif 100 <= sbp < 110: gbs_score += 1
        
    # Heart Rate Component
    if hr >= 100: gbs_score += 1
    
    # Presentation Features
    if "Melena (Black tarry stools)" in presentation: gbs_score += 1
    if "Syncope (Fainting / Collapse)" in presentation: gbs_score += 2
        
    # History Comorbidities
    if "Hepatic Disease / Cirrhosis" in comorbidities: gbs_score += 2
    if "Cardiac Failure / Heart Failure" in comorbidities: gbs_score += 2

    st.markdown("---")
    st.markdown("<div class='section-header'>📊 Risk Stratification Output</div>", unsafe_allow_html=True)
    st.metric("Glasgow-Blatchford Score (GBS)", f"{gbs_score} / 23", 
              delta="High Risk (Needs Admission)" if gbs_score > 1 else "Low Risk (Potential Outpatient)")

# ==============================================================================
# RIGHT COLUMN: Clinical Pathways & Local Adaptive Protocols
# ==============================================================================
with col_protocol:
    st.markdown("<div class='section-header'>⚡ 2. Definitive Acute Management Protocols</div>", unsafe_allow_html=True)
    
    # Resuscitation Thresholds
    st.markdown("### 🩸 Phase I: Initial Resuscitation & Transfusion Strategy")
    if "Hepatic Disease / Cirrhosis" in comorbidities:
        st.warning("⚠️ **RESTRICTIVE TRANSFUSION MANDATE:** Patient has Cirrhosis. Target Hemoglobin strictly **7.0 - 8.0 g/dL**. Do NOT over-transfuse, as expanding intravascular volume increases portal pressure and precipitates massive re-bleeding from Varices!")
    else:
        if hb < 7.0:
            st.error("🚨 CRITICAL ANEMIA: Hemoglobin < 7.0 g/dL. Cross-match and transfuse 1 Unit of Packed Red Blood Cells (PRBCs) immediately.")
        else:
            st.success("✅ Hemoglobin ≥ 7.0 g/dL. Hold routine blood transfusion unless patient exhibits active hemodynamic instability / hemorrhagic shock.")

    st.markdown("---")

    # Pathway Splitter: Variceal vs Non-Variceal
    st.markdown("### 🛠️ Phase II: Pathway Differentiation & Medication Commands")
    
    if "Hepatic Disease / Cirrhosis" in comorbidities:
        st.error("🔴🔴 PATHWAY A: SUSPECTED VARICEAL BLEEDING PROTOCOL ACTIVATED")
        st.markdown("""
        * **Vasoactive Therapy (Stat):** Start **Octreotide** continuous infusion immediately. 
            * *Bolus Dose:* **50 mcg IV STAT**.
            * *Infusion Rate:* **50 mcg/hour continuous IV** (Maintain for 2-5 days).
        * **Prophylactic Antibiotics (Mandatory Local Protocol):** Start **Ceftriaxone 1g IV every 24 hours**. 
            * *Rationale:* Reduces bacterial translocation, peritonitis risk, and markedly decreases mortality in cirrhotic bleeding.
        * **Urgent GI Consultation:** Arrange for Diagnostic/Therapeutic Esophagogastroduodenoscopy (EGD) for **Variceal Band Ligation** within 12 hours.
        """)
    else:
        st.warning("🟡🟡 PATHWAY B: SUSPECTED NON-VARICEAL BLEEDING PROTOCOL (Peptic Ulcer)")
        st.markdown("""
        * **Proton Pump Inhibitor (PPI) High-Dose Protocol:** Start **Omeprazole / Pantoprazole**.
            * *Bolus Dose:* **80 mg IV Push STAT**.
            * *Continuous Infusion:* **8 mg/hour** continuous IV infusion for 72 hours (Alternatively: 40mg IV every 12 hours according to updated local hospital guidelines if infusion pumps are unavailable).
        * **GI Consultation:** Arrange for EGD within 24 hours to identify and treat ulcer base (e.g., clipping, epinephrine injection).
        """)

    st.markdown("""
    ---
    **🔬 Mandatory Safeguards:**
    * [ ] Secure **two large-bore peripheral IV lines** (14G or 16G) immediately.
    * [ ] Keep the patient strictly **NPO** (Nothing Per Os).
    * [ ] Stop and hold all NSAIDs, Aspirin, Anticoagulants, and Antiplatelets.
    """)

# ==============================================================================
# BOTTOM SECTION: High-Yield Board Review Questions & Explanations
# ==============================================================================
st.markdown("---")
st.markdown("<div class='board-header'>🎓 3. High-Yield Board-Level Case Review (GI Bleeding & Portal Hypertension Focus)</div>", unsafe_allow_html=True)
st.caption("A classic board trap regarding the choice of antibiotics and transfusion boundaries in Upper GI Bleeding.")

with st.expander("❓ Click to Reveal the Board Question & Scientific Rationale"):
    st.markdown("""
    **Clinical Scenario:** A 45-year-old male with a known history of Child-Pugh Class B Liver Cirrhosis presents to the emergency room with 3 episodes of large-volume hematemesis. His blood pressure is 95/60 mmHg, and heart rate is 112 bpm. Laboratory studies show a Hemoglobin of **7.4 g/dL** and platelets of 65,000. 
    
    **In addition to aggressive fluid resuscitation, which of the following represents the most appropriate immediate medical intervention to reduce this patient's mortality?**
    
    * **A)** Transfuse 3 units of Packed Red Blood Cells to bring the Hemoglobin above 10 g/dL.
    * **B)** **Correct.** Initiate empirical IV Ceftriaxone 1g daily and start an IV Octreotide infusion.
    * **C)** Administer empirical Oral Amoxicillin and Clarithromycin for H. pylori eradication.
    * **D)** Give a bolus of IV Tranexamic Acid (TXA) to stabilize the clot structure.
    
    ---
    
    ### 📝 Comprehensive Scientific Evidence-Based Explanation:
    * **The Correct Answer is B.** In cirrhotic patients presenting with upper GI bleeding, bacterial infection occurs in up to 20% of cases within 48 hours of admission and is associated with early re-bleeding and higher mortality. **Prophylactic antibiotics (Ceftriaxone)** are a Grade 1A recommendation because they significantly decrease infectious complications and overall mortality. Combined with **Octreotide** (which causes splanchnic vasoconstriction to decrease portal pressures), this forms the medical cornerstone before endoscopy.
    * **The Over-Transfusion Trap (Critique of A):** A liberal transfusion strategy targeting Hb > 9 or 10 g/dL is associated with increased re-bleeding and higher mortality in variceal hemorrhage. A **restrictive transfusion target (7.0 - 8.0 g/dL)** must be strictly followed.
    * **Tranexamic Acid Note (Critique of D):** The HALT-IT trial demonstrated that TXA does *not* reduce mortality in gastrointestinal bleeding and is associated with an increased risk of venous thromboembolic events; thus, it is not indicated here.
    """)

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 12px;'>Al-Ahli Hospital Internal Medicine CDSS Platforms © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
