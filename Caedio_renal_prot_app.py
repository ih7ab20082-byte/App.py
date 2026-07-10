import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Al-Ahli Cardio-Renal Protection Suite",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling to match your high clinical standards
st.markdown("""
    <style>
    .main-title { font-size:30px !important; font-weight: bold; color: #DC2626; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:15px !important; color: #4B5563; text-align: center; margin-bottom: 25px; font-style: italic; }
    .branding-bar { background-color: #FEF2F2; padding: 20px; border-radius: 10px; border-left: 6px solid #DC2626; margin-bottom: 25px; }
    .branding-bar strong { color: #DC2626 !important; font-weight: bold; }
    .branding-text { color: #1F2937 !important; font-size: 15px !important; line-height: 1.6; }
    .section-header { font-size:20px !important; font-weight: bold; color: #DC2626; margin-top: 15px; margin-bottom: 15px; border-bottom: 2px solid #E5E7EB; padding-bottom: 5px; }
    .status-box { background-color: #F9FAFB; padding: 15px; border-radius: 8px; border: 1px solid #E5E7EB; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# App Header & Signature
st.markdown("<div class='main-title'>🫀 Al-Ahli Hospital Cardio-Renal Protection Suite</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Evidence-Based Guideline Optimization Engine for SGLT2 Inhibitors & Non-Steroidal MRAs (Finerenone)</div>", unsafe_allow_html=True)

st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Project Founder & Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Clinical Core:</strong> 2023 KDIGO CKD Diabetes Guidelines, ESC Heart Failure Protocols, Focus on Dapagliflozin & Finerenone Safety Boundaries
    </div>
</div>
""", unsafe_allow_html=True)

# Layout Split
col_input, col_dashboard = st.columns([1, 1.2])

# ==============================================================================
# LEFT COLUMN: CLINICAL INPUTS
# ==============================================================================
with col_input:
    st.markdown("<div class='section-header'>📋 Patient Clinical Profile</div>", unsafe_allow_html=True)
    
    # Vital inputs for staging and safety eligibility
    egfr = st.number_input("Calculated eGFR (mL/min/1.73m²):", min_value=5.0, max_value=150.0, value=35.0, step=1.0)
    u_acr = st.number_input("Urine Albumin-to-Creatinine Ratio (Urine ACR mg/g):", min_value=5.0, max_value=5000.0, value=450.0, step=10.0)
    potassium = st.number_input("Serum Potassium (K+ mEq/L):", min_value=2.5, max_value=7.5, value=4.6, step=0.1)
    
    st.markdown("---")
    st.subheader("Comorbidities & Status")
    has_diabetes = st.checkbox("Type 2 Diabetes Mellitus (T2DM)", value=True)
    has_hf = st.checkbox("Heart Failure (HFrEF / HFpEF)", value=False)
    is_hypovolemic = st.checkbox("Active Volume Depletion / Hypotension Risk", value=False)
    on_ace_arb = st.checkbox("Currently on Maximized ACEi or ARB therapy", value=True)

