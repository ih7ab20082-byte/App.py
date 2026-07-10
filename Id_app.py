import streamlit as st

st.set_page_config(page_title="Al-Ahli ID Pro Engine", layout="wide")

st.markdown("<h1 style='text-align: center; color: #991b1b;'>🦠 Al-Ahli ID Pro: Diagnostic & Stewardship Engine</h1>", unsafe_allow_html=True)

# --- 1. Inventory ---
with st.sidebar:
    st.header("📦 Pharmacy Inventory")
    stock = {
        "Vanco": st.checkbox("Vancomycin"),
        "Mero": st.checkbox("Meropenem"),
        "Rocephin_Flagyl": st.checkbox("Rocephin + Flagyl", True),
        "Levoflox": st.checkbox("Levofloxacin", True),
        "Doxy_Rif": st.checkbox("Doxy + Rifampin", True),
        "Gent": st.checkbox("Gentamycin")
    }

# --- 2. Tabs ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["CNS", "Respiratory", "Abdominal/UTI", "Foot/Skin", "Endo/Brucella"])

# --- CNS ---
with tab1:
    st.header("🧠 CNS: Meningitis vs Encephalitis")
    cns_dx = st.selectbox("Diagnosis:", ["Meningitis", "Encephalitis"])
    st.subheader("Diagnostic Criteria")
    if cns_dx == "Meningitis":
        st.write("- **LP Findings:** High Protein, Low Glucose, Neutrophilic (Bacterial) vs Lymphocytic (Viral).")
        st.write("- **Signs:** Fever, Nuchal Rigidity, Kernig/Brudzinski signs.")
    else:
        st.write("- **Features:** Altered Mental Status, Seizures, Focal neuro deficits.")
    
    if stock["Vanco"]: st.success("Rx: Vanco + Rocephin + Dexamethasone")
    else: st.warning("Rx: Rocephin + Dexamethasone")

# --- Respiratory ---
with tab2:
    st.header("🫁 CAP / HAP")
    st.write("### Dx Criteria:")
    st.write("- **CAP:** New infiltrate + Fever/Cough. **HAP:** >48h admission.")
    sev = st.radio("Patient Status:", ["Stable", "Unstable/Septic"])
    if sev == "Stable": st.success("Rx: Rocephin + Azithromycin")
    else: 
        if stock["Mero"]: st.error("Rx: Meropenem + Vanco")
        else: st.warning("Rx: Rocephin + Levofloxacin + Gentamycin")

# --- Abdominal & UTI ---
with tab3:
    st.header("腹 Abdominal & UTI")
    st.write("### Dx:")
    st.write("- **Intra-abd:** Imaging (CT), Signs of peritonitis.")
    st.write("- **Complicated UTI:** Pyuria, positive culture + Systemic signs.")
    if stock["Mero"]: st.error("Rx: Meropenem (Intra-abd)")
    else: st.success("Rx: Rocephin + Flagyl")

# --- Foot/Skin ---
with tab4:
    st.header("🦶 Diabetic Foot & Osteomyelitis")
    st.write("### Diagnostic Approach:")
    st.write("- **Probe-to-bone test:** Positive = High Osteo risk.")
    st.write("- **Imaging:** X-ray (late signs), MRI (Gold Standard).")
    st.write("- **Culture:** Deep tissue biopsy (Stop superficial swabs).")
    if st.radio("Status:", ["Stable", "Septic"]) == "Septic":
        st.error("Rx: Rocephin + Flagyl + Gentamycin")
    else: st.success("Rx: Levofloxacin + Flagyl")

# --- Endo / Brucella ---
with tab5:
    st.header("❤️ Endocarditis & Brucellosis")
    cond = st.selectbox("Case:", ["Infective Endocarditis", "Brucellosis"])
    if cond == "Infective Endocarditis":
        st.write("### Duke's Criteria:")
        st.write("- **Major:** Blood cultures + Echo findings.")
        st.write("- **Minor:** Fever, Vascular phenomena, Immunologic signs.")
        st.warning("Rx: Rocephin + Gentamycin (if Vanco not avail)")
    else:
        st.write("### Brucellosis Dx:")
        st.write("- Fever, Arthralgia, Night sweats + High index of suspicion (Epidemiology).")
        if stock["Doxy_Rif"]: st.success("Rx: Doxycycline + Rifampin (6 weeks).")
        else: st.warning("Rx: Doxycycline + Gentamycin.")

st.sidebar.markdown("---")
st.sidebar.write("💡 **Stewardship:** Always reassess at 48h.")
