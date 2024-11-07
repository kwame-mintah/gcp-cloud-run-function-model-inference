from typing import List

import uvicorn
from fastapi import FastAPI, status

from columns import WineQualityData
from predict import predict_wine_quality

app = FastAPI()


@app.post(
    path="/predict/",
    operation_id="winePrediction",
    summary="Predict wine quality",
    response_model=List[float],
    status_code=status.HTTP_200_OK,
)
async def predict(data: List[WineQualityData]) -> List[float]:
    """
    predict the quality of wine based on quantitative features
    like the wines “fixed acidity”, “pH”, “residual sugar”, and so on.

    :param data: list of different wine qualities
    :return:
    """
    return predict_wine_quality(wine_list=data)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
