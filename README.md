🧠 Quizzify: AI Interview Question Generator

Quizzify is a privacy-first, offline tool that generates realistic technical interview questions and answers for any job role using local AI models. Choose your role, set the difficulty, and get instant, context-aware questions—no internet or cloud required.

🌟 Features

- 100% Offline: All processing is local—your data never leaves your computer.
- Role-based Q&A: Generate questions for any job role (e.g., Data Scientist, Software Engineer).
- Difficulty Modes: Choose Beginner or Advanced for tailored questions and answers.
- Save to Markdown: Download your generated questions as a Markdown file.
- LLM Powered: Uses Ollama to run large language models locally.
- Modern Web UI: Clean, responsive interface for easy interaction.

🧐 How It Works

1. Prompt Template: Loads a customizable prompt for your selected job role and settings.
2. LLM Generation: Sends the prompt to a local LLM (via Ollama) for question and answer generation.
3. Output: Displays the results in the web UI and allows you to save them as a Markdown file.

🛠️ Requirements

- Python 3.8 or higher
- Ollama (for local LLM inference)
- See requirements.txt for Python dependencies

⚡ Quickstart

Clone the repository:

```sh
git clone https://github.com/Nishi-Kanta-Paul/Quizzify-AI-Interview-Question-Generator.git
cd ai_interview_generator
```

Install Python dependencies:

```sh
pip install -r requirements.txt
```

Install Ollama and add to PATH:

- Download from [Ollama.com](https://ollama.com/)
- Make sure `ollama` runs from your terminal (test with `ollama --version`)
- Pull a model (e.g., `phi`):
  ```sh
  ollama pull phi
  ```

Run the app:

```sh
python app.py
```

Open your browser: Go to http://localhost:5000

�️ Usage

Web App

- Go to http://localhost:5000
- Enter a job role, number of questions, and select mode
- Click "Generate Questions"
- Optionally, save the questions to a Markdown file

🧩 Project Structure

├── app.py # Flask web app
├── generator.py # Generates questions using Ollama
├── ollama_interface.py # LLM interaction
├── utils.py # Utility functions
├── requirements.txt # Python dependencies
├── prompts/
│ └── base_prompt.txt # Prompt template
├── static/
│ └── style.css # App styling
├── templates/
│ └── index.html # Web UI
└── **pycache**/ # Python cache (gitignored)

� Troubleshooting

Ollama not found?

- Make sure Ollama is installed and its directory is in your system PATH.
- Restart your terminal after installation.

No response or timeout?

- The first run may take longer as the model is downloaded and loaded.
- Increase the timeout in `ollama_interface.py` if needed.
- Check for errors in the terminal where you started the Flask app.

❓ FAQ

**Q: Is my data sent to the cloud?**  
A: No. All processing is local. Your job roles and questions never leave your machine.

**Q: Can I use my own LLM model?**  
A: Yes! You can change the model name in `ollama_interface.py` (default is `phi`).

**Q: Why is it slow the first time?**  
A: The model may need to be downloaded and loaded into memory. Subsequent runs are faster.

**Q: Can I use this for non-technical roles?**  
A: Yes! Just enter any job role you want.

🤝 Contributing

Pull requests and suggestions are welcome! Please open an issue or submit a PR.

📜 License

This project is licensed under the MIT License.

🙏 Credits

Ollama for local LLM serving  
Flask  
Made with ❤️ for privacy-conscious interview preparation.
