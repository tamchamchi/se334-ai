from fastapi import FastAPI

from src.predictor.multilingual_predictor import MultilingualPredictor
from src.utils.common import load_config

from api.schema.predictor import PredictRequest, PredictResponse

config = load_config(path="./config/model_config.yaml")
cfg_multilingual_model = config["predictor"]["multilingual"]

predictor = MultilingualPredictor(
    model_name=cfg_multilingual_model.get("model_name"),
    device=cfg_multilingual_model.get("device"),
    seed=cfg_multilingual_model.get("seed")
)

app = FastAPI(title="Sentiment Analysis API")


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    results = predictor.run(request.texts)
    return {"results": results}
