import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Al-Ahli Rheumatology Phenotyper",
    page_icon="Bone",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for Clinical & Academic Sophistication
st.markdown("""
    <style>
    .main-title { font-size:30px !important; font-weight: bold; color: #4338CA; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:15px !important; color: #4B5563; text-align: center; margin-bottom: 25px; font-style: italic; }
    .branding-bar { background-color: #EEF2F6; padding: 20px; border-radius: 10px; border-left: 6px solid #4338CA; margin-bottom: 25px; }
    .branding-bar strong { color: #4338CA !important; font-weight: bold; }
    .branding-text { color: #1F2937 !important; font-size: 15px !important; line-height: 1.6; }
    .section-header { font-size:20px !important; font-weight: bold; color: #4338CA; margin-top: 15px; margin-bottom: 15px; border-bottom: 2px solid #E5E7EB; padding-bottom: 5px; }
    .status-box { padding: 15px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #E5E7EB; background-color: #F9FAFB; }
    .board-header { font-size:22px !important; font-weight: bold; color: #D97706; margin-top: 30px; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<div class='main-title'>🦴 Al-Ahli Hospital Rheumatology & Autoimmune Phenotyper</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Ultimate Diagnostic Decision Engine with EULAR Classification, Synovial Analysis, & Biologic Stewardship</div>", unsafe_allow_html=True)

# Professional Branding Block
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Project Founder & Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Clinical Core:</strong> EULAR/ACR 2019 Rules, Synovial Fluid Differential Matrix, CDC Pre-Immunosuppression Screening Guidelines
    </div>
</div>
""", unsafe_allow_html=True)

# Main Application Tabs to isolate workflows beautifully
app_tab1, app_tab2, app_tab3 = st.tabs(["🧬 EULAR/ACR SLE Classifier", "🧪 Synovial Fluid Interpreter", "🛡️ Pre-Biologic Safety Checklist"])

