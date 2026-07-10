import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Al-Ahli Emergency Dialysis Predictor (AEIOU)",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for Emergency and Intensive Care Rigor
st.markdown("""
    <style>
    .main-title { font-size:30px !important; font-weight: bold; color: #991B1B; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size:15px !important; color: #4B5563; text-align: center; margin-bottom: 25px; font-style: italic; }
    .branding-bar { background-color: #FEF2F2; padding: 20px; border-radius: 10px; border-left: 6px solid #991B1B; margin-bottom: 25px; }
    .branding-bar strong { color: #991B1B !important; font-weight: bold; }
    .branding-text { color: #1F2937 !important; font-size: 15px !important; line-height: 1.6; }
    .section-header { font-size:20px !important; font-weight: bold; color: #991B1B; margin-top: 15px; margin-bottom: 15px; border-bottom: 2px solid #E5E7EB; padding-bottom: 5px; }
    .status-box { padding: 15px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #E5E7EB; }
    .board-header { font-size:22px !important; font-weight: bold; color: #D97706; margin-top: 30px; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<div class='main-title'>🚨 Al-Ahli Hospital Emergency Dialysis Predictor (AEIOU)</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Advanced Inpatient Decision Support System (CDSS) for Hyperacute Uremic & Metabolic Emergencies</div>", unsafe_allow_html=True)

# Professional Branding Block
st.markdown(f"""
<div class='branding-bar'>
    <div class='branding-text'>
        <strong>Project Founder & Director:</strong> Dr. Ihab Abbass Abu Hilail<br>
        <strong>Department:</strong> Internal Medicine, Al-Ahli Hospital, Palestine<br>
        <strong>Clinical Protocol:</strong> KDIGO Acute Kidney Injury Criteria, AEIOU Hyperacute Dialysis Indications, Continuous Cardio-Renal Risk Stratification
    </div>
</div>
""", unsafe_allow_html=True)

# Layout Split
col_input, col_dashboard = st.columns([1, 1.2])

# ==============================================================================
# LEFT COLUMN: CRITICAL LABS & RECOGNITION TRIGGERS
# ==============================================================================
with col_input:
    st.markdown("<div class='section-header'>📋 1. Acute Metabolic & Vitals Input</div>", unsafe_allow_html=True)
    
    # Blood Gas & Electrolytes
    ph = st.number_input("Arterial pH [Normal: 7.35 - 7.45]:", min_value=6.50, max_value=7.80, value=7.24, step=0.01)
    hco3 = st.number_input("Serum Bicarbonate (HCO3- mEq/L):", min_value=2.0, max_value=40.0, value=14.0, step=1.0)
    potassium = st.number_input("Serum Potassium (K+ mEq/L):", min_value=2.0, max_value=9.0, value=5.8, step=0.1)
    bun = st.number_input("Blood Urea Nitrogen (BUN mg/dL):", min_value=5, max_value=300, value=90, step=5)
    
    # Anion Gap Calculator Inputs
    st.subheader("Anion Gap Panel (Optional)")
    sodium = st.number_input("Serum Sodium (Na+ mEq/L):", min_value=100, max_value=170, value=135, step=1)
    chloride = st.number_input("Serum Chloride (Cl- mEq/L):", min_value=70, max_value=130, value=102, step=1)
    
    st.markdown("<div class='section-header'>🫁 2. Fluid & Clinical Status</div>", unsafe_allow_html=True)
    fluid_overload_refractory = st.checkbox("Refractory Fluid Overload (e.g., Acute Pulmonary Edema unresponsive to high-dose IV Loop Diuretics)", value=False)
    urine_output_24h = st.number_input("Total 24-Hour Urine Output (mL):", min_value=0, max_value=5000, value=300, step=50)
    
    st.markdown("<div class='section-header'>🧠 3. Neurological & Cardiovascular Uremic Signs</div>", unsafe_allow_html=True)
    has_uremic_encephalopathy = st.checkbox("Uremic Encephalopathy (Altered mental status, asterixis, or seizures attributed to uremia)", value=False)
    has_uremic_pericarditis = st.checkbox("Uremic Pericarditis / Pleuritis (Pericardial friction rub, chest pain, or new effusion)", value=False)
    toxic_ingestion = st.checkbox("Toxic Ingestion of Dialyzable Substance (e.g., Methanol, Ethylene Glycol, Lithium, Salicylates)", value=False)

    # Background Logic: Calculate Anion Gap
    anion_gap = sodium - (chloride + hco3)

# ==============================================================================
# RIGHT COLUMN: EMERGENCY DIALYSIS SCOREBOARD & TRIGGER ANALYSIS
# ==============================================================================
with col_dashboard:
    st.markdown("<div class='section-header'>⚡ Hyperacute Dialysis Indication Scoreboard</div>", unsafe_allow_html=True)
    
    # Calculate Severity Index based on flags
    aeiou_triggers = []
    urgency_score = 0
    
    # A - Acidosis
    if ph < 7.15 or hco3 < 10:
        aeiou_triggers.append("🟢 **[A] - Severe Refractory Metabolic Acidosis**")
        urgency_score += 3
    elif ph < 7.30:
        urgency_score += 1
        
    # E - Electrolytes
    if potassium >= 6.5:
        aeiou_triggers.append("🟢 **[E] - Life-threatening Hyperkalemia (K⁺ ≥ 6.5 mEq/L)**")
        urgency_score += 3
    elif potassium >= 5.5:
        urgency_score += 1
        
    # I - Ingestion
    if toxic_ingestion:
        aeiou_triggers.append("🟢 **[I] - Toxic Ingestion of Dialyzable Toxins**")
        urgency_score += 3
        
    # O - Overload
    if fluid_overload_refractory:
        aeiou_triggers.append("🟢 **[O] - Refractory Volume Overload / Pulmonary Edema**")
        urgency_score += 3
    elif urine_output_24h < 400: # Oliguria flag
        urgency_score += 1
        
    # U - Uremia
    if has_uremic_encephalopathy or has_uremic_pericarditis or bun > 100:
        aeiou_triggers.append("🟢 **[U] - Severe Symptomatic Uremia / End-Organ Damage**")
        urgency_score += 3
    elif bun > 60:
        urgency_score += 1

    # Display Urgency Level
    st.markdown("### 🚨 Emergency Status & Action Matrix")
    
    if len(aeiou_triggers) > 0:
        st.error(f"🔴 **CRITICAL ALERT: IMMEDIATE NEPHROLOGY CONSULTATION REQUIRED**")
        st.write(f"**Active Absolute Indications Detected:**")
        for trigger in aeiou_triggers:
            st.markdown(trigger)
            
        if urgency_score >= 6:
            status_color = "#FEF2F2"
            border_color = "#991B1B"
            text_recommend = "❌ **CRITICAL CRITERIA MET:** Prepare patient for immediate emergent Hemodialysis catheter placement (e.g., Shiley line). Stop all potassium-retaining medications and stabilize membranes with IV Calcium Gluconate if ECG changes are present."
        else:
            status_color = "#FFFBEB"
            border_color = "#D97706"
            text_recommend = "⚠️ **URGENT CRITERIA MET:** High risk of immediate deterioration. Notify the Nephrology fellow on-call and consider a trial of continuous renal replacement therapy (CRRT) if the patient is hemodynamically unstable in the ICU."
    else:
        status_color = "#F0FDF4"
        border_color = "#15803D"
        text_recommend = "🟢 **STABLE BOUNDARIES:** No absolute emergency dialysis indications present at this hour. Continue optimal medical management and monitor metabolic panels every 12 hours."
        
    st.markdown(f"""
    <div class='status-box' style='background-color: {status_color}; border: 2px solid {border_color};'>
        <strong>Clinical Action Plan:</strong><br>{text_recommend}
    </div>
    """, unsafe_allow_html=True)

    # TABS FOR METABOLIC BREAKDOWN
    tab_acid, tab_elec, tab_urea = st.tabs(["🧬 Acid-Base & Anion Gap", "🍏 Hyperkalemia Guard", "🩸 Uremic Thresholds"])
    
    with tab_acid:
        st.markdown("### 🧬 Advanced Acid-Base Analytics")
        st.metric("Calculated Serum Anion Gap", f"{anion_gap:.1f} mEq/L", 
                  delta="High Anion Gap (HAGMA)" if anion_gap > 12 else "Normal Anion Gap (NAGMA)",
                  delta_color="inverse" if anion_gap > 12 else "normal")
        st.markdown(f"""
        * **Interpretation:** The current pH is **{ph}**. 
        * {"If the Anion Gap is high (>12), prioritize ruling out accumulation of uremic toxins (sulfates, phosphates) or concomitant lactic acidosis." if anion_gap > 12 else "The Anion Gap is within normal limits. Acidosis may be primarily driven by bicarbonate loss or severe renal tubular dysfunction."}
        """)
        
    with tab_elec:
        st.markdown("### 🍏 Hyperkalemia Membrane Stabilization Protocol")
        st.write(f"📊 **Current Serum Potassium:** `{potassium} mEq/L`")
        if potassium >= 6.0:
            st.markdown("""
            ⚠️ **Hyperkalemia Shift & Stabilization Protocol (Ward Orders):**
            1. **Membrane Stabilization:** Administer **10 mL of 10% Calcium Gluconate IV** over 5-10 minutes if ECG shows tented T-waves or QRS widening (repeat if no improvement in 5 mins).
            2. **Intracellular Shifting:** Infuse **10 units of Regular Insulin** in **50 mL of Dextrose 50% (D50W)** over 15-30 minutes.
            3. **Elimination:** Initiate **Salbutamol (Albuterol) Nebulization** 10-20 mg, and consider oral potassium binders if hemodialysis is delayed.
            """)
        else:
            st.write("🟢 Potassium is currently under emergency thresholds; monitor closely to prevent sudden spikes.")

    with tab_urea:
        st.markdown("### 🩸 Uremic Toxin Accumulation Analysis")
        st.write(f"📊 **Current BUN:** `{bun} mg/dL` (Estimated Serum Urea: `~{bun * 2.14:.1f} mg/dL`) ")
        if bun > 100:
            st.markdown("""
            ⚠️ **Uremic Threat Detected:** Extreme accumulation of nitrogenous waste.
            * Monitor closely for **Uremic Serositis** (pericardial/pleural friction rubs).
            * Assess neurological status hourly for signs of **Uremic Flap (Asterixis)** or progressive lethargy, which represent definitive signs to initiate dialysis immediately regardless of absolute lab values.
            """)
        else:
            st.write("🟢 Nitrogenous waste is elevated but below immediate absolute organ-threat thresholds.")

# ==============================================================================
# HIGH-YIELD BOARD EXAM REVIEW MATERIAL (Created for the Scientific Club)
# ==============================================================================
st.markdown("---")
st.markdown("<div class='board-header'>🎓 High-Yield Board-Level Review (Emergency Dialysis Physiology)</div>", unsafe_allow_html=True)

with st.expander("❓ Click to Reveal the Board Question & Scientific Rationale"):
    st.markdown("""
    **Clinical Scenario:** A 68-year-old female with an acute-on-chronic kidney injury secondary to severe sepsis is admitted to the medical ward. Over the past 24 hours, her urine output is a total of **150 mL** despite aggressive fluid resuscitation and a high-dose trial of intravenous Furosemide. Her vital signs show Blood Pressure **155/92 mmHg**, Heart Rate **98 bpm**, and Oxygen Saturation **88% on room air** with prominent bilateral pulmonary crackles on auscultation. Labs reveal: pH **7.22**, HCO3⁻ **12 mEq/L**, Potassium **6.2 mEq/L**, and BUN **84 mg/dL**. 
    
    **Which clinical finding represents the most absolute and immediate indication for urgent hemodialysis initiation according to the AEIOU framework?**
    
    * **A)** A serum potassium level of 6.2 mEq/L.
    * **B)** Severe oliguria with a total 24-hour urine output of 150 mL.
    * **C)** Refractory volume overload presenting as acute pulmonary edema with hypoxemia.
    * **D)** An arterial pH of 7.22 accompanied by metabolic acidosis.
    
    ---
    
    ### 📝 Comprehensive Scientific Evidence-Based Explanation:
    * **The Correct Answer is C.** While all options reflect severe metabolic and renal distress, **Refractory Volume Overload (the "O" in AEIOU)** causing acute pulmonary edema and respiratory compromise is an **absolute, life-threatening emergency** that requires immediate mechanical removal of fluid via hemodialysis.
    * **Why the other options are not the primary choice:**
      * **A & D:** Hyperkalemia ($K^+ = 6.2$) and Acidosis ($pH = 7.22$) are severe, but they can initially be managed or buying time with aggressive medical shifting therapies (IV Insulin/Dextrose, Calcium Gluconate, Sodium Bicarbonate infusions) if no ECG changes are present. Dialysis becomes mandatory if these values cross extreme thresholds ($K^+ \ge 6.5$ or $pH < 7.1$) or fail medical therapy.
      * **B:** Oliguria is a diagnostic component of AKI ($KDIGO$ Stage 3), but in isolation without systemic complications, it is not an absolute indication for immediate emergency dialysis line placement.
    * **Clinical Pearl for Residents:** Always treat the patient's physiological threat first. Refractory hypoxia due to fluid retention cannot wait for medical optimization; it is a direct trigger for emergent ultrafiltration.
    """)

# Footer Signature
st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF; font-size: 11px;'>Al-Ahli Hospital Internal Medicine CDSS Platforms © 2026 • Curated by Dr. Ihab Abbass Abu Hilail</div>", unsafe_allow_html=True)
