import streamlit as st

# Page Configuration
st.set_page_config(page_title="Al-Ahli ID Master Engine", layout="wide")

# Styling
st.markdown("""
    <style>
    .main-title { font-size:32px !important; font-weight: bold; color: #7f1d1d; text-align: center; }
    .section-header { font-size:22px !important; font-weight: bold; color: #991b1b; margin-top: 20px; }
    .stApp { background-color: #fef2f2; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🦠 Al-Ahli Hospital: Intelligent ID & Stewardship Engine</div>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'><strong>Clinical Director:</strong> Dr. Ihab Abbass Abu Hilail</p>", unsafe_allow_html=True)

# --- Inventory Sidebar (THE SMART STOCK) ---
with st.sidebar:
    st.header("📦 Pharmacy Inventory Status")
    stock = {
        "Vanco": st.checkbox("Vancomycin Available", False),
        "Tazocin": st.checkbox("Tazocin Available", False),
        "Mero": st.checkbox("Meropenem Available", False),
        "Colistin": st.checkbox("Colistin Available", False),
        "Tigacyclin": st.checkbox("Tigacyclin Available", False),
        "Rocephin_Flagyl": st.checkbox("Rocephin & Flagyl Available", True)
    }

# --- Module Selector ---
menu = st.radio("Select System:", ["CNS & Meningitis", "Respiratory (CAP/HAP)", "Abdominal & UTI", "Diabetic Foot & Osteomyelitis", "Endocarditis & Brucellosis"])

# --- CNS & Meningitis ---
if menu == "CNS & Meningitis":
    st.header("🧠 CNS Infections")
    lp = st.selectbox("LP Findings:", ["Bacterial", "Viral", "Fungal"])
    if lp == "Bacterial":
        if stock["Vanco"]:
            st.error("Protocol: Vancomycin + Rocephin + Dexamethasone.")
        else:
            st.warning("Protocol: Rocephin + Dexamethasone (Consult ID if no clinical response).")
    st.write("---")
    st.markdown("### 📋 CSF Analysis Findings:")
    st.markdown("""
    | Type | Cells | Protein | Glucose |
    | :--- | :--- | :--- | :--- |
    | Bacterial | High Neutrophils | High | Low |
    | Viral | High Lymphocytes | Normal/Mild | Normal |
    | TB | High Lymphocytes | Very High | Low |
    """)

# --- Respiratory ---
elif menu == "Respiratory (CAP/HAP)":
    st.header("🫁 CAP & HAP")
    sev = st.radio("Severity:", ["Stable", "Septic/Unstable"])
    if sev == "Stable":
        st.success("Protocol: Rocephin + Azithromycin PO.")
    else:
        st.warning("Protocol: Rocephin + Levofloxacin + (Tazocin/Meropenem if available).")

# --- Abdominal & UTI ---
elif menu == "Abdominal & UTI":
    st.header("腹 Abdominal & UTI")
    cond = st.selectbox("Condition:", ["Intra-abdominal", "UTI (Complicated)", "Prostatitis"])
    if cond == "Intra-abdominal":
        if stock["Mero"]:
            st.error("Protocol: Meropenem (Septic coverage).")
        else:
            st.success("Protocol: Rocephin + Flagyl (Standard of Care).")
    elif cond == "UTI (Complicated)":
        st.success("Protocol: Rocephin or Levofloxacin.")

# --- Diabetic Foot / Osteo ---
elif menu == "Diabetic Foot & Osteomyelitis":
    st.header("🦶 Diabetic Foot & Osteomyelitis")
    stat = st.radio("Status:", ["Stable", "Septic/Unstable"])
    st.markdown("### 🧠 Diagnostic Approach:")
    st.write("1. Probe-to-bone test. 2. X-ray / MRI. 3. Cultures from deep tissue (not superficial swab).")
    if stat == "Septic/Unstable":
        st.error("Rx: Vancomycin + Rocephin + Flagyl (If stocks available). If Vanco/Tazocin missing -> Gentamycin + Flagyl.")
    else:
        st.success("Rx: Levofloxacin + Flagyl.")

# --- Endocarditis & Brucellosis ---
elif menu == "Endocarditis & Brucellosis":
    st.header("❤️ Endocarditis & Brucellosis")
    sub = st.selectbox("Select:", ["Infective Endocarditis", "Brucellosis"])
    if sub == "Infective Endocarditis":
        st.markdown("### 🎯 Duke's Criteria:")
        st.write("Major: Positive blood cultures, Echo findings.")
        st.warning("Rx: Vancomycin + Rocephin (Adjust based on sensitivity).")
    elif sub == "Brucellosis":
        st.info("Rx: Doxycycline + Rifampin or Doxycycline + Gentamycin.")

st.sidebar.markdown("---")
st.sidebar.write("💡 **Stewardship Reminder:** De-escalate antibiotics 48-72h post-culture results!")
