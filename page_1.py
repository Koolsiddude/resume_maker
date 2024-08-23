import streamlit as st
from jinja2 import Template
import pandas as pd
import fitz
from io import BytesIO

# Function to generate resume
def generate_resume(template, context):
    return Template(template).render(context)

# Streamlit interface
st.title("Resume Builder")

# User inputs
st.header("Personal Information")
name = st.text_input("Full Name", key="Full Name")
email = st.text_input("Email", key="Email")
phone = st.text_input("Phone", key="Phone")
linkedin = st.text_input("LinkedIn URL", key="LinkedIn URL")
# Profile Summary
st.header("Profile Summary")
profile = st.text_area("Profile Summary")

# Work Experience
include_work_experience = st.checkbox("Include Work Experience")
work_experience = []
if include_work_experience:
    st.header("Work Experience")
    num_jobs = st.number_input("Number of Jobs", min_value=1, max_value=10, value=1)
    for i in range(num_jobs):
        with st.expander(f"Experiance {i + 1}"):
            designation = st.text_input(f"Position {i + 1}", key=f"Position {i + 1}")
            company_name = st.text_input(f"Company {i + 1}", key=f"Company {i + 1}")
            years = st.text_input(f"Total Years {i + 1} (or 'Present')", key =f"years {i + 1}")
            details = st.text_area(f"Responsibilities {i + 1} (Separate by newline)")
            work_experience.append({
                "designation": designation,
                "company_name": company_name,
                "years": years,
                "details": details
            })

# Education
st.header("Education")
education = []
num_education = st.number_input("Number of Educational Qualifications", min_value=1, max_value=10, value=1)
for i in range(num_education):
    with st.expander(f"Education {i + 1}"):
        degree = st.text_input(f"Degree {i + 1}", key=f"Degree {i + 1}")
        institution = st.text_input(f"Institution {i + 1}", key=f"Institution {i + 1}")
        board_university = st.text_input(f"Board/University {i + 1}",key=f"B&U {i + 1}")
        edu_CGPA = st.text_input(f"CGPA {i + 1}", key=f"CGPA education {i + 1}")
        edu_end_date = st.text_input(f"End Date {i + 1}", key=f"End Date education{i + 1}")
        education.append({
            "degree": degree,
            "institution": institution,
            "board_university": board_university,
            "CGPA": edu_CGPA,
            "end_date": edu_end_date
        })

include_intern_experience = st.checkbox("Include Interships")
internships = []
if include_intern_experience:
    st.header("Intermships")
    num_intern = st.number_input("Number of Internships", min_value=1, max_value=10, value=1)
    for i in range(num_intern):
        with st.expander(f"Experiance {i + 1}"):
            designation = st.text_input(f"Position {i + 1}", key=f"Position_intern{i + 1}")
            company_name = st.text_input(f"Company {i + 1}", key=f"Company_intern {i + 1}")
            months = st.text_input(f"Total Months {i + 1}", key =f"months_intern {i + 1}")
            details = st.text_area(f"Details {i + 1} (Separate by newline)")
            internships.append({
                "designation": designation,
                "company_name": company_name,
                "months": months,
                "details": details
            })

# Skills
st.header("Skills")
skills = st.text_area("Skills (Separate by commas)")

