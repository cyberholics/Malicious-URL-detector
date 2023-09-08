import requests

while True:
    # Prompt user to enter a URL
    url = input("ENTER URL SAMPLE (or type 'exit' to quit): ")

    if url.lower() == 'exit':
        break  # Exit the loop if the user types 'exit'

    # Specify prediction web service URL
    web_service_url = 'http://localhost:9696/predict'

    # Send POST request as JSON data to the prediction web service
    response = requests.post(web_service_url, json={"url": url})

    # Check the response status code and return predictions
    if response.status_code == 200:
        result = response.json()
        url_prediction = result['url_prediction']
        if url_prediction == "good":
            print("This is a good URL, you are safe to browse")
        elif url_prediction == "bad":
            print("This is a malicious URL, do not enter this link!!")
    else:
        print("Failed to get a valid response from the prediction service.")
