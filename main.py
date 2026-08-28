from src.train import train_model
from src.predict import predict


def main():

    print("=" * 50)
    print("House Price Prediction Project")
    print("=" * 50)

    print("\nStep 1: Training model...\n")
    train_model()

    print("\nStep 2: Making predictions...\n")
    predict()

    print("\nProject completed successfully.")


if __name__ == "__main__":
    main()