import streamlit as st

def advanced_sepsis_engine():
    st.header("🛡️ Sepsis Management: Al-Ahli Protocol")
    
    # 1. التقييم السريري الدقيق
    with st.expander("📊 Step 1: Clinical Assessment", expanded=True):
        lactate = st.number_input("Lactate (mmol/L):", 0.0, 20.0, 1.5)
        map_val = st.number_input("MAP (mmHg):", 20, 120, 70)
        comorbidities = st.multiselect("Active Comorbidities:", ["CKD", "DM", "Immunocompromised"])
        
    # 2. خطة العمل الموجهة
    st.subheader("📋 Step 2: 1-Hour Bundle Actions")
    action_1 = st.checkbox("Blood Cultures collected?")
    action_2 = st.checkbox("Broad-spectrum Antibiotics started (Meropenem)?")
    action_3 = st.checkbox("Fluid Resuscitation initiated (30ml/kg)?")
    
    # 3. محرك التحليل والتوثيق
    if action_1 and action_2 and action_3:
        st.success("✅ 1-Hour Bundle Completed successfully.")
        if st.button("Generate Official Sepsis Note"):
            note = f"Sepsis Protocol Followed. MAP: {map_val}, Lactate: {lactate}. Actions: Bundle complete."
            st.code(note)
    else:
        st.warning("⚠️ Pending Actions: Please complete the 1-Hour Bundle requirements.")

# advanced_sepsis_engine()
