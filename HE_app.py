import streamlit as st
import math

# Page Configuration
st.set_page_config(
    page_title="Al-Ahli Hospital Hepatic Command Center",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for Clinical Rigor
st.markdown("""
    <style>
    .main-title { font-size:30px !important; font-weight: bold; color: #14532D; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:15px !important; color: #4B5563; text-align: center; margin-bottom: 25px; font-style: italic; }
    .branding-bar { background-color: #F0FDF4; padding: 20px; border-radius: 10px; border-left: 6px solid #14532D; margin-bottom: 25px; }
    .branding-bar strong { color: #14532D !important; font-weight: bold; }
    .branding-text { color: #1F2937 !important; font-size: 15px !important; line-height: 1.6; }
    .section-header { font-size:20px !important; font-weight: bold; color: #14532D; margin-top: 15px; margin-bottom: 15px; border-bottom: 2px solid #E5E7EB; padding-bottom: 5px; }
    .status-box { background-color: #F9FAFB; padding: 15px; border-radius: 8px; border: 1px solid #E5E7EB; margin-bottom: 15px; }
    .board-header { font-size:22px !important; font-weight: bold; color: #D97706; margin-top: 30px; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<div class='main-title'>🧠 Al-Ahli Hospital Hepatic Command Center</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Advanced Decision Support System for Cirrhosis Stratification, Paracentesis Stewardship & Hepatorenal Safeguards</div>", unsafe_allow_html=True)

# Professional Branding Block
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Project Founder & Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Clinical Core:</strong> AASLD & EASL 2024 Guidelines, MELD-Na Calculator, Ganzoni Iron Core, Post-Paracentesis Induced Circulatory Dysfunction (PICD) Prevention Protocols
    </div>
</div>
""", unsafe_allow_html=True)

# Layout Split
col_input, col_dashboard = st.columns([1, 1.2])

# ==============================================================================
# LEFT COLUMN: CLINICAL INPUT PANEL
# ==============================================================================
with col_input:
    st.markdown("<div class='section-header'>📋 1. Patient Demographics & Labs</div>", unsafe_allow_html=True)
    
    # Core Labs for Scores
    creatinine = st.number_input("Serum Creatinine (mg/dL):", min_value=0.4, max_value=15.0, value=1.1, step=0.1)
    bilirubin = st.number_input("Total Bilirubin (mg/dL):", min_value=0.3, max_value=40.0, value=2.4, step=0.1)
    inr = st.number_input("INR:", min_value=0.8, max_value=10.0, value=1.6, step=0.1)
    sodium = st.number_input("Serum Sodium (mEq/L):", min_value=110, max_value=160, value=133, step=1)
    albumin = st.number_input("Serum Albumin (g/dL):", min_value=1.0, max_value=5.5, value=2.8, step=0.1)
    
    st.markdown("<div class='section-header'>🌊 2. Paracentesis Fluid Tracker</div>", unsafe_allow_html=True)
    is_paracentesis = st.checkbox("Patient underwent Therapeutic Paracentesis (Ascitic Tap) today", value=False)
    ascitic_volume = st.number_input("Volume of Ascitic Fluid Removed (Liters):", min_value=0.0, max_value=20.0, value=6.5, step=0.5) if is_paracentesis else 0.0

    st.markdown("<div class='section-header'>🧠 3. Hepatic Encephalopathy Status</div>", unsafe_allow_html=True)
    he_stage = st.selectbox(
        "West Haven Criteria Grade:",
        ["Grade 0: Normal", 
         "Grade 1: Trivial lack of awareness, euphoria or anxiety, shortened attention span", 
         "Grade 2: Lethargy or apathy, minimal disorientation, inappropriate behavior, Asterixis present", 
         "Grade 3: Somnolence to semi-stupor, responsive to stimuli, gross disorientation", 
         "Grade 4: Coma"]
    )

    # ==========================================================================
    # INTERNAL MATH CALCULATIONS
    # ==========================================================================
    # MELD-Na 2016 Equation
    cr_meld = min(max(creatinine, 1.0), 4.0)
    bil_meld = min(max(bilirubin, 1.0), 40.0)
    inr_meld = min(max(inr, 1.0), 3.0)
    
    meld_pure = (0.378 * math.log(bil_meld)) + (0.957 * math.log(cr_meld)) + (1.120 * math.log(inr_meld)) + 0.643
    meld_pure = (meld_pure * 10)
    
    # Apply Sodium correction if MELD > 11
    if meld_pure > 11:
        na_bound = min(max(sodium, 125), 137)
        meld_na = meld_pure + 1.32 * (137 - na_bound) - [0.033 * meld_pure * (137 - na_bound)]
    else:
        meld_na = meld_pure
        
    meld_na = min(round(meld_na), 40)

    # Child-Pugh Score Calculation
    cp_score = 0
    # Bilirubin component
    if bilirubin < 2.0: cp_score += 1
    elif 2.0 <= bilirubin <= 3.0: cp_score += 2
    else: cp_score += 3
    # Albumin component
    if albumin > 3.5: cp_score += 1
    elif 2.8 <= albumin <= 3.5: cp_score += 2
    else: cp_score += 3
    # INR component
    if inr < 1.7: cp_score += 1
    elif 1.7 <= inr <= 2.3: cp_score += 2
    else: cp_score += 3
    # Ascites / HE estimation based on inputs
    cp_score += 2 if is_paracentesis else 1 # Simple dynamic mapping
    cp_score += 3 if "Grade 3" in he_stage or "Grade 4" in he_stage else (2 if "Grade 1" in he_stage or "Grade 2" in he_stage else 1)
    
    if cp_score <= 6: cp_class, cp_survival = "A", "100%"
    elif 7 <= cp_score <= 9: cp_class, cp_survival = "B", "80%"
    else: cp_class, cp_survival = "C", "45%"

# ==============================================================================
# RIGHT COLUMN: REAL-TIME MANAGEMENT DASHBOARD
# ==============================================================================
with col_dashboard:
    st.markdown("<div class='section-header'>⚡ Clinical Decision Support Dashboard</div>", unsafe_allow_html=True)
    
    tab_strat, tab_para, tab_he = st.tabs(["📊 Severity Stratification", "💧 Post-Paracentesis Guard", "🧠 Encephalopathy Protocol"])
    
    # TAB 1: SEVERITY STRATIFICATION
    with tab_strat:
        st.markdown("### 🔍 Objective Liver Mortality & Survival Matrix")
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.metric("Calculated MELD-Na Score", f"{meld_na} / 40")
        with col_m2:
            st.metric(f"Child-Pugh Class {cp_class}", f"Score: {cp_score} (1-Yr Survival: ~{cp_survival})")
            
        st.markdown("<div class='status-box'>", unsafe_allow_html=True)
        st.write("📋 **Clinical Status Interpretation:**")
        if meld_na >= 15:
            st.error(f"⚠️ **High Mortality Risk Alert (MELD-Na ≥ 15):** The patient should be evaluated for liver transplantation referral. High risk of decompensation under stress.")
        else:
            st.success("🟢 Stable scoring boundaries. Monitor clinical status and trending vitals daily.")
            
        # Check for Hepatorenal Syndrome (HRS) risk boundaries
        if creatinine > 1.5 and sodium < 130:
            st.error("🚨 **CRITICAL CO-MORBIDITY: High Risk of Hepatorenal Syndrome (HRS-AKI)**")
            st.markdown("""
            * **Pathophysiology:** Co-existence of hypercreatininemia and dilutional hyponatremia reflects extreme splanchnic vasodilation.
            * **Action Plan:** Hold all diuretics (Furosemide/Spironolactone). Avoid NSAIDs and Aminoglycosides completely. Ensure volume expansion with active **20% Albumin** if AKI criteria met.
            """)
        st.markdown("</div>", unsafe_allow_html=True)

    # TAB 2: PARACENTESIS INITIATION & ALBUMIN STEWARDSHIP
    with tab_para:
        st.markdown("### 🌊 Post-Paracentesis Induced Circulatory Dysfunction (PICD) Prevention")
        
        if is_paracentesis:
            st.markdown(f"**Ascitic Fluid Extracted:** `{ascitic_volume} Liters`")
            if ascitic_volume > 5.0:
                # Calculate required Albumin: AASLD recommends 6-8g of 20% Albumin per Liter removed
                albumin_grams = ascitic_volume * 8.0
                # 1 bottle of 20% albumin typically has 50mL or 100mL (20g per 100mL)
                st.error("🚨 **LARGE VOLUME PARACENTESIS (LVP) TRIGGERED:**")
                st.markdown(f"""
                * **Risk Factor:** Removal of $> 5\ L$ of ascitic fluid triggers extreme systemic vasodilation and severe kidney shutdown (**PICD**).
                * **Mandatory Order:** Administer **{albumin_grams:.0f} grams** of intravenous **20% Albumin** (roughly **400 mL** of 20% Albumin solution).
                * **Timing:** Infuse concurrently or immediately post-tap to preserve intra-vascular volume and prevent acute HRS-AKI.
                """)
            else:
                st.warning("⚪ **Volume ≤ 5 Liters:** Albumin substitution is optional but generally recommended if baseline kidney function is compromised or blood pressure is low.")
        else:
            st.info("⚪ Paracentesis tracker is inactive. Check the input box on the left if an ascitic tap is performed.")

    # TAB 3: HEPATIC ENCEPHALOPATHY PROTOCOL
    with tab_he:
        st.markdown("### 🧠 Neuro-Metabolic Ammonium Clearance System")
        st.write(f"▶️ **Current Assessment:** `{he_stage}`")
        
        st.markdown("<div class='status-box'>", unsafe_allow_html=True)
        if "Grade 0" in he_stage:
            st.success("🟢 No overt signs of encephalopathy. Maintain standard lactulose titration if there is a history of HE.")
        else:
            st.warning("🚨 **Active Overt Hepatic Encephalopathy Protocol Initiated:**")
            st.markdown("""
            * **First-Line Therapy (Lactulose):** Initiate or titrate **Lactulose 30-45 mL orally every 1-2 hours** until the patient achieves 2 to 3 soft bowel movements per day, then transition to maintenance dosing (15-30 mL q8-12h).
            * **Enema Option:** If the patient is somnolent or unable to take oral meds safely (Grade 3/4), administer **Lactulose Enemas** (300 mL Lactulose in 700 mL water) q6-8h.
            * **Second-Line Addition:** Add **Rifaximin 550 mg PO twice daily** immediately if this is a recurrent episode or if the patient is currently hospitalized.
            * **Critical Safety Rule:** **DO NOT** give empiric sedatives or hypnotics. Rule out precipitating factors immediately: *Infection (Spontaneous Bacterial Peritonitis - SBP), Constipation, Gastrointestinal Bleeding, or Over-diuresis.*
            """)
        st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# HIGH-YIELD BOARD EXAM REVIEW MATERIAL (Created for the Scientific Club)
# ==============================================================================
st.markdown("<div class='board-header'>🎓 High-Yield Internal Medicine Board Review (Al-Ahli Scientific Research Club)</div>", unsafe_allow_html=True)

st.markdown("""
Below are challenging, board-level multiple-choice questions designed to test internal medicine residents on advanced hepatology and fluid stewardship management according to AASLD guidelines.
""")

# Question 1
st.info("""
**Question 1:** A 54-year-old male with a known history of alcoholic cirrhosis presents to the medical ward with progressive abdominal distension. On examination, he is alert and oriented, but has tense ascites and shifting dullness. Labs reveal: Serum Creatinine 0.9 mg/dL, Total Bilirubin 1.8 mg/dL, INR 1.3, Albumin 2.5 g/dL, and Serum Sodium 136 mEq/L. A therapeutic large-volume paracentesis is performed, and 7.5 Liters of clear ascitic fluid are evacuated. 

Which of the following represents the most appropriate next step to prevent post-paracentesis circulatory dysfunction (PICD)?
* **A)** Intravenous administration of 60 grams of 20% Human Albumin.
* **B)** Intravenous infusion of 1 Liter of Normal Saline (0.9% NaCl).
* **C)** Resuming Spironolactone at double the baseline dose immediately.
* **D)** Administration of IV Terlipressin combined with Albumin.

* **Correct Answer for Club Discussion:** **A**. *Rationale:* For any large-volume paracentesis exceeding 5 Liters, guideline-directed medical therapy dictates replacing 6 to 8 grams of albumin per Liter of fluid removed to prevent severe intravascular volume depletion, rebound ascites, and AKI. 7.5 Liters × 8g = 60 grams of active Albumin. Normal saline is ineffective and will worsen sodium retention.
""")

st.markdown("---")

# Question 2
st.info("""
**Question 2:** A 61-year-old female with Child-Pugh Class C cirrhosis is brought to the emergency department due to progressive confusion and combativeness over the past 24 hours. On physical examination, she is somnolent but responsive to loud verbal commands, grossly disoriented to time and place, and exhibits a prominent flapping tremor (asterixis) when extending her arms. 

Which of the following represents a critical management guideline for this patient's current neuro-metabolic state?
* **A)** Perform an immediate high-resolution CT brain scan and start empiric IV Midazolam for acute agitation.
* **B)** Administer oral Lactulose every 1-2 hours until 2-3 soft stools are passed, and rule out spontaneous bacterial peritonitis (SBP) as a precipitant.
* **C)** Restrict all dietary protein intake to 0.5 g/kg/day to minimize systemic ammonia production.
* **D)** Order an immediate serum ammonia level; if the level is within normal limits, discontinue lactulose.

* **Correct Answer for Club Discussion:** **B**. *Rationale:* The patient presents with overt Hepatic Encephalopathy (West Haven Grade 3). Aggressive lactulose titration is the cornerstone of management. Overt HE is heavily driven by precipitating factors; therefore, a diagnostic paracentesis to rule out SBP, alongside checking for GI bleeds or infections, is mandatory. Empiric sedatives like Midazolam are strictly contraindicated as they will precipitate coma. Protein restriction is no longer recommended as it worsens malnutrition in cirrhotic patients. Diagnosis is clinical, and absolute serum ammonia levels do not track clinical severity reliably.
""")

# Footer Signature
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 11px;'>Al-Ahli Hospital Internal Medicine CDSS Platforms © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
