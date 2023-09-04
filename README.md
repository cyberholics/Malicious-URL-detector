# This repo contains my capstone project for the [machine learning zoomcamp](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp) which I completed.



## Table of contents

- [1. About the project](#topic1)
- [2. Project important files and folder explained](#topic2)
- [3. Running this project](#topic3)
- [4. Summary](#topic4)
- [5. Technologies used to complete this project](#topic5)


<h2 id="topic1"> 1. About the project</h2> 

Malicious URLs are web links created to achieve dubious acts like scams, frauds, or phishing. Some malicious URLs are designed to install malware on user devices when clicked on. The interesting thing about these URLs is that they are designed to appear like normal, safe URLs, therefore luring naive users to click on them.
Conventional approaches to combating these threats have depended on the use of blacklists and whitelists, which consist of URL listings classified as malicious or safe. Nevertheless, blacklists have limitations in terms of their applicability and their inability to safeguard against novel, unidentified malicious URLs. In this project, machine learning techniques will be applied to address this challenge. A machine learning model will be trained using a mathematical algorithm on datasets containing URL samples, comprising both malicious and legitimate URLs. This model will learn from the data to distinguish between what constitutes a legitimate URL and what characterises a malicious one. When provided with new URL samples, the model will generate predictions to classify them as either malicious or legitimate. Following this training, the model can be deployed for real-world usage in a production environment.
This is a machine learning **classification** problem 

<h2 id="topic2"> 2. Project important files and folders explained</h2> 

- **phishing_site_urls.csv:** This is the dataset used to train the machine learning model; it contains 549846 unique URL entries.
and 2 columns, namely, URLs and labels.
The Labels include two categories: Good and Bad. Good is a non-malicious URL. Bad is a malicious URL. The dataset is available to download on [Kaggle](https://www.kaggle.com/datasets/ashharfarooqui/phising-urls).

- **malicious_url.ipynb:** This is a Jupyter Notebook where I carried out exploratory (EDA) data analysis on the dataset, processed the data, and experimented with different machine learning techniques to build this project.


![Phishing image](Images/maxresdefault.jpeg)
[Image source](https://www.govtech.com/blogs/lohrmann-on-cybersecurity/what-to-do-about-phishing.html)
