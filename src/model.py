from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

from src.preprocess import create_preprocessing_pipeline


def create_model_pipeline():
    """
    Create the complete machine learning pipeline.
    """

    preprocessing = create_preprocessing_pipeline()

    pipeline = Pipeline(
        steps=[
            ("preprocessing", preprocessing),
            ("model", LinearRegression())
        ]
    )

    return pipeline