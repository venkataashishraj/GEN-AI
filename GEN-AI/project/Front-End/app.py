import streamlit as st
t1, t2 = st.tabs(["🔐 Login", "📝 Registration"])
with t1:
    st.title("🔐 Login")
    with st.form("Login"):
        st.text_input( "👤 Username",placeholder="Enter your username")
        st.text_input("🔑 Password",placeholder="Enter your password",type="password")
        st.selectbox("👨‍💼 Role",["", "Trainer", "Student"])
        st.form_submit_button("🚀 Login")
with t2:
    st.title("📝 Registration")
    with st.form("Registration"):
        st.text_input("👤 Name",placeholder="Enter your name")
        st.text_input("📧 E-mail",placeholder="Enter your E-mail")
        st.text_input("🔑 Password",placeholder="Enter your password",type="password")
        st.text_input("🔒 Confirm Password",placeholder="Enter confirm password",type="password")
        st.selectbox("👨‍💼 Role",["", "Trainer", "Student"])
        st.form_submit_button("✅ Register")