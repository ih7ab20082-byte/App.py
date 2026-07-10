import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Al-Ahli Rheumatology Diagnostic Suite",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for Clinical & Academic Sophistication
st.markdown("""
    <style>
    .main-title { font-size:32px !important; font-weight: bold; color: #1E3A8A; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:16px !important; color: #4B5563; text-align: center; margin-bottom: 25px; font-style: italic; }
    .branding-bar { background-color: #F0F4F8; padding: 20px; border-radius: 10px; border-left: 6px solid #1E3A8A; margin-bottom: 25px; }
    .branding-bar strong { color: #1E3A8A !important; font-weight: bold; }
    .branding-text { color: #1F2937 !important; font-size: 15px !important; line-height: 1.6; }
    .section-header { font-size:22px !important; font-weight: bold; color: #1E3A8A; margin-top: 15px; margin-bottom: 15px; border-bottom: 2px solid #E5E7EB; padding-bottom: 5px; }
    .status-box { padding: 15px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #E5E7EB; background-color: #F9FAFB; line-height: 1.6; }
    .board-header { font-size:24px !important; font-weight: bold; color: #D97706; margin-top: 30px; margin-bottom: 15px; }
    .danger-box { padding: 15px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #DC2626; background-color: #FEF2F2; color: #991B1B; line-height: 1.6; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<div class='main-title'>🩺 Al-Ahli Hospital Advanced Rheumatology Diagnostic Suite</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Comprehensive Decision-Support & Clinical Stewardship Engine for Internal Medicine Residents</div>", unsafe_allow_html=True)

# Professional Branding Block
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Project Founder & Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Clinical Core:</strong> ACR/EULAR Classification Rules, Advanced Kinetics Matrix, Vasculitis Red-Flag Alerts
    </div>
</div>
""", unsafe_allow_html=True)

# Creating Tabs for the Whole Suite
tabs = st.tabs([
    "🦋 SLE Classifier", 
    "🦴 RA Calculator", 
    "🧪 Synovial Interpreter", 
    "🤰 APS Risk Tiering", 
    "💊 Steroid Equivalence", 
    "🚨 Vasculitis Gate",
    "🛡️ Pre-Biologic Screen"
])

