import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import joblib
import os

def load_data():
    data = pd.read_csv("./language_detection.csv")
    replacements = {
        "Sweedish": "Swedish",
        "Portugeese": "Portuguese"
    }
    for old, new in replacements.items():
        print("Renaming language", old, "to", new, "...")
        data.loc[data["Language"] == old, "Language"] = new
    return data

def train_model(data):
    x = np.array(data["Text"])
    y = np.array(data["Language"])
    cv = CountVectorizer()
    X = cv.fit_transform(x)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
    print(f"# DATASET\nDataset size: {X.shape[0]} items, \nTrain size: {X_train.shape[0]} items, \nTest size: {X_test.shape[0]} items\n")
    model = MultinomialNB()
    model.fit(X_train, y_train)

    train_accuracy = model.score(X_train, y_train)
    test_accuracy = model.score(X_test, y_test)
    print(f"# ACCURACY\nTrain accuracy: {train_accuracy:.2%}\nTest accuracy: {test_accuracy:.2%}")
    return model, cv

def save_model(model, vectorizer, filename = "models/multinomial_language_detector.joblib"):
    os.makedirs("models", exist_ok=True)
    full_model = (model, vectorizer)
    paths = joblib.dump(full_model, filename)
    for path in paths:
        print("Saved model to", path)

if __name__ == '__main__':
    data = load_data()
    model, cv = train_model(data)
    save_model(model, cv)
