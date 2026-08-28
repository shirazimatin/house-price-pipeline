# House Price Prediction Pipeline

A machine learning pipeline for house price prediction using Python and scikit-learn.

## Project Status

Version: 0.1.0

This is the initial version of the project.

## Features

- Load house price data from CSV
- Data preprocessing
- Missing value handling
- Feature scaling
- Train/test split
- Linear Regression model
- Model evaluation using Mean Squared Error
- Save trained model with Joblib
- House price prediction
- Basic project structure for future API deployment

## Project Structure

```text
house-price-pipeline/
│
├── app/
│   ├── core/
│   │   └── config.py
│   ├── models/
│   ├── schemas/
│   │   └── house.py
│   ├── services/
│   │   └── predictor.py
│   └── main.py
│
├── data/
│   ├── train.csv
│   └── test.csv
│
├── docs/
│   └── architecture.md
│
├── models/
│   └── .gitkeep
│
├── src/
│   ├── data_loader.py
│   ├── model.py
│   ├── predict.py
│   ├── preprocess.py
│   ├── train.py
│   └── utils.py
│
├── tests/
│   └── test_model.py
│
├── main.py
├── notebook.ipynb
├── requirements.txt
└── README.md