# ==============================================================================
# TAB 1: EULAR/ACR SLE CLASSIFIER
# ==============================================================================
with tabs[0]:
    st.markdown("<div class='section-header'>🔬 EULAR/ACR 2019 Systemic Lupus Erythematosus Classifier</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        ana_titer = st.selectbox("ANA Titer (Entry Criterion):", ["Negative / Less than 1:80", "1:80", "1:160", "1:320", "1:640", "1:1280"], key="sle_ana")
        ana_pattern = st.selectbox("ANA Morphological Pattern:", ["Homogeneous", "Speckled", "Centromere", "Nucleolar", "Peripheral / Rim"], key="sle_pat")
        fever = st.checkbox("Unexplained Fever (> 38.5°C)", value=False)
        
        cutaneous_select = st.selectbox("Skin Manifestation:", ["None", "Acute Cutaneous Lupus / Malar Rash (6 pts)", "Subacute Cutaneous OR Discoid Lupus (4 pts)", "Oral Ulcers (2 pts)", "Non-scarring Alopecia (2 pts)"])
        joint_select = st.checkbox("Synovitis / Arthritis in ≥ 2 joints with morning stiffness (6 pts)", value=False)
        
    with col2:
        renal_select = st.selectbox("Renal Biopsy / Proteinuria:", ["None", "Class III or IV Lupus Nephritis (10 pts)", "Class II or V Lupus Nephritis (8 pts)", "Proteinuria > 0.5g/24h (4 pts)"])
        hemato_select = st.multiselect("Hematological Parameters:", ["Autoimmune Hemolytic Anemia (4 pts)", "Thrombocytopenia < 100k (4 pts)", "Leukopenia < 4k (3 pts)"])
        immuno_select = st.multiselect("Specific Autoantibodies:", ["Anti-dsDNA OR Anti-Smith (6 pts)", "Antiphospholipid Antibodies (2 pts)"])
        comp_select = st.selectbox("Complement Levels:", ["Normal Complements", "Both Low C3 AND Low C4 (4 pts)", "Either Low C3 OR Low C4 alone (3 pts)"])

    # Score Calculation
    score = (2 if fever else 0)
    score += {"None": 0, "Acute Cutaneous Lupus / Malar Rash (6 pts)": 6, "Subacute Cutaneous OR Discoid Lupus (4 pts)": 4, "Oral Ulcers (2 pts)": 2, "Non-scarring Alopecia (2 pts)": 2}[cutaneous_select]
    score += 6 if joint_select else 0
    score += {"None": 0, "Class III or IV Lupus Nephritis (10 pts)": 10, "Class II or V Lupus Nephritis (8 pts)": 8, "Proteinuria > 0.5g/24h (4 pts)": 4}[renal_select]
    
    h_pts = [0]
    if "Autoimmune Hemolytic Anemia (4 pts)" in hemato_select: h_pts.append(4)
    if "Thrombocytopenia < 100k (4 pts)" in hemato_select: h_pts.append(4)
    if "Leukopenia < 4k (3 pts)" in hemato_select: h_pts.append(3)
    score += max(h_pts)
    
    i_pts = [0]
    if "Anti-dsDNA OR Anti-Smith (6 pts)" in immuno_select: i_pts.append(6)
    if "Antiphospholipid Antibodies (2 pts)" in immuno_select: i_pts.append(2)
    score += max(i_pts)
    
    score += {"Normal Complements": 0, "Both Low C3 AND Low C4 (4 pts)": 4, "Either Low C3 OR Low C4 alone (3 pts)": 3}[comp_select]

    st.markdown(f"### Total SLE Score: `{score} / 10 Points Required`")
    if ana_titer == "Negative / Less than 1:80":
        st.error("🛑 Entry Criterion Failed: ANA must be positive ($\ge 1:80$) for SLE classification.")
    elif score >= 10:
        st.success("✅ Criteria Met: Confirms Classification of Systemic Lupus Erythematosus (SLE).")
    else:
        st.warning("⚠️ Probable Criteria Insufficiency for formal classification.")

# ==============================================================================
# TAB 2: ACR/EULAR 2010 RHEUMATOID ARTHRITIS CALCULATOR (NEW)
# ==============================================================================
with tabs[1]:
    st.markdown("<div class='section-header'>Joint Destruction Guard: ACR/EULAR 2010 Rheumatoid Arthritis Score</div>", unsafe_allow_html=True)
    col_ra1, col_ra2 = st.columns(2)
    
    with col_ra1:
        ra_joints = st.selectbox("Joint Involvement Distribution:", [
            "1 large joint (0 pts)",
            "2-10 large joints (1 pt)",
            "1-3 small joints (with or without large joints) (2 pts)",
            "4-10 small joints (with or without large joints) (3 pts)",
            ">10 joints (at least 1 small joint) (5 pts)"
        ])
        ra_serology = st.selectbox("Serology (RF & Anti-CCP):", [
            "Negative RF AND Negative Anti-CCP (0 pts)",
            "Low-positive RF OR Low-positive Anti-CCP (<3x ULN) (2 pts)",
            "High-positive RF OR High-positive Anti-CCP (≥3x ULN) (3 pts)"
        ])
    
    with col_ra2:
        ra_reactants = st.selectbox("Acute-Phase Reactants (CRP & ESR):", [
            "Normal CRP AND Normal ESR (0 pts)",
            "Abnormal CRP OR Abnormal ESR (1 pt)"
        ])
        ra_duration = st.selectbox("Duration of Symptoms:", [
            "< 6 Weeks (0 pts)",
            "≥ 6 Weeks (1 pt)"
        ])

    # Score Mapping
    ra_score = int(ra_joints[-6]) if ra_joints[1].isdigit() or ra_joints[0] == ">" else int(ra_joints[2])
    ra_score = 5 if ra_joints[0] == ">" else ra_score
    ra_score += int(ra_serology[-6])
    ra_score += int(ra_reactants[-6])
    ra_score += int(ra_duration[-6])
    
    st.markdown(f"### Total RA Score: `{ra_score} / 6 Points Required`")
    if ra_score >= 6:
        st.success("🎉 **DEFINITE RHEUMATOID ARTHRITIS:** Patient qualifies for early DMARD integration (e.g., Methotrexate) to prevent erosive joint pathomechanics.")
    else:
        st.info("ℹ️ Does not meet full diagnostic criteria for definite RA at this juncture.")

# ==============================================================================
# TAB 3: SYNOVIAL FLUID INTERPRETER
# ==============================================================================
with tabs[2]:
    st.markdown("<div class='section-header'>🧪 Synovial Fluid Differential Kinetic Engine</div>", unsafe_allow_html=True)
    col_syn1, col_syn2 = st.columns(2)
    with col_syn1:
        syn_wbc = st.number_input("Synovial WBC Count (cells/µL):", min_value=0, max_value=250000, value=1500)
        syn_pmn = st.slider("PMN Neutrophils (%):", min_value=0, max_value=100, value=25)
        syn_crystals = st.selectbox("Microscopy Crystals:", ["None", "Needle-shaped, Negatively Birefringent (Gout)", "Rhomboid-shaped, Positively Birefringent (Pseudogout)"])
    
    with col_syn2:
        if syn_wbc > 50000 or syn_pmn > 75:
            st.markdown("<div class='danger-box'><strong>🚨 EMERGENCY ALERT: SEPTIC ARTHRITIS HIGHLY LIKELY!</strong><br>Perform emergency joint aspiration, send urgent Gram stain, and start empiric IV Vancomycin + Ceftazidime. Delayed therapy causes permanent chondrocyte death within 24 hours.</div>", unsafe_allow_html=True)
        elif 2000 <= syn_wbc <= 50000:
            st.markdown("<div class='status-box' style='border-left: 5px solid #D97706;'><strong>🔥 Inflammatory Pattern:</strong> Consistent with Rheumatoid Arthritis, Crystal Arthropathy, or Autoimmune flares.</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='status-box'><strong>🟢 Non-Inflammatory / Osteoarthritic Pattern:</strong> Consistent with degenerative joint disease or trauma.</div>", unsafe_allow_html=True)

        if "Gout" in syn_crystals: st.error("💎 Crystal-Confirmed Gouty Arthritis.")
        elif "Pseudogout" in syn_crystals: st.warning("💎 Crystal-Confirmed CPPD (Pseudogout).")

# ==============================================================================
# TAB 4: APS CLASSIFIER & RISK TIERING (NEW)
# ==============================================================================
with tabs[3]:
    st.markdown("<div class='section-header'>🤰 Antiphospholipid Syndrome (APS) Risk Stratification Suite</div>", unsafe_allow_html=True)
    col_aps1, col_aps2 = st.columns(2)
    
    with col_aps1:
        st.subheader("Clinical Criteria")
        thrombosis = st.checkbox("Vascular Thrombosis (Arterial, Deep Venous, or Small Vessel confirmed by imaging/histology)")
        pregnancy = st.multiselect("Pregnancy Complications:", [
            "≥1 unexplained death of normal fetus at/beyond 10th week of gestation",
            "≥1 premature birth of normal neonate before 34th week due to severe eclampsia/placental insufficiency",
            "≥3 unexplained consecutive spontaneous abortions before 10th week"
        ])
    
    with col_aps2:
        st.subheader("Laboratory Criteria")
        labs = st.multiselect("Positive Serology (Must be present on 2 or more occasions at least 12 weeks apart):", [
            "Lupus Anticoagulant (LA)",
            "Anti-cardiolipin IgG or IgM (Medium/High titer >40 GPL/MPL)",
            "Anti-beta2-Glycoprotein I IgG or IgM (>99th percentile)"
        ])

    st.markdown("### 📊 Classification Logic")
    clinical_met = thrombosis or len(pregnancy) > 0
    lab_met = len(labs) > 0
    
    if clinical_met and lab_met:
        st.success("🩸 **CRITERIA MET FOR DEFINITE APS:** Patient possesses both clinical and serological profiles. Requires long-term anticoagulation (Warfarin is gold-standard; DOACs are contraindicated in triple-positive APS due to high failure rates).")
        st.warning("⚠️ **The 12-Week Rule:** Ensure these positive labs are repeated 12 weeks from baseline to clear transient post-infectious elevations.")
    else:
        st.info("ℹ️ Criteria incomplete. Requires at least ONE clinical AND at least ONE laboratory criterion for diagnosis.")

# ==============================================================================
# TAB 5: STEROID DOSE EQUIVALENCY & TAPERING GUIDE (NEW)
# ==============================================================================
with tabs[4]:
    st.markdown("<div class='section-header'>💉 Clinical Pharmacology: Corticosteroid Equivalence Engine</div>", unsafe_allow_html=True)
    
    col_st1, col_st2 = st.columns(2)
    with col_st1:
        source_steroid = st.selectbox("Select Current Steroid:", [
            "Hydrocortisone", "Prednisone", "Prednisolone", "Methylprednisolone", "Dexamethasone"
        ])
        source_dose = st.number_input("Enter Current Dose (mg):", min_value=0.0, value=5.0, step=1.0)
    
    # Ratios referenced to 5mg Prednisone
    ratios = {
        "Hydrocortisone": 20.0, "Prednisone": 5.0, "Prednisolone": 5.0, "Methylprednisolone": 4.0, "Dexamethasone": 0.75
    }
    
    base_prednisone_equiv = (source_dose / ratios[source_steroid]) * 5.0
    
    with col_st2:
        st.markdown(f"### 🎯 Equivalent Dose Matrix")
        st.write(f"This is equivalent to **`{base_prednisone_equiv:.2f} mg`** of Oral Prednisone.")
        
        # Display all conversions
        st.markdown(f"""
        * **Hydrocortisone:** `{(base_prednisone_equiv / 5.0) * 20.0:.2f} mg` (Short-acting)
        * **Prednisone / Prednisolone:** `{base_prednisone_equiv:.2f} mg` (Intermediate-acting)
        * **Methylprednisolone:** `{(base_prednisone_equiv / 5.0) * 4.0:.2f} mg` (Intermediate-acting)
        * **Dexamethasone:** `{(base_prednisone_equiv / 5.0) * 0.75:.2f} mg` (Long-acting / High potency)
        """)
        
    if base_prednisone_equiv >= 20.0:
        st.error("🚨 **ADRENAL CRISIS RISK:** Patient is on high-dose supraphysiologic steroids. Do NOT discontinue abruptly. If used for >3 weeks, initiate a structured slow tapering protocol to allow HPA-axis recovery.")

# ==============================================================================
# TAB 6: VASCULITIS RED-FLAGS & ANCA INTERPRETER (NEW)
# ==============================================================================
with tabs[5]:
    st.markdown("<div class='section-header'>👁️ Vasculitis Red-Flags & Serological Classifier</div>", unsafe_allow_html=True)
    
    v_flags = st.multiselect("Select critical presentation markers:", [
        "New onset severe temporal headache with jaw claudication OR sudden visual loss",
        "Palpable Purpura (Non-blanching cutaneous lesions)",
        "Pulmonary-Renal Syndrome (Hemoptysis + Rapidly Progressive Glomerulonephritis)",
        "Mononeuritis Multiplex (Foot drop / Wrist drop asymmetry)"
    ])
    
    v_anca = st.radio("ANCA Serology Panel Profile:", [
        "Negative ANCA", 
        "c-ANCA positive (PR3-specific reactivity)", 
        "p-ANCA positive (MPO-specific reactivity)"
    ])
    
    if "New onset severe temporal headache with jaw claudication OR sudden visual loss" in v_flags:
        st.markdown("<div class='danger-box'><strong>🚨 EMERGENCY ALERT: SUSPECTED GIANT CELL ARTHRITIS (TEMPORAL)</strong><br>Do not wait for a temporal artery biopsy! Initiate high dose IV Methylprednisolone or oral Prednisone (60mg) immediately to protect patient from permanent, irreversible blindness.</div>", unsafe_allow_html=True)
        
    if "Pulmonary-Renal Syndrome (Hemoptysis + Rapidly Progressive Glomerulonephritis)" in v_flags:
        if v_anca == "c-ANCA positive (PR3-specific reactivity)":
            st.error("🩺 **Granulomatosis with Polyangiitis (GPA / Wegener's):** Classic c-ANCA/PR3 correlation. Requires immediate pulse steroids + Rituximab or Cyclophosphamide to rescue lung and renal parenchyma.")
        elif v_anca == "p-ANCA positive (MPO-specific reactivity)":
            st.error("🩺 **Microscopic Polyangiitis (MPA) OR EGPA (Churg-Strauss):** Correlate with peripheral eosinophilia and asthma history to clarify specific phenotype.")

# ==============================================================================
# TAB 7: PRE-BIOLOGIC SAFETY CHECKLIST
# ==============================================================================
with tabs[6]:
    st.markdown("<div class='section-header'>🛡️ Pre-Biologic & Immunosuppressive Safety Protocol</div>", unsafe_allow_html=True)
    tb_screen = st.checkbox("TB Screen Clear (Quantiferon-Gold negative)", value=False)
    hbv_screen = st.checkbox("Hepatitis B Panel Clear (HBsAg & Anti-HBc negative)", value=False)
    hcv_screen = st.checkbox("Hepatitis C Clear (Anti-HCV negative)", value=False)
    live_vax = st.checkbox("No Live Vaccines administered within trailing 4 weeks", value=True)
    
    if tb_screen and hbv_screen and hcv_screen and live_vax:
        st.success("🟢 Biologic Stewardship Clearance Approved. Safe to proceed with Anti-TNF or targeted biologic therapy.")
    else:
        st.markdown("<div class='danger-box'><strong>🛑 HOLD PRESCRIPTION:</strong> Checklist incomplete. Inadvertent Anti-TNF delivery in untreated Latent TB triggers catastrophic granuloma breakdown and disseminated miliary TB reactivation.</div>", unsafe_allow_html=True)

# ==============================================================================
# HIGH-YIELD BOARD EXAM REVIEW MATERIAL
# ==============================================================================
st.markdown("---")
st.markdown("<div class='board-header'>🎓 High-Yield Board-Level Review (Al-Ahli Scientific Research Club)</div>", unsafe_allow_html=True)

with st.expander("❓ Click to Reveal the Rheumatology Board Question & Scientific Rationale"):
    st.markdown("""
    **Clinical Scenario:** A 32-year-old female with known Systemic Lupus Erythematosus (SLE) presents with acute painful swelling of the left calf. Duplex ultrasonography confirms an extensive proximal deep vein thrombosis (DVT). Her past medical history is notable for two spontaneous first-trimester miscarriages. Laboratory evaluation reveals a prolonged activated partial thromboplastin time (aPTT) that fails to correct on a 1:1 mixing study, and a high-titer IgG anticardiolipin antibody.
    
    **Which of the following represents the most appropriate long-term management strategy for this patient?**
    
    * **A)** Start Rivaroxaban (DOAC) 20 mg daily, as it requires no monitoring and is non-inferior to Warfarin.
    * **B)** Initiate therapeutic Heparin bridging to long-term Warfarin therapy, targeting an INR of 2.0–3.0.
    * **C)** Prescribe Low-Dose Aspirin (81 mg) daily combined with hydroxychloroquine, avoids anticoagulation risks.
    * **D)** Deliver a 6-month course of Apixaban and discontinue if follow-up ultrasound shows clot resolution.
    
    ---
    
    ### 📝 Comprehensive Scientific Evidence-Based Explanation:
    * **The Correct Answer is B.** This patient fulfills the criteria for **Secondary Antiphospholipid Syndrome (APS)** secondary to SLE, with a confirmed thrombotic event (DVT) and laboratory confirmation (mixing study failure indicating a lupus anticoagulant and positive cardiolipin). 
    * **Clinical Pearl for the Club (The TRAPS Trial Evidence):** Landmark clinical trials (like the TRAPS trial) demonstrated that DOACs (Rivaroxaban, Apixaban) are **inferior** to Warfarin in patients with high-risk triple-positive or thrombotic APS, showing significantly higher rates of recurrent arterial and venous thromboembolic events. Therefore, lifelong therapeutic anticoagulation with **Warfarin (INR 2.0-3.0)** remains the absolute gold standard!
    """)

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 11px;'>Al-Ahli Hospital Internal Medicine CDSS Platforms © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
