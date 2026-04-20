from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("best_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
encoders = pickle.load(open("encoders.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.form.to_dict()

    data["gender"] = encoders["gender"].transform([data["gender"]])[0]
    data["ssc_board"] = encoders["ssc_board"].transform([data["ssc_board"]])[0]
    data["hsc_board"] = encoders["hsc_board"].transform([data["hsc_board"]])[0]
    data["degree_stream"] = encoders["degree_stream"].transform([data["degree_stream"]])[0]
    data["university"] = encoders["university"].transform([data["university"]])[0]

    input_data = [
        float(data["gender"]),
        float(data["work_experience"]),
        float(data["ssc_board"]),
        float(data["ssc_percentage"]),
        float(data["hsc_board"]),
        float(data["hsc_percentage"]),
        float(data["degree_stream"]),
        float(data["cgpa"]),
        float(data["backlogs"]),
        float(data["university"]),
        float(data["coding_score"]),
        float(data["communication_score"]),
        float(data["aptitude_score"]),
        float(data["internships"]),
        float(data["projects"]),
        float(data["certifications"])
    ]

    input_array = np.array(input_data).reshape(1, -1)
    input_scaled = scaler.transform(input_array)

    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0]

    if prediction == 1:
        result = "Placed"
        prob = probability[1] * 100
        color = "green"
    else:
        result = "Not Placed"
        prob = probability[0] * 100
        color = "red"

    return render_template("index.html", prediction_text=result, probability=prob, color=color)

if __name__ == "__main__":
    app.run(debug=True)