import io
import streamlit as st
from jinja2 import Template
import pandas as pd
from io import BytesIO
import zipfile
from streamlit_extras.let_it_rain import rain

# Set the page configuration
st.set_page_config(
    page_title="ResumeBuilder.io",  # Tab title
    page_icon=":book:",            # Tab icon (emoji or URL to an image)                # Use wide mode
)

# Function to generate resume
def generate_resume(template, context):
    return Template(template).render(context)

# Function to generate a template
def generate_template(params):
   template = """ 
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
        font-size: 10px;
      }

       @media print {
        .container {
          width: 210mm; /* A4 width */
          height: 297mm; /* A4 height */
          margin-top: 0;
          padding-top: 0;
          padding-right: 5mm;
        }
      }

      table {
            width: 100%;
            border-collapse: collapse;
            border-spacing: 0;
            margin: 0;
            padding: 0;
            table-layout: fixed;
            
        }

        th, td {
            border: 1px solid black;
            padding: 10 px;
            text-align: left;
            vertical-align: middle;
        }
        
        .title-education th {
          border: 1px solid #000;
          background-color: #c7cfeb;
          text-align: center;
          font-size: 11px;
          margin: 0;
          padding: 8px;
        }
        .education-data td{
          border: 1px solid #000;
          padding: 8px;
          text-align: center;
          font-size: 10px;
          margin: 0;
        }
        .section-education table{
          width: 100%;
            border-collapse: collapse;
            border-spacing: 0;
            margin: 0;
            padding: 0;
        }

      .header {
        text-align: left;
      }

      .header h1 {
        margin: 0;
        font-size: 2em;
      }

      .header p {
        margin: 0;
        padding-left: 25px;
      }
      
      .work-exp-header th,
      .title-work-exp th,
      td {
        border: 1px solid #000;
        padding: 10px;
        text-align: center;
        font-size: 10px;
        margin: 100px;
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
        font-size: 10px;
        margin: 0;
      }
      .title-languages {
        text-align: center;
        background-color: #c7cfeb;
        border: 1px solid #000;
        padding: 8px;
        text-align: left;
        font-size: 10px;
        margin: 0;
      }
      .live-project th{
        border: 1px solid #000;
        padding: 8px;
        text-align: left;
        font-size: 10px;
        margin: 0;
        border-collapse: collapse;
      }
      .live-project td :first-child{
        border: 0px;
        padding: 8px;
        text-align: left;
        font-size: 10px;
        margin: 0;
        border-collapse: collapse;
      }
      .live-projects th{
        border: 1px solid #000;
        background-color: #f2f2f2;
        padding: 8px;
        text-align: center;
        font-size: 10px;
        margin: 0;
        border-collapse: collapse;
      }
      .skills th{
        border: 1px solid #000;
        padding: 8px;
        text-align: left;
        font-size: 10px;
        margin: 0;
        border-collapse: collapse;
      }
      .skills td :first-child{
        border: 0px;
        padding: 8px;
        text-align: left;
        font-size: 10px;
        margin: 0;
        border-collapse: collapse;
        display: flex;
        flex-wrap: wrap;
      }
    </style>
  </head>
  <body>
    <div class="container">
   <img src="vbs-logo-removebg-preview.png" alt="Institution Logo" style="float: right; top:0; width: 200px; height: auto;"></img>     
      <div class="header">
        <h1>{{name}}</h1>
        <p>
          Email:
          <a href="mailto:{{email}}">{{email}}</a>
          | Phone: {{phone}} | LinkedIn: <a href="{{linkedin}}">Linkedin</a>
        </p>
      </div>
      """
   
   if "include_intern_experience" in params and not "include_work_experience" in params:
       template += """ 
        <div class="section-profile">
        <table>
          <thead>
          <tr class="title-work-exp">
            <th>Career Objective</th>
          </tr>
          <tr class="work-exp-data">
            <td>{{ profile }}</td>
          </tr>
      </div>
      <div class="section-education">
        <table>
          <thead>
          <tr class="title-education">
            <th>Degree</th>
            <th>Institute</th>
            <th>Board/University</th>
            <th>%/CGPA</th>
            <th>Year</th>
          </tr>
        </thead>
          {% for education in education %}
          <tbody>
          <tr class="education-data">
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

      <div class="section-internship">
        <table>
          <colgroup>
            <col style="width: 10%;">
            <col style="width: 10%;">
            <col style="width: 10%;">
            <col style="width: 10%;">
          </colgroup>
          <tr class="title-work-exp">
            <th class="title-work-exp" colspan="5">Internships</th>
          </tr>
          {% for intern in internships %}
          <tr class="work-exp-header">
            <th class="comp_name" colspan="2">{{intern.company_name}}</th>
            <th class="des" colspan="3">{{intern.designation}}</th>
          </tr>
          {% set details = intern.details %}
          {% set sentences = details.split(";") %}
          {% for sentence in sentences %}
          <tr class="work-exp-data">
            {% if loop.first %}
            <td rowspan="{{ sentences|length }}" colspan="2">{{intern.months}}</td>
            {% endif %}
            <td colspan="3"> &bull; {{sentence}}</td>
          </tr>
          {% endfor %}
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
              """
   if "include_work_experience"in params and not "include_intern_experience" in params:
       template += """
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
              <tr class="title-education">
                <th>Degree</th>
                <th>Institute</th>
                <th>Board/University</th>
                <th>%/CGPA</th>
                <th>Year</th>
              </tr>
            </thead>
              {% for education in education %}
              <tbody>
              <tr class="education-data">
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
              <colgroup>
                <col style="width: 10%;">
                <col style="width: 10%;">
                <col style="width: 10%;">
                <col style="width: 10%;">
              </colgroup>
                <tr class="title-work-exp">
                  <th class="title-work-exp" colspan="5">Work Experience</th>
                </tr>
                {% for work_exp in work_experience %}
                <tr class="work-exp-header">
                  <th class="comp_name" colspan="2">{{work_exp.company_name}}</th>
                  <th class="des" colspan="3">{{work_exp.designation}}</th>
                </tr>
                {% set details_work = work_exp.details %}
                {% set sentences_work = details_work.split(";") %}
                {% for sentence_work in sentences_work %}
                <tr class="work-exp-data">
                  {% if loop.first %}
                  <td rowspan="{{ sentences_work|length }}" colspan="2">{{work_exp.years}}</td>
                  {% endif %}
                  <td colspan="3">&bull; {{sentence_work}}</td>
                </tr>
              {% endfor %}
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
      """ 
   if "include_work_experience" in params and "include_intern_experience" in params:
       template += """
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
          <tr class="title-education">
          <th>Degree</th>
          <th>Institute</th>
          <th>Board/University</th>
          <th>%/CGPA</th>
          <th>Year</th>
          </tr>
          </thead>
          {% for education in education %}
          <tbody>
          <tr class="education-data">
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
          <colgroup>
          <col style="width: 10%;">
          <col style="width: 10%;">
          <col style="width: 10%;">
          <col style="width: 10%;">
          </colgroup>
          <tr class="title-work-exp">
          <th class="title-work-exp" colspan="5">Work Experience</th>
          </tr>
          {% for work_exp in work_experience %}
          <tr class="work-exp-header">
          <th class="comp_name" colspan="2">{{work_exp.company_name}}</th>
          <th class="des" colspan="3">{{work_exp.designation}}</th>
          </tr>
          {% set details_work = work_exp.details %}
          {% set sentences_work = details_work.split(";") %}
          {% for sentence_work in sentences_work %}
          <tr class="work-exp-data">
          {% if loop.first %}
          <td rowspan="{{ sentences_work|length }}" colspan="2">{{work_exp.years}}</td>
          {% endif %}
          <td colspan="3">&bull; {{sentence_work}}</td>
          </tr>
          {% endfor %}
          {% endfor %}
          </table>
          </div>

          <div class="section-internship">
          <table>
          <colgroup>
          <col style="width: 10%;">
          <col style="width: 10%;">
          <col style="width: 10%;">
          <col style="width: 10%;">
          </colgroup>
          <tr class="title-work-exp">
          <th class="title-work-exp" colspan="5">Internships</th>
          </tr>
          {% for intern in internships %}
          <tr class="work-exp-header">
          <th class="comp_name" colspan="2">{{intern.company_name}}</th>
          <th class="des" colspan="3">{{intern.designation}}</th>
          </tr>
          {% set details = intern.details %}
          {% set sentences = details.split(";") %}
          {% for sentence in sentences %}
          <tr class="work-exp-data">
          {% if loop.first %}
          <td rowspan="{{ sentences|length }}" colspan="2">{{intern.months}}</td>
          {% endif %}
          <td colspan="3"> &bull; {{sentence}}</td>
          </tr>
          {% endfor %}
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
          """    
   if "include_certificate" in params:
       template += """
            <tr class="live-project">
              <th id="comp_name" colspan="1">Certifications</th>
              <td id="des" colspan="4">
                <table class="live-project">
                  <colgroup>
                    <col style="width: 20%;">
                  </colgroup>
                  {% for cert in certifications %}
                  <tr>
                    <td> &bull; {{ cert.name }} {{ cert.year }}</td>
                  </tr>
                  {% endfor %}
                </table>
              </td>
            </tr>
        </table>
                        """
   if "include_projects" in params:
       template += """
          <div class="section-liveprojects">
            <table>
              <colgroup>
                <col style="width: 10%;">
                <col style="width: 10%;">
                <col style="width: 10%;">
                <col style="width: 10%;">
              </colgroup>
              <tr class="live-projects">
                <th class="title-work-exp" colspan="5">Live Projects</th>
              </tr>
              {% for project in projects %}
              <tr class="work-exp-header">
                <th class="comp_name" colspan="2">{{project.company_name}}</th>
                <th class="des" colspan="3">{{project.name}}</th>
              </tr>
              {% set description = project.description %}
              {% set sentences_proj = description.split(";") %}
              {% for sentence_proj in sentences_proj %}
              <tr class="work-exp-data">
                {% if loop.first %}
                <td rowspan="{{ sentences|length }}" colspan="2">{{project.year}}</td>
                {% endif %}
                <td colspan="3"> &bull; {{ sentence_proj }}</td>
              </tr>
              {% endfor %}
              {% endfor %}
            </table>
          </div>
            """
   if "include_pos" in params:
       template += """ 
         <table>
            <tr class="live-project">
              <th id="comp_name" colspan="1">Position of Responsibility</th>
              <td id="des" colspan="4">
                <table class="live-project">
                  <colgroup>
                    <col style="width: 20%;">
                  </colgroup>
                  {% for pos_rep in position_of_responsibility %}
                  <tr>
                    <td>&bull; {{ pos_rep.name }} {{ pos_rep.year }}</td>
                  </tr>
                  {% endfor %}
                </table>
              </td>
            </tr>
            """
   if "include_soc_proj" in params:
       template += """ 
         <tr class="live-project">
              <th id="comp_name" colspan="1">Social Projects</th>
              <td id="des" colspan="4">
                <table class="live-project">
                  <colgroup>
                    <col style="width: 20%;">
                  </colgroup>
                  {% for soc_proj in Social_projects %}
                  <tr>
                    <td>&bull; {{ soc_proj.name }}</td>
                  </tr>
                  <tr>
                    <td> &nbsp; {{ soc_proj.description }}</td>
                  </tr>
                  {% endfor %}
                </table>
              </td>
            </tr>
            """
   if "include_skills" in params:
       template += """
        <tr class="live-project">
              <th id="comp_name" colspan="1">Skills</th>
              <td id="des" colspan="4">
                <table class="live-project">
                  <colgroup>
                    <col style="width: 20%;">
                  </colgroup>
                  <tr>
                    <td class="skills-container">
                      {% for sk in skills %}
                      <span class="skill-item">&bull; {{ sk.name }}</span>
                      {% endfor %}
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
      """
   if "include_res" in params:
       template += """
        <div class="section-academic-achievements">
        <table>
          <thead>
            <tr class="title-work-exp">
              <th class="title-work-exp" colspan="5">Academic Achievements</th>
            </tr>
            <tr class="live-project">
              <th id="comp_name" colspan="1"> Research Papers </th>
              <td id="des" colspan="4">
                <table class="live-project">
                  {% for res_p in research_papers %}
                  <tr>
                    <td>&bull; {{ res_p.name }}</td>
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
   if "include_res" not in params:
       template +="""
        <div class="section-academic-achievements">
                <table>
                  <thead>
                    <tr class="title-work-exp">
                      <th class="title-work-exp" colspan="5">Academic Achievements</th>
                    </tr>

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
   return template
 
