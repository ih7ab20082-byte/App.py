import streamlit as st
from fpdf import FPDF
import io

# --- الإعدادات العامة ---
st.set_page_config(page_title="Al-Ahli ID Master Engine", layout="wide")
st.title("🛡️ Al-Ahli Clinical Intelligence System")

# --- دالة حساب التصفية الكلوية (CrCl) ---
def calculate_crcl(age, weight, creatinine, gender):
    crcl = ((140 - age) * weight) / (72 * creatinine)
    if gender == "Female": crcl *= 0.85
    return round(crcl, 2)

# --- دالة تصدير الـ PDF ---
def generate_report(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, "Al-Ahli Hospital - Clinical Report", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    for key, val in data.items():
        pdf.cell(200, 10, f"{key}: {str(val)}", ln=True)
    return pdf.output(dest='S').encode('latin-1')

# --- اللوحة الجانبية (المخزون + الكلى) ---
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
    gender = st.radio("Gender:", ["Male", "Female"])
    crcl = calculate_crcl(age, weight, creat, gender)
    st.write(f"### Current CrCl: {crcl} mL/min")

# --- الموديولات الرئيسية ---
tabs = st.tabs(["CNS", "Respiratory", "Abdominal/UTI", "Diabetic Foot", "Endo/Brucella"])

# 1. CNS
with tabs[0]:
    st.header("🧠 Meningitis/Encephalitis")
    if st.checkbox("Bacterial Meningitis?"):
        rx = "Vanco + Rocephin + Dex" if inv["Vanco"] else "Rocephin + Dex"
        st.success(f"Protocol: {rx}")
        if crcl < 50: st.warning("Adjust Vanco/Rocephin dose per CrCl!")

# 2. Respiratory
with tabs[1]:
    st.header("🫁 HAP/CAP")
    status = st.radio("Status:", ["Stable", "Septic"])
    rx = "Rocephin + Levofloxacin" if status == "Stable" else ("Meropenem" if inv["Mero"] else "Rocephin + Levofloxacin + Gent")
    st.success(f"Protocol: {rx}")

# 3. Abdominal/UTI
with tabs[2]:
    st.header("腹 Abdominal/UTI")
    rx = "Meropenem" if inv["Mero"] else "Rocephin + Flagyl"
    st.success(f"Protocol: {rx}")

# 4. Diabetic Foot
with tabs[3]:
    st.header("🦶 Diabetic Foot & Osteo")
    st.write("Target: Deep tissue culture. Stop superficial swabs.")
    rx = "Levofloxacin + Flagyl"
    st.success(f"Protocol: {rx}")

# 5. Endo/Brucella
with tabs[4]:
    st.header("❤️ Endo / Brucella")
    cond = st.selectbox("Disease:", ["Infective Endocarditis", "Brucellosis"])
    if cond == "Infective Endocarditis":
        rx = "Vanco + Rocephin" if inv["Vanco"] else "Rocephin + Gentamycin"
    else:
        rx = "Doxy + Rifampin" if inv["Doxy_Rif"] else "Doxy + Gentamycin"
    st.success(f"Protocol: {rx}")

# --- التصدير ---
st.markdown("---")
if st.button("Generate Final PDF Report"):
    report_data = {"Diagnosis": "Infectious Case", "CrCl": crcl, "Plan": "Verified Protocol"}
    st.download_button("Download Report", generate_report(report_data), "Clinical_Report.pdf", "application/pdf")
