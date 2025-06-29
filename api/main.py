from fastapi import FastAPI

from src.predictor.multilingual_predictor import MultilingualPredictor
from src.predictor.factory import PredictorFactory
from src.utils.common import load_config

from api.schema.predictor import PredictRequest, PredictResponse

config = load_config(path="./config/model_config.yaml")
cfg_multilingual_model = config["predictor"]["multilingual"]

PredictorFactory.register("multilingual", MultilingualPredictor)

predictor = PredictorFactory.create("multilingual",**cfg_multilingual_model)

app = FastAPI(title="Sentiment Analysis API")


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    results = predictor.run(request.texts)
    return {"results": results}
