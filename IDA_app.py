import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Al-Ahli Anemia & Iron Deficit Engine",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for Clinical and Academic Excellence
st.markdown("""
    <style>
    .main-title { font-size:30px !important; font-weight: bold; color: #B91C1C; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:15px !important; color: #4B5563; text-align: center; margin-bottom: 25px; font-style: italic; }
    .branding-bar { background-color: #FEF2F2; padding: 20px; border-radius: 10px; border-left: 6px solid #B91C1C; margin-bottom: 25px; }
    .branding-bar strong { color: #B91C1C !important; font-weight: bold; }
    .branding-text { color: #1F2937 !important; font-size: 15px !important; line-height: 1.6; }
    .section-header { font-size:20px !important; font-weight: bold; color: #B91C1C; margin-top: 15px; margin-bottom: 15px; border-bottom: 2px solid #E5E7EB; padding-bottom: 5px; }
    .status-box { padding: 15px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #E5E7EB; background-color: #F9FAFB; }
    .board-header { font-size:22px !important; font-weight: bold; color: #D97706; margin-top: 30px; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<div class='main-title'>🩸 Al-Ahli Hospital Anemia & Iron Deficit Engine</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Advanced Decision Support System for Automated Diagnostic Phenotyping & Iron Substitution</div>", unsafe_allow_html=True)

# Professional Branding Block
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Project Founder & Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Clinical Core:</strong> Mentzer Index Diagnostic Trees, Ganzoni Total Deficit Protocol, AABB Blood Transfusion Thresholds
    </div>
</div>
""", unsafe_allow_html=True)

# Layout Split
col_input, col_dashboard = st.columns([1, 1.2])

# ==============================================================================
# LEFT COLUMN: CBC & IRON PROFILE INPUT PANEL
# ==============================================================================
with col_input:
    st.markdown("<div class='section-header'>📊 1. Complete Blood Count (CBC) Panel</div>", unsafe_allow_html=True)
    
    hb = st.number_input("Current Hemoglobin (g/dL):", min_value=3.0, max_value=18.0, value=8.5, step=0.1)
    hct = st.number_input("Hematocrit (Hct %):", min_value=10.0, max_value=55.0, value=26.0, step=1.0)
    mcv = st.number_input("Mean Corpuscular Volume (MCV fL):", min_value=45.0, max_value=130.0, value=68.0, step=1.0)
    rbc_count = st.number_input("Red Blood Cell Count (RBC × 10⁶/µL):", min_value=1.5, max_value=8.0, value=4.2, step=0.1)
    rdw = st.number_input("Red Cell Distribution Width (RDW %):", min_value=10.0, max_value=30.0, value=16.5, step=0.5)
    retic = st.number_input("Reticulocyte Count (%):", min_value=0.1, max_value=15.0, value=0.8, step=0.1)

    st.markdown("<div class='section-header'>🧪 2. Advanced Iron Biomarkers & Metrics</div>", unsafe_allow_html=True)
    ferritin = st.number_input("Serum Ferritin (ng/mL):", min_value=1, max_value=2000, value=15, step=5)
    
    # Advanced TSAT Inputs
    has_iron_profile = st.checkbox("Detailed Iron Profile Available (Serum Iron / TIBC)", value=False)
    serum_iron = st.number_input("Serum Iron (µg/dL):", min_value=10, max_value=300, value=35) if has_iron_profile else 0
    tibc = st.number_input("Total Iron Binding Capacity (TIBC µg/dL):", min_value=100, max_value=600, value=410) if has_iron_profile else 1
    
    weight = st.number_input("Patient Actual Body Weight (kg):", min_value=30, max_value=200, value=70, step=5)
    has_cardiac_history = st.checkbox("Patient has severe Cardiovascular Disease (e.g., Active ACS / CAD)", value=False)

    # ==========================================================================
    # INTERNAL MATHEMATICAL CALCULATIONS
    # ==========================================================================
    # 1. Corrected Reticulocyte Count
    corrected_retic = retic * (hct / 45.0)
    
    # 2. Mentzer Index Calculation (MCV / RBC)
    if rbc_count > 0:
        mentzer_index = mcv / rbc_count
    else:
        mentzer_index = 0
        
    # 3. TSAT Calculation
    tsat = (serum_iron / tibc) * 100 if has_iron_profile else 0
    
    # 4. Ganzoni Formula Math
    target_hb = 14.0 if has_cardiac_history else 13.0
    if target_hb > hb:
        ganzoni_deficit = (weight * (target_hb - hb) * 2.4) + 500
    else:
        ganzoni_deficit = 0

