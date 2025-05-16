# 🤖 RAG-Based YouTube Transcript Chatbot

Ask intelligent questions from any **YouTube video** using its transcript — powered by **LangChain**, **Google Gemini**, **FAISS**, and a modern **Streamlit frontend**.
Built with a clean **modular Python backend**, complete with **CI/CD**, **auto-deployment**, and **pre-commit quality gates**.

---

## 🎯 Features

- ✅ Paste a YouTube video link
- ✅ Automatically fetch transcript (with fallback handling)
- ✅ RAG-powered answers using context-aware generation
- ✅ Persistent conversation history for each video
- ✅ Modular backend with clean directory structure
- ✅ Chat-bubble styled frontend with Streamlit
- ✅ Auto-deploys to Streamlit Cloud on every push
- ✅ Linting, formatting, secret detection via pre-commit
- ✅ CI checks via GitHub Actions (Black, Flake8, YAML, Secrets)

---

## 🛠️ Tech Stack

- [LangChain](https://www.langchain.com/)
- [Google Gemini 1.5 Flash](https://deepmind.google/technologies/gemini/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Streamlit](https://streamlit.io/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [pre-commit](https://pre-commit.com/)

---

## 🚀 Deployment (Streamlit Cloud)

This app is continuously deployed via [Streamlit Cloud](https://streamlit.io/cloud).

---

## ⚙️ Local Development

```bash
# 1. Clone the repo
git clone https://github.com/torqbit13/rag-youtube-chatbot.git
cd rag-youtube-chatbot

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your environment variables
touch .env
echo "GOOGLE_API_KEY=your-api-key-here" >> .env

# 5. Run the app
streamlit run app/main.py
```

---

## 🔒 Pre-commit Hooks

We use [pre-commit](https://pre-commit.com/) to maintain code quality and consistency.

```bash
# Install pre-commit hooks
pre-commit install

# Run all hooks manually
pre-commit run --all-files
```

### ✅ Included Hooks

- `black` (code formatter)
- `flake8` (linter)
- `trailing-whitespace`, `end-of-file-fixer`
- `check-yaml`, `debug-statements`
- `detect-secrets` (detects accidental secrets in commits)

---

## ✅ CI/CD with GitHub Actions

Every push to `main` or any `feature/*` branch automatically runs:

- 🔧 Dependency install
- 🎨 Code formatting check via `black`
- 🕵️ Linting via `flake8`
- 🧾 YAML syntax validation
- 🔐 Secret detection via `detect-secrets`
- 🚀 Auto-deployment to Streamlit Cloud (if linked)

---

## 💬 Chat Flow Example

```text
[User]  Paste a YouTube URL
[Bot]   Fetches and splits transcript
[User]  "What’s the main argument in this video?"
[Bot]   Answers using retrieved context via Gemini
[User]  "Can you summarize the ending?"
[Bot]   Responds based on follow-up + chat history
```

---

## 📌 Limitations

- 🚫 YouTube may block cloud IPs (can be handled via proxy or local dev)
- 🔐 Requires a valid Gemini API key
- 📼 Videos must have transcripts (or allow user-uploaded transcripts)

---

## 📣 Contributing

Pull requests are welcome!

```bash
# Before committing, ensure code is clean
pre-commit run --all-files
```

---

## 🔗 Live App

🌐 [Streamlit App Link](https://chat-ai-youtube.streamlit.app/)

---

## 👤 Author

Made with ❤️ by **Aseem Chemjong Limbu**
GitHub → [@torqbit13](https://github.com/torqbit13)
