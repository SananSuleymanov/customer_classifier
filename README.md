# FastAPI Customer Prediction Service

This repository contains a FastAPI-based web service for making predictions using a pre-trained machine learning model for classification of customers anlongside model training notebook (model_training.ipynb). The service is designed to handle transaction data, preprocess it, and return a prediction (whether customer will repeat transaction within 2 months or not) based on the provided features.

## Features

- **Prediction Endpoint**: Accepts JSON input for transaction data and returns a prediction.
- **Data Preprocessing**: Automatically applies the same preprocessing steps used during model training.
- **Dockerized**: The service can be easily containerized using Docker for consistent deployment across environments.

## Prerequisites

- Docker (for containerized deployment)
- Python 3.9+ (if running locally)

## Installation

### Running Locally

1. **Clone the repository**:
    ```bash
    git clone https://github.com/SananSuleymanov/customer_classifier.git
    cd customer_classifier
    ```

2. **Create and activate a virtual environment (optional but recommended)**:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    uvicorn main:app --reload
    ```

    The API will be available at `http://127.0.0.1:8000`.

### Running with Docker

1. **Build the Docker image**:
    ```bash
    docker build -t fastapi-prediction-customer .
    ```

2. **Run the Docker container**:
    ```bash
    docker run -d -p 8000:8000 fastapi-prediction-customer
    ```

    The API will be available at `http://127.0.0.1:8000`.

### Running with AWS Elastic Beanstalk endpoint

The API will be available at `http://classifier-customer.eu-central-1.elasticbeanstalk.com/`.

## Usage

### Prediction Endpoint

- **Endpoint**: `/predict`
- **Method**: `POST`
- **Content-Type**: `application/json`
- **Request Body**:
  
  ```json
  {
      "Product": "string",
      "Gender": "string",
      "Device_Type": "string",
      "Country": "string",
      "State": "string",
      "City": "string",
      "Category": "string",
      "Customer_Login_type": "string",
      "Delivery_Type": "string",
      "Transaction_Result": int,
      "Amount_USD": float,
      "Individual_Price_USD": float,
      "Quantity": int
  }


### Example Request
 ```bash
    curl -X 'POST' \
  'http://classifier-customer.eu-central-1.elasticbeanstalk.com/predict' \
  -H 'Content-Type: application/json' \
  -d '{
    "Product": "Hair Band",
    "Gender": "Female",
    "Device_Type": "Web",
    "Country": "United States",
    "State": "New York",
    "City": "New York City",
    "Category": "Accessories",
    "Customer_Login_type": "Member",
    "Delivery_Type": "one-day deliver",
    "Transaction_Result": 1,
    "Amount_USD": 100,
    "Individual_Price_USD": 10,
    "Quantity": 1
}'
    ```

Output:
```bash
   {
    "prediction": 0
}
    ```
