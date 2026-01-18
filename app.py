from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

def get_reply(msg):
    msg = msg.lower()

    if "hi" in msg or "hello" in msg:
        return "Hi 😊 What do you like? coding, data, ai, cyber, mobile, or cloud?"

    if "coding" in msg:
        return "👨‍💻 Web Developer\nLearn HTML, CSS, JavaScript"

    if "ai" in msg:
        return "🤖 AI Engineer\nLearn Python, ML, Deep Learning"

    if "cloud" in msg:
        return "☁️ Cloud Engineer\nLearn Linux, AWS, Docker"

    return "Please type: coding, ai, or cloud"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    return jsonify({"reply": get_reply(data["message"])})

if __name__ == "__main__":
    app.run(debug=True)
