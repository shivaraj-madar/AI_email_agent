# 📧 Agentic Gmail 
### An Autonomous Inbox Assistant powered by Llama 3.3 & LangChain

---

## 🌟 Overview

This project is a **Reasoning AI Agent** designed to automate the "boring" parts of email management. Unlike a standard script with fixed rules, this agent uses a Large Language Model (LLM) to understand the **context** of your emails and decide whether to summarize, draft replies, or suggest deletions — based on real-time analysis.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| 🧠 Brain | `Llama-3.3-70b` via [Groq Cloud](https://console.groq.com/) |
| 🔗 Framework | `LangChain` (Structured Chat Agents) |
| 📬 Nervous System | `Gmail API` (Google Cloud Console) |
| 🐍 Language | Python 3.11+ |

---

## 🚀 Key Features

- **Contextual Summarization** — Analyzes incoming mail (e.g. LinkedIn notifications) and produces 1-sentence executive summaries.
- **Autonomous Decision Making** — Distinguishes between *Noise* (spam/notifications) and *Signals* (real, actionable messages).
- **Snippet-Based Processing** — Optimized to stay under API rate limits by analyzing email metadata instead of heavy HTML bodies.
- **Dynamic Tool Use** — Intelligently calls `search_gmail`, `create_gmail_draft`, and `send_gmail_message` as needed.

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai_email_agent.git
cd ai_email_agent
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Google Cloud

1. Enable the **Gmail API** in the [Google Cloud Console](https://console.cloud.google.com/).
2. Create **OAuth 2.0 Credentials** (Desktop App type).
3. Download `credentials.json` and place it in the project root folder.

### 4. Set Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY="your_api_key_here"
```

Or export it directly in your shell:

```bash
export GROQ_API_KEY="your_api_key_here"
```

### 5. Run the Agent

```bash
python agent.py
```

On first run, a browser window will open for Gmail OAuth2 authentication. A `token.json` file will be saved locally for future sessions.

---

## 🧠 How It Works: The ReAct Loop

The agent operates on a continuous **Thought → Action → Observation** loop:

```
Thought     →  "I need to find LinkedIn emails to clean the inbox."
Action      →  Calls search_gmail(query='from:LinkedIn')
Observation →  Receives a list of email snippets.
Reasoning   →  "These are connection suggestions — noise. Flag for deletion."
Final Answer →  Delivers a summary and a draft deletion log to the user.
```

This loop repeats until the agent reaches a confident final answer, making it far more adaptable than hard-coded rule-based scripts.

---

## 🚧 Challenges Overcome

| Challenge | Solution |
|---|---|
| **Rate Limiting** | Switched to snippet-based analysis to stay within Groq's TPM/RPM limits |
| **Encoding Errors** | Resolved `cp1252` codec errors when processing special characters in email headers |
| **OAuth2 Scope Management** | Carefully scoped Gmail permissions to balance agent capability with security |

---

## 📁 Project Structure

```
ai_email_agent/
├── agent.py              # Main agent entry point
├── tools.py              # Gmail tool definitions (search, draft, send)
├── credentials.json      # OAuth2 credentials (not committed to git)
├── token.json            # Auto-generated auth token (not committed to git)
├── .env                  # Environment variables (not committed to git)
├── requirements.txt      # Python dependencies
└── README.md
```

---

## 🔒 Security Notes

- **Never commit** `credentials.json`, `token.json`, or `.env` to version control.
- Add them to `.gitignore` before your first push:

```
credentials.json
token.json
.env
```

---

## 📜 License

MIT License — Free to use, modify, and distribute. Save yourself some inbox time every morning!

---

## 🙌 Acknowledgements

- [Groq](https://groq.com/) for blazing-fast LLM inference
- [LangChain](https://www.langchain.com/) for the agent framework
- [Google Gmail API](https://developers.google.com/gmail/api) for email access
