import streamlit as st

# Page Configuration for a clean, dedicated clinical tool
st.set_page_config(
    page_title="Al-Ahli Hospital Sepsis & Septic Shock Protocol",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Medical Branding Styles
st.markdown("""
    <style>
    .main-title { font-size:32px !important; font-weight: bold; color: #065F46; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:16px !important; color: #4B5563; text-align: center; margin-bottom: 25px; font-style: italic; }
    .branding-bar { background-color: #ECFDF5; padding: 20px; border-radius: 10px; border-left: 6px solid #059669; margin-bottom: 25px; }
    .branding-bar strong { color: #065F46 !important; font-weight: bold; }
    .branding-text { color: #1F2937 !important; font-size: 16px !important; line-height: 1.6; }
    .section-header { font-size:22px !important; font-weight: bold; color: #065F46; margin-top: 15px; margin-bottom: 15px; }
    .board-header { font-size:20px !important; font-weight: bold; color: #D97706; margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<div class='main-title'>🧬 Al-Ahli Hospital Sepsis & Septic Shock Command Center</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Dedicated Clinical Decision Support Tool & 1-Hour Bundle Integration</div>", unsafe_allow_html=True)

# Professional Badge
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Project Founder & Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Focus:</strong> Local Empirical Protocols & Evidence-Based Resident Training
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Layout Split
col_input, col_protocol = st.columns([1, 1.2])

# ==============================================================================
# LEFT COLUMN: Vital Signs & Clinical Scores
# ==============================================================================
with col_input:
    st.markdown("<div class='section-header'>🩺 1. Acute Vital Signs & Clinical Inputs</div>", unsafe_allow_html=True)
    
    weight = st.number_input("Patient Weight (kg):", min_value=30, max_value=200, value=70)
    sbp = st.number_input("Systolic Blood Pressure (SBP mmHg):", min_value=40, max_value=250, value=82)
    dbp = st.number_input("Diastolic Blood Pressure (DBP mmHg):", min_value=20, max_value=150, value=45)
    rr = st.number_input("Respiratory Rate (breaths/min):", min_value=8, max_value=60, value=24)
    temperature = st.number_input("Temperature (°C):", min_value=33.0, max_value=43.0, value=38.9, step=0.1)
    
    st.markdown("---")
    st.markdown("**Neurological Assessment (GCS Component):**")
    altered_mental = st.radio("Mental Status Assessment:", ("Altered Mental Status / Confusion", "Normal / Baseline Alert"))
    
    st.markdown("---")
    st.markdown("**Laboratory Parameters (If available):**")
    lactate = st.number_input("Serum Lactate (mmol/L):", min_value=0.5, max_value=20.0, value=3.2, step=0.1)
    suspected_source = st.selectbox(
        "Suspected Primary Source of Infection:",
        ["Urinary Tract (UTI / Pyelonephritis)", "Respiratory (Pneumonia / CAP / HAP)", "Intra-abdominal", "Skin / Soft Tissue / Cellulitis", "Unknown Source"]
    )

    # Calculate Mean Arterial Pressure (MAP)
    map_val = dbp + (1/3) * (sbp - dbp)
    
    # Calculate qSOFA Score
    qsofa = 0
    if sbp <= 100: qsofa += 1
    if rr >= 22: qsofa += 1
    if altered_mental == "Altered Mental Status / Confusion": qsofa += 1

    st.markdown("---")
    st.markdown("<div class='section-header'>📊 Calculated Hemodynamic Scores</div>", unsafe_allow_html=True)
    st.metric("Calculated MAP", f"{map_val:.1f} mmHg", delta="Hypotension (<65)" if map_val < 65 else "Normal")
    st.metric("qSOFA Score", f"{qsofa} / 3", delta="High Risk (≥2)" if qsofa >= 2 else "Low Risk")

# ==============================================================================
# RIGHT COLUMN: Surviving Sepsis 1-Hour Bundle & Medication Logic
# ==============================================================================
with col_protocol:
    st.markdown("<div class='section-header'>⚡ 2. Surviving Sepsis 1-Hour Bundle Mandates</div>", unsafe_allow_html=True)
    
    # Stratify Diagnosis
    is_septic_shock = (map_val < 65 or sbp < 90) and (lactate > 2.0)
    is_sepsis = (qsofa >= 2 or lactate > 2.0) and not is_septic_shock

    if is_septic_shock:
        st.error("🔴 CRITICAL: PATIENT MEETS CRITERIA FOR SEPTIC SHOCK (Refractory Hypotension + Elevated Lactate)")
    elif is_sepsis:
        st.warning("🟡 WARNING: HIGH SUSPICION OF SEPSIS. INTERVENE IMMEDIATELY TO PREVENT SHOCK")
    else:
        st.info("🟢 Patient is hemodynamically stable, but screen continuously if clinical signs evolve.")

    st.markdown("---")
    
    # 1. Fluid Resuscitation Box (30 mL/kg Standard)
    st.markdown("### 💧 Step 1: Immediate Fluid Resuscitation")
    fluid_req = weight * 30
    st.write(f"**Target Fluid Volume:** Infuse **{fluid_req} mL** of Crystalloids (**Normal Saline 0.9% or Balanced Salt Solution**) within the first 3 hours.")
    st.caption("⚠️ Ensure aggressive monitoring of lung fields for fluid overload/crepitations during administration.")

    st.markdown("---")

    # 2. Vasopressor Titration Logic
    st.markdown("### 💉 Step 2: Vasopressor Protocol (Target MAP ≥ 65 mmHg)")
    if map_val < 65:
        st.error("🚨 MAP < 65 mmHg: Fluid resuscitation alone is insufficient. Initiate Vasopressors Immediately!")
        st.markdown("""
        *   **First-Line Agent:** **Norepinephrine Infusion** (Standard concentration). 
        *   **Initial Dose:** Titrate from **0.05 - 0.15 mcg/kg/min** via a central line if available.
        *   **Refractory Option:** If Norepinephrine maxed out without achieving MAP ≥ 65, add **Vasopressin 0.03 units/min** fixed dose.
        """)
    else:
        st.success("✅ MAP ≥ 65 mmHg: Current perfusion pressure is acceptable. Continue to monitor fluid responsiveness.")

    st.markdown("---")

    # 3. Empiric Antimicrobial Selection Guide based on Selected Source
    st.markdown("### 💊 Step 3: Local Empirical Antibiotic Selector")
    st.markdown(f"**Target Source Identified:** {suspected_source}")
    
    if suspected_source == "Urinary Tract (UTI / Pyelonephritis)":
        st.success("🟢 **Recommended Protocol:** Ceftriaxone 2g IV q24h. *If Pseudomonas risk exists (prior instrumentation/urology admission), use Ceftazidime 2g IV q8h or Piperacillin/Tazobactam 4.5g IV q6h.*")
    elif suspected_source == "Respiratory (Pneumonia / CAP / HAP)":
        st.success("🟢 **Recommended Protocol:** Ceftriaxone 2g IV q24h + Azithromycin 500mg IV q24h. *If Healthcare-Associated (HAP/VAP), optimize to Ceftazidime 2g IV q8h + Levofloxacin 750mg IV q24h to cover Gram-negatives.*")
    elif suspected_source == "Intra-abdominal":
        st.success("🟢 **Recommended Protocol:** Ceftriaxone 2g IV q24h + Metronidazole 500mg IV q8h (or Monotherapy with Piperacillin/Tazobactam 4.5g IV q6h).")
    elif suspected_source == "Skin / Soft Tissue / Cellulitis":
        st.success("🟢 **Recommended Protocol:** Oxacillin 2g IV q4h or Cefazolin 2g IV q8h. *If necrotizing infection or high MRSA risk suspected, substitute/add Vancomycin (dose based on renal profile).*")
    else:
        st.warning("⚠️ **Unknown Source Protocol:** Broad-spectrum coverage required. Initiate **Piperacillin/Tazobactam 4.5g IV q6h** or **Meropenem 1g IV q8h** immediately after blood cultures are drawn.")

    st.markdown("""
    *   **Culture Mandate:** **Draw 2 sets of Blood Cultures** (one peripheral, one central if line present) BEFORE infusing the first antibiotic dose. Do NOT delay antibiotics for more than 45 mins if cultures are difficult to draw.
    *   **Lactate Clearance:** Repeat Serum Lactate measurement **within 2 to 4 hours** to assess resuscitation adequacy (Aim for a clearance of > 10%).
    """)

# ==============================================================================
# BOTTOM SECTION: High-Yield Board Review Questions & Explanations
# ==============================================================================
st.markdown("---")
st.markdown("<div class='board-header'>🎓 3. High-Yield Board-Level Case Review (Sepsis Resuscitation Focus)</div>", unsafe_allow_html=True)
st.caption("Crucial teaching point regarding the prioritization of therapies in Septic Shock for residents and interns.")

with st.expander("❓ Click to Reveal the Board Question & Scientific Rationale"):
    st.markdown("""
    **Clinical Scenario:**  
    A 68-year-old female presents to the Emergency Department with severe lethargy, productive cough, and fever. Vital signs: BP 78/42 mmHg, HR 122 bpm, RR 26 bpm, Temp 39.1°C. She is given a 500 mL bolus of Normal Saline, but 30 minutes later, her blood pressure remains 80/44 (MAP < 55 mmHg). Peripheral access is secured, but a central line cannot be placed for another hour due to a busy department shift. 
    
    **What is the most appropriate next step according to the latest Surviving Sepsis Guidelines?**
    
    *   **A)** Continue fluid resuscitation until the full 30 mL/kg bolus is finished before considering any vasopressors.
    *   **B)** Delay vasopressors until a central venous catheter is safely placed to avoid peripheral extravasation.
    *   **C)** **Correct.** Initiate Norepinephrine infusion immediately via a well-placed peripheral IV line while arranging for central access.
    *   **D)** Give a bolus of IV Hydrocortisone 100mg to restore vascular tone.
    
    ---
    
    ### 📝 Comprehensive Scientific Evidence-Based Explanation:
    *   **The Correct Answer is C.** The modern *Surviving Sepsis Campaign Guidelines* emphasize that **delays in correcting hypotension significantly increase mortality** in septic shock. If a patient remains hypotensive during or immediately after early fluid administration, vasopressors (Norepinephrine) should be started **peripherally** in a large vein (e.g., antecubital fossa) for a short duration (< 24 hours) rather than waiting for central access.
    *   **Local Application Concept:** In our local wards or crowded ER settings, waiting for central lines can consume critical time. Teaching residents that peripheral Norepinephrine is safe and preferred over prolonged hypotension is a high-yield clinical pearl.
    *   **Fluid Target Reminder:** The 30 mL/kg target is a guideline benchmark, but it should not delay the active initiation of vasopressors if the MAP is profoundly low and compromising coronary or cerebral perfusion.
    """)

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 12px;'>Al-Ahli Hospital Internal Medicine CDSS Platforms © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
