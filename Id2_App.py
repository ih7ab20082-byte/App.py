import streamlit as st

st.set_page_config(page_title="Al-Ahli Diagnostic Engine", layout="wide")
st.title("🩺 Al-Ahli Clinical Diagnostic Engine")

# 1. إدخال المعطيات السريرية (Diagnostic Input)
with st.sidebar:
    st.header("Patient Presentation")
    temp = st.number_input("Temperature (°C):", 36.0, 42.0, 37.0)
    wbc = st.number_input("WBC Count (x10^9/L):", 0.0, 50.0, 8.0)
    crp = st.number_input("CRP (mg/L):", 0, 300, 10)
    focus = st.selectbox("Suspected Focus:", ["CNS", "Resp", "Abdominal", "Skin/Bone", "Blood"])

# 2. منطق التشخيص التفاعلي (Diagnostic Logic)
st.subheader("💡 Diagnostic Probability & Management")

if focus == "CNS":
    st.write("### Clinical Station: CNS")
    signs = st.multiselect("Positive Findings:", ["Neck Stiffness", "Altered Mental Status", "Photophobia", "Focal Deficit"])
    lp = st.radio("LP Result:", ["Not Done", "Bacterial Profile", "Viral Profile"])
    
    if "Neck Stiffness" in signs and lp == "Bacterial Profile":
        st.error("Diagnosis: Bacterial Meningitis. Action: Immediate Empirical Vanco + Rocephin.")
    elif "Altered Mental Status" in signs:
        st.warning("Diagnosis: Consider Encephalitis. Action: Acyclovir + Steroids.")

elif focus == "Abdominal":
    st.write("### Clinical Station: Abdominal & UTI")
    abd_pain = st.checkbox("Localized Peritonitis")
    dysuria = st.checkbox("Dysuria/Suprapubic pain")
    if abd_pain:
        st.error("Diagnosis: Suspected Intra-abdominal Infection (Peritonitis). Action: Meropenem or Rocephin/Flagyl.")
    elif dysuria:
        st.success("Diagnosis: UTI. Check Pyuria. Action: Urine Culture then treat.")

elif focus == "Skin/Bone":
    st.write("### Clinical Station: Diabetic Foot/Bone")
    probe = st.checkbox("Probe-to-bone positive?")
    if probe:
        st.error("Diagnosis: High probability of Osteomyelitis. Action: MRI + Tissue Biopsy.")
    else:
        st.info("Diagnosis: Superficial Skin Infection. Action: Cover Staph/Strep.")
