import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Thal-Analyst AI", page_icon="🔬")

# 2. Visit Counter
st.markdown("![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fthelesemiatratindentifier.streamlit.app&count_bg=%2379C83D&title_bg=%23555555&icon=%23E7E7E7&title=Total+Visits&edge_flat=false)")

# 3. Heading & Language Selection
st.title("🔬 AI Hematology Diagnostic Tool")
st.markdown("### Specialized for Beta Thalassemia Trait (BTT) Screening")
lang = st.radio("Select Language / زبان منتخب کریں", ("English", "Urdu"))

# 4. Input Form
with st.form("medical_form"):
    st.markdown("##### Enter Values from Report:")
    col1, col2 = st.columns(2)
    with col1:
        hb = st.number_input("Hemoglobin / ہیموگلوبن (g/dL)", value=13.0)
        rbc = st.number_input("RBC Count / ریڈ سیل کاؤنٹ", value=5.0)
    with col2:
        mcv = st.number_input("MCV (fL)", value=76.0)
        hba2 = st.number_input("HbA2 %", value=2.0)
    
    btn_text = "Analyze" if lang == "English" else "تجزیہ کریں"
    submitted = st.form_submit_button(btn_text)

# 5. Result Logic (Flexible Army Standards)
if submitted:
    st.divider()
    # Check for BTT first (HbA2 > 3.5%)
    if hba2 > 3.5:
        st.error(f"RESULT: Beta Thalassemia Trait (HbA2: {hba2}%)" if lang=="English" else f"نتیجہ: بیٹا تھیلیسیمیا ٹریٹ (HbA2: {hba2}%)")
        st.info("BTT is usually fit in Army if Hb is stable." if lang=="English" else "خون پورا ہونے کی صورت میں آرمی میں فٹ قرار دیا جا سکتا ہے۔")
    
    # Army Friendly: Fit if Hb >= 13 and MCV >= 75
    elif hb >= 13.0 and mcv >= 75.0:
        st.success("RESULT: MEDICALLY FIT" if lang=="English" else "نتیجہ: آپ میڈیکلی فٹ ہیں")
    
    # Unfit/Low Values
    else:
        st.warning("RESULT: UNFIT / REVIEW NEEDED" if lang=="English" else "نتیجہ: ان فٹ / ڈاکٹر سے مشورہ کریں")

# 6. Disclaimer & Guide
st.divider()
st.warning("⚠️ DISCLAIMER: This is an AI tool for education. Final decision belongs to the Army Medical Board." if lang=="English" else "⚠️ اعلان: یہ ایک تعلیمی ٹول ہے۔ آخری فیصلہ آرمی میڈیکل بورڈ کا ہی ہوگا۔")

# 7. WhatsApp Share
site_url = "https://thelesemiatratindentifier.streamlit.app/"
share_msg = f"Check your BTT & Fitness Report here: {site_url}"
whatsapp_url = f"https://wa.me/?text={share_msg}"

st.markdown(f'<a href="{whatsapp_url}" target="_blank"><button style="background-color: #25D366; color: white; padding: 12px; border: none; border-radius: 10px; width: 100%; cursor: pointer; font-weight: bold;">{ "Share on WhatsApp" if lang=="English" else "واٹس ایپ پر شیئر کریں" }</button></a>', unsafe_allow_html=True)
        
