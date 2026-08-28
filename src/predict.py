from pathlib import Path

import joblib
import pandas as pd


def predict():

    model_path = Path("models/house_price_model.pkl")

    if not model_path.exists():
        print("Model not found.")
        return

    model = joblib.load(model_path)

    sample = pd.DataFrame(
        [
            {
                "Area": 165,
                "Bedrooms": 3,
                "Bathrooms": 2,
                "Age": 7,
                "Parking": 1,
            }
        ]
    )

    prediction = model.predict(sample)

    print(f"Predicted house price: ${prediction[0]:,.0f}")


if __name__ == "__main__":
    predict()