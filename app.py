import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
Diabetes_detector_model = pickle.load(open('diabetes.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    
    features_name = [ "num_preg","glucose_conc","diastolic_bp","thickness","insulin","bmi","diab_pred","age","skin"]
    
    data= pd.DataFrame(features_value, columns=features_name)
    output = Diabetes_detector_model.predict(data)
        
    if output == 1:
        res_val = "** Diabatic Patient and Please Consult to the Doctor**"
    else:
        res_val = " Patient has no Diabaties and Enjoy your life"
        

    return render_template('index.html', prediction_text='Patient has {}'.format(res_val))

if __name__ == "__main__":
    app.run()