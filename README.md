# 🧠 Quizzify: AI Interview Question Generator

**Quizzify** is a privacy-first, fully offline tool that generates realistic technical interview questions and answers using **local AI models**. Whether you're preparing for a **Software Engineer** or **Data Scientist** role, Quizzify tailors questions to your job role and difficulty level—all without sending your data to the cloud.

---

## 🌟 Features

- ✅ **100% Offline** – All data and AI inference run locally on your machine.
- 👩‍💻 **Role-based Q&A** – Get questions for any job role (e.g., Backend Developer, AI Engineer).
- 🎚️ **Difficulty Levels** – Choose between **Beginner** and **Advanced** modes.
- 📝 **Export to Markdown** – Save your generated questions as a `.md` file.
- 🤖 **LLM Powered** – Uses [Ollama](https://ollama.com) to run large language models locally.
- 💻 **Modern Web UI** – Clean and responsive Flask-based interface.

---

## 🧐 How It Works

1. **Prompt Loading** – Custom prompt templates are used based on the selected job role and difficulty.
2. **LLM Generation** – Sends prompts to your local LLM using Ollama.
3. **Display & Export** – Questions and answers appear in the web UI with an option to export.

---

## 🛠️ Requirements

- Python 3.8 or higher
- [Ollama](https://ollama.com) installed and added to your PATH
- Dependencies listed in `requirements.txt`

---

## ⚡ Quickstart

### 1. Clone the Repository

```bash
git clone https://github.com/Nishi-Kanta-Paul/Quizzify-AI-Interview-Question-Generator.git
cd ai_interview_generator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install & Configure Ollama

- Download Ollama: [https://ollama.com](https://ollama.com)
- Add `ollama` to your system PATH
- Test it:

```bash
ollama --version
```

- Pull a local LLM (e.g., `phi`):

```bash
ollama pull phi
```

### 4. Run the App

```bash
python app.py
```

Open in your browser:

👉 [http://localhost:5000](http://localhost:5000)

---

## 🖥️ Usage

1. Navigate to [http://localhost:5000](http://localhost:5000)
2. Input a job role (e.g., "Frontend Developer")
3. Select number of questions and difficulty
4. Click **Generate Questions**
5. Optionally, click **Download Markdown** to save your results

---

## 📁 Project Structure

```
├── app.py                 # Flask web app
├── generator.py           # Main logic for generating Q&A
├── ollama_interface.py    # Handles local LLM interactions
├── utils.py               # Helper functions
├── requirements.txt       # Python dependencies
├── prompts/
│   └── base_prompt.txt    # Prompt template for LLM
├── static/
│   └── style.css          # Styling for the UI
├── templates/
│   └── index.html         # Web UI template
└── __pycache__/           # Python cache (auto-generated)
```

---

## ❓ FAQ

**Q: Is my data sent to the cloud?**

**A:** Never. All processing happens locally via Ollama.

**Q: Can I use a different LLM model?**

**A:** Yes. Modify the model name in `ollama_interface.py` (default is `phi`).

**Q: Why is the first run slow?**

**A:** The model is downloaded and loaded into memory. Future runs are much faster.

**Q: Can I use this for non-technical roles?**

**A:** Absolutely. Just input any job title you want!

---

## 🛠 Troubleshooting

**Problem:** `ollama` not found

**Solution:**

- Ensure Ollama is installed and added to PATH
- Restart terminal after installation

**Problem:** Timeout or no response

**Solution:**

- Wait for the model to fully load
- Increase timeout in `ollama_interface.py` if necessary
- Check terminal for error messages

---

## 🤝 Contributing

We welcome contributions! Please open an issue or submit a pull request with improvements or feature suggestions.

---

## 📜 License

This project is licensed under the **MIT License**. See `LICENSE` for details.

---

## 🙏 Credits

- [Ollama](https://ollama.com) – For enabling local LLM inference
- [Flask](https://flask.palletsprojects.com) – For building the web UI
- Built with ❤️ for **privacy-conscious** interview preparation
