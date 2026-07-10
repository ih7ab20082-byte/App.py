import streamlit as st

st.set_page_config(page_title="Al-Ahli ID Command Center", layout="wide")

# --- Custom Styling ---
st.markdown("""<style>
    .stApp { background-color: #f8fafc; }
    .header { color: #7f1d1d; font-weight: bold; text-align: center; }
    .inv-box { background-color: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #e2e8f0; }
</style>""", unsafe_allow_html=True)

st.markdown("<h1 class='header'>🦠 Al-Ahli Hospital: Intelligent ID & Stewardship Engine</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'>Director: Dr. Ihab Abbass Abu Hilail</p>", unsafe_allow_html=True)

# --- Inventory Status (The Smart Stock) ---
with st.sidebar:
    st.markdown("<div class='inv-box'><h3>📦 Pharmacy Stock Status</h3></div>", unsafe_allow_html=True)
    stock = {
        "Vanco": st.checkbox("Vancomycin Available", True),
        "Tazocin": st.checkbox("Tazocin Available", False),
        "Mero": st.checkbox("Meropenem Available", False),
        "Colistin": st.checkbox("Colistin Available", False),
        "Tigacyclin": st.checkbox("Tigacyclin Available", False)
    }

# --- Module Selector ---
menu = st.sidebar.radio("Select System:", ["CNS/Meningitis", "Respiratory/CAP/HAP", "Abdominal/UTI", "Diabetic Foot/Osteomyelitis"])

# --- Logic Implementation ---
if menu == "Diabetic Foot/Osteomyelitis":
    st.header("🦶 Diabetic Foot & Osteomyelitis")
    status = st.radio("Patient Status:", ["Stable (Outpatient/Ward)", "Unstable (Septic/Severe)"])
    
    st.subheader("Approach & Diagnosis:")
    st.write("1. Check for Peripheral Vascular Disease (PVD) & Neuropathy.")
    st.write("2. Bone probe test (positive = high probability of Osteomyelitis).")
    st.write("3. Imaging: X-ray initially, MRI is Gold Standard.")
    
    st.subheader("Rx Strategy:")
    if status == "Unstable (Septic/Severe)":
        if stock["Mero"]:
            st.error("Protocol: Meropenem + Vancomycin (if available).")
        else:
            st.error("Protocol: Rocephin + Flagyl + Gentamycin (De-escalate ASAP).")
    else:
        st.success("Protocol: Rocephin + Flagyl + Levofloxacin (Oral if possible).")

elif menu == "CNS/Meningitis":
    st.header("🧠 Meningitis & Encephalitis")
    st.write("Criteria: Fever, Headache, Nuchal rigidity. LP findings: Bacterial = High protein, Low glucose.")
    
    if stock["Vanco"]:
        st.warning("Rx: Vancomycin + Rocephin + Dexamethasone.")
    else:
        st.warning("Rx: Rocephin + Dexamethasone. (Urgent ID Consult).")

# --- Stewardship Logic ---
st.sidebar.markdown("---")
st.write("💡 **Stewardship Tip:** Always aim for 48h re-evaluation for De-escalation.")
