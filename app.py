import pandas as pd
from flask import Flask,render_template,request
import pickle
import numpy as np

app = Flask(__name__)

data= pd.read_csv("Cleaned_data.csv")

pipe = pickle.load(open("HouseP.pkl","rb"))


@app.route('/')
def Home():
    locations = sorted(data["location"].unique())
    return render_template('Home.html',locations=locations)


@app.route("/predict",methods=["POST"])
def predict():
    location =request.form.get("location")
    bhk = request.form.get("bhk")
    bath= request.form.get("bath")
    sqft = request.form.get("total_sqft")
    print(location,bhk,bath,sqft)
    input= pd.DataFrame([[location,sqft,bath,bhk]],columns=["location","total_sqft","bath","bhk"])
    prediction = pipe.predict(input)[0] * 1e5




    return str(np.round(prediction))

if __name__=="__main__":
    app.run(debug=True,port=5003)