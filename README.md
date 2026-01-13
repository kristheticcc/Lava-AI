# 🌴 Lava AI: Smart Hawaiian BBQ Assistant

Lava AI is a context-aware **AI Agent** designed for the Lava Hawaiian BBQ restaurant (hypothetical). Unlike a standard chatbot, Lava AI is connected to a live **SQLite database**, allowing it to provide real-time pricing, descriptions, and category-based recommendations using natural language.



## 🚀 Features

* **Natural Language Menu Search:** Users can ask for "Appetizers," "seafood," or specific prices.
* **Tool Calling (Agentic Workflow):** The AI autonomously decides when to query the database and when to answer from its own knowledge.
* **Fuzzy SQL Matching:** Uses `LIKE` operators to find menu items even if the user doesn't type the exact name.
* **Conditional Persona:** The bot's behavior changes dynamically (e.g., handling dessert queries with custom logic).
* **Persistent Data:** All menu items are stored in a structured SQL format for easy updates.

---

## 🛠️ Tech Stack

* **Language:** Python 3.12
* **LLM:** GPT-4.1-mini 
* **Database:** SQLite3
* **Interface:** Gradio (Web UI)
* **API:** OpenAI 

---

## 📂 Project Structure

```text
.
├── app.py                # Main Gradio application & AI logic
├── menu_tools.py         # SQL search functions & Tool schemas
├── database_manager.py   # Database initialization & Seeding
├── .env                  # Environment variables (API Keys)
└── requirements.txt      # Project dependencies
```

---

## ⚡ Quick Start
**1. Clone & Install**

```
git clone https://github.com/kristheticcc/Lava-AI.git
cd Lava-AI
pip install -r requirements.txt
```

**2. Set up your Environment**
: Create a .env file in the root directory:

```
OPENAI_API_KEY=your_actual_key_here
```

**3. Initialize the Database**

Run this once to create your lava_menu.db and seed it with items:
```
python database_manager.py
```

**4. Launch the AI**

```
python app.py
```
---
**Extra Note:** The restaurant and menu are fictional, created solely for demonstrating AI-agent capabilities with a 
live database. However, menu items and restaurant name are inspired by iLava Hawaiian BBQ's menu at https://www.ilavahawaiianbbq.com.
### 👨‍💻Author: Krish Makwana