# 📧 Cold Email Generator

An AI-powered Cold Email Generator that automatically scrapes job postings from career pages, extracts relevant information (role, experience, skills, description), matches them with your portfolio, and generates tailored cold emails for business outreach.

---

## 🚀 Features

- 🔍 **Web Scraping with LangChain** – Extracts job postings directly from a careers page URL.
- 🤖 **LLM-Powered Job Extraction** – Uses LLaMA-3 (via Groq API) to parse unstructured job data into structured JSON.
- 🧩 **Portfolio Matching** – Matches extracted skills with your personal/company portfolio stored in ChromaDB.
- ✉️ **Cold Email Generation** – Automatically generates personalized emails highlighting the most relevant portfolio projects.
- 📊 **Streamlit Web App** – Simple and interactive UI for generating emails from any job posting URL.

---

## 🛠️ Tech Stack

- [**Streamlit**](https://streamlit.io/) – Web application framework  
- [**LangChain**](https://www.langchain.com/) – Orchestration for prompts, parsing, and LLM integration  
- [**Groq (LLaMA-3-70B)**](https://groq.com/) – High-performance LLM inference  
- [**ChromaDB**](https://www.trychroma.com/) – Vector database for portfolio storage & querying  
- [**Pandas**](https://pandas.pydata.org/) – Portfolio CSV management  
- [**Python-dotenv**](https://pypi.org/project/python-dotenv/) – For secure environment variable management  

---

## 📂 Project Structure

cold-email-generator/
│── app/
│ ├── resource/
│ │ └── my_portfolio.csv # Portfolio CSV (Techstack, Links)
│── main.py # Streamlit app entry point
│── chains.py # LLM chains for job extraction & email writing
│── portfolio.py # Portfolio loading & querying logic
│── utils.py # Text cleaning helpers
│── requirements.txt # Project dependencies
│── README.md # Project documentation

yaml
Copy
Edit

---

## ⚙️ Setup & Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/cold-email-generator.git
   cd cold-email-generator
Create a virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set up environment variables
Create a .env file in the root directory:

ini
Copy
Edit
GROQ_API_KEY=your_groq_api_key_here
Prepare portfolio CSV
Update app/resource/my_portfolio.csv with your portfolio:

csv
Copy
Edit
Techstack,Links
NLP,https://github.com/yourprofile/nlp-project
Flask,https://github.com/yourprofile/webapp
Computer Vision,https://github.com/yourprofile/cv-model
▶️ Usage
Run the Streamlit app:

bash
Copy
Edit
streamlit run main.py
Enter a careers/job posting URL.

The app will scrape and clean the text.

AI extracts jobs with role, skills, description.

Portfolio projects are matched based on required skills.

A tailored cold email is generated and displayed.

📝 Example Output
Input:
https://jobs.nike.com/job/R-33460

Extracted Job:

Role: Data Scientist

Experience: 2+ years

Skills: Python, Machine Learning, SQL

Description: Work on predictive analytics and data-driven decision-making.

Generated Email:

Dear Hiring Team,
I’m Kirtirajsinh Parmar, BDE at NexaCore Solutions. We specialize in AI and software consulting...
(includes relevant portfolio links automatically)

📌 Future Enhancements
✅ Multi-URL batch processing

✅ Better portfolio ranking by semantic similarity

✅ Email template customization (formal/informal)

✅ Option to export generated emails as PDF/Word

🤝 Contributing
Contributions are welcome!
Fork the repo, make changes, and submit a PR 🚀

