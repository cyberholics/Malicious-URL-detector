import requests

# prompt user to enter a url
url_sample=input("ENTER URL SAMPLE")

#specify prediction web service url
web_service_url = 'http://localhost:9696/predict'

#send POST request as a JSON data to the prediction web service
response = requests.post(web_service_url, json={"url": url})

#check the response status code and return predictions
if response.status_code == 200:
    result = response.json()
    url_prediction = result['url_prediction']
    if url_prediction  == "good":
        print("This is a good URL, you are safe to browse")
    elif url_prediction == "bad":
        print("This is a malicious , do not enter this link!!")
    
else:
    print("Failed to get a valid response from the prediction service.")
  