from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

scaler = joblib.load('scaler.pkl')
encoded_columns = joblib.load('encoded_columns.pkl')
model = joblib.load('model.pkl')

class InferenceRequest(BaseModel):
    Product: str
    Gender: str
    Device_Type: str
    Country: str
    State: str
    City: str
    Category: str
    Customer_Login_type: str
    Delivery_Type: str
    Transaction_Result: int
    Amount_USD: float  
    Individual_Price_USD: float  
    Quantity: int

# Preprocessing function
def preprocess_input(data: pd.DataFrame):
   
    #Repeating same preprocessing used in training for inference 
    numerical_features = ['Amount US$', 'Individual_Price_US$', 'Quantity']
    data[numerical_features] = scaler.transform(data[numerical_features])
    
    categorical_features = ['Product', 'Gender', 'Device_Type', 'Country', 
                            'State', 'City', 'Category', 'Customer_Login_type', 
                            'Delivery_Type']
    data_encoded = pd.get_dummies(data, columns=categorical_features)
    
    data_encoded = data_encoded.reindex(columns=encoded_columns, fill_value=0)
    
    return data_encoded

# Prediction endpoint
@app.post("/predict")
def predict(request: InferenceRequest):
    try:
        input_data = pd.DataFrame([request.dict()])

        #during trainig we used "Amount US$" and "Individual_Price_US$". 
        # in order to make it easy for developers we can use "Amount_USD", "Individual_Price_USD"
    
        input_data.rename(columns={
            "Amount_USD": "Amount US$",
            "Individual_Price_USD": "Individual_Price_US$"
        }, inplace=True)
        
        processed_data = preprocess_input(input_data)

        prediction = model.predict(processed_data)
        return {"prediction": int(prediction[0])}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
