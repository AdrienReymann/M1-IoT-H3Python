from fastapi import FastAPI
from sklearn.svm import SVC
app=FastAPI()

@app.get("/")
async def root():
	return{"message" : "Hello World!"}
	
@app.post('/predict')
async def predict():
    #load model 
    model_filename = "./model/hatespeech.joblib.z" #target a changer 
    clf = joblib.load(model_filename)
    # Receives the input query from form
    if request.method == 'POST':
	    namequery = request.form['namequery']
	    data = [namequery]
	    probas = clf.predict_proba([str(data)])[0]
    return render_template('result.html', probas=probas)  #Changer rendus