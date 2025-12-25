import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Thal-Analyst AI", page_icon="🔬")

# 2. Visit Counter (Top of Page)
st.markdown("![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fthelesemiatratindentifier.streamlit.app&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=Total+Visits&edge_flat=false)")

# 3. Heading & Language Selection
st.title("🔬 AI Hematology Diagnostic Tool")
st.markdown("### Specialized for Beta Thalassemia Trait (BTT) Screening")
lang = st.radio("Select Language / زبان منتخب کریں", ("English", "Urdu"))

# 4. Input Form
with st.form("medical_form"):
    st.markdown("##### Enter Values from Report:")
    col1, col2 = st.columns(2)
    with col1:
        hb = st.number_input("Hemoglobin / ہیموگلوبن (g/dL)", value=12.8, help="Target for Army: >12.0")
        rbc = st.number_input("RBC Count / ریڈ سیل کاؤنٹ (10^6/uL)", value=6.02)
    with col2:
        mcv = st.number_input("MCV (fL)", value=69.9)
        hba2 = st.number_input("HbA2 % (Electrophoresis)", value=5.0)
    
    submitted = st.form_submit_button("Analyze / تجزیہ کریں")

# 5. Analysis Logic
if submitted:
    mentzer = mcv / rbc
    st.divider()
    
    # Check for Dangerously High HB
    if hb > 18.5:
        st.error("⚠️ CRITICAL: Hemoglobin is dangerously HIGH. Please consult a doctor immediately." if lang=="English" else "⚠️ انتہائی اہم: ہیموگلوبن بہت زیادہ ہے۔ فوری ڈاکٹر سے رجوع کریں۔")
    
    # Check for BTT (Gold Standard HbA2 > 3.5%)
    elif hba2 > 3.5:
        if lang == "English":
            st.error(f"RESULT: Beta Thalassemia Trait Confirmed (HbA2: {hba2}%)")
            st.info("💡 ARMY INSIGHT: BTT is a genetic carrier status, NOT a disease. You can be FIT if your Hb is >12.0 and physical fitness is normal.")
        else:
            st.error(f"نتیجہ: بیٹا تھیلیسیمیا ٹریٹ کی تصدیق ہو گئی ہے (HbA2: {hba2}%)")
            st.info("💡 اہم معلومات: یہ بیماری نہیں جینیاتی کیفیت ہے۔ اگر خون کی مقدار پوری ہو تو آپ فوج کے لیے فٹ ہو سکتے ہیں۔")
            
    # Check for Normal/Fit
    elif hb >= 13.0 and mcv >= 80:
        st.success("RESULT: MEDICALLY FIT / NORMAL" if lang=="English" else "نتیجہ: آپ میڈیکلی فٹ ہیں")
    
    # Low HB / Anemia
    else:
        st.warning("RESULT: UNFIT / LOW HEMOGLOBIN (Anemia)" if lang=="English" else "نتیجہ: ان فٹ / خون کی کمی")

# 6. Army Candidates Guide
st.divider()
st.subheader("📋 Guide for Army Candidates / امیدواروں کے لیے رہنمائی")
with st.expander("Steps if declared UNFIT / ان فٹ ہونے کی صورت میں کیا کریں؟"):
    st.write("""
    1. **Check Hb:** Ensure Hemoglobin is above 12 g/dL.
    2. **AMB Appeal:** You have the right to appeal at the Appeal Medical Board.
    3. **Expert Opinion:** BTT candidates are often FIT if physically strong.
    """)
    st.write("""
    1. **ہیموگلوبن:** یقینی بنائیں کہ خون کی مقدار 12 سے زیادہ ہو۔
    2. **اپیل:** آپ اپیل میڈیکل بورڈ (AMB) میں دوبارہ معائنہ کی درخواست دے سکتے ہیں۔
    3. **ماہرِ خون:** اگر آپ جسمانی طور پر مضبوط ہیں تو BTT کے باوجود فٹ ہو سکتے ہیں۔
    """)

# 7. WhatsApp Share Button
site_url = "https://thelesemiatratindentifier.streamlit.app/"
share_msg = f"Check your blood report for Thalassemia Trait & Army Fitness here: {site_url}"
whatsapp_url = f"https://wa.me/?text={share_msg}"

st.markdown(f"""
<a href="{whatsapp_url}" target="_blank">
    <button style="background-color: #25D366; color: white; padding: 12px; border: none; border-radius: 10px; width: 100%; font-size: 18px; cursor: pointer; font-weight: bold;">
        Share on WhatsApp / واٹس ایپ پر شیئر کریں
    </button>
</a>
""", unsafe_allow_html=True)

st.caption("Educational tool based on Clinical Standards (HbA2 > 3.5%). Not a replacement for a Doctor.")
    
