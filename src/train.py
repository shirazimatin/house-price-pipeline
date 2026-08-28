from pathlib import Path
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

from src.data_loader import load_data
from src.model import create_model_pipeline


def train_model():

    data_path = Path("data/train.csv")

    df = load_data(data_path)

    X = df.drop(columns=["Price"])
    y = df["Price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    pipeline = create_model_pipeline()

    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)

    mse = mean_squared_error(y_test, predictions)

    print(f"Mean Squared Error: {mse:.2f}")

    Path("models").mkdir(exist_ok=True)

    joblib.dump(
        pipeline,
        "models/house_price_model.pkl"
    )

    print("Model saved successfully.")


if __name__ == "__main__":
    train_model()