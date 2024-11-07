from pydantic import BaseModel, Field


class WineQualityData(BaseModel):
    """
    Required data needed to predict the wine quality. \n
    **NOTE**: The order of the fields must much how the data was trained.
    """

    fixed_acidity: float = Field(alias="fixed acidity")
    volatile_acidity: float = Field(alias="volatile acidity")
    citric_acid: float = Field(alias="citric acid")
    residual_sugar: float = Field(alias="residual sugar")
    chlorides: float = Field()
    free_sulfur_dioxide: float = Field(alias="free sulfur dioxide")
    total_sulfur_dioxide: float = Field(alias="total sulfur dioxide")
    density: float = Field()
    pH: float = Field()
    sulphates: float = Field()
    alcohol: float = Field()
