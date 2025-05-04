from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model
import os

model_path = os.path.join(os.path.dirname(__file__), "model", "model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    proba = None
    url = ""  # Initialize URL

    if request.method == "POST":
        url = request.form["url"]
        prediction = model.predict([url])[0]
        probabilities = model.predict_proba([url])[0]  # [prob_legit, prob_phish]

        result = "legitimate" if prediction == 0 else "phishing"
        proba = {
            "legitimate": round(probabilities[0], 3),
            "phishing": round(probabilities[1], 3)
        }

    return render_template("index.html", result=result, proba=proba, url=url)

if __name__ == "__main__":
    app.run(debug=True)
