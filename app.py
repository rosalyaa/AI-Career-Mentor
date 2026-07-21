import streamlit as st
import base64

from src.parser import extract_text_from_pdf
from src.extractor import extract_email, extract_phone, extract_skills
from src.career import recommend_career
from src.skill_gap import get_skill_gap
from src.roadmap import generate_roadmap
from src.scorer import calculate_score
from src.resume_score import get_resume_status

st.set_page_config(
    page_title="AI Career Mentor",
    page_icon="📄",
    layout="wide"
)

def load_image(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()


bg = load_image("assets/background.png")
logo = load_image("assets/logo.png")

st.markdown(
    f"""
<style>

.stApp {{
    background-image: url("data:image/png;base64,{bg}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

.block-container {{
    padding-top:2rem;
    padding-bottom:2rem;
}}

.main-title {{
    text-align:center;
    color:white;
    font-size:42px;
    font-weight:bold;
}}

.sub-title {{
    text-align:center;
    color:#009fc7;
    margin-bottom:30px;
}}

.section {{
    color:white;
    font-size:26px;
    font-weight:bold;
    margin-top:25px;
    margin-bottom:15px;
}}

.metric-card {{
    background:black;
    border-radius:10px;
    padding:18px;
    text-align:center;
    box-shadow:0 5px 15px rgba(0,0,0,.15);
}}

.metric-card h2 {{
    color:#009fc7;
    margin:0;
    font-size:34px;
}}

.skill-box {{
    color:white;
    border-radius:8px;
    padding:10px;
    text-align:center;
    margin-bottom:10px;
}}

</style>
""",
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <center>
        <img src="data:image/png;base64,{logo}" width="110">
    </center>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<div class='main-title'>AI Career Mentor</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Analyze your Resume and Receive AI Career Insights</div>",
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    text = extract_text_from_pdf(uploaded_file)

    email = extract_email(text)
    phone = extract_phone(text)
    skills = extract_skills(text)

    score, feedback = calculate_score(text)

    status = get_resume_status(score)

    career = recommend_career(skills)

    missing_skills = get_skill_gap(
        skills,
        career
    )

    roadmap = generate_roadmap(career)

    st.markdown(
        "<div class='section'>📊 Dashboard</div>",
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            f"""
            <div class="metric-card">
                <h2>{score}/100</h2>
                Resume Score
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="metric-card">
                <h2>{career}</h2>
                Recommended Career
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            f"""
            <div class="metric-card">
                <h2>{len(skills)}</h2>
                Skills Found
            </div>
            """,
            unsafe_allow_html=True
        )

    with c4:
        st.markdown(
            f"""
            <div class="metric-card">
                <h2>{len(missing_skills)}</h2>
                Missing Skills
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        "<div class='section'>👤 Personal Information</div>",
        unsafe_allow_html=True
    )

    info1, info2 = st.columns(2)

    with info1:
        st.info(f"📧 Email : {email}")

    with info2:
        st.info(f"📱 Phone : {phone}")

    st.markdown(
        "<div class='section'>💻 Skills Detected</div>",
        unsafe_allow_html=True
    )

    if skills:

        cols = st.columns(3)

        for i, skill in enumerate(skills):

            cols[i % 3].markdown(
                f"""
                <div class="skill-box">
                    {skill}
                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        st.warning("No skills found.")

    st.markdown(
        "<div class='section'>🎯 Recommended Career</div>",
        unsafe_allow_html=True
    )

    st.success(career)

    st.markdown(
        "<div class='section'>📚 Skill Gap Analysis</div>",
        unsafe_allow_html=True
    )

    if missing_skills:

        for skill in missing_skills:
            st.warning(f"❌ {skill}")

    else:

        st.success("No major skill gaps found.")

    st.markdown(
        "<div class='section'>🗺️ Learning Roadmap</div>",
        unsafe_allow_html=True
    )

    for week, topic in enumerate(roadmap, start=1):

        st.markdown(
            f"**Week {week} :** {topic}"
        )

    st.markdown(
        "<div class='section'>📈 Resume Score</div>",
        unsafe_allow_html=True
    )

    st.progress(score / 100)

    score_col1, score_col2 = st.columns(2)

    with score_col1:

        st.metric(
            "Overall Score",
            f"{score}/100"
        )

    with score_col2:

        st.metric(
            "Status",
            status
        )

    st.markdown(
        "<div class='section'>💡 Suggestions</div>",
        unsafe_allow_html=True
    )

    if feedback:

        for item in feedback:

            st.warning(item)

    else:

        st.success("Excellent Resume! No major improvements required.")

    st.markdown(
        "<div class='section'>📄 Extracted Resume</div>",
        unsafe_allow_html=True
    )

    st.text_area(
        "Resume Text",
        text,
        height=350
    )

else:

    st.info(
        "📄 Upload a PDF resume to begin the analysis."
    )