# ==============================================================================
# RIGHT COLUMN: CARDIO-RENAL DECISION SUPPORT DASHBOARD
# ==============================================================================
with col_dashboard:
    st.markdown("<div class='section-header'>⚡ Cardio-Renal Guideline Optimization Dashboard</div>", unsafe_allow_html=True)
    
    tab_sglt2, tab_mra = st.tabs(["💊 SGLT2i (Dapagliflozin / Empagliflozin)", "🧪 ns-MRA Protocol (Finerenone)"])
    
    # ------------------------------------------------------------------
    # TAB 1: SGLT2 INHIBITORS ENGINE
    # ------------------------------------------------------------------
    with tab_sglt2:
        st.markdown("### 🔍 SGLT2 Inhibitor Eligibility & Safety Checklist")
        
        # Primary Indicators Checklist Based on KDIGO/ESC
        eligible_sglt2 = False
        if egfr >= 20 and (has_diabetes or has_hf or u_acr >= 200):
            eligible_sglt2 = True
            
        if eligible_sglt2:
            if is_hypovolemic:
                st.warning("⚠️ **Relative Contraindication Detected:**")
                st.markdown("""
                * **Status:** Patient is eligible based on eGFR, but there is active **Volume Depletion / Hypotension**.
                * **Clinical Recommendation:** Correct volume status and hold/adjust background loop diuretics *before* initiating SGLT2i to prevent severe AKI or symptomatic hypotension.
                """)
            elif egfr < 20:
                st.error("🚫 **SGLT2i Initiation Contraindicated (eGFR < 20):**")
                st.write("Do not initiate if eGFR is below 20 mL/min. However, if the patient was already taking it and eGFR drops below 20, it can be safely continued until dialysis starts.")
            else:
                st.success("🟢 **PATIENT ELIGIBLE FOR SGLT2i INITIATION**")
                st.markdown(f"""
                * **Indication Class:** **Class IA Recommendation** (KDIGO 2023 / ESC).
                * **Suggested Regimen:** **Dapagliflozin 10 mg PO once daily** OR **Empagliflozin 10 mg PO once daily**.
                * **Expected Renal Dynamics:** Warn the resident about an expected initial **acute "dip" in eGFR (up to 30%)** within the first 2-4 weeks. This is a functional hemodynamic change reflecting reduced intraglomerular pressure and indicates long-term nephroprotection. Do not stop the drug unless the drop exceeds 30%.
                """)
        else:
            st.info("⚪ **Patient does not meet primary initiation criteria for SGLT2i at this stage.**")
            st.write("Initiation is optimized for patients with T2DM, Heart Failure, or proteinuric CKD (Urine ACR ≥ 200) with eGFR ≥ 20.")

    # ------------------------------------------------------------------
    # TAB 2: NON-STEROIDAL MRA (FINERENONE) ENGINE
    # ------------------------------------------------------------------
    with tab_mra:
        st.markdown("### 🧪 Non-Steroidal MRA (Finerenone) Guard System")
        
        # Finerenone Criteria: T2DM + CKD (egfr >= 25, normal K, on max ACEi/ARB)
        if not has_diabetes:
            st.info("⚪ **Finerenone (ns-MRA) Indicator Note:**")
            st.write("Finerenone is currently heavily indicated and approved for patients with **Type 2 Diabetes and CKD** to reduce renal failure and CV mortality.")
        else:
            st.markdown("<div class='status-box'>", unsafe_allow_html=True)
            st.write("📊 **Evaluating FIDELIO-DKD & FIGARO-DKD Criteria Alignment:**")
            
            # Check mandatory baseline safeguards
            errors = []
            if egfr < 25:
                errors.append(f"eGFR is too low ({egfr} mL/min). Initiation requires eGFR ≥ 25.")
            if potassium > 5.0:
                errors.append(f"Serum Potassium is elevated ({potassium} mEq/L). Initiation requires Baseline K⁺ ≤ 5.0 mEq/L.")
            if not on_ace_arb:
                errors.append("Patient must be on a maximized/tolerated dose of an ACEi or ARB prior to adding Finerenone.")
                
            if errors:
                st.error("🚫 **Finerenone Initiation Blocked / Critical Safeguards Triggered:**")
                for err in errors:
                    st.markdown(f"- {err}")
            else:
                st.success("🟢 **PATIENT ELIGIBLE FOR FINERENONE (ns-MRA) INITIATION**")
                
                # Dose Selection based on eGFR
                if egfr >= 60:
                    suggested_dose = "20 mg PO once daily"
                else:
                    suggested_dose = "10 mg PO once daily (Target titration to 20 mg if K⁺ remains stable)"
                    
                st.markdown(f"""
                * **Recommended Starting Dose:** **{suggested_dose}**.
                * **Monitoring Safeguard Protocol:** * Mandatory Serum Potassium check **4 weeks** post-initiation.
                    * **Hold Medication** immediately if Potassium climbs above **5.5 mEq/L** during follow-up.
                """)
            st.markdown("</div>", unsafe_allow_html=True)

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 11px;'>Al-Ahli Hospital Internal Medicine CDSS Platforms © 2026 • Platform Design curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
