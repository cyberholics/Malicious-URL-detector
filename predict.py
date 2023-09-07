import pickle
from flask import Flask, request,jsonify

#load model
with open("final_model.pkl","rb") as f_in:
    final_model=pickle.load(f_in)
    
#create a prediction function

def predict_url(url):
    prediction = final_model.predict(url)
    return prediction

#create web service 

app = Flask("Malicious_url_detector")

@app.route("/predict",methods=["POST"])
def predict():
    
    #get the JSON data from the request
    data = request.get_json()
    
    #get url from JSON data
    url = data["url"]
    
    #make prediction with url by calling the prediction function
    prediction = predict_url(url)
    result = {"url_prediction":str(prediction)} 
    
    # send back the data in json format
    return jsonify(result)  

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)