# Streamlit interface
st.title(":violet[ResumeBuilder.io] :book:")
st.write(":violet[Create Resume's in few clicks!] :smile:")

st.sidebar.image("vbs-logo-removebg-preview.png", use_column_width=True)

# User inputs
st.markdown('<h1 style="color: pink; font-size: 3.4vh;">Personal Information 😎</h1>', unsafe_allow_html=True)
name = st.text_input("Full Name", key="Full Name", help="Enter your Full Name here", placeholder="Full Name")
email = st.text_input("Email", key="Email", help="Enter your Email address here", placeholder="Email Address")
phone = st.text_input("Phone", key="Phone",help="Enter your Phone number here", placeholder="Phone Number")
linkedin = st.text_input("LinkedIn URL", key="LinkedIn URL", help="Enter your LinkedIn address here", placeholder="LinkedIn URL")

# Profile Summary
st.markdown('<h1 style="color: pink; font-size: 3.4vh;">Career Objective/Profile Summary 🙂</h1>', unsafe_allow_html=True)
profile = st.text_area(" ", key="Summary", help="Write a short description about yourself", placeholder="Start typing here...")

# Education
st.markdown('<h1 style="color: pink; font-size: 3vh;">Education 🤓</h1>', unsafe_allow_html=True)
education = []
num_education = st.number_input("Number of Educational Qualifications", min_value=1, max_value=10, value=1)
for i in range(num_education):
    with st.expander(f"Education {i + 1}"):
        degree = st.text_input(f"Degree", key=f"Degree {i + 1}")
        institution = st.text_input(f"Institution", key=f"Institution {i + 1}")
        board_university = st.text_input(f"Board/University",key=f"B&U {i + 1}")
        edu_CGPA = st.text_input(f"%/CGPA", key=f"CGPA education {i + 1}")
        edu_end_date = st.text_input(f"Year", key=f"Year education{i + 1}")
        education.append({
            "degree": degree,
            "institution": institution,
            "board_university": board_university,
            "CGPA": edu_CGPA,
            "end_date": edu_end_date
        })

