import streamlit as st
from jinja2 import Template
import pandas as pd

# Function to generate resume
def generate_resume(template, context):
    return Template(template).render(context)

# Streamlit interface
st.title("Resume Builder")

# User inputs
name = st.text_input("Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
summary = st.text_area("Summary")
education = st.text_area("Education")
work_experience = st.text_area("Work Experience")
skills = st.text_area("Skills")

# Custom template input
template_input = st.text_area("Paste your custom template here")

# Create a context for the template
context = {
    "name": name,
    "email": email,
    "phone": phone,
    "summary": summary,
    "education": education,
    "work_experience": work_experience,
    "skills": skills,
}

if st.button("Generate Resume"):
    if template_input:
        resume = generate_resume(template_input, context)
        st.markdown(resume, unsafe_allow_html=True)

        # Optionally, you can provide an option to download the resume as PDF
        st.download_button(label="Download Resume", data=resume, file_name="resume.html", mime="text/html")
    else:
        st.error("Please provide a template.")

