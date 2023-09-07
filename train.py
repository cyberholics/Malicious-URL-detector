# import libraries

import pandas as pd #data manipulatio
from nltk.tokenize import RegexpTokenizer #splits a string into substrings using a regular expression
from nltk.stem.snowball import SnowballStemmer # help improve the efficiency of text analysis and information retrieval systems
from sklearn.feature_extraction.text import CountVectorizer # Transform text into mumerical features by creating a sparse matrix of words
from sklearn.model_selection import train_test_split # spliting the data in to train and test sets
from sklearn.linear_model import LogisticRegression #logistic regression algorithm
from sklearn.pipeline import make_pipeline # Machine learning pipeline used for combining all preprocessor techniques and model training 
import pickle # save and load model
print("libraries imported... Reading the data")

# read the data 
df=pd.read_csv("phishing_site_urls.csv")
print("Data preprocessing")
 
# data preprocessing
df=df.sample(frac=1).reset_index(drop=True)
df.columns=df.columns.str.lower()
 
#split the data
X_train, X_test, y_train, y_test = train_test_split(df["url"], df["label"])
 
# Making a training pipeline
pipeline = make_pipeline(CountVectorizer(tokenizer = RegexpTokenizer(r'[A-Za-z]+').tokenize, stop_words='english'), LogisticRegression(max_iter=10000))

# fit data into the pipeline 
pipeline.fit(X_train, y_train)
print("Training model")

# use pipeline to predict and get score
model_accuracy=pipeline.score(X_test, y_test)
print("model accuracy is: {}".format(model_accuracy))
print("Done with training")

# saving the model to disk
with open("final_model.pkl", "wb") as f_out:
    pickle.dump(pipeline,f_out)
    
