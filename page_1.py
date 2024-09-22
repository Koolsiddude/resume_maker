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
        padding: 10px;
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
          font-size: 12px;
          margin: 0;
          padding: 8px;
        }
        .education-data td{
          border: 1px solid #000;
          padding: 8px;
          text-align: center;
          font-size: 12px;
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
      }
      
      .work-exp-header th,
      .title-work-exp th,
      td {
        border: 1px solid #000;
        padding: 10px;
        text-align: center;
        font-size: 12px;
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
        background-color: #c7cfeb;
      }
      .title-work-new {
        background-color: #c7cfeb;
        padding:0;
        text-align: center;
        font-size: 15px;
        margin: 0;
      }
      .title-work-new-proj {
        background-color: #f2f2f2;
        padding:0;
        text-align: center;
        font-size: 15px;
        margin: 0;
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
        background-color: #f2f2f2;
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
      .live-projects th{
        border: 1px solid #000;
        background-color: #f2f2f2;
        padding: 8px;
        text-align: center;
        font-size: 12px;
        margin: 0;
        border-collapse: collapse;
      }
      .skills th{
        border: 1px solid #000;
        padding: 8px;
        text-align: left;
        font-size: 12px;
        margin: 0;
        border-collapse: collapse;
      }
      .skills td :first-child{
        border: 0px;
        padding: 8px;
        text-align: left;
        font-size: 12px;
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
        <tr class="title-work-new">
        {% for work_exp in work_experience %}
        <th class="title-work-new" colspan="5">Work Experience</th>
        </tr>
        <tr class="work-exp-header">
        <th class="comp_name" colspan="2">{{work_exp.company_name}}</th>
        <th class="des" colspan="3">{{work_exp.designation}}</th>
        </tr>
        <tr class="work-exp-data">
        <td colspan="2">{{work_exp.years}}</td>
        <td colspan="3">
        {% set details_work = work_exp.details %}
        {% set sentences_work = details_work.split(";") %}
        {% for sentence_work in sentences_work %}
        &bull; {{sentence_work}}<br>
        {% endfor %}
        </td>
        </tr>
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
        <tr class="title-work-new">
        <th class="title-work-new" colspan="5">Internships</th>
        </tr>
        {% for intern in internships %}
        <tr class="work-exp-header">
        <th class="comp_name" colspan="2">{{intern.company_name}}</th>
        <th class="des" colspan="3">{{intern.designation}}</th>
        </tr>
        <tr class="work-exp-data">
        <td colspan="2">{{intern.months}}</td>
        <td colspan="3"> 
        {% set details = intern.details %}
        {% set sentences = details.split(";") %}
        {% for sentence in sentences %}
        &bull; {{sentence}}<br>
        {% endfor %}
        </td>
        </tr>
        {% endfor %}
        </table>
        </div>
        <div class="section-extra_activities">
        <table>
        <tr class="title-work-new">
        <th class="title-work-new" colspan="5">
        Co-Curricular & Extra-Curricular Activities
        </th>
        </tr>
        <tr class="live-project">
            <th id="comp_name" colspan="1">Certifications</th>
            <td id="des" colspan="4">
              <table class="live-project">
                <colgroup>
                  <col style="width: 20%;">
                </colgroup>
                <tr>
                  <td> 
                    {% for cert in certifications %}
                    &bull; {{ cert.name }} {{ cert.year }}<br>
                    {% endfor %}
                  </td>
                </tr>
              </table>
            </td>
          </tr>
      </table>
      <div class="section-liveprojects">
        <table>
          <colgroup>
            <col style="width: 10%;">
            <col style="width: 10%;">
            <col style="width: 10%;">
            <col style="width: 10%;">
          </colgroup>
          <tr class="title-work-new-proj">
            <th class="title-work-new-proj" colspan="5">Live Projects</th>
          </tr>
          {% for project in projects %}
          <tr class="work-exp-header">
            <th class="comp_name" colspan="2">{{project.company_name}}</th>
            <th class="des" colspan="3">{{project.name}}</th>
          </tr>
          <tr class="work-exp-data">
            <td colspan="2">{{project.date}}</td>
            <td colspan="3"> 
              {% set description = project.description %}
              {% set sentences_proj = description.split(";") %}
              {% for sentence_proj in sentences_proj %}
              &bull; {{ sentence_proj }}<br>
              {% endfor %}
            </td>
          </tr>
          {% endfor %}
        </table>
      </div>
      <table>
        <tr class="live-project">
          <th id="comp_name" colspan="1">Position of Responsibility</th>
          <td id="des" colspan="4">
            <table class="live-project">
              <colgroup>
                <col style="width: 20%;">
              </colgroup>
              <tr>
                <td>
                  {% for pos_rep in position_of_responsibility %}
                  &bull; {{ pos_rep.name }} {{ pos_rep.year }}<br>
                  {% endfor %}
                </td>
              </tr>
            
            </table>
          </td>
        </tr>
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
          <div class="section-academic-achievements">
            <table>
              <thead>
                <tr class="title-work-new">
                  <th class="title-work-new" colspan="5">Achievements</th>
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
                  <tr class="live-project">
                    <th id="comp_name" colspan="1"> Scholarships</th>
                    <td id="des" colspan="4">
                      <table class="live-project">
                        {% for sc in scholarships %}
                        <tr>
                          <td>&bull; {{ sc.name }}</td>
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
            <div class="section-academic-achievements">
                <table>
                    <thead>
                      <tr class="title-work-new">
                        <th class="title-work-new" colspan="5">&nbsp;</th>
                      </tr>
            </div>
            </div>
            </div>
            </body>
            </html>