context = {
    "name": name,
    "email": email,
    "phone": phone,
    "linkedin": linkedin,
    "profile": profile,
    "education": education,
}

selected_params = []
# Work Experience
include_work_experience = st.checkbox("Include Work Experience 🧑‍💼")
if include_work_experience:
    st.markdown('<h1 style="color: pink; font-size: 3vh;">Work Experience 🧑‍💼</h1>', unsafe_allow_html=True)
    work_experience = []
    selected_params.append("include_work_experience")
    num_jobs = st.number_input("Number of Jobs (Please only add 4 pointers in the description)", min_value=1, max_value=10, value=1)
    for i in range(num_jobs):
        with st.expander(f"Experience {i + 1}"):
            designation = st.text_input(f"Position", key=f"Position {i + 1}")
            company_name = st.text_input(f"Company", key=f"Company {i + 1}")
            years = st.text_input(f"Total Years (Mar’24 - Jun’24) or ('Present')", key =f"years {i + 1}")
            details = st.text_area(f"Responsibilities (Separate by commas)")
            work_experience.append({
                "designation": designation,
                "company_name": company_name,
                "years": years,
                "details": details
            })
    context["work_experience"] = work_experience

include_intern_experience = st.checkbox("Include Internships 🧑‍💼")
if include_intern_experience:
    st.markdown('<h1 style="color: pink; font-size: 3vh;">Internships 🧑‍💼</h1>', unsafe_allow_html=True)
    internships = []
    selected_params.append("include_intern_experience")
    num_intern = st.number_input("Number of Internships (Only add 4 pointers in the description please)", min_value=1, max_value=10, value=1)
    for i in range(num_intern):
        with st.expander(f"Experience {i + 1}"):
            designation = st.text_input(f"Position", key=f"Position_intern{i + 1}")
            company_name = st.text_input(f"Company ", key=f"Company_intern {i + 1}")
            months = st.text_input(f"Total Months (Mar’24 - Jun’24)", key =f"months_intern {i + 1}")
            details_int = st.text_area(f"Details (Separate by semi-colon ' ; ')", key=f"Details_intern {i + 1}")
            internships.append({
                "designation": designation,
                "company_name": company_name,
                "months": months,
                "details": details_int
            })
    context["internships"] = internships

