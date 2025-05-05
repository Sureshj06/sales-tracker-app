import streamlit as st
import requests
import pandas as pd

# 🔗 Replace this with your actual Render backend URL
BASE_URL = "https://your-backend-name.onrender.com"

st.set_page_config(page_title="Sales Tracker", layout="wide")
st.title("📊 Sales Tracker Dashboard")

tab1, tab2, tab3 = st.tabs(["Admin Panel", "Telecaller Panel", "License Matcher"])

# 🚀 Tab 1: Admin Panel
with tab1:
    st.header("👤 Students")
    try:
        students = requests.get(f"{BASE_URL}/students").json()
        st.dataframe(pd.DataFrame(students))
    except:
        st.error("Failed to load students.")

    st.header("🏢 Subunits")
    try:
        subunits = requests.get(f"{BASE_URL}/subunits").json()
        st.dataframe(pd.DataFrame(subunits))
    except:
        st.error("Failed to load subunits.")

    st.header("💼 Sales")
    try:
        sales = requests.get(f"{BASE_URL}/sales").json()
        st.dataframe(pd.DataFrame(sales))
    except:
        st.error("Failed to load sales.")

# ☎️ Tab 2: Telecaller Panel
with tab2:
    st.header("📞 Student Calling List")
    try:
        students = requests.get(f"{BASE_URL}/students").json()
        for student in students:
            st.markdown(f"**{student['name']}** | Phone: {student['phone']} | Status: {student['status']}")
    except:
        st.error("Could not fetch student list.")

# 🧾 Tab 3: License Matcher
with tab3:
    st.header("🔍 Upload License CSV")
    uploaded_file = st.file_uploader("Upload your license CSV", type="csv")

    if uploaded_file:
        try:
            files = {"file": uploaded_file.getvalue()}
            response = requests.post(f"{BASE_URL}/licenses/match", files=files)
            matched = response.json()
            st.success("License match completed!")
            st.dataframe(pd.DataFrame(matched))
        except Exception as e:
            st.error(f"Upload failed: {e}")
