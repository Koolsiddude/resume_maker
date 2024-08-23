import streamlit as st
from jinja2 import Template
import pandas as pd
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
            details = details.split("\n")
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
        edu_end_date = st.text_input(f"Year {i + 1}", key=f"Year education{i + 1}")
        education.append({
            "degree": degree,
            "institution": institution,
            "board_university": board_university,
            "CGPA": edu_CGPA,
            "end_date": edu_end_date
        })

include_intern_experience = st.checkbox("Include Internships")
internships = []
if include_intern_experience:
    st.header("Internships")
    num_intern = st.number_input("Number of Internships", min_value=1, max_value=10, value=1)
    for i in range(num_intern):
        with st.expander(f"Experiance {i + 1}"):
            designation = st.text_input(f"Position {i + 1}", key=f"Position_intern{i + 1}")
            company_name = st.text_input(f"Company {i + 1}", key=f"Company_intern {i + 1}")
            months = st.text_input(f"Total Months {i + 1}", key =f"months_intern {i + 1}")
            details_int = st.text_area(f"Details {i + 1} (Separate by newline)", key=f"Details_intern {i + 1}")
            details_int = details.split("\n")
            internships.append({
                "designation": designation,
                "company_name": company_name,
                "months": months,
                "details": details
            })

# Skills
include_skills = st.checkbox("Include Skills")
skills = []
if include_skills:
    st.header("Skills")
    num_sk = st.number_input("Number Skills", min_value=1, max_value=10, value=1)
    for i in range(num_sk):
        with st.expander(f"Skill {i + 1}"):
            sk_name = st.text_input(f"Name {i + 1}",key=f"skill_Name {i + 1}")
            sk_name = sk_name.split("\n")
            skills.append({
                "name": sk_name,
                "num": num_sk
            })


# Projects
include_projects = st.checkbox("Include Live Projects")
projects = []
if include_projects:
    st.header(" Live Projects")
    num_projects = st.number_input("Number of Projects", min_value=1, max_value=10, value=1)
    for i in range(num_projects):
        with st.expander(f"Project {i + 1}"):
            project_name = st.text_input(f"Project Name {i + 1}",key=f"Project Name {i + 1}")
            project_date = st.text_input(f"Project Date {i + 1}",key=f"Project Date {i + 1}")
            project_description = st.text_area(f"Project Description {i + 1}",key=f"Project Description {i + 1}")
            project_description = project_description.split("\n")
            projects.append({
                "name": project_name,
                "date": project_date,
                "description": project_description,
                "num": num_projects
            })

# Certifications
include_certificate = st.checkbox("Include Certifications")
certifications = []
if include_certificate:
    st.header("Certifications")
    num_certificate = st.number_input("Number of Certification", min_value=1, max_value=10, value=1)
    for i in range(num_certificate):
        with st.expander(f"Certificate {i + 1}"):
            certificate_name = st.text_input(f"Certificate Name {i + 1}",key=f"cert_name {i + 1}")
            certificate_name = certificate_name.split("\n")
            certifications.append({
                "name": certificate_name,
                "num": num_certificate
            })

#Position of responsibility
include_pos = st.checkbox("Include Position of Responsibility")
pos = []
if include_pos:
    st.header("Position of Responsibility")
    num_pos = st.number_input("Number of Responsibilities", min_value=1, max_value=10, value=1)
    for i in range(num_pos):
        with st.expander(f"Responsibility {i + 1}"):
            pos_name = st.text_input(f"Title {i + 1}",key=f"pos_name {i + 1}")
            pos_description = st.text_area(f"Resposibility_description{i + 1}",key=f"pos_description {i + 1}")
            pos_description = pos_description.split("\n")
            pos.append({
                "name": pos_name,
                "description": pos_description,
                "num": num_pos
            })

#Research Papers
include_res = st.checkbox("Include Research Papers")
res = []
if include_res:
    st.header("Research Papers")
    num_res = st.number_input("Number of Research Papers", min_value=1, max_value=10, value=1)
    for i in range(num_res):
        with st.expander(f"Research Paper {i + 1}"):
            res_name = st.text_input(f"Title {i + 1}",key=f"res_title {i + 1}")
            res.append({
                "name": res_name,
                "num": num_res
            })

#Social Projects
include_res = st.checkbox("Include Social Projects")
soc_proj = []
if include_res:
    st.header("Social Projects")
    num_soc_proj = st.number_input("Number of Social Projects", min_value=1, max_value=10, value=1)
    for i in range(num_soc_proj):
        with st.expander(f"Social Project {i + 1}"):
            soc_proj_name = st.text_input(f"Title {i + 1}",key=f"res_title {i + 1}")
            soc_proj_description = st.text_area(f"Description {i + 1}",key=f"soc_proj_description {i + 1}")
            soc_proj.append({
                "name": soc_proj_name,
                "description": soc_proj_description,
                "num": num_soc_proj
            })

