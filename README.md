# IRES

> **An Intelligent AI-Powered Desktop Assistant for Windows**

IRES is an open-source desktop voice assistant built with Python that enables users to interact with their computer using natural language voice commands. It combines speech recognition, text-to-speech, AI capabilities, and desktop automation into a modular and extensible architecture.

The long-term vision of IRES is to evolve from a simple voice assistant into a fully featured AI-powered desktop companion capable of automating everyday tasks, managing files, interacting with applications, and assisting users through natural conversation.

---

## ✨ Features

### Current Features

- 🎤 Voice Recognition
- 🔊 Text-to-Speech
- 🌐 Open Websites
- 🔍 Google Search
- 🤖 AI-Powered Responses (OpenAI)
- 💾 Save AI Conversations
- 🖥 Launch Desktop Applications
- 🎯 Smart Command Parsing
- 🔎 Fuzzy Command Matching
- 📁 Modular Project Architecture

---

## 🚀 Planned Features

- Smart Installed Application Discovery
- File & Folder Search
- Open Documents using Voice
- Conversation Memory
- Wake Word Detection ("Hey IRES")
- GUI Interface
- Plugin System
- Clipboard Manager
- Reminder System
- Weather Information
- Calendar Integration
- Email Automation
- Desktop Automation
- Local AI Model Support (Ollama)
- PDF Chat
- Image Understanding

---

# 🏗 Project Structure

```
IRES/
│
├── commands/
│   ├── apps.py
│   ├── browser.py
│   ├── search.py
│   └── system.py
│
├── utils/
│   ├── parser.py
│   ├── app_finder.py
│   └── app_index.py
│
├── cache/
│   └── apps.json
│
├── ai.py
├── speech.py
├── config.py
├── command_processor.py
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚙ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.10+ |
| Speech Recognition | SpeechRecognition |
| Text To Speech | pyttsx3 |
| AI | OpenAI API |
| Environment Variables | python-dotenv |
| Data Storage | JSON |
| Version Control | Git & GitHub |

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/IRES.git
```

Move into the project directory

```bash
cd IRES
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
OPENAI_API_KEY=your_api_key_here
```

Run the assistant

```bash
python main.py
```

---

# 📌 Roadmap

| Version | Status |
|----------|--------|
| v0.1 | ✅ Basic Voice Assistant |
| v0.2 | ✅ Modular Architecture |
| v0.3 | ✅ Smart Command Parser |
| v0.4 | 🚧 Smart Application Discovery |
| v0.5 | 📅 File & Folder Management |
| v0.6 | 📅 Conversation Memory |
| v0.7 | 📅 GUI Interface |
| v0.8 | 📅 Plugin System |
| v0.9 | 📅 Desktop Automation |
| v1.0 | 🎯 Intelligent Desktop Assistant |

---

# 🎯 Vision

IRES aims to become a powerful AI desktop assistant capable of understanding natural language, interacting with desktop applications, automating repetitive tasks, and assisting users in their daily computing activities.

The project emphasizes clean software architecture, modular design, scalability, and practical desktop automation.

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve IRES:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub.

It helps the project grow and motivates future development.