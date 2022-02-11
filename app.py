#Import Essentials
from flask import Flask, request, render_template
import numpy as np
import pickle

#Get Pickled Model In Environment
predictive_model = pickle.load(open("predictive_model.pkl", "rb"))

#Set Up Flask Environment
app = Flask(__name__)

#Get a Home Page Going
@app.route('/')
def home():
    return render_template('home.html')

#Get Predictions
@app.route("/predict", methods = ["POST"])
def predict():
    #Get Scores from "Home" Page and Convert to Integers
    scores_list = []
    section_1_total = scores_list.append(int(request.form["Section-1-Total"]))
    section_2_total = scores_list.append(int(request.form["Section-2-Total"]))
    section_3_total = scores_list.append(int(request.form["Section-3-Total"]))
    overall_total = scores_list.append(sum(scores_list))

    #Convert List to NumPy Array
    prediction_array = np.array([scores_list])
    print(prediction_array)

    #Feed NumPy Array into Prediction Algorithm
    prediction = predictive_model.predict(prediction_array)
    print(prediction)
    return render_template("prediction.html", data = prediction)

#Main Function
if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port=9696)