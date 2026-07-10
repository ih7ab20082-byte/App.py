import streamlit as st

# Page Configuration
st.set_page_config(page_title="Al-Ahli ID Master Engine", layout="wide")

st.markdown("<h1 style='color: #7f1d1d; text-align: center;'>🦠 Al-Ahli ID Master Engine: Clinical Command Center</h1>", unsafe_allow_html=True)

# --- Inventory Status ---
with st.sidebar:
    st.header("📦 Pharmacy Stock Status")
    stock = {
        "Vanco": st.checkbox("Vancomycin", False),
        "Tazocin": st.checkbox("Tazocin", False),
        "Mero": st.checkbox("Meropenem", False),
        "Doxy": st.checkbox("Doxycycline", True),
        "Rifampin": st.checkbox("Rifampin", True),
        "Gent": st.checkbox("Gentamycin", True)
    }

# --- Module Selector ---
menu = st.radio("System/Condition:", ["CNS & Meningitis", "Respiratory", "Abdominal & UTI", "Diabetic Foot", "Endocarditis", "Brucellosis"])

# --- Endocarditis Module ---
if menu == "Endocarditis":
    st.header("❤️ Infective Endocarditis (IE)")
    st.markdown("### 🎯 Duke's Criteria Checklist:")
    fever = st.checkbox("Fever > 38°C")
    echo = st.checkbox("Positive Echo (Vegetations)")
    bc = st.checkbox("Positive Blood Cultures")
    if fever and echo and bc:
        st.error("Diagnosis: Definite IE. Start Empiric Therapy.")
    
    st.subheader("Rx Strategy:")
    if stock["Vanco"]:
        st.success("Protocol: Vancomycin + Rocephin (Standard).")
    else:
        st.warning("Protocol: Rocephin + Gentamycin (Monitor Renal Function!).")

# --- Brucellosis Module ---
elif menu == "Brucellosis":
    st.header("🫘 Brucellosis")
    st.write("Clinical: Fever, Night Sweats, Arthralgia, Hepatosplenomegaly.")
    if stock["Doxy"] and stock["Rifampin"]:
        st.success("Protocol: Doxycycline (100mg BID) + Rifampin (600mg OD) for 6 weeks.")
    else:
        st.warning("Alternative: Doxycycline + Gentamycin (if Rifampin missing).")

# --- Other Modules (Consolidated) ---
elif menu == "Diabetic Foot":
    st.header("🦶 Diabetic Foot / Osteomyelitis")
    status = st.radio("Severity:", ["Stable", "Septic"])
    if status == "Septic":
        st.error("Protocol: Rocephin + Flagyl + Gentamycin (Check renal dose).")
    else:
        st.success("Protocol: Levofloxacin + Flagyl.")

# --- General Stewardship ---
st.sidebar.markdown("---")
st.sidebar.info("💡 **Clinical Tip:** Always perform deep tissue culture before antibiotics in Diabetic Foot.")
