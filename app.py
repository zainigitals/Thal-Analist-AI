import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Thal-Analyst AI", page_icon="🔬")

# 2. Visit Counter
st.markdown("![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fthelesemiatratindentifier.streamlit.app&count_bg=%2379C83D&title_bg=%23555555&icon=%23E7E7E7&title=Total+Visits&edge_flat=false)")

# 3. Title
st.title("🔬 AI Hematology Diagnostic Tool")
st.markdown("### Specialized for Beta Thalassemia Trait (BTT) Screening")

# Language Selection
lang = st.radio("Select Language / زبان منتخب کریں", ("English", "Urdu"))

# 4. Input Form
with st.form("medical_form"):
    if lang == "English":
        st.markdown("##### Enter Values from Report:")
    else:
        st.markdown("##### رپورٹ سے ویلیوز یہاں لکھیں:")
        
    col1, col2 = st.columns(2)
    with col1:
        hb = st.number_input("Hemoglobin / ہیموگلوبن", value=12.8)
        rbc = st.number_input("RBC Count / ریڈ سیل کاؤنٹ", value=6.02)
    with col2:
        mcv = st.number_input("MCV", value=69.9)
        hba2 = st.number_input("HbA2 %", value=5.0)
    
    btn_text = "Analyze" if lang == "English" else "تجزیہ کریں"
    submitted = st.form_submit_button(btn_text)

# 5. Result Logic
if submitted:
    st.divider()
    # Check for Dangerously High HB first
    if hb > 18.5:
        if lang == "English":
            st.error("⚠️ CRITICAL: Hemoglobin is dangerously HIGH. Consult a doctor.")
        else:
            st.error("⚠️ انتہائی اہم: ہیموگلوبن بہت زیادہ ہے۔ فوری ڈاکٹر سے رجوع کریں۔")
            
    # Check for Beta Thalassemia Trait (HbA2 > 3.5%)
    elif hba2 > 3.5:
        if lang == "English":
            st.error(f"RESULT: Beta Thalassemia Trait (HbA2: {hba2}%)")
            st.info("💡 ARMY INSIGHT: BTT is NOT a disease. You can be FIT if your Hb is >12.0.")
        else:
            st.error(f"نتیجہ: بیٹا تھیلیسیمیا ٹریٹ کی تصدیق (HbA2: {hba2}%)")
            st.info("💡 اہم معلومات: یہ بیماری نہیں جینیاتی کیفیت ہے۔ خون پورا ہونے پر آپ فٹ ہو سکتے ہیں۔")
            
    # Check for Fit
    elif hb >= 13.0:
        if lang == "English":
            st.success("RESULT: MEDICALLY FIT")
        else:
            st.success("نتیجہ: آپ میڈیکلی فٹ ہیں")
            
    # Low HB
    else:
        if lang == "English":
            st.warning("RESULT: UNFIT / LOW HEMOGLOBIN")
        else:
            st.warning("نتیجہ: ان فٹ / خون کی کمی")

# 6. Guide & WhatsApp (Bottom)
st.divider()
if lang == "English":
    st.subheader("📋 Guide for Army Candidates")
    with st.expander("What to do if UNFIT?"):
        st.write("1. Check Hb (>12). 2. Appeal at AMB. 3. Consult Hematologist.")
else:
    st.subheader("📋 امیدواروں کے لیے رہنمائی")
    with st.expander("ان فٹ ہونے کی صورت میں کیا کریں؟"):
        st.write("1. ہیموگلوبن 12 سے اوپر رکھیں۔ 2. اپیل بورڈ (AMB) میں جائیں۔")

# WhatsApp Button
site_url = "https://thelesemiatratindentifier.streamlit.app/"
share_msg = "Check your BTT report here:" if lang=="English" else "اپنی رپورٹ یہاں چیک کریں:"
whatsapp_url = f"https://wa.me/?text={share_msg} {site_url}"

st.markdown(f'<a href="{whatsapp_url}" target="_blank"><button style="background-color: #25D366; color: white; padding: 12px; border: none; border-radius: 10px; width: 100%; cursor: pointer; font-weight: bold;">Share on WhatsApp / واٹس ایپ پر شیئر کریں</button></a>', unsafe_allow_html=True)
