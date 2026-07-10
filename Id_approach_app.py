import streamlit as st

# إعداد واجهة التطبيق
st.set_page_config(page_title="Al-Ahli Clinical Expert", layout="wide")

def advanced_sepsis_engine():
    st.header("🛡️ Sepsis Management: Al-Ahli Protocol")
    st.markdown("---")
    
    # 1. التقييم السريري الدقيق
    with st.expander("📊 Step 1: Clinical Assessment", expanded=True):
        lactate = st.number_input("Serum Lactate (mmol/L):", 0.0, 20.0, 1.5)
        map_val = st.number_input("Mean Arterial Pressure (MAP - mmHg):", 20, 120, 70)
        comorbidities = st.multiselect("Active Comorbidities:", ["CKD", "DM", "Immunocompromised"])
        
    # 2. خطة العمل الموجهة
    st.subheader("📋 Step 2: 1-Hour Bundle Actions")
    action_1 = st.checkbox("Blood Cultures collected (Before Antibiotics)?")
    action_2 = st.checkbox("Broad-spectrum Antibiotics started (Meropenem)?")
    action_3 = st.checkbox("Fluid Resuscitation initiated (30ml/kg Crystalloids)?")
    
    # 3. محرك التحليل والتوثيق
    if action_1 and action_2 and action_3:
        st.success("✅ 1-Hour Bundle Completed successfully.")
        
        if st.button("Generate Official Sepsis Note"):
            note = f"""
            ---
            **Sepsis Clinical Note (Al-Ahli System)**
            - Lactate: {lactate} mmol/L
            - MAP: {map_val} mmHg
            - Protocol Status: 1-Hour Bundle Completed.
            - Plan: Continue monitoring and reassess in 6 hours.
            ---
            """
            st.code(note, language="markdown")
    else:
        st.warning("⚠️ Pending Actions: Please complete the 1-Hour Bundle requirements.")

# هذا السطر هو مفتاح تشغيل الكود، لا تنسه أبداً
if __name__ == "__main__":
    advanced_sepsis_engine()
