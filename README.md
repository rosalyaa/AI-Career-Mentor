<h1>AI Career Mentor</h1>
AI Career Mentor is a web-based resume analysis application built using Python and Streamlit. It extracts key information from resumes, evaluates resume quality, recommends suitable career paths, identifies skill gaps, and generates a personalized learning roadmap to help users improve their employability.

<h2>Demo:</h2> 

[http://localhost:8502](http://localhost:8502)

<h2>1. Features:</h2>

- Resume Upload
- Resume Score
- Skill Extraction
- Career Recommendation
- Skill Gap Analysis
- Learning Roadmap

<h2>2. Technologies Used:</h2>

- Python
- Streamlit
- HTML
- CSS
- PyMuPDF
- Regex


<h2>3. Project Structure:</h2>


AI-Career-Mentor/

1. app.py
   <br>
2. requirements.txt
   <br>
3. README.md
   <br>
4. assets/
   <br>
     (a) background.png
   <br>
     (b) logo.png
   <br>
6. src/
   <br>
     (a) parser.py
   <br>
     (b) extractor.py
   <br>
     (c) scorer.py
   <br>
     (d) resume_score.py
   <br>
     (e) career.py
   <br>
     (f) skill_gap.py
   <br>
     (g) roadmap.py
   <br>
     (h) analyzer.py
   <br>
     (i) report.py
   <br>
     (j) chart.py
   <br>                         
7. data/
   <br>
     (a) skills.csv
   <br>    
8. sample_resume/
   <br>
     (a) Resume.pdf
   <br>        
9. images/
    <br>
     (a) screenshots/
   <br>
10. notebooks/
    <br>
     (a) experimentation.ipynb
    <br>
11. models/                  
<br>
12. reports/                  
<br>
13. .gitignore                

<h2>4. Installation:</h2>

- Clone the repository: git clone https://github.com/rosalyaa/AI-Career-Mentor.git
- Navigate to the project directory: cd AI-Career-Mentor
- Create a virtual environment: python -m venv .venv
- Activate it
(macOS/Linux): source .venv/bin/activate 
(Windows): .venv\Scripts\activate
- Install dependencies: pip install -r requirements.txt
- Launch the application:streamlit run app.py
- Open your web browser and visit: http://localhost:8502



<h2>5. How It Works:</h2>
- Upload Resume: User uploads a resume in PDF format through the Streamlit interface.
<br>
- Resume Parsing: The application extracts the text from the uploaded PDF using PyMuPDF.
<br>
- Information Extraction: Email address, phone number, and technical skills are identified using regular expressions(re) and a predefined skills database.
<br>
- Resume Evaluation: The resume is analyzed for essential sections such as Education, Skills, Projects, Experience, and Certifications to calculate a resume score and generate improvement suggestions.
<br>
- Career Recommendation: Based on the extracted skills, the application recommends the most suitable career path.
<br>
- Skill Gap Analysis: The detected skills are compared with the required skills for the recommended career to identify missing competencies.
<br>
- Learning Roadmap: A personalized week-by-week learning roadmap is generated to help users acquire the missing skills and prepare for their target career.
<br>
- Results Dashboard: Resume Score, Recommended Career, Skills Detected, Missing Skills, Resume Suggestions, Personalized Learning Roadmap, Extracted Resume Text

<h2>6. Future Improvements</h2>
- Add ATS compatibility checking.
- Support DOCX and image-based resumes.
- Recommend online courses based on skill gaps.
- Generate altered resumes and cover letters.
- Integrate real-time job recommendations from job portals.
- Deploy the application on a cloud platform for public access.


<h2>7. Learning Outcomes</h2>

Through this project I learned:
- Developed a web application using Python and Streamlit.
- Learned PDF text extraction and data processing techniques.
- Implemented resume analysis and rule-based career recommendations.
- Applied HTML and CSS to design an interactive user interface.
- Gained experience with Git, GitHub, and project deployment workflows.


Author: Rosalya Gabriel,
        Computer Science Engineering Student

GitHub: https://github.com/rosalyaa
