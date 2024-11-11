from typing import List

import uvicorn
from fastapi import FastAPI, status

from columns import WineQualityData
from predict import predict_wine_quality

app = FastAPI(
    title="Wine Quality Prediction",
    description="An example project for running a prediction using a machine learning model stored within a GCP bucket",
    contact={
        "name": "Kwame Mintah",
        "url": "https://github.com/kwame-mintah/kwame-mintah/discussions/categories/general",
        "email": "email@email.com",
    },
    license_info={
        "name": "GNU GENERAL PUBLIC LICENSE",
        "url": "https://www.gnu.org/licenses/gpl-3.0.en.html#license-text",
    },
)


@app.post(
    path="/predict/",
    operation_id="winePrediction",
    summary="Predict wine quality",
    response_model=List[float],
    status_code=status.HTTP_200_OK,
)
async def predict(data: List[WineQualityData]) -> List[float]:
    """
    Predict the quality of wine based on quantitative features
    like the wines “fixed acidity”, “pH”, “residual sugar”, and so on.

    :param data: list of different wine qualities
    :return:
    """
    return predict_wine_quality(wine_list=data)


if __name__ == "__main__":
    # Useful when running application locally.
    uvicorn.run(app, host="0.0.0.0", port=8000)
