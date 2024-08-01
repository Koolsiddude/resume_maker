import streamlit as st
from jinja2 import Template
import pandas as pd

# Function to generate resume
def generate_resume(template, context):
    return Template(template).render(context)

# Streamlit interface
st.title("Resume Builder")

# User inputs
st.header("Personal Information")
name = st.text_input("Full Name", key="Full Name")
address = st.text_input("Address", key="Address")
email = st.text_input("Email", key="Email")
phone = st.text_input("Phone", key="Phone")
linkedin = st.text_input("LinkedIn URL", key="LinkedIn URL")
github = st.text_input("GitHub URL", key="GitHub URL")

# Profile Summary
st.header("Profile Summary")
profile = st.text_area("Profile Summary")

# Work Experience
st.header("Work Experience")
work_experience = []
num_jobs = st.number_input("Number of Jobs", min_value=1, max_value=10, value=1)
for i in range(num_jobs):
    with st.expander(f"Job {i + 1}"):
        position = st.text_input(f"Position {i + 1}", key=f"Position {i + 1}")
        company = st.text_input(f"Company {i + 1}", key=f"Company {i + 1}")
        start_date = st.text_input(f"Start Date {i + 1}", key=f"Start Date {i + 1}")
        end_date = st.text_input(f"End Date {i + 1} (or 'Present')", key =f"End Date {i + 1}")
        responsibilities = st.text_area(f"Responsibilities {i + 1} (Separate by newline)").splitlines()
        work_experience.append({
            "position": position,
            "company": company,
            "start_date": start_date,
            "end_date": end_date,
            "responsibilities": responsibilities
        })

# Education
st.header("Education")
education = []
num_education = st.number_input("Number of Educational Qualifications", min_value=1, max_value=10, value=1)
for i in range(num_education):
    with st.expander(f"Education {i + 1}"):
        degree = st.text_input(f"Degree {i + 1}", key=f"Degree {i + 1}")
        institution = st.text_input(f"Institution {i + 1}", key=f"Institution {i + 1}")
        edu_start_date = st.text_input(f"Start Date {i + 1}", key=f"Start Date {i + 1}")
        edu_end_date = st.text_input(f"End Date {i + 1}", key=f"End Date {i + 1} another")
        details = st.text_area(f"Details {i + 1}",key=f"Details {i + 1}")
        education.append({
            "degree": degree,
            "institution": institution,
            "start_date": edu_start_date,
            "end_date": edu_end_date,
            "details": details
        })

# Skills
st.header("Skills")
skills = st.text_area("Skills (Separate by commas)").split(",")

# Projects
st.header("Projects")
projects = []
num_projects = st.number_input("Number of Projects", min_value=1, max_value=10, value=1)
for i in range(num_projects):
    with st.expander(f"Project {i + 1}"):
        project_name = st.text_input(f"Project Name {i + 1}",key=f"Project Name {i + 1}")
        project_date = st.text_input(f"Project Date {i + 1}",key=f"Project Date {i + 1}")
        project_description = st.text_area(f"Project Description {i + 1}",key=f"Project Description {i + 1}")
        projects.append({
            "name": project_name,
            "date": project_date,
            "description": project_description
        })

# Certifications
st.header("Certifications")
certifications = st.text_area("Certifications (Separate by commas)", key="Certificates").split(",")

# Custom template input
template_input = st.text_area("Paste your custom template here", key="Custom Template")

# Create a context for the template
context = {
    "name": name,
    "address": address,
    "email": email,
    "phone": phone,
    "linkedin": linkedin,
    "github": github,
    "profile": profile,
    "work_experience": work_experience,
    "education": education,
    "skills": [skill.strip() for skill in skills],
    "projects": projects,
    "certifications": [cert.strip() for cert in certifications]
}


if st.button("Generate Resume"):
    if template_input:
        resume = generate_resume(template_input, context)
        st.header("Resume Preview")
        st.markdown(resume, unsafe_allow_html=True)

        # Optionally, you can provide an option to download the resume as PDF
        st.download_button(label="Download Resume", data=resume, file_name="resume.html", mime="text/html")
    else:
        st.error("Please provide a template.")

