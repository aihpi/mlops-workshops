import argparse
import joblib

def load_model(filename):
    return joblib.load(filename)

def predict_text(model, cv, texts):
    vectorized = cv.transform([texts])
    prediction = model.predict(vectorized)[0]
    return prediction

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Predict language of the provided text using a trained model.")
    parser.add_argument("text", type=str, help="Text to predict the language for.")
    parser.add_argument("-m", "--model", type=str, default="models/multinomial_language_detector.joblib", help="Path to the trained model joblib file.")
    
    args = parser.parse_args()
    model, cv = load_model(args.model)
    prediction = predict_text(model, cv, args.text)
    print(prediction)
