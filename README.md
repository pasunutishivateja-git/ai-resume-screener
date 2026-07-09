# 🚀 AI-Powered Resume Screener

**Live Demo:** [View the Application Here](https://ai-resume-screener-1vtu.onrender.com)

## 📌 Overview
The AI-Powered Resume Screener is a full-stack web application designed to streamline the recruitment process. It uses Natural Language Processing (NLP) to analyze the semantic similarity between a given job description and a candidate's resume (uploaded as a PDF), outputting a precise percentage match. 

This project demonstrates an end-to-end Machine Learning engineering pipeline: from unstructured data ingestion and text preprocessing to mathematical vectorization and full-scale cloud deployment.

## ✨ Features
* **PDF Processing:** Automatically extracts and parses text from uploaded `.pdf` documents using `PyPDF2`.
* **Advanced NLP Pipeline:** Cleans noise, tokenizes text, and removes stop-words using standard natural language processing techniques.
* **Mathematical Semantic Matching:** Utilizes TF-IDF and Cosine Similarity to evaluate the alignment between a candidate's skills and the job requirements.
* **Interactive UI/UX:** Clean, responsive, custom-built HTML/CSS front-end tailored for ease of use.
* **Cloud Deployed:** Fully hosted and accessible via a live URL using a Flask backend and Gunicorn WSGI server.

## 🛠️ Tech Stack
* **Backend:** Python, Flask, Gunicorn
* **Machine Learning & NLP:** Scikit-learn, NLTK
* **Data Processing:** PyPDF2, Regular Expressions (Regex)
* **Frontend:** HTML5, CSS3
* **Deployment:** Render, GitHub

## 🧠 How It Works (The Core Logic)

### 1. Text Sanitization
Raw text from both the job description and the resume is standardized. URLs, special characters, and punctuation are stripped using Regular Expressions to prevent non-alphanumeric noise from skewing the results.

### 2. Tokenization & Stop-word Removal
Using the `NLTK` library, the cleaned strings are chopped into individual word tokens. Common filler words (e.g., "the", "and", "is") are removed, condensing the data into purely semantic keywords.

### 3. TF-IDF Vectorization
The application converts the filtered text into mathematical vectors using Term Frequency-Inverse Document Frequency (TF-IDF). This algorithm assigns higher weights to unique, domain-specific keywords and lower weights to common terms.

$$TF = \frac{\text{Count of word in document}}{\text{Total words in document}}$$
$$IDF = \log\left(\frac{\text{Total documents}}{\text{Documents containing word}}\right)$$

### 4. Cosine Similarity Measurement
Once vectorized, the model calculates the Cosine Similarity between the Resume Vector and the Job Description Vector. Instead of measuring straight-line distance, this calculates the geometric angle between the vectors to determine how closely their semantic meanings align.

$$\text{Cosine Similarity} = \frac{A \cdot B}{||A|| \times ||B||}$$

## 💻 Local Installation & Setup
If you wish to run this project locally on your machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/ai-resume-screener.git](https://github.com/YOUR_GITHUB_USERNAME/ai-resume-screener.git)
   cd ai-resume-screener