st.markdown('<h1 style="color: pink; font-size: 3.4vh;">Co-Curricular & Extra-Curricular Activities 🛠️</h1>', unsafe_allow_html=True)

# Certifications
include_certificate = st.checkbox("Include Certifications 📜")
if include_certificate:
    st.markdown('<h1 style="color: pink; font-size: 3vh;">Certifications 📜</h1>', unsafe_allow_html=True)
    certifications = []
    selected_params.append("include_certificate")
    num_certificate = st.number_input("Number of Certification", min_value=1, max_value=10, value=1)
    for i in range(num_certificate):
        with st.expander(f"Certificate {i + 1}"):
            certificate_name = st.text_input(f"Certificate Name",key=f"cert_name {i + 1}")
            certificate_year = st.text_input(f"Year",key=f"cert_year {i + 1}")
            certifications.append({
                "name": certificate_name,
                "num": num_certificate,
                "year": certificate_year
            })
    context["certifications"] = certifications

# Projects
include_projects = st.checkbox("Include Live Projects 🤝📋")
if include_projects:
    st.markdown('<h1 style="color: pink; font-size: 3vh;">Live Projects 🤝📋</h1>', unsafe_allow_html=True)
    projects = []
    selected_params.append("include_projects")
    num_projects = st.number_input("Number of Projects", min_value=1, max_value=10, value=1)
    for i in range(num_projects):
        with st.expander(f"Project {i + 1}"):
            project_name = st.text_input(f"Project Name ",key=f"Project Name {i + 1}")
            project_company = st.text_input(f"Company Name",key=f"Company Name {i + 1}")
            project_date = st.text_input(f"Project Date",key=f"Project Date {i + 1}")
            project_description = st.text_area(f"Project Description (Separate by semi-colon ' ; ')",key=f"Project Description {i + 1}")
            projects.append({
                "name": project_name,
                "date": project_date,
                "description": project_description,
                "num": num_projects,
                "company_name": project_company
            })
    context["projects"] = projects