# ==============================================================================
# TAB 1: EULAR/ACR SLE CLASSIFIER (MODULARIZED & ENHANCED)
# ==============================================================================
with app_tab1:
    col_input, col_dashboard = st.columns([1.1, 1.1])

    with col_input:
        st.markdown("<div class='section-header'>🔬 1. Immunofluorescence (IFA) ANA Gate</div>", unsafe_allow_html=True)
        ana_titer = st.selectbox("ANA Titer (Entry Criterion):", ["Negative / Less than 1:80", "1:80", "1:160", "1:320", "1:640", "1:1280"], key="sle_ana_titer")
        ana_pattern = st.selectbox("ANA Morphological Pattern:", ["Homogeneous", "Speckled", "Centromere", "Nucleolar", "Peripheral / Rim"], key="sle_ana_pattern")

        st.markdown("<div class='section-header'>📋 2. EULAR/ACR 2019 Domain Evaluation</div>", unsafe_allow_html=True)
        with st.expander("🌡️ Constitutional Domain"):
            fever = st.checkbox("Unexplained Fever (> 38.5°C)", value=False, key="sle_fever")
            constitutional_score = 2 if fever else 0

        with st.expander("🦋 Cutaneous Domains"):
            cutaneous_select = st.radio("Select highest skin manifestation:", ["None", "Acute Cutaneous Lupus / Malar Rash (6 pts)", "Subacute Cutaneous OR Discoid Lupus (4 pts)", "Oral / Nasal Ulcers (2 pts)", "Non-scarring Alopecia (2 pts)"], key="sle_skin")
            cutaneous_score = {"None": 0, "Acute Cutaneous Lupus / Malar Rash (6 pts)": 6, "Subacute Cutaneous OR Discoid Lupus (4 pts)": 4, "Oral / Nasal Ulcers (2 pts)": 2, "Non-scarring Alopecia (2 pts)": 2}[cutaneous_select]

        with st.expander("Q Joints Domain"):
            joint_select = st.radio("Joint Involvement Presence:", ["None", "Synovitis / Arthritis in ≥ 2 joints with morning stiffness (6 pts)"], key="sle_joint")
            joint_score = 6 if "Synovitis" in joint_select else 0

        with st.expander("🩸 Renal Domain (Proteinuria / Biopsy)"):
            renal_select = st.radio("Renal Manifestation Severity:", ["None", "Class III or IV Lupus Nephritis on Biopsy (10 pts)", "Class II or V Lupus Nephritis on Biopsy (8 pts)", "Severe Proteinuria > 0.5g/24h (4 pts)"], key="sle_renal")
            renal_score = {"None": 0, "Class III or IV Lupus Nephritis on Biopsy (10 pts)": 10, "Class II or V Lupus Nephritis on Biopsy (8 pts)": 8, "Severe Proteinuria > 0.5g/24h (4 pts)": 4}[renal_select]

        with st.expander("🩸 Hematologic Domain"):
            hemato_select = st.multiselect("Select all matching hematological parameters:", ["Autoimmune Hemolytic Anemia (4 pts)", "Thrombocytopenia < 100,000/µL (4 pts)", "Leukopenia < 4,000/µL (3 pts)"], key="sle_hemato")
            h_pts = [0]
            if "Autoimmune Hemolytic Anemia (4 pts)" in hemato_select: h_pts.append(4)
            if "Thrombocytopenia < 100,000/µL (4 pts)" in hemato_select: h_pts.append(4)
            if "Leukopenia < 4,000/µL (3 pts)" in hemato_select: h_pts.append(3)
            hemato_score = max(h_pts)

        with st.expander("🧬 Immunology Labs (Specific Autoantibodies)"):
            immuno_select = st.multiselect("Positive Specific Immunological Labs:", ["Anti-dsDNA Antibody OR Anti-Smith Antibody (6 pts)", "Antiphospholipid Antibodies (LA, Anti-Cardiolipin, or Anti-beta2GP1) (2 pts)"], key="sle_immuno")
            i_pts = [0]
            if "Anti-dsDNA Antibody OR Anti-Smith Antibody (6 pts)" in immuno_select: i_pts.append(6)
            if "Antiphospholipid Antibodies (LA, Anti-Cardiolipin, or Anti-beta2GP1) (2 pts)" in immuno_select: i_pts.append(2)
            immuno_score = max(i_pts)

        with st.expander("🧪 Complement Cascades"):
            comp_select = st.radio("Complement Depletion Status:", ["Normal Complements", "Both Low C3 AND Low C4 (4 pts)", "Either Low C3 OR Low C4 alone (3 pts)"], key="sle_comp")
            comp_score = {"Normal Complements": 0, "Both Low C3 AND Low C4 (4 pts)": 4, "Either Low C3 OR Low C4 alone (3 pts)": 3}[comp_select]

        total_eular_score = (constitutional_score + cutaneous_score + joint_score + renal_score + hemato_score + immuno_score + comp_score)

    with col_dashboard:
        st.markdown("<div class='section-header'>⚡ Real-Time Immunological Dashboard</div>", unsafe_allow_html=True)
        if ana_titer == "Negative / Less than 1:80":
            st.error("🛑 **ENTRY CRITERION FAILED:** ANA titer must be $\ge 1:80$ to use this classification algorithm.")
        else:
            st.success(f"✅ **ENTRY CRITERION MET:** ANA Titer is `{ana_titer}`.")

        pattern_details = {
            "Homogeneous": ("Anti-dsDNA, Anti-Histone", "SLE, Drug-Induced Lupus"),
            "Speckled": ("Anti-Ro (SSA), Anti-La (SSB), Anti-Sm, Anti-RNP", "Sjögren's, MCTD, SLE"),
            "Centromere": ("Anti-Centromere Antibodies (ACA)", "Limited Cutaneous Systemic Sclerosis (CREST)"),
            "Nucleolar": ("Anti-Scl-70, Anti-RNA Polymerase III", "Diffuse Systemic Sclerosis"),
            "Peripheral / Rim": ("Anti-dsDNA", "Highly Active SLE")
        }[ana_pattern]

        st.markdown(f"""
        <div class='status-box' style='border-left: 5px solid #4338CA; background-color: #F5F3FF;'>
            <strong>Target ENA Profile:</strong> <code>{pattern_details[0]}</code><br>
            <strong>Primary Differentials:</strong> {pattern_details[1]}
        </div>
        """, unsafe_allow_html=True)

        if renal_score >= 8:
            st.error("🚨 **URGENT:** High-grade Lupus Nephritis suspected on biopsy. Evaluate immediately for pulse steroid protocols.")

        st.markdown(f"### Total Classification Weight: `{total_eular_score} Points`")
        if total_eular_score >= 10 and ana_titer != "Negative / Less than 1:80":
            st.markdown(f"<div class='status-box' style='background-color: #F0FDF4; border-left: 5px solid #16A34A;'><strong>🎉 CRITERIA MET:</strong> Classifies as Systemic Lupus Erythematosus (SLE).</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='status-box' style='background-color: #FFFBEB; border-left: 5px solid #D97706;'><strong>⚠️ NOTICE:</strong> Does not fully classify as SLE yet ({total_eular_score}/10).</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 2: SYNOVIAL FLUID INTERPRETER (NEW ADVANCED ELEMENT)
# ==============================================================================
with app_tab2:
    st.markdown("<div class='section-header'>🧪 Synovial Fluid Differential Kinetic Engine</div>", unsafe_allow_html=True)
    st.write("Input the parameters of the synovial fluid aspirate to classify the type of joint inflammation.")

    col_syn1, col_syn2 = st.columns(2)
    
    with col_syn1:
        syn_clarity = st.selectbox("Fluid Gross Appearance & Clarity:", ["Clear & Straw Colored", "Translucent / Mildly Turbid", "Opaque & Purulent / Thick Yellow", "Bloody / Hemorrhagic"])
        syn_wbc = st.number_input("Synovial WBC Count (cells/µL):", min_value=0, max_value=250000, value=1500, step=500)
        syn_pmn = st.slider("Polymorphonuclear (PMN) Neutrophils (%):", min_value=0, max_value=100, value=25)
        syn_crystals = st.selectbox("Polarized Microscopy Crystal Assessment:", ["No Crystals Seen", "Needle-shaped, Negatively Birefringent (Monosodium Urate)", "Rhomboid-shaped, Positively Birefringent (CPPD)"])

    with col_syn2:
        st.markdown("### 📊 Fluid Classification & Diagnostic Logic")
        
        fluid_category = "Normal / Non-inflammatory"
        fluid_action = "Consistent with osteoarthritis or mechanical joint trauma."
        fluid_color = "#F9FAFB"
        fluid_border = "#9CA3AF"

        # Diagnostic Rules Array
        if syn_wbc > 50000 or syn_pmn > 75:
            fluid_category = "🚨 SEPTIC / INFECTIOUS ARTHRITIS SUSPECTED"
            fluid_action = "Emergency! High risk of joint destruction. Obtain urgent Gram stain, cultures, and initiate empirical IV antibiotics (e.g., Vancomycin + Ceftazidime) prior to definitive culture return."
            fluid_color = "#FEF2F2"
            fluid_border = "#DC2626"
        elif 2000 <= syn_wbc <= 50000 or 50 <= syn_pmn <= 75:
            fluid_category = "🔥 INFLAMMATORY ARTHRITIS (Rheumatoid / Autoimmune / Crystal)"
            fluid_action = "Consistent with RA, SLE, or crystal-induced arthropathies. Correlate with serum autoantibodies and crystal panel below."
            fluid_color = "#FFFBEB"
            fluid_border = "#D97706"
        elif syn_clarity == "Bloody / Hemorrhagic":
            fluid_category = "🩸 HEMORRHAGIC ARTHROPATHY"
            fluid_action = "Consider hemophilia, trauma, over-anticoagulation, or joint hemangiomas."
            fluid_color = "#FEF2F2"
            fluid_border = "#B91C1C"

        st.markdown(f"""
        <div class='status-box' style='background-color: {fluid_color}; border-left: 5px solid {fluid_border};'>
            <strong>Fluid Category:</strong> {fluid_category}<br><br>
            <strong>Recommended Stewardship Action:</strong> {fluid_action}
        </div>
        """, unsafe_allow_html=True)

        if "Negatively Birefringent" in syn_crystals:
            st.error("💎 **CRYSTAL GUARD:** Monosodium Urate Crystals found. Confirms acute **Gouty Arthritis**.")
        elif "Positively Birefringent" in syn_crystals:
            st.warning("💎 **CRYSTAL GUARD:** Calcium Pyrophosphate (CPPD) Crystals found. Confirms **Pseudogout**.")

# ==============================================================================
# TAB 3: PRE-BIOLOGIC SAFETY CHECKLIST (NEW ADVANCED ELEMENT)
# ==============================================================================
with app_tab3:
    st.markdown("<div class='section-header'>🛡️ Pre-Biologic & Heavy Immunosuppression Safety Screen</div>", unsafe_allow_html=True)
    st.write("Ensure these mandatory safety protocols are satisfied before starting a patient on Biologics (TNF-inhibitors, Rituximab, etc.) or high-dose pulse steroids.")

    col_ch1, col_ch2 = st.columns(2)
    
    with col_ch1:
        st.markdown("### 📋 Mandatory Screening Checklist")
        tb_screen = st.checkbox("TB Screening Completed (Quantiferon Gold or TST text negative)", value=False)
        hbv_screen = st.checkbox("Hepatitis B Panel Clear (HBsAg negative and Anti-HBc negative)", value=False)
        hcv_screen = st.checkbox("Hepatitis C Screening Clear (Anti-HCV negative)", value=False)
        hiv_screen = st.checkbox("HIV Status Verified / Screened Negative", value=False)
        live_vax = st.checkbox("Verified that NO Live Attenuated Vaccines were given within 4 weeks", value=True)

    with col_ch2:
        st.markdown("### ⚡ Clinical Clearance Clearance Verification")
        
        if tb_screen and hbv_screen and hcv_screen and hiv_screen and live_vax:
            st.markdown("<div class='status-box' style='background-color: #F0FDF4; border-left: 5px solid #16A34A;'><strong>🟢 IMMUNOSUPPRESSION CLEARANCE APPROVED:</strong> All primary opportunistic infectious screens are clear. Safe to proceed with prescribing immunosuppressive or biologic regimens with routine clinical follow-up.</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='status-box' style='background-color: #FEF2F2; border-left: 5px solid #DC2626;'><strong>❌ HOLD PRESCRIPTION:</strong> Safety screen incomplete. Risk of fatal infectious reactivation:<br><br>"
                        "• If <strong>TB Screen</strong> is missing/positive: Risk of latent TB reactivation.<br>"
                        "• If <strong>HBV Panel</strong> is missing/positive: Biologics (especially Anti-CD20 Rituximab) can cause fulminant hepatic failure via HBV reactivation. Ensure prophylaxis is active if Anti-HBc is positive!</div>", unsafe_allow_html=True)

# ==============================================================================
# HIGH-YIELD BOARD EXAM REVIEW MATERIAL (Created for the Scientific Club)
# ==============================================================================
st.markdown("---")
st.markdown("<div class='board-header'>🎓 High-Yield Board-Level Review (Al-Ahli Scientific Research Club)</div>", unsafe_allow_html=True)

with st.expander("❓ Click to Reveal the Rheumatology Board Question & Scientific Rationale"):
    st.markdown("""
    **Clinical Scenario:** A 45-year-old male with severe rheumatoid arthritis is being evaluated in the clinic to initiate biologic therapy with an anti-TNF alpha inhibitor (Infliximab). His baseline infectious workup reveals a positive Quantiferon-TB Gold test, but a chest X-ray shows no active infiltrates or cavities. He is completely asymptomatic from a respiratory standpoint. 
    
    **Which of the following represents the most appropriate management sequence before the first dose of Infliximab is administered?**
    
    * **A)** Start Infliximab immediately since the chest X-ray is negative for active pulmonary tuberculosis.
    * **B)** Initiate treatment for Latent Tuberculosis Infection (LTBI) with Isoniazid and Rifapentine, and wait at least 1 to 2 months before starting Infliximab.
    * **C)** Cancel biologic therapy permanently; anti-TNF agents are absolutely contraindicated in anyone with a positive Quantiferon test.
    * **D)** Order a sputum culture for acid-fast bacilli (AFB) three times and proceed with Infliximab if they return negative.
    
    ---
    
    ### 📝 Comprehensive Scientific Evidence-Based Explanation:
    * **The Correct Answer is B.** This patient has documented **Latent Tuberculosis Infection (LTBI)** (positive Quantiferon with normal CXR and no symptoms). Anti-TNF therapies drastically downregulate granuloma maintenance, meaning starting a biologic in an untreated LTBI patient carries an extremely high risk of progression to **fulminant, disseminated, or miliary active tuberculosis**. 
    * **Clinical Pearl for the Club:** Guidelines require initiating latent TB prophylaxis (e.g., Isoniazid/Rifapentine or Isoniazid monotherapy) and completing at least **1 month of therapy** before safely introducing the first biologic dose. This is one of the most high-yield safety board questions in internal medicine!
    """)

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 11px;'>Al-Ahli Hospital Internal Medicine CDSS Platforms © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
