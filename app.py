import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
import io

st.set_page_config(page_title="AI Resume Screener", page_icon="🤖")

st.title("🤖 AI Resume Screener")
st.markdown("*Built by [Minshu Vijay](https://linkedin.com/in/minshu-vijay) | GSoC '24 | LeetCode 2000*")
st.markdown("---")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def score_resume(resume_text, job_description):
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([resume_text, job_description])
    score = cosine_similarity(vectors[0], vectors[1])[0][0]
    return round(score * 100, 2)

def get_missing_keywords(resume_text, job_description):
    jd_words = set(job_description.lower().split())
    resume_words = set(resume_text.lower().split())
    stopwords = {'the','a','an','and','or','but','in','on','at','to','for',
                 'of','with','by','from','is','are','was','were','be','been'}
    missing = jd_words - resume_words - stopwords
    return [w for w in missing if len(w) > 4][:15]

col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Upload Resume")
    uploaded_file = st.file_uploader("Upload PDF", type="pdf")

with col2:
    st.subheader("💼 Job Description")
    job_desc = st.text_area("Paste job description here", height=200)

if uploaded_file and job_desc:
    resume_text = extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    score = score_resume(resume_text, job_desc)
    missing_kw = get_missing_keywords(resume_text, job_desc)

    st.markdown("---")
    st.subheader("📊 Results")

    col3, col4 = st.columns(2)
    with col3:
        color = "green" if score > 60 else "orange" if score > 40 else "red"
        st.markdown(f"### Match Score: :{color}[{score}%]")
        if score > 60:
            st.success("✅ Strong match! Apply with confidence.")
        elif score > 40:
            st.warning("⚠️ Moderate match. Tailor your resume.")
        else:
            st.error("❌ Low match. Significant tailoring needed.")

    with col4:
        st.markdown("### 🔑 Missing Keywords")
        if missing_kw:
            for kw in missing_kw:
                st.markdown(f"- `{kw}`")
        else:
            st.success("Great keyword coverage!")

    st.markdown("---")
    with st.expander("📝 Extracted Resume Text"):
        st.text(resume_text[:2000] + "..." if len(resume_text) > 2000 else resume_text)
