import streamlit as st

st.set_page_config(page_title="Thal-Analyst AI", page_icon="🔬")

# 1. Visit Counter
st.markdown("![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fthelesemiatratindentifier.streamlit.app&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=Total+Visits&edge_flat=false)")

st.title("🔬 AI Hematology Diagnostic Tool")
st.markdown("### Specialized for Beta Thalassemia Trait (BTT) Screening")

# Language Selection
lang = st.radio("Select Language / زبان منتخب کریں", ("English", "Urdu"))

# Input Form
with st.form("medical_form"):
    hb = st.number_input("Hemoglobin / ہیموگلوبن", value=12.8)
    rbc = st.number_input("RBC Count / ریڈ سیل کاؤنٹ", value=6.02)
    mcv = st.number_input("MCV", value=69.9)
    hba2 = st.number_input("HbA2 % (Electrophoresis)", value=5.0)
    submitted = st.form_submit_button("Analyze / تجزیہ کریں")

if submitted:
    mentzer = mcv / rbc
    st.divider()
    
    if hba2 > 3.5:
        if lang == "English":
            st.error(f"RESULT: Beta Thalassemia Trait Confirmed (HbA2: {hba2}%)")
            st.info("Advice: This is a genetic carrier status, not a disease. Avoid unnecessary iron.")
        else:
            st.error(f"نتیجہ: بیٹا تھیلیسیمیا ٹریٹ کی تصدیق ہو گئی ہے (HbA2: {hba2}%)")
            st.info("مشورہ: یہ ایک جینیاتی کیفیت ہے، بیماری نہیں۔ بلا ضرورت فولاد (Iron) کی دوائیں مت کھائیں۔")
    
    elif mentzer > 13:
        if lang == "English":
            st.warning("RESULT: Possible Iron Deficiency Anemia.")
        else:
            st.warning("نتیجہ: ممکنہ طور پر جسم میں خون/فولاد کی کمی ہے۔")
            
    else:
        st.success("RESULT: Medically Fit / Normal")
            