# ==============================================================================
# RIGHT COLUMN: AUTOMATED DIAGNOSTIC LOGIC & REPLACEMENT MATRIX
# ==============================================================================
with col_dashboard:
    st.markdown("<div class='section-header'>⚡ Automated Clinical Diagnostic Intelligence</div>", unsafe_allow_html=True)
    
    # Blood Transfusion Safety Switch
    if hb < 7.0 or (hb < 8.0 and has_cardiac_history):
        st.error(f"🚨 **CRITICAL TRANSFUSION TRIGGER MET (Hb = {hb} g/dL):**")
        st.markdown("""
        * **Immediate Action Plan:** Patient requires active **Packed RBC Transfusion** (1-2 units). Do not rely solely on iron replacement at this hour.
        * **Rationale:** Physiological tissue oxygenation is compromised. Target post-transfusion Hb is $> 7-8\ g/dL$.
        """)
        st.markdown("---")
        
    # Diagnostic Engine Logic Incorporating Mentzer Index & TSAT
    anemia_type = ""
    differential_diagnosis = ""
    clinical_action = ""
    box_color = "#F9FAFB"
    
    if mcv < 80:
        anemia_type = "🔬 Microcytic Anemia"
        if ferritin < 30 or (has_iron_profile and tsat < 20 and ferritin < 100):
            if mentzer_index > 13:
                differential_diagnosis = f"🎯 **Absolute Iron Deficiency Anemia (IDA)** (Mentzer Index: {mentzer_index:.1f} is $>13$, confirming cell volume loss due to substrate depletion)."
            else:
                differential_diagnosis = f"🎯 **Iron Deficiency Anemia with Concomitant Thalassemia Trait** (Mentzer Index: {mentzer_index:.1f} is $\le 13$)."
            clinical_action = "✅ **Action Plan:** Order GI endoscopy workup for source of blood loss. Initiate IV Iron substitution."
            box_color = "#FEF2F2"
        elif ferritin >= 100 and mentzer_index <= 13 and rdw <= 14.5:
            differential_diagnosis = f"🎯 **Thalassemia Minor / Trait Suspected** (Mentzer Index: {mentzer_index:.1f} is $\le 13$ with normal red cell distribution uniformity)."
            clinical_action = "⚠️ **Action Plan:** Hold empiric iron therapy. Order Hemoglobin Electrophoresis to screen for Alpha/Beta Thalassemia."
            box_color = "#FFFBEB"
        else:
            differential_diagnosis = "🎯 **Anemia of Chronic Disease (ACD) / Inflammation**"
            clinical_action = "📋 **Action Plan:** Check inflammatory cascade (CRP/ESR). If TSAT $<20\%$ with normal ferritin, consider functional iron deficiency component."
            box_color = "#F3F4F6"
            
    elif 80 <= mcv <= 100:
        anemia_type = "🌗 Normocytic Anemia"
        if corrected_retic >= 2.0:
            differential_diagnosis = "🎯 **Hyperproliferative Anemia (Acute Hemorrhage or Active Hemolysis)**"
            clinical_action = "🚨 **Action Plan:** Reticulocyte kinetics show marrow survival. Check LDH, Haptoglobin, Coomb's test, and search for occult bleeding."
            box_color = "#FEF2F2"
        else:
            differential_diagnosis = "🎯 **Hypoproliferative Anemia (Early Nutrient Deficiency, CKD, or Bone Marrow Suppression)**"
            clinical_action = "📋 **Action Plan:** Check renal markers (GFR) and serum erythropoietin levels."
            box_color = "#F3F4F6"
            
    else:
        anemia_type = "🌌 Macrocytic Anemia"
        if corrected_retic < 2.0:
            differential_diagnosis = "🎯 **Megaloblastic Anemia (Vitamin B12 / Folate Deficiencies) vs. Alcohol / Liver Suppression**"
            clinical_action = "✅ **Action Plan:** Check Serum B12 and Folate. Look for hypersegmented neutrophils on peripheral blood smear."
            box_color = "#FFFBEB"
        else:
            differential_diagnosis = "🎯 **Macrocytic Recovery Phase** (Active bone marrow responding to prior stress or drug interference)."
            box_color = "#F3F4F6"

    # Display Diagnostic Output Summary
    st.markdown(f"### Morphological Phenotype: `{anemia_type}`")
    st.markdown(f"""
    <div class='status-box' style='background-color: {box_color}; border-left: 5px solid #B91C1C;'>
        <strong>Primary Differential Diagnosis:** {differential_diagnosis}<br><br>
        <strong>Guideline Action Protocol:** {clinical_action}
    </div>
    """, unsafe_allow_html=True)

    # ADVANCED KINETICS AND DOSING TABS
    tab_ganzoni, tab_biomarkers = st.tabs(["💊 IV Iron Ganzoni Calculation", "🧬 Advanced Biomarker Panels"])
    
    with tab_ganzoni:
        st.markdown("### 🧬 Tailored Intravenous Iron Prescription Guide")
        if ganzoni_deficit > 0:
            st.metric("Total Body Iron Deficit (Ganzoni Score)", f"{round(ganzoni_deficit)} mg")
            
            st.markdown("#### 🧪 Standard Dosing Implementation Guide:")
            col_v1, col_v2 = st.columns(2)
            with col_v1:
                vials_required = ganzoni_deficit / 500
                st.info(f"**Ferric Carboxymaltose (e.g., Ferinject 500mg/vial):**\n* Total Required: `{vials_required:.1f} vials` \n* Infusion Limit: Maximum 1000mg per weekly dose.")
            with col_v2:
                st.success(f"**Clinical Order Set:** Dilute in 100mL Normal Saline and run over 15 minutes. Re-evaluate Hemoglobin metrics in **4 to 6 weeks**.")
        else:
            st.write("🟢 No iron deficit calculated based on current target boundaries.")

    with tab_biomarkers:
        st.markdown("### 🧬 Kinetic Diagnostics and Indices")
        col_b1, col_b2 = st.columns(2)
        with col_b1:
            st.metric("Calculated Mentzer Index", f"{mentzer_index:.1f}", 
                      delta="Favors IDA (>13)" if mentzer_index > 13 else "Favors Thalassemia (≤13)",
                      delta_color="normal" if mentzer_index > 13 else "inverse")
        with col_b2:
            if has_iron_profile:
                st.metric("Transferrin Saturation (TSAT)", f"{tsat:.1f} %",
                          delta="Absolute Iron Deficiency" if tsat < 20 else "Normal Saturation Pools",
                          delta_color="inverse" if tsat < 20 else "normal")
            else:
                st.write("⚪ Complete the Iron Profile check box to calculate dynamic TSAT index.")

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 11px;'>Al-Ahli Hospital Internal Medicine CDSS Platforms © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
