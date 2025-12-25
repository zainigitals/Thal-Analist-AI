        import streamlit as st

st.set_page_config(page_title="Thal-Analyst AI", page_icon="🔬")

# Visit Counter
st.markdown("![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fthelesemiatratindentifier.streamlit.app&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=Total+Visits&edge_flat=false)")

st.title("🔬 AI Hematology Diagnostic Tool")
st.markdown("### Specialized for Beta Thalassemia Trait (BTT) Screening")

lang = st.radio("Select Language / زبان منتخب کریں", ("English", "Urdu"))

with st.form("medical_form"):
    hb = st.number_input("Hemoglobin / ہیموگلوبن (Normal: 13-17)", value=12.8)
    rbc = st.number_input("RBC Count / ریڈ سیل کاؤنٹ", value=6.02)
    mcv = st.number_input("MCV", value=69.9)
    hba2 = st.number_input("HbA2 % (Electrophoresis)", value=5.0)
    submitted = st.form_submit_button("Analyze / تجزیہ کریں")

if submitted:
    mentzer = mcv / rbc
    st.divider()
    
    # NEW LOGIC: Checking for High/Low HB and BTT
    if hb > 18.0:
        msg = "CRITICAL: Hemoglobin is dangerously HIGH. Please consult a doctor immediately." if lang=="English" else "انتہائی اہم: آپ کا ہیموگلوبن بہت زیادہ ہے۔ فوری طور پر ڈاکٹر سے رجوع کریں۔"
        st.error(msg)
    elif hba2 > 3.5:
        if lang == "English":
            st.error(f"RESULT: Beta Thalassemia Trait Confirmed (HbA2: {hba2}%)")
        else:
            st.error(f"نتیجہ: بیٹا تھیلیسیمیا ٹریٹ کی تصدیق ہو گئی ہے (HbA2: {hba2}%)")
    elif hb < 13.0:
        msg = "RESULT: UNFIT (Low Hemoglobin/Anemia)" if lang=="English" else "نتیجہ: ان فٹ (خون کی کمی)"
        st.warning(msg)
    else:
        st.success("RESULT: MEDICALLY FIT" if lang=="English" else "نتیجہ: آپ فٹ ہیں")
    # WhatsApp Share Feature
st.divider()
st.subheader("📲 Share with Friends / دوستوں کے ساتھ شیئر کریں")

# Website link and text for WhatsApp
share_text = "Check your blood report for Beta Thalassemia Trait (BTT) and Army Fitness here:"
site_url = "https://thelesemiatratindentifier.streamlit.app/"
whatsapp_url = f"https://wa.me/?text={share_text} {site_url}"

# Styled Button
st.markdown(f"""
<a href="{whatsapp_url}" target="_blank">
    <button style="
        background-color: #25D366;
        color: white;
        padding: 10px 24px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 18px;
        width: 100%;">
        Share on WhatsApp / واٹس ایپ پر شیئر کریں
    </button>
</a>
""", unsafe_allow_html=True)
    
