from base import IPredictor


class VietnamesePredictor(IPredictor):
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.predictor = self.load_model()

    def load_model(self):
        pass

    def run(self, texts: list[str]) -> dict[str, str]:
        return {
            "text": "Tên của tôi là Tâm Anh",
            "label": "netural"
        }


if __name__ == "__main__":
    from factory import PredictorFactory

    PredictorFactory.register("vn", VietnamesePredictor)
    model = PredictorFactory.create("vn")
    texts = ["Toi", "Hi"]
    print(model.run(texts))