#Position of responsibility
include_pos = st.checkbox("Include Position of Responsibility ⚜️")
if include_pos:
    st.markdown('<h1 style="color: pink; font-size: 3vh;">Position of Responsibility ⚜️</h1>', unsafe_allow_html=True)
    pos = []
    selected_params.append("include_pos")
    num_pos = st.number_input("Number of Responsibilities (Please only add 2 pointers in description per Responsibility)", min_value=1, max_value=10, value=1)
    for i in range(num_pos):
        with st.expander(f"Responsibility {i + 1}"):
            pos_name = st.text_input(f"Position",key=f"pos_name {i + 1}")
            pos_year = st.text_input(f"Year",key=f"pos_description {i + 1}")
            pos.append({
                "name": pos_name,
                "num": num_pos,
                "year": pos_year
            })
    context["position_of_responsibility"] = pos

#Social Projects
include_soc_proj = st.checkbox("Include Social Projects 🗂️")
if include_soc_proj:
    st.markdown('<h1 style="color: pink; font-size: 3vh;">Social Projects 🗂️</h1>', unsafe_allow_html=True)
    soc_proj = []
    selected_params.append("include_soc_proj")
    num_soc_proj = st.number_input("Number of Social Projects", min_value=1, max_value=10, value=1)
    for i in range(num_soc_proj):
        with st.expander(f"Social Project {i + 1}"):
            soc_proj_name = st.text_input(f"Title",key=f"soc_proj_description_title {i + 1}")
            soc_proj_description = st.text_area(f"Description",key=f"soc_proj_description {i + 1}")
            soc_proj.append({
                "name": soc_proj_name,
                "description": soc_proj_description,
                "num": num_soc_proj
            })
    context["Social_projects"] =  soc_proj

