import streamlit as st
import math

# Page Configuration
st.set_page_config(
    page_title="Al-Ahli Rheumatology Master Engine",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Enhanced CSS for Medical UI Design
st.markdown("""
    <style>
    .main-title { font-size:32px !important; font-weight: bold; color: #1E3A8A; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:16px !important; color: #4B5563; text-align: center; margin-bottom: 25px; font-style: italic; }
    .branding-bar { background-color: #F0F4F8; padding: 18px; border-radius: 12px; border-left: 6px solid #1E3A8A; margin-bottom: 25px; }
    .section-header { font-size:22px !important; font-weight: bold; color: #1E3A8A; margin-top: 15px; margin-bottom: 15px; border-bottom: 2px solid #E5E7EB; padding-bottom: 5px; }
    .status-box { padding: 15px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #E5E7EB; background-color: #F9FAFB; line-height: 1.6; }
    .danger-box { padding: 15px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #DC2626; background-color: #FEF2F2; color: #991B1B; line-height: 1.6; }
    .metric-card { background-color: #FFFFFF; border: 1px solid #E5E7EB; padding: 15px; border-radius: 8px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<div class='main-title'>🫁 Al-Ahli Hospital Elite Rheumatology & Decision Suite</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Ultimate Clinical Intelligence System featuring Continuous Kinetic Metrics & Automated Order-Set Triggers</div>", unsafe_allow_html=True)

# Dr. Ihab Branding Bar
st.markdown(f"""
<div class='branding-bar'>
    <div style='color: #1F2937; font-size: 15px; line-height: 1.6;'>
        <strong>Project Director & System Architect:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Clinical Affiliate:</strong> Department of Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Engine Capabilities:</strong> Advanced DAS28 Formula, Real-Time Dynamic Tapering Algorithms, Critical Vasculitis Mortality Scoring
    </div>
</div>
""", unsafe_allow_html=True)

# Creating Highly Responsive Tabs
tabs = st.tabs([
    "🦋 SLE Phenotyper & SLEDAI", 
    "🦴 RA Core & DAS28-Formula", 
    "🧪 Advanced Synovial & Gout Gate", 
    "🤰 APS & GAPSS Thrombotic Risk", 
    "💊 Smart Steroid Taper Engine", 
    "🚨 Vasculitis Five-Factor Score"
])

# ==============================================================================
# TAB 1: SLE PHENOTYPER & SLEDAI METRICS
# ==============================================================================
with tabs[0]:
    st.markdown("<div class='section-header'>🦋 Combined ACR/EULAR Classification & Active SLEDAI Flare Metrics</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🌐 Baseline Classification")
        ana_titer = st.selectbox("ANA Entry Gate Titer:", ["Negative", "1:80", "1:160", "1:320", "1:640", "1:1280"])
        sle_rash = st.checkbox("Active Malar Rash / Acute Cutaneous Lupus (6 points)")
        sle_renal = st.checkbox("Biopsy-Proven Class III/IV Lupus Nephritis (10 points)")
        sle_dsdna = st.checkbox("Positive Anti-dsDNA or Anti-Smith Antibodies (6 points)")
        
    with col2:
        st.subheader("🔥 Longitudinal Disease Activity (SLEDAI Track)")
        sledai_seizures = st.checkbox("New Onset Seizures / Psychosis (8 points)")
        sledai_proteinuria = st.checkbox("New/Worsening Proteinuria > 0.5g/24h (4 points)")
        sledai_thrombo = st.checkbox("New Thrombocytopenia < 100,000/µL (1 point)")
        sledai_alopecia = st.checkbox("New Onset Diffuse Alopecia (2 points)")

    # Calculations
    class_score = (6 if sle_rash else 0) + (10 if sle_renal else 0) + (6 if sle_dsdna else 0)
    sledai_score = (8 if sledai_seizures else 0) + (4 if sledai_proteinuria else 0) + (1 if sledai_thrombo else 0) + (2 if sledai_alopecia else 0)
    
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.metric("ACR/EULAR Classification Points", f"{class_score} / 10")
    with col_m2:
        st.metric("Calculated SLEDAI Score", f"{sledai_score} Points")
        
    if sledai_score > 7:
        st.markdown("<div class='danger-box'>🚨 **HIGH LUPUS FLARE ACTIVITY DETECTED:** SLEDAI score indicates an aggressive exacerbation. Prepare for induction therapy discussion (e.g., Mycophenolate Mofetil or Cyclophosphamide) alongside systemic steroids.</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 2: RA CORE & DAS28-FORMULA
# ==============================================================================
with tabs[1]:
    st.markdown("<div class='section-header'>🦴 Formal Disease Activity Scoring (DAS28-CRP Advanced Formula)</div>", unsafe_allow_html=True)
    st.write("The definitive scientific mathematical model utilized in trials and high-yield board scenarios to measure objective treatment responses.")
    
    col_ra1, col_ra2 = st.columns(2)
    with col_ra1:
        tjc28 = st.number_input("Tender Joint Count (0 - 28):", min_value=0, max_value=28, value=4)
        sjc28 = st.number_input("Swollen Joint Count (0 - 28):", min_value=0, max_value=28, value=2)
    with col_ra2:
        crp_value = st.number_input("C-Reactive Protein (mg/L):", min_value=0.0, value=12.5, step=0.5)
        vsa_gh = st.slider("Patient Global Assessment of Health (Visual Analog Scale 0-100 mm):", 0, 100, 45)

    # DAS28 Equation execution using natural log and square roots
    # DAS28-CRP = 0.56*sqrt(TJC28) + 0.28*sqrt(SJC28) + 0.70*ln(CRP + 1) + 0.014*GH
    das28_result = (0.56 * math.sqrt(tjc28)) + (0.28 * math.sqrt(sjc28)) + (0.70 * math.log(crp_value + 1)) + (0.014 * vsa_gh)
    
    st.markdown(f"### Real-Time DAS28-CRP Score: `{das28_result:.2f}`")
    
    if das28_result > 5.1:
        st.markdown("<div class='danger-box'>🔴 **HIGH DISEASE ACTIVITY (DAS28 > 5.1):** Severe joint inflammation. Biologic agent tracking or DMARD dose escalation is recommended to halt erosion progression.</div>", unsafe_allow_html=True)
    elif 3.2 <= das28_result <= 5.1:
        st.markdown("<div class='status-box' style='border-left: 5px solid #D97706;'>🟡 **MODERATE DISEASE ACTIVITY:** Optimize therapeutic baselines. Target a score of < 2.6 (Remission).</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='status-box' style='border-left: 5px solid #16A34A;'>🟢 **CLINICAL REMISSION / LOW ACTIVITY (DAS28 < 3.2):** Current management plan is highly effective.</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 3: ADVANCED SYNOVIAL & GOUT GATE
# ==============================================================================
with tabs[2]:
    st.markdown("<div class='section-header'>🧪 Synovial Fluid Crystals & Kinetic Gout Safety Track</div>", unsafe_allow_html=True)
    col_g1, col_g2 = st.columns(2)
    
    with col_g1:
        crystal_type = st.radio("Meticulous Polarized Microscopic Findings:", ["No crystals seen", "Needle-shaped, strongly negative birefringent", "Rhomboid, weakly positive birefringent"])
        patient_gfr = st.number_input("Patient Baseline GFR (mL/min/1.73m²):", min_value=5, max_value=150, value=45)
        
    with col_g2:
        if "negative" in crystal_type:
            st.error("💎 **ACUTE GOUTY ARTHRITIS CONFIRMED:** Monosodium urate crystals identified.")
            if patient_gfr < 30:
                st.markdown("<div class='danger-box'>🛑 **RENAL WARNING (GFR < 30):** Traditional full-dose NSAIDs are strictly contraindicated. Avoid high-dose Colchicine due to high toxicity risks. Prefer Short-course Oral Corticosteroids or Intra-articular steroid injections.</div>", unsafe_allow_html=True)
            else:
                st.success("🟢 Renal clearance satisfies criteria for standard treatment options (e.g., Short-course NSAID or Colchicine protocol).")
        else:
            st.info("ℹ️ Fluid profile clear of active crystalline precipitates.")

# ==============================================================================
# TAB 4: APS & GAPSS THROMBOTIC RISK
# ==============================================================================
with tabs[3]:
    st.markdown("<div class='section-header'>🤰 Global Antiphospholipid Syndrome Score (GAPSS Risk Engine)</div>", unsafe_allow_html=True)
    st.write("Quantifies the specific likelihood of recurrent thrombosis for a patient with positive antiphospholipid antibodies.")
    
    col_ap1, col_ap2 = st.columns(2)
    with col_ap1:
        la_pos = st.checkbox("Positive Lupus Anticoagulant (5 points)")
        acl_pos = st.checkbox("Positive Anti-cardiolipin IgG/IgM (5 points)")
        ab2_pos = st.checkbox("Positive Anti-beta2-Glycoprotein I IgG/IgM (4 points)")
    with col_ap2:
        g_htn = st.checkbox("Concomitant Arterial Hypertension History (1 point)")
        g_hyper = st.checkbox("Hyperlipidemia Panel Active (3 points)")
        
    gapss_total = (5 if la_pos else 0) + (5 if acl_pos else 0) + (4 if ab2_pos else 0) + (1 if g_htn else 0) + (3 if g_hyper else 0)
    
    st.markdown(f"### Total Calculated GAPSS Score: `{gapss_total} / 18 Points`")
    if gapss_total >= 10:
        st.markdown(f"<div class='danger-box'>🚨 **CRITICAL EMBOLIC PROFILE (GAPSS: {gapss_total}):** Patient exhibits a high thrombotic profile. Strict therapeutic international normalized ratio (INR 2.0-3.0) maintenance via Warfarin is crucial. Avoid direct oral anticoagulants.</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='status-box'>ℹ️ Moderate baseline cardiovascular risk tiering. Optimize modifiable factors.</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 5: SMART STEROID TAPER ENGINE
# ==============================================================================
with tabs[4]:
    st.markdown("<div class='section-header'>📋 Precision Algorithmic Corticosteroid Tapering Scheduler</div>", unsafe_allow_html=True)
    st.write("Automates a safe, gradual reduction plan for long-term prednisone therapy to minimize the risk of secondary adrenal insufficiency.")
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        current_prednisone = st.number_input("Current Daily Prednisone Dose (mg):", min_value=5.0, max_value=100.0, value=40.0, step=5.0)
        taper_speed = st.selectbox("Select Clinically Indicated Taper Speed:", ["Standard Conservative Taper", "Accelerated / Post-Flare Taper"])
        
    with col_t2:
        st.markdown("### 🗓️ Generated Clinical Tapering Protocol")
        
        if taper_speed == "Standard Conservative Taper":
            st.markdown(f"""
            * **Weeks 1–2:** Reduce dose to `{current_prednisone - 5.0:.1f} mg` daily.
            * **Weeks 3–4:** Reduce dose to `{max(5.0, current_prednisone - 10.0):.1f} mg` daily.
            * **Weeks 5–6:** Reduce dose to `{max(5.0, current_prednisone - 15.0):.1f} mg` daily.
            * **When dose reaches 10mg:** Taper much slower by **1 mg every 2-4 weeks** to allow the adrenal glands to resume normal function.
            """)
        else:
            st.markdown(f"""
            * **Days 1–5:** Maintain dose at `{current_prednisone:.1f} mg` daily.
            * **Days 6–10:** Reduce dose to `{current_prednisone / 2:.1f} mg` daily.
            * **Days 11+:** Adjust to a low baseline of `5.0 mg` daily or transition to alternative DMARDs.
            """)

# ==============================================================================
# TAB 6: VASCULITIS FIVE-FACTOR SCORE
# ==============================================================================
with tabs[5]:
    st.markdown("<div class='section-header'>🚨 Systemic Necrotizing Vasculitis Five-Factor Score (FFS)</div>", unsafe_allow_html=True)
    st.write("Calculates 5-year mortality risk for conditions like Polyarteritis Nodosa, GPA, MPA, and EGPA.")
    
    col_v1, col_v2 = st.columns(2)
    with v_v1 if 'v_v1' in locals() else col_v1:
        v_age = st.checkbox("Age > 65 Years old (1 point)")
        v_renal = st.checkbox("Renal Insufficiency (Serum Creatinine > 140 µmol/L) (1 point)")
        v_gi = st.checkbox("Severe Gastrointestinal Involvement (Infarction, Bleeding, Perforation) (1 point)")
    with v_v2 if 'v_v2' in locals() else col_v2:
        v_cardio = st.checkbox("Cardio-Pulmonary Specific Involvement / Cardiomyopathy (1 point)")
        v_ent = st.checkbox("Absence of Ear, Nose, and Throat (ENT) involvement in GPA (1 point)")

    ffs_score = (1 if v_age else 0) + (1 if v_renal else 0) + (1 if v_gi else 0) + (1 if v_cardio else 0) + (1 if v_ent else 0)
    
    # Mortality estimation mapping
    mortality_estimate = "12%" if ffs_score == 0 else ("26%" if ffs_score == 1 else "46% or greater")
    
    st.markdown(f"### Total Five-Factor Score (FFS): `{ffs_score} Points`")
    st.markdown(f"<div class='status-box'>📊 **Estimated 5-Year Mortality Index:** Around ~<strong>{mortality_estimate}</strong> without aggressive treatment.</div>", unsafe_allow_html=True)
    
    if ffs_score >= 1:
        st.markdown("<div class='danger-box'>⚠️ **HIGH-RISK STRATIFICATION:** FFS $\ge 1$ dictates the absolute necessity of adding potent cytotoxic therapy (e.g., Cyclophosphamide infusion or Rituximab) alongside high-dose pulse steroids to save vital organs.</div>", unsafe_allow_html=True)

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 11px;'>Al-Ahli Hospital Internal Medicine CDSS Platforms © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
