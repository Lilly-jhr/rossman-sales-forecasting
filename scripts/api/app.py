from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)


model = joblib.load('models/sales_prediction_model.pkl')

@app.route('/predict', methods=['POST'])
def predict_sales():
    data = request.get_json()  
    df = pd.DataFrame(data)
    
    prediction = model.predict(df)  
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)