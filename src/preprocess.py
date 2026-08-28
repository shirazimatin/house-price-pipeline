from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


def create_preprocessing_pipeline():

    preprocessing_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="mean")
            ),
            (
                "scaler",
                StandardScaler()
            )
        ]
    )

    return preprocessing_pipeline