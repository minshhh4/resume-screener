AI Resume Screener

An NLP-powered tool that scores how well a resume matches 
a job description — and tells you exactly what's missing.

🔗 [Live Demo](https://minshu-resume-screener.streamlit.app)**

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![NLP](https://img.shields.io/badge/NLP-TF--IDF-green)

---

 What It Does

- Upload any resume as PDF
- Paste a job description
- Get an instant match score (0-100%)
- See missing keywords to optimize your resume
- Color-coded feedback (strong / moderate / weak match)

---

 How It Works

Uses **TF-IDF vectorization** and **cosine similarity** to 
semantically compare resume content against job requirements.
Extracts and ranks missing keywords to guide resume optimization.

---

 Tech Stack

- Python 3.8+
- Streamlit (UI)
- Scikit-learn (TF-IDF + Cosine Similarity)
- PyPDF2 (PDF text extraction)

---

 Run Locally

```bash
git clone https://github.com/minshhh4/resume-screener
cd resume-screener
pip install -r requirements.txt
streamlit run app.py
```

---

 Author

**Minshu Vijay** | GSoC '24 | LeetCode Max 2000 | ICPC Algo Queen
- LinkedIn: [linkedin.com/in/minshu-vijay](https://linkedin.com/in/minshu-vijay)
- GitHub: [github.com/minshhh4](https://github.com/minshhh4)
- Live App: [minshu-resume-screener.streamlit.app](https://minshu-resume-screener.streamlit.app)
