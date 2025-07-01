import torch
from .base import IPredictor
from torch.nn.functional import softmax
from tqdm import tqdm
from transformers import AutoModelForSequenceClassification, AutoTokenizer

from src.utils.common import set_seed


class MultilingualPredictor(IPredictor):
    def __init__(
        self,
        model_name: str = "tabularisai/multilingual-sentiment-analysis",
        device: str = None,
        seed: int = 42,
    ):
        self.model_name = model_name
        self.device = torch.device(
            device if device else (
                "cuda" if torch.cuda.is_available() else "cpu")
        )
        self.seed = seed
        set_seed(self.seed)
        self.model, self.tokenizer = self._load_model()
        self.model.eval()

        self.label_map = {
            0: "negative",
            1: "negative",
            2: "neutral",
            3: "positive",
            4: "positive",
        }

    def _load_model(self):
        try:
            tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            model = AutoModelForSequenceClassification.from_pretrained(
                self.model_name)
            model.to(self.device)
            return model, tokenizer
        except Exception as e:
            raise RuntimeError(f"Failed to load model or tokenizer: {e}")

    def run(self, texts: list[str], batch_size: int = 16) -> list[dict[str, str]]:
        predictions = []

        for i in tqdm(range(0, len(texts), batch_size), desc="Predicting"):
            batch = texts[i: i + batch_size]
            inputs = self.tokenizer(
                batch,
                return_tensors="pt",
                truncation=True,
                padding=True,
                max_length=512,
            ).to(self.device)

            with torch.no_grad():
                outputs = self.model(**inputs)
                probs = softmax(outputs.logits, dim=-1)
                preds = torch.argmax(probs, dim=-1)

            for text, label_id in zip(batch, preds.tolist()):
                predictions.append(
                    {"sentence": text, "label": self.label_map[label_id]})

        return predictions


if __name__ == "__main__":
    texts = [
        # English
        "I absolutely love the new design of this app!",
        "The customer service was disappointing.",
        "The weather is fine, nothing special.",
        # Vietnamese
        "cho mình xin bài nhạc tên là gì với ạ",
        "uớc gì sau này về già vẫn có thể như cụ này :))",
        "Mày nhìn cái chó gì :)))"
    ]

    predictor = MultilingualPredictor()
    pred_data = predictor.run(texts)

    for result in pred_data:
        print(f"{result['label']:>8} | {result['text']}")