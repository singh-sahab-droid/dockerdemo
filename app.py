from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Hello Mukesh Singh from git hub gui changed file for  your Dockerized Flask app!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
