# Project Lunatic

**Project Lunatic** is a dark-themed AI chatbot web app created using **Flask** and **Gemini 1.5 Flash**, built with user login, per-user chat history, Tailwind CSS UI, and GPT-level replies via Google’s LLM.

> **“Project Lunatic: The most probable chat to enlightenment.”**

---

## 👨‍💻 Author

- [Kamogelo Baloyi](https://github.com/Vlad64-prog)

---

## ⚠️ Gemini API Notice

This app relies on Google’s **Gemini 1.5 Flash** model. Usage is **token-limited** — if you exceed the quota, you’ll start getting:

- `Error 429` (Too Many Requests)  
- `Error 401` (Invalid credentials)  
- Or no replies at all  

It’s like summoning a demon. The more you ask, the more mana it consumes.

---

## 🔐 .env Secrets (Important)

All sensitive keys (like your Gemini API Key and Flask secret) are stored in a `.env` file.

**Already configured if you cloned this project.**

However, if you're modifying or deploying it yourself, create a file `.env` at the root and paste:

```env
GEMINI_API_KEY=your_actual_gemini_api_key
SECRET_KEY=any_random_secure_string
```

---

## 🔖 Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Made with Flask](https://img.shields.io/badge/Made%20with-Flask-blue.svg)](https://flask.palletsprojects.com/)
[![TailwindCSS](https://img.shields.io/badge/UI-TailwindCSS-38B2AC?logo=tailwindcss)](https://tailwindcss.com/)
[![Gemini API](https://img.shields.io/badge/API-Google%20Gemini-blueviolet)](https://ai.google.dev/)

---

## 💻 Tech Stack

| Layer        | Technology              |
|--------------|--------------------------|
| Frontend     | HTML, Tailwind CSS       |
| Backend      | Python (Flask)           |
| AI Engine    | Google Gemini API        |
| Auth System  | Flask Session + JSON     |
| Storage      | users.json + chat logs   |

---

## 🎯 Features

- 🧠 Gemini AI Chatbot integration  
- 🔐 Register & Login system  
- 💬 Per-user chat history  
- 🎨 Tailwind CSS themed divine dark UI  
- 📂 Flask-based full stack integration  
- 🚪 Logout functionality  
- 📱 Responsive page layouts  

---

## 🧾 UI Pages

| Page Name      | Purpose                        | Background Image        |
|----------------|--------------------------------|--------------------------|
| `home.html`    | Intro with "Begin" CTA         | `/static/images/PL0.png` |
| `login.html`   | Secure login                   | `/static/images/PL2.png` |
| `register.html`| New account creation           | `/static/images/PL1.png` |
| `index.html`   | Chat interface (main feature)  | `/static/images/PL.png`  |

---

## 📦 Project Folder Structure

```
projectlunatic/
├── static/
│   └── images/
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   └── index.html
├── chat_logs/
│   └── [username].txt
├── users.json
├── .env
├── .gitignore
├── app.py
└── README.md
```

---

## 🎨 Color Reference

| Name             | Hex Code                                                       |
|------------------|----------------------------------------------------------------|
| Divine Black     | ![#0a0a0a](https://via.placeholder.com/10/0a0a0a?text=+) `#0a0a0a` |
| Ghost White      | ![#f8f8f8](https://via.placeholder.com/10/f8f8f8?text=+) `#f8f8f8` |
| Celestial Cyan   | ![#00d1a0](https://via.placeholder.com/10/00d1a0?text=+) `#00d1a0` |
| Divine Green     | ![#00b48a](https://via.placeholder.com/10/00b48a?text=+) `#00b48a` |

---

## 📡 API Reference

### 🔹 Gemini 1.5 Flash Endpoint

```http
POST https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=YOUR_API_KEY
```

### 🔸 Example Payload

```json
{
  "contents": [
    {
      "parts": [
        { "text": "What's the meaning of life?" }
      ]
    }
  ]
}
```

| Parameter   | Type     | Description                           |
|-------------|----------|---------------------------------------|
| `key`       | string   | Your Gemini API key (from `.env`)     |
| `contents`  | array    | User prompts in LLM-supported format  |

---

## 🛠 Installation Guide

To run **Project Lunatic** locally, follow these steps:

### 1. Clone the repo

```bash
git clone https://github.com/your-username/projectlunatic.git
cd projectlunatic
```

---

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows
```

---

### 3. Install dependencies

```bash
pip install flask requests python-dotenv
```

---

### 4. Create `.env` file

If not already present, create a `.env` file in the root and add:

```env
GEMINI_API_KEY=your_actual_key
SECRET_KEY=random_secure_string
```

---

### 5. Run the app

```bash
python app.py
```

Then go to [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 📸 Demo

*(Insert demo GIF or screen recording here)*

---

## 🪪 License

This project is under the [MIT License](https://choosealicense.com/licenses/mit/)

---

## 🤝 Contributing

If you're a fellow lunatic with visions of enlightenment, feel free to fork and tweak.

PRs are welcome. Just don’t break the veil of reality too hard.

---