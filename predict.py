from typing import List

import pandas as pd
from sklearn.linear_model import ElasticNet

from columns import WineQualityData
from utils import load_object


def predict_wine_quality(wine_list: List[WineQualityData]) -> List[float]:
    """
    Load model artifact from directory and predict with LinearModel
    :param wine_list: wine list
    :return: wine quality
    """
    dataframe = pd.DataFrame(data=[res.model_dump(by_alias=True) for res in wine_list])
    model: ElasticNet = load_object(file_path="model.pkl")
    return model.predict(dataframe)
