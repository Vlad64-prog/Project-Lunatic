from flask import Flask, render_template, request, redirect, session, url_for
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

API_KEY = os.getenv("GEMINI_API_KEY")
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

USERS_FILE = "users.json"#Where user credentials are stored (in plain text, yikes).
CHAT_LOG_DIR = "chat_logs"#Directory for chat histories.

if not os.path.exists(CHAT_LOG_DIR):
    os.makedirs(CHAT_LOG_DIR)#Create the chat log directory if it doesn't exist.

##USER & CHAT UTILITIES##
def load_users():
    if not os.path.exists(USERS_FILE):
        return {}#No users file?Start fresh.
    with open(USERS_FILE, "r") as f:
        return json.load(f)#Load existing users.

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)#Save user data.Pretty simple.

def save_chat(username, user_msg, bot_reply):
    path = os.path.join(CHAT_LOG_DIR, f"{username}.txt")
    with open(path, "a") as f:
        f.write(f"You: {user_msg}\nLunatic: {bot_reply}\n\n")#Append chat to user's log.

def load_chat_history(username):
    path = os.path.join(CHAT_LOG_DIR, f"{username}.txt")
    if not os.path.exists(path):
        return ""#No chat history yet, nothing to load.
    with open(path, "r") as f:
        return f.read()#Load the entire chat history.

##Home Page##
@app.route("/")
def home_page():
    return render_template("home.html")#Just the basic home page.

##Login##
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users = load_users()

        #Check credentials.This is where the magic (or failure) happens.
        if username in users and users[username]["password"] == password:
            session["username"] = username
            return redirect(url_for("chat"))#Success!Off to the chat.
        return "Invalid credentials."#Oops, wrong username or password.
    return render_template("login.html")#Show the login form.

##Register##
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users = load_users()

        if username in users:
            return "Username already exists."#Can't have two of the same, sorry.

        users[username] = {"password": password}
        save_users(users)#New user, new entry.
        return redirect(url_for("login"))#Back to login, now that they're registered.
    return render_template("register.html")#Show the registration form.

##Logout##
@app.route("/logout")
def logout():
    session.pop("username", None)#Clear the session.Goodbye!
    return redirect(url_for("login"))#Back to the login page.

##Chat Page(index)##
@app.route("/chat", methods=["GET", "POST"])
def chat():
    if "username" not in session:
        return redirect(url_for("login"))#Gotta be logged in to chat with Lunatic.

    response_text = ""
    user_input = ""
    chat_history = load_chat_history(session["username"])#Load past conversations.

    if request.method == "POST":
        user_input = request.form["user_input"]

        headers = {"Content-Type": "application/json"}
        payload = {
            "contents": [
                {"parts": [{"text": user_input}]}
            ]
        }

        try:
            #Making the call to the Gemini API.Fingers crossed for a good response.
            res = requests.post(API_URL, headers=headers, data=json.dumps(payload))
            if res.status_code == 200:
                data = res.json()
                response_text = data["candidates"][0]["content"]["parts"][0]["text"]
                save_chat(session["username"], user_input, response_text)#Save this epic conversation.
                chat_history = load_chat_history(session["username"])#Reload to show new entry.
            else:
                response_text = f"Error {res.status_code}: {res.text}"#API error, lovely.
        except Exception as e:
            response_text = f"Exception: {e}"#Something went really wrong.

    return render_template("index.html", user_input=user_input, response=response_text, chat_history=chat_history)#Render chat page with updated info.

if __name__ == "__main__":
    app.run(debug=True)#Run the Flask app.Debug mode is on, so don't deploy this directly!
