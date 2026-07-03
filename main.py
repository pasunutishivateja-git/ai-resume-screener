from flask import Flask, render_template, request
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2  # <-- New import for handling PDFs

nltk.download('stopwords', quiet=True)

app = Flask(__name__)

# --- 1. NEW FUNCTION: EXTRACT PDF TEXT ---
def extract_text_from_pdf(pdf_file):
    """Reads a PDF file object and extracts all text."""
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        # Extract text from each page and add it to our string
        extracted = page.extract_text()
        if extracted:
            text += extracted
    return text

# --- 2. YOUR CORE NLP LOGIC (Unchanged) ---
def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def calculate_match(resume, job_desc):
    clean_res = clean_text(resume)
    clean_jd = clean_text(job_desc)
    
    vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'))
    tfidf_matrix = vectorizer.fit_transform([clean_res, clean_jd])
    match_score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
    
    return round(match_score * 100, 2)

# --- 3. THE WEB ROUTE (Updated for Files) ---
@app.route("/", methods=["GET", "POST"])
def home():
    match_score = None
    
    if request.method == "POST":
        # Get the job description text
        job_desc = request.form.get("job_desc")
        
        # Get the uploaded file
        resume_file = request.files.get("resume")
        
        # Check if both exist and if the file is a PDF
        if job_desc and resume_file and resume_file.filename.endswith('.pdf'):
            
            # Convert the PDF into a single string of text
            resume_text = extract_text_from_pdf(resume_file)
            
            # Run the matching algorithm
            match_score = calculate_match(resume_text, job_desc)

    return render_template("index.html", score=match_score)

if __name__ == "__main__":
    app.run(debug=True)