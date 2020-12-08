from fastapi import FastAPI
import joblib

app = FastAPI()

@app.get("/{stri}")
def param(stri: str):
    model_filename = "./model/hatespeech.joblib.z"
    clf = joblib.load(model_filename)
    # Receives the input query from form
    probas = clf.predict_proba([stri])[0]
    return {"Hate speech : ": probas[0], "Offensive language : ": probas[1], "Neither : ": probas[2]}





