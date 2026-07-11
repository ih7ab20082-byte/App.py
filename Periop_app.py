import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Al-Ahli Perioperative Fitness Engine",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Enhanced CSS for Professional Clinical Interface
st.markdown("""
    <style>
    .main-title { font-size:30px !important; font-weight: bold; color: #0F766E; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:15px !important; color: #4B5563; text-align: center; margin-bottom: 25px; font-style: italic; }
    .branding-bar { background-color: #F0FDFA; padding: 18px; border-radius: 12px; border-left: 6px solid #0F766E; margin-bottom: 25px; }
    .section-header { font-size:20px !important; font-weight: bold; color: #0F766E; margin-top: 15px; margin-bottom: 15px; border-bottom: 2px solid #E5E7EB; padding-bottom: 5px; }
    .status-box { padding: 15px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #E5E7EB; background-color: #F9FAFB; line-height: 1.6; color: #1F2937; }
    .danger-box { padding: 15px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #DC2626; background-color: #FEF2F2; color: #991B1B; line-height: 1.6; }
    .info-box { padding: 15px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #2563EB; background-color: #EFF6FF; color: #1E40AF; line-height: 1.6; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<div class='main-title'>🏥 Al-Ahli Hospital Comprehensive Perioperative Medical Fitness Engine</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Advanced Decision-Support Matrix for Surgical Clearance & Multi-System Comorbidity Optimization</div>", unsafe_allow_html=True)

# Professional Branding Block
st.markdown(f"""
<div class='branding-bar'>
    <div style='color: #1F2937; font-size: 15px; line-height: 1.6;'>
        <strong>Project Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Core Standards:</strong> Revised Cardiac Risk Index (RCRI), ARISCAT Pulmonary Risk, ASA Status, Perioperative Antithrombotic Guidelines
    </div>
</div>
""", unsafe_allow_html=True)

# Main Application Tabs
tabs = st.tabs([
    "🎯 Surgical Risk & ASA", 
    "🫀 Cardiovascular Risk (RCRI)", 
    "🫁 Pulmonary Assessment (ARISCAT)", 
    "🧬 Comorbidities: What to do (الامراض المزمنة)", 
    "💊 Perioperative Medication Stewardship"
])

# ==============================================================================
# TAB 1: SURGICAL TYPE, DURATION, AND ASA CLASSIFICATION
# ==============================================================================
with tabs[0]:
    st.markdown("<div class='section-header'>🎯 Surgical Risk Stratification & ASA Global Scoring</div>", unsafe_allow_html=True)
    col_s1, col_s2 = st.columns(2)
    
    with col_s1:
        op_type = st.selectbox("Type of Scheduled Surgery / Inherent Risk:", [
            "Low Risk (Cataract, Superficial Surgery, Endoscopy)",
            "Intermediate Risk (Orthopedic, Cholecystectomy, Prostatectomy, Uncomplicated Hernia)",
            "High Risk (Major Vascular, Aortic Surgery, Thoracoabdominal, Total Cystectomy)"
        ])
        op_duration = st.number_input("Expected Duration of Surgery (in Hours):", min_value=0.5, max_value=12.0, value=2.0, step=0.5)
        
        # New Addition: ASA Score Dropdown
        asa_class = st.selectbox("Assign ASA Physical Status Classification:", [
            "ASA I: A normal healthy patient",
            "ASA II: A patient with mild systemic disease (e.g., well-controlled HTN/DM)",
            "ASA III: A patient with severe systemic disease (e.g., CKD on dialysis, stable CAD)",
            "ASA IV: A patient with severe systemic disease that is a constant threat to life"
        ])
    
    with col_s2:
        st.markdown("### 📋 Mandated Lab & Investigation Directives")
        if "Low Risk" in op_type:
            st.markdown("<div class='status-box'>🟢 **Routine Labs Not Indicated:** Asymptomatic patients undergoing low-risk surgeries do NOT require screening labs, CXR, or ECG. Order strictly based on specific comorbidities only.</div>", unsafe_allow_html=True)
        else:
            directives = """
            * **ECG:** Mandated for all intermediate/high-risk surgeries if patient has any cardiovascular risk factors or age > 65.
            * **CBC & Kidney Function (Creatinine/Electrolytes):** Required due to expected fluid shifts or blood loss.
            * **PT/PTT/INR:** Only if history of bleeding diathesis, liver disease, or chronic anticoagulation.
            """
            st.markdown(f"<div class='info-box'>{directives}</div>", unsafe_allow_html=True)
            
        if "ASA III" in asa_class or "ASA IV" in asa_class:
            st.markdown("<div class='danger-box'>⚠️ **HIGH ASA TIER WARNING:** Patient has advanced systemic disease. High-yield anesthetic risks predicted. Ensure ICU/HDU bed availability is checked prior to incision.</div>", unsafe_allow_html=True)
            
        if op_duration > 3.0:
            st.markdown("<div class='danger-box'>⚠️ **PROLONGED SURGICAL DURATION (>3 Hours):** Independent risk factor for postoperative deep vein thrombosis (DVT) and pulmonary complications. Ensure strict mechanical/chemical prophylaxis protocols are charted.</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 2: CARDIOVASCULAR RISK (RCRI) & FUNCTIONAL CAPACITY
# ==============================================================================
with tabs[1]:
    st.markdown("<div class='section-header'>🫀 Cardiovascular Stratification (Revised Cardiac Risk Index - RCRI)</div>", unsafe_allow_html=True)
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.subheader("RCRI Risk Factors")
        rcri_1 = st.checkbox("High-risk surgery (Intrathoracic, intra-abdominal, or suprainguinal vascular)")
        rcri_2 = st.checkbox("History of Ischemic Heart Disease (IHD / CAD / Prior MI or Positive Stress Test)")
        rcri_3 = st.checkbox("History of Congestive Heart Failure (CHF / Pulmonary Edema / EF < 40%)")
        rcri_4 = st.checkbox("History of Cerebrovascular Disease (Stroke or TIA)")
        rcri_5 = st.checkbox("Preoperative Insulin therapy for Diabetes Mellitus")
        rcri_6 = st.checkbox("Preoperative Serum Creatinine > 2.0 mg/dL (177 µmol/L)")
        
    with col_c2:
        st.subheader("🏃 Functional Capacity Assessment (METs)")
        mets_capacity = st.radio("Can the patient perform activities equivalent to >= 4 METs? (e.g., climb 2 flights of stairs carrying groceries, walk up a hill without stopping)", ["Yes (≥ 4 METs)", "No (< 4 METs)"])

    # Score Calculation
    rcri_score = sum([rcri_1, rcri_2, rcri_3, rcri_4, rcri_5, rcri_6])
    risk_mapping = {0: "0.4% (Low Risk)", 1: "1.0% (Moderate Risk)", 2: "2.4% (High Risk)", 3: "5.4% or greater (Critical Risk)"}
    estimated_risk = risk_mapping.get(rcri_score, "5.4% or greater (Critical Risk)")
    
    st.markdown(f"### Total RCRI Criteria Met: `{rcri_score} Points`")
    st.markdown(f"<div class='status-box'>📊 **Estimated Risk of Major Adverse Cardiac Events (MACE):** <strong>{estimated_risk}</strong> during the perioperative period.</div>", unsafe_allow_html=True)
    
    # Decision Pathway Matrix
    if rcri_score >= 1 and mets_capacity == "No (< 4 METs)":
        st.markdown("<div class='danger-box'>🚨 **ACC/AHA DECISION TRIGGER:** Elevated cardiac risk with poor functional capacity ($<4$ METs). If surgery is non-urgent, hold clearance and request a cardiology consultation for an **Echocardiogram** or **Pharmacological Stress Test**.</div>", unsafe_allow_html=True)
    else:
        st.success("🟢 **Cardiac Clearance Status:** Safe to proceed from a cardiac standpoint without advanced non-invasive testing. Optimize home cardiac medications.")

# ==============================================================================
# TAB 3: PULMONARY ASSESSMENT (ARISCAT)
# ==============================================================================
with tabs[2]:
    st.markdown("<div class='section-header'>🫁 Postoperative Pulmonary Complications (PPC) Risk Index</div>", unsafe_allow_html=True)
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        p_age = st.number_input("Patient Age:", min_value=18, max_value=100, value=55)
        p_spo2 = st.selectbox("Preoperative SpO2 (on Room Air):", [
            "≥ 96% (0 pts)",
            "91 - 95% (8 pts)",
            "≤ 90% (24 pts)"
        ])
        p_resp = st.checkbox("Active Respiratory Infection in the past 4 weeks? (17 pts)")
        p_anemia = st.checkbox("Preoperative Anemia (Hemoglobin ≤ 10 g/dL)? (11 pts)")
        
    with col_p2:
        p_site = st.selectbox("Surgical Incision Site:", [
            "Peripheral (0 pts)",
            "Upper Abdominal (15 pts)",
            "Intrathoracic (24 pts)"
        ])
        p_time = st.checkbox("Expected Surgical Duration > 3 hours? (16 pts)")
        p_emerg = st.checkbox("Is this an Emergency Surgery? (8 pts)")

    # Score Tabulation
    p_score = 0
    if 51 <= p_age <= 80: p_score += 3
    elif p_age > 80: p_score += 11
    
    p_score += {"≥ 96% (0 pts)": 0, "91 - 95% (8 pts)": 8, "≤ 90% (24 pts)": 24}[p_spo2]
    p_score += 17 if p_resp else 0
    p_score += 11 if p_anemia else 0
    p_score += {"Peripheral (0 pts)": 0, "Upper Abdominal (15 pts)": 15, "Intrathoracic (24 pts)": 24}[p_site]
    p_score += 16 if p_time else 0
    p_score += 8 if p_emerg else 0
    
    st.markdown(f"### Calculated ARISCAT Score: `{p_score} Points`")
    if p_score >= 45:
        st.markdown(f"<div class='danger-box'>🔴 **HIGH PULMONARY RISK (Score {p_score} ≥ 45):** Predicts a >40% chance of severe postoperative complications (Atelectasis, Pneumonia, Respiratory Failure).<br>**Mandated Strategy:** Initiate intensive incentive spirometry pre-op, schedule post-op bronchodilator nebulizers, and optimize smoking cessation immediately.</div>", unsafe_allow_html=True)
    elif 26 <= p_score <= 44:
        st.markdown(f"<div class='status-box' style='border-left: 5px solid #D97706;'>🟡 **MODERATE PULMONARY RISK (Score {p_score}):** Moderate probability of PPC. Avoid fluid overload and encourage early post-op mobilization.</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='status-box' style='border-left: 5px solid #16A34A;'>🟢 **LOW PULMONARY RISK:** Standard post-operative care.</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 4: COMORBIDITIES - WHAT TO DO (الامراض المزمنة وشو الها وعليها)
# ==============================================================================
with tabs[3]:
    st.markdown("<div class='section-header'>🧬 Comorbidities Profile: Optimization and What to Do (شو الها وعليها)</div>", unsafe_allow_html=True)
    st.write("إرشادات تفصيلية للتعامل مع المشاكل الصحية المزمنة الأكثر شيوعاً في الأجنحة وكيفية تجهيزها الطبي:")
    
    selected_comorb = st.multiselect("Select Patient's Active Comorbidities:", [
        "Diabetes Mellitus (السكري)",
        "Hypertension (ارتفاع ضغط الدم)",
        "Chronic Kidney Disease (الفشل الكلوي المزمن)",
        "COPD / Asthma (الربو والأمراض الرئوية المزمنة)",
        "Ischemic Heart Disease / Heart Failure (أمراض القلب وقصور العضلة)",
        "Chronic Steroid Use (المريض بياخذ كورتيزون بالبيت)"
    ])
    
    if "Diabetes Mellitus (السكري)" in selected_comorb:
        st.markdown("""
        <div class='info-box'>
            <strong>🍬 Diabetes Mellitus Protocol:</strong><br>
            * **الهدف السريري:** الحفاظ على مستوى السكر بين 100-180 mg/dL أثناء الجراحة.
            * **الـ HbA1c المثالي:** يفضل أن يكون < 8% قبل العمليات غير الطارئة.
            * **ماذا تفعل بالأدوية؟** انظر تبويب إدارة الأدوية المرفق بالقسم التالي لتعديل الإنسولين والمحاذير.
        </div>
        """, unsafe_allow_html=True)
        
    if "Hypertension (ارتفاع ضغط الدم)" in selected_comorb:
        st.markdown("""
        <div class='info-box'>
            <strong>🩸 Hypertension Protocol:</strong><br>
            * **حد الأمان:** لا تؤجل العملية إلا إذا كان الضغط شديد الارتفاع (Systolic ≥ 180 mmHg أو Diastolic ≥ 110 mmHg).
            * **حماية التخدير:** الارتفاع البسيط لا يبرر تأجيل الجراحة، ولكن الهبوط أثناء التخدير خطر. يجب إيقاف الـ ACEIs/ARBs صباح العملية.
        </div>
        """, unsafe_allow_html=True)
        
    if "Chronic Kidney Disease (الفشل الكلوي المزمن)" in selected_comorb:
        st.markdown("""
        <div class='info-box'>
            <strong>🧪 Chronic Kidney Disease (CKD) Protocol:</strong><br>
            * **مرضى غسيل الكلى (Dialysis):** يجب جدولة جلسة الغسيل الكلوي **قبل العملية بـ 12-24 ساعة** لتجنب اضطراب السوائل، والتأكد من فحص البوتاسيوم ($K$) قبل الدخول لغرفة العمليات مباشرة (يجب أن يكون < 5.5 mEq/L).
            * **الأدوية خطرة الإفراز:** تجنب الـ NSAIDs تماماً للسيطرة على الألم بعد العملية لمنع التدهور الحاد للاستجابة الكلوية.
        </div>
        """, unsafe_allow_html=True)

    if "COPD / Asthma (الربو والأمراض الرئوية المزمنة)" in selected_comorb:
        st.markdown("""
        <div class='info-box'>
            <strong>🌬️ COPD / Asthma Optimization:</strong><br>
            * **الوضعية المثالية:** يجب ألا يكون المريض يعاني من ويزينغ ($Wheezing$) حاد أو هجمة قريبة.
            * **الإجراء:** إذا كان المريض يستخدم البخاخات، يستمر عليها حتى صباح العملية. يمكن إضافة كورس قصير من الستيرويد الفموي (Prednisone 40mg) لمدة 3-5 أيام قبل العملية إذا كان هناك ضيق تنفس غير مستقر.
        </div>
        """, unsafe_allow_html=True)

    if "Ischemic Heart Disease / Heart Failure (أمراض القلب وقصور العضلة)" in selected_comorb:
        st.markdown("""
        <div class='info-box'>
            <strong>🫀 Cardiopulmonary Disease Optimization:</strong><br>
            * **الجلطة الحديثة:** يمنع دخول العمليات الاختيارية تماماً إذا كان المريض قد عانى من جلطة قلبية حديثة ($Myocardial\ Infarction$) خلال **الـ 6 أشهر الماضية** (إلا في الحالات الطارئة جداً للإنقاذ).
            * **قصور العضلة:** تأكد من أن المريض في حالة (Euvolemic) ولا يعاني من احتقان سوائل بالرئتين أو تورم شديد بالأقدام قبل التخدير.
        </div>
        """, unsafe_allow_html=True)

    # New Addition: Chronic Steroid Comorbidity Guidance
    if "Chronic Steroid Use (المريض بياخذ كورتيزون بالبيت)" in selected_comorb:
        st.markdown("""
        <div class='danger-box' style='background-color: #FFFBEB; border-color: #D97706; color: #92400E;'>
            <strong>💊 Hydrocortisone Stress Dosing Protocol (حماية الغدة الكظرية):</strong><br>
            إذا كان المريض يأخذ ≥ 5mg Prednisone لمدة تزيد عن 3 أسابيع، يجب حمايته من هبوط الضغط الحاد أثناء العملية الحاصل بسبب خمول الغدة (Adrenal Insufficiency):<br>
            * **العمليات الصغرى (Minor Surgery):** خذ الجرعة الصباحية المعتادة فماً، ولا داعي لجرعات وريدية إضافية.
            * **العمليات المتوسطة (Moderate e.g., Cholecystectomy):** إعطاء **50 mg Hydrocortisone IV** قبل الشق الجراحي مباشرة، ثم 25 mg كل 8 ساعات لمدة 24 ساعة.
            * **العمليات الكبرى (Major e.g., Whipple, Vascular):** إعطاء **100 mg Hydrocortisone IV** قبل الشق الجراحي، ثم 50 mg كل 8 ساعات لمدة 24-48 ساعة، ثم العودة للجرعة المعتادة فماً.
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# TAB 5: PERIOPERATIVE MEDICATION STEWARDSHIP
# ==============================================================================
with tabs[4]:
    st.markdown("<div class='section-header'>💊 Perioperative Medication Stewardship (إدارة الأدوية الحرجة)</div>", unsafe_allow_html=True)
    
    med_cat = st.radio("Select Medication Class to Review Hold/Resume Guidelines:", [
        "Oral Antiplatelets & Anticoagulants (مسيلات الدم والوارفارين والـ DOACs)",
        "Diabetes Medications (أدوية السكري والإنسولين)",
        "Antihypertensives & Cardiovascular Drugs (أدوية الضغط والقلب)"
    ])
    
    if "Anticoagulants" in med_cat:
        st.markdown("""
        <div class='status-box'>
            <strong>🩸 Antithrombotic Management Matrix:</strong><br>
            1. **Aspirin (81mg):** يُستكمل عادةً في مرضى تركيب الشبكات القلبية الدعامية ($Coronary\ Stents$)، ويُوقف فقط إذا كانت الجراحة في مكان مغلق شديد الخطورة كالعمود الفقري أو الدماغ.
            2. **Clopidogrel (Plavix):** يُوقف قبل العملية بـ **5 أيام كاملة**.
            3. **Warfarin:** يُوقف قبل العملية بـ **5 أيام**، ونبدأ بالـ (Heparin Bridging) فقط إذا كان المريض عالي الخطورة (صمام قلب ميكانيكي قديم، أو جلطة وريدية حديثة جداً < 3 أشهر).
            4. **DOACs (Apixaban / Rivaroxaban):** تُوقف قبل **24-48 ساعة** بناءً على خطورة النزيف في العملية وحالة وظائف الكلى للمريض ($GFR$)، ولا تحتاج إلى Heparin bridging كقاعدة عامة.
        </div>
        """, unsafe_allow_html=True)
        
    elif "Diabetes" in med_cat:
        st.markdown("""
        <div class='status-box'>
            <strong>🍬 Diabetes Medication Adjustments:</strong><br>
            1. **Metformin:** يُوقف قبل العملية بـ **24 ساعة** لتجنب خطر الحماض اللبني ($Lactic\ Acidosis$).
            2. **SGLT2 Inhibitors (Empagliflozin / Dapagliflozin):** تُوقف قبل العملية بـ **3-4 أيام** نظراً لخطر حدوث حماض كيتوني سكري طبيعي السكر ($Euglycemic\ DKA$).
            3. **Long-Acting Insulin (Glargine/Lantus):** يتم تقليل الجرعة في ليلة العملية أو صباح يوم العملية إلى **75-80% فقط من الجرعة المعتادة** (تجنب الإيقاف التام لمنع الـ DKA).
            4. **Short-Acting Insulin:** يُوقف تماماً أثناء صيام المريض (NPO)، ويتم الانتقال إلى نظام (Sliding Scale) كل 6 ساعات لمتابعة السكر بالمستشفى.
        </div>
        """, unsafe_allow_html=True)
        
    elif "Antihypertensives" in med_cat:
        st.markdown("""
        <div class='status-box'>
            <strong>💊 Cardiovascular Medication Rules:</strong><br>
            1. **ACE Inhibitors / ARBs (Enalapril, Valsartan, etc.):** **تُوقف صباح يوم العملية** (Hold on day of surgery) لحماية المريض من الهبوط الحاد في الضغط المقاوم للأدوية أثناء التخدير العام ($Refractory\ Hypotension$).
            2. **Beta-Blockers & Calcium Channel Blockers:** **تُستكمل حتماً وبشكل صارم** يوم العملية مع رشفة ماء صغيرة؛ إيقاف البيتا بلوكر المفاجئ يسبب تسارع قلب ارتدادي وجلطات قلبية حادة ($Rebound\ Tachycardia\ &\ MI$).
            3. **Diuretics (Furosemide / Lasix):** تُوقف صباح يوم العملية لتجنب الجفاف الشديد واضطراب الشوارد أثناء العملية.
        </div>
        """, unsafe_allow_html=True)

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 11px;'>Al-Ahli Hospital Internal Medicine CDSS Platforms © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