# Projects
include_projects = st.checkbox("Include Projects")
projects = []
if include_projects:
    st.header("Projects")
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
st.header("Academic Achievements")
academic_achievement = []
certifications = st.text_input("Certifications (Separate by commas)", key="Certificates")
research_papers = st.text_area("Research Papers (Separate by commas)", key="Research Papers")
scholarships = st.text_area("Scholarships (Separate by commas)", key="Scholarships")
comp_exam = st.text_area("Competitive Exams (Separate by commas)", key="comp_exam")
languages = st.text_area("Languages Known (Separate by commas)", key="lang")
hobbies = st.text_area("Hobbies and Interests (Separate by commas)", key="h/b")
# Custom template input
template_input = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{{name}}'s CV</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 20px;
        background-color: #f4f4f4;
      }
      .container {
        width: 100%;
        max-width: 800px;
        margin: 0 auto;
        background: #fff;
        padding: 20px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      }
      @media print {
        .container {
          width: 210mm; /* A4 width */
          height: 297mm; /* A4 height */
          margin: 0 auto;
          padding: 20mm;
          box-shadow: none;
        }
      }
      .header,
      .section {
        margin-bottom: 20px;
      }
      .header {
        text-align: left;
      }
      .header h1 {
        margin: 0;
        font-size: 2em;
      }
      .header p {
        margin: 5px 0;
        padding-left: 25px;
      }
      .section h2 {
        border-bottom: 2px solid #000;
        padding-bottom: 5px;
      }
      .section ul {
        list-style-type: none;
        padding: 0;
      }
      .section ul li {
        margin-bottom: 5px;
      }
      .section-work h2 {
        text-align: center;
        font-size: 18px;
        font-style: normal;
        border: 1px solid #000;
        padding: 8px;
        font-size: 15px;
      }
      table {
        width: 100%;
        border-collapse: collapse;
        border-spacing: 0;
        margin: 0;
        padding: 0;
      }
      .table-header th,
      .table-data td {
        border: 1px solid #000;
        padding: 8px;
        text-align: left;
        font-size: 12px;
        margin: 0;
        text-align: center;
      }
      .work-exp-header th,
      .title-work-exp th,
      td {
        border: 1px solid #000;
        padding: 8px;
        text-align: left;
        font-size: 12px;
        margin: 0;
      }
      .table-header th {
        background-color: #c7cfeb;
        text-align: center;
      }
      .work-exp-header th {
        background-color: #f2f2f2;
        text-align: center;
      }
      .title-work-exp th {
        text-align: center;
        background-color: #c7cfeb;
      }
      .work-exp-data td {
        text-align: center;
      }
      .work-exp-data th {
        background-color: #f2f2f2;
        text-align: center;
        border: 1px solid #000;
        padding: 8px;
        font-size: 12px;
        margin: 0;
      }
      .title-languages {
        text-align: center;
        background-color: #c7cfeb;
        border: 1px solid #000;
        padding: 8px;
        text-align: left;
        font-size: 12px;
        margin: 0;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="header">
        <h1>{{name}}</h1>
        <p>
          Email:
          <a href="{{email}}">{{email}}</a>
          | Phone: {{phone}} | LinkedIn:{{linkedin}}
        </p>
      </div>

      <div class="section">
        <table>
          <tr class="table-header">
            <th>Degree</th>
            <th>Institute</th>
            <th>Board/University</th>
            <th>%/CGPA</th>
            <th>Year</th>
          </tr>
          {% for education in education %}
          <tr class="table-data" style="border-top: 1px solid #000">
            <td>{{ education.degree }}</td>
            <td>{{ education.institution }}</td>
            <td>{{ education.board_university }}</td>
            <td>{{ education.CGPA }}</td>
            <td>{{ education.end_date }}</td>
          </tr>
          {% endfor %}
        </table>
      </div>

      <div class="section-work">
        <table>
          {% for work_exp in work_experience %}
          <thead>
            <tr class="title-work-exp">
              <th class="title-work-exp" colspan="5">Work Experience</th>
            </tr>
            <tr class="work-exp-header">
              <th class="comp_name" colspan="2">{{work_exp.company_name}}</th>
              <th class="des" colspan="3">{{work_exp.designation}}</th>
            </tr>
          </thead>
          <tbody>
            <tr class="work-exp-data">
              <td colspan="2">{{work_exp.years}}</td>
              <td colspan="3">{{work_exp.details}}</td>
            </tr>
          </tbody>
          {% endfor %}
        </table>
      </div>

      <div class="section-internship">
        <table>
          {% for intern in internships %}
          <thead>
            <tr class="title-work-exp">
              <th class="title-work-exp" colspan="5">Internships</th>
            </tr>
            <tr class="work-exp-header">
              <th class="comp_name" colspan="2">{{intern.company_name}}</th>
              <th class="des" colspan="3">{{intern.designation}}</th>
            </tr>
          </thead>
          <tbody>
            <tr class="work-exp-data">
              <td colspan="2">{{intern.months}}</td>
              <td colspan="3">{{intern.details}}</td>
            </tr>
          </tbody>
          {% endfor %}
        </table>
      </div>

      <div class="section-extra_activities">
        <table>
          <thead>
            <tr class="title-work-exp">
              <th class="title-work-exp" colspan="5">
                Co-Curricular & Extra-Curricular Activities
              </th>
            </tr>
            <tr class="work-exp-header">
              <th class="comp_name" colspan="1">Certifications</th>
              <td class="des" colspan="4">{{certifications}}</td>
            </tr>
          </thead>
          <tbody>
            {% for proj in projects %}
            <tr class="work-exp-header">
              <th id="comp_name" colspan="1">Live Projects</th>
              <td id="des" colspan="4">
                {{proj.name}} {{proj.description}} {{proj.date}}
              </td>
            </tr>
            {% endfor %}
            <tr class="work-exp-header">
              <th id="comp_name" colspan="1">Skills</th>
              <td id="des" colspan="4">{{skills}}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="section-academic-achievements">
        <table>
          <thead>
            <tr class="title-work-exp">
              <th class="title-work-exp" colspan="5">Academic Achievements</th>
            </tr>
            <tr class="work-exp-header">
              <th colspan="1">Research Paper</th>
              <td colspan="4">{{research_papers}}</td>
            </tr>
          </thead>
          <tbody>
            <tr class="work-exp-header">
              <th>Scholarship</th>
              <td colspan="4">{{Scholarships}}</td>
            </tr>
            <tr class="work-exp-header">
              <th class="comp_name" colspan="1">Comp. Exam</th>
              <td class="des" colspan="4">{{competitive_exams}}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="section-languages">
        <table>
          <thead>
            <tr class="title-languages">
              <th class="title-work-exp" colspan="5">
                Languages Known: {{languages}}
              </th>
            </tr>
          </thead>
        </table>
      </div>

      <div class="section-hobbies">
        <table>
          <thead>
            <tr class="title-languages">
              <th class="title-work-exp" colspan="5">
                Hobbies/Interests: {{Hobbies}}
              </th>
            </tr>
          </thead>
        </table>
      </div>
    </div>
  </body>
</html>
"""

# Create a context for the template
context = {
    "name": name,
    "email": email,
    "phone": phone,
    "linkedin": linkedin,
    "profile": profile,
    "work_experience": work_experience if include_work_experience else ["N.A"],
    "education": education,
    "internships": internships,
    "skills": skills,
    "projects": projects if include_projects else [],
    "certifications": certifications,
    "research_papers": research_papers,
    "Scholarships": scholarships,
    "competitive_exams": comp_exam,
    "languages":languages,
    "Hobbies": hobbies
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