st.header("Academic Achievements")
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
      table {
            width: 100%;
            border-collapse: collapse;
        }

        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
            vertical-align: middle;
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
        margin: 0px;
        text-align: center;
      }
      .work-exp-header th,
      .title-work-exp th,
      td {
        border: 1px solid #000;
        padding: 8px;
        text-align: left;
        font-size: 12px;
        margin: 0px;
      }
      .table-header th {
        background-color: #c7cfeb;
        text-align: center;
      }
      .work-exp-header th {
        background-color: #f2f2f2;
        text-align: left;
      }
      .title-work-exp th {
        text-align: center;
        background-color: #c7cfeb;
      }
      .work-exp-data td {
        text-align: left;
      }
      .work-exp-data th {
        background-color: #f2f2f2;
        text-align: left;
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
      .live-project th{
        border: 1px solid #000;
        padding: 8px;
        text-align: left;
        font-size: 12px;
        margin: 0;
        border-collapse: collapse;
      }
      .live-project td :first-child{
        border: 0px;
        padding: 8px;
        text-align: left;
        font-size: 12px;
        margin: 0;
        border-collapse: collapse;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="header">
        <h1>{{name}}</h1>
        <p>
          Email:
          <a href="mailto:{{email}}">{{email}}</a>
          | Phone: {{phone}} | LinkedIn: <a href="{{linkedin}}">{{linkedin}}</a>
        </p>
      </div>
      <div class="section-profile">
        <table>
          <thead>
          <tr class="title-work-exp">
            <th>Profile Summary</th>
          </tr>
          <tr class="work-exp-data">
            <td>{{ profile }}</td>
          </tr>
      </div>
      <div class="section-education">
        <table>
          <thead>
          <tr class="title-work-exp">
            <th>Degree</th>
            <th>Institute</th>
            <th>Board/University</th>
            <th>%/CGPA</th>
            <th>Year</th>
          </tr>
        </thead>
          {% for education in education %}
          <tbody>
          <tr class="work-exp-data">
            <td>{{ education.degree }}</td>
            <td>{{ education.institution }}</td>
            <td>{{ education.board_university }}</td>
            <td>{{ education.CGPA }}</td>
            <td>{{ education.end_date }}</td>
          </tr>
        </tbody>
          {% endfor %}
        </table>
      </div>

      <div class="section-work">
        <table>
          {% for work_exp in work_experience %}
            <tr class="title-work-exp">
              <th class="title-work-exp" colspan="5">Work Experience</th>
            </tr>
            <tr class="work-exp-header">
              <th class="comp_name" colspan="4">{{work_exp.company_name}}</th>
              <th class="des" colspan="4">{{work_exp.designation}}</th>
            </tr>
            <tr class="work-exp-data">
              <td colspan="4">{{work_exp.years}}</td>
              <td colspan="4">{{work_exp.details}}</td>
            </tr>
          {% endfor %}
        </table>
      </div>

      <div class="section-internship">
        <table>
          <thead>
            <tr class="title-work-exp">
              <th class="title-work-exp" colspan="5">Internships</th>
            </tr>
            {% for intern in internships %}
            <tr class="work-exp-header">
              <th class="comp_name" colspan="4">{{intern.company_name}}</th>
              <th class="des" colspan="4">{{intern.designation}}</th>
            </tr>
          </thead>
          <tbody>
            <tr class="work-exp-data">
              <td colspan="4">{{intern.months}}</td>
              <td colspan="4">{{intern.details}}</td>
            </tr>
          </tbody>
          {% endfor %}
        </table>
      </div>

      <div class="section-extra_activities">
        <table>
            <tr class="title-work-exp">
              <th class="title-work-exp" colspan="5">
                Co-Curricular & Extra-Curricular Activities
              </th>
            </tr>

            <tr class="live-project">
              <th id="comp_name" colspan="1">Certifications</th>
              <td id="des" colspan="4">
                <table class="live-project">
                  {% for cert in certifications %}
                  <tr>
                    <td>{{ cert.num }} {{ cert.name }}</td>
                  </tr>
                  {% endfor %}
                </table>
              </td>
            </tr>


            <tr class="live-project">
              <th id="comp_name" colspan="1">Live Projects</th>
              <td id="des" colspan="4">
                <table class="live-project">
                  {% for project in projects %}
                  <tr>
                    <td>{{ project.num }} {{ project.name }}<br>
                    {{ project.description }}</td>
                  </tr>
                  {% endfor %}
                </table>
              </td>
            </tr>

            <tr class="live-project">
              <th id="comp_name" colspan="1">Position of Responsibility</th>
              <td id="des" colspan="4">
                <table class="live-project">
                  {% for pro_rep in position_of_responsibility %}
                  <tr>
                    <td>{{ pos_rep.num }} {{ pos_rep.name }}<br>
                    {{ pos_rep.description }}</td>
                  </tr>
                  {% endfor %}
                </table>
              </td>
            </tr>

            <tr class="live-project">
              <th id="comp_name" colspan="1">Social Projects</th>
              <td id="des" colspan="4">
                <table class="live-project">
                  {% for soc_proj in Social_projects %}
                  <tr>
                    <td>{{ soc_proj.num }} {{ soc_proj.name }}<br>
                    {{ soc_proj.description }}</td>
                  </tr>
                  {% endfor %}
                </table>
              </td>
            </tr>

            <tr class="live-project">
              <th id="comp_name" colspan="1">Skills</th>
              <td id="des" colspan="4">
                <table class="live-project">
                  {% for sk in skills %}
                  <tr>
                    <td>{{ sk.num }} {{ sk.name }}</td>
                  </tr>
                  {% endfor %}
                </table>
              </td>
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
            <tr class="live-project">
              <th id="comp_name" colspan="1">Research Papers</th>
              <td id="des" colspan="4">
                <table class="live-project">
                  {% for res_p in research_papers %}
                  <tr>
                    <td>{{ res_p.num }} {{ res_p.name }}</td>
                  </tr>
                  {% endfor %}
                </table>
              </td>
            </tr>
          </thead>
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
    "skills": skills if include_skills else [],
    "Position_of_responsibility": pos if include_pos else [],
    "projects": projects if include_projects else [],
    "certifications": certifications if include_certificate else [],
    "research_papers": res,
    "Social_projects": soc_proj,
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
