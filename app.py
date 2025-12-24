import streamlit as st

st.set_page_config(page_title="Thal-Analyst AI", page_icon="🔬")

st.title("🔬 AI Hematology Diagnostic Tool")
st.markdown("### Specialized for Beta Thalassemia Trait (BTT) Screening")

# Sidebar for Medical Standards References
st.sidebar.header("Clinical Guidelines")
st.sidebar.info("Diagnosis based on HbA2 > 3.5% as the Gold Standard for BTT.")

# Input Form
with st.form("cbc_form"):
    col1, col2 = st.columns(2)
    with col1:
        hb = st.number_input("Hemoglobin (g/dL)", value=12.8)
        mcv = st.number_input("MCV (fL)", value=69.9)
    with col2:
        rbc = st.number_input("RBC Count (10^6/uL)", value=6.02)
        hba2 = st.number_input("HbA2 %", value=5.0)
    
    submit = st.form_submit_button("Analyze Report")

if submit:
    mentzer = mcv / rbc
    st.divider()
    
    if hba2 > 3.5:
        st.error(f"### RESULT: UNFIT / BTT CARRIER")
        st.write(f"**Findings:** HbA2 level is **{hba2}%**, which confirms Beta Thalassemia Trait.")
        st.write(f"**Mentzer Index:** {mentzer:.2f} (Index < 13 supports BTT over Iron Deficiency).")
    elif hb < 13.0:
        st.warning("### RESULT: UNFIT (Anemia)")
        st.write("Hemoglobin is below the required threshold for selection.")
    else:
        st.success("### RESULT: MEDICALLY FIT")

st.caption("Disclaimer: This tool is for educational purposes. Based on Sadiq et al. (2018).")
                             
