# 🚀 AI Web Scraper

An AI-powered web scraping and content extraction tool built with Streamlit and Python. This application enables users to input any webpage URL, retrieve and clean its DOM content, and dynamically extract structured insights using advanced language models.

## ✨ Features

- **🌐 Dynamic Web Scraping:**
Input any URL to fetch and display its DOM structure using robust scraping logic.
- **🧹 Content Cleaning \& Filtering:**
Automated cleaning of extracted HTML to isolate textual content for further analysis.
- **🤖 AI-Powered Extraction:**
Integrates Ollama models with LangChain to parse, summarize, and extract specific insights from large webpage contents based on user-defined tasks.
- **🧩 Chunk-Based Parsing:**
Efficiently handles large DOM content by automatically chunking input for accurate AI processing.
- **⏳ Progress Updates:**
Real-time feedback in the Streamlit app as each stage of scraping and parsing completes.


## 🛠️ Tech Stack

Python, Streamlit, Ollama, LangChain, BeautifulSoup, Requests

## 📦 Key Modules

- `ai_scraper.py`: Main Streamlit web application interface.
- `content.py`: URL fetching, content cleaning, and chunking utilities.
- `parse.py`: Integration with Ollama models via LangChain for AI-driven parsing and structured extraction.
- `requirements.txt`: Python dependencies for easy setup.


## ⚡ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/ai-web-scraper.git
cd ai-web-scraper
```

2. **(Optional) Create a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Install Ollama models:**
Visit [Ollama](https://ollama.com/) or use:

```bash
ollama run llama3.2:1b
```

Ensure the correct model is referenced in `parse.py`.

## ▶️ Usage

1. **Start the Streamlit app:**

```bash
streamlit run ai_scraper.py
```

2. **Steps:**
    - Enter the target URL in the app’s input box.
    - Scrape the webpage content.
    - View/filter the DOM content.
    - Provide user instructions for AI-powered parsing.
3. **Results:**
See extraction and status updates in real-time.

## 🧑💻 Customization

- Swap or extend language models in `parse.py` for new use-cases.
- Adapt the scraper for headless browser logic as needed.


## 📸 Example Screenshot

![App Screenshot](./AISCRAPER.png)

## 📄 License

This project is open for educational use and as a starter for your own AI scraping solutions.
