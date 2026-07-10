import streamlit as st

# الإعدادات
st.set_page_config(page_title="Al-Ahli ID Engine", layout="wide")
st.title("🛡️ Al-Ahli Clinical Intelligence System")

# -- المخزون --
with st.sidebar:
    st.header("📦 Inventory Checklist")
    inv = {
        "Vanco": st.checkbox("Vancomycin"),
        "Mero": st.checkbox("Meropenem"),
        "Rocephin_Flagyl": st.checkbox("Rocephin + Flagyl", True),
        "Levoflox": st.checkbox("Levofloxacin", True),
        "Doxy_Rif": st.checkbox("Doxy + Rifampin", True)
    }
    st.markdown("---")
    st.header("🧮 Renal Function")
    age = st.number_input("Age:", 1, 100, 50)
    weight = st.number_input("Weight (kg):", 30, 150, 70)
    creat = st.number_input("S. Creatinine:", 0.1, 10.0, 1.0)
    crcl = ((140 - age) * weight) / (72 * creat)
    st.write(f"**CrCl:** {round(crcl, 2)} mL/min")

# -- الموديولات --
tabs = st.tabs(["CNS", "Respiratory", "Abdominal/UTI", "Diabetic Foot", "Endo/Brucella"])

with tabs[0]:
    st.header("🧠 Meningitis")
    rx = "Vanco + Rocephin + Dex" if inv["Vanco"] else "Rocephin + Dex"
    st.success(f"Protocol: {rx}")
    if crcl < 50: st.warning("Adjust doses per CrCl!")

with tabs[1]:
    st.header("🫁 HAP/CAP")
    status = st.radio("Status:", ["Stable", "Septic"])
    rx = "Rocephin + Levofloxacin" if status == "Stable" else ("Meropenem" if inv["Mero"] else "Rocephin + Levofloxacin + Gent")
    st.success(f"Protocol: {rx}")

with tabs[2]:
    st.header("腹 Abdominal/UTI")
    rx = "Meropenem" if inv["Mero"] else "Rocephin + Flagyl"
    st.success(f"Protocol: {rx}")

with tabs[3]:
    st.header("🦶 Diabetic Foot")
    st.write("Target: Deep tissue culture.")
    rx = "Levofloxacin + Flagyl"
    st.success(f"Protocol: {rx}")

with tabs[4]:
    st.header("❤️ Endo / Brucella")
    cond = st.selectbox("Disease:", ["Endocarditis", "Brucellosis"])
    if cond == "Endocarditis":
        rx = "Vanco + Rocephin" if inv["Vanco"] else "Rocephin + Gentamycin"
    else:
        rx = "Doxy + Rifampin" if inv["Doxy_Rif"] else "Doxy + Gentamycin"
    st.success(f"Protocol: {rx}")