# Skills
include_skills = st.checkbox("Include Skills ⬆")
if include_skills:
    st.markdown('<h1 style="color: pink; font-size: 3vh;">Skills ⬆</h1>', unsafe_allow_html=True)
    skills = []
    selected_params.append("include_skills")
    num_sk = st.number_input("Number Skills (Please add only 4 Skills)", min_value=1, max_value=4, value=1)
    for i in range(num_sk):
        with st.expander(f"Skill {i + 1}"):
            sk_name = st.text_input(f"Name",key=f"skill_Name {i + 1}")
            skills.append({
                "name": sk_name,
                "num": num_sk
            })
    context["skills"] = skills

st.markdown('<h1 style="color: pink; font-size: 3.4vh;">Academic Achievements 🎓</h1>', unsafe_allow_html=True)

#Research Papers
include_res = st.checkbox("Include Research Papers 📇")
if include_res:
    st.markdown('<h1 style="color: pink; font-size: 3vh;">Research Papers 📇</h1>', unsafe_allow_html=True)
    res = []
    selected_params.append("include_res")
    num_res = st.number_input("Number of Research Papers", min_value=1, max_value=10, value=1)
    for i in range(num_res):
        with st.expander(f"Research Paper {i + 1}"):
            res_name = st.text_input(f"Title",key=f"res_title {i + 1}")
            res.append({
                "name": res_name,
                "num": num_res
            })
    context["research_papers"] = res

languages = st.text_area("Languages Known (Separate by commas) 🗣", key="lang", help="Enter the languages you speak here", placeholder="Languages")
context["languages"] = languages
hobbies = st.text_area("Hobbies and Interests (Separate by commas) 🎨🎮🎼", key="h/b", help="what hobbies do you have?", placeholder="Hobbies")
context["Hobbies"] = hobbies

picture_path = "vbs-logo-removebg-preview.png"

template = generate_template(selected_params)

if st.button("Generate Resume"):
    
    resume_html = generate_resume(template, context)

    if resume_html:
        # Create a ZIP file in memory
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
            # Add the HTML resume to the ZIP file
            zip_file.writestr("resume.html", resume_html)
            
            # Add the picture to the ZIP file
            with open(picture_path, "rb") as picture_file:
                zip_file.writestr("vbs-logo-removebg-preview.png", picture_file.read())
        
        # Move the buffer position to the beginning
        zip_buffer.seek(0)
        
        # Provide the ZIP file for download
        st.download_button(
            label="Download Resume (ZIP)",
            data=zip_buffer,
            file_name=f"{name}'s resume.zip",
            mime="application/zip"
            )
    if st.download_button:
            rain(
            emoji="🎈",
            font_size=54,
            falling_speed=7,
            animation_length="20 sec",
            )
            
    else:
        st.write("Error in generating Resume")

