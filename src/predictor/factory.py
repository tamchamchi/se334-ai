from base import IPredictor
from typing import Type


class PredictorFactory:
    default_strategy: str = "en"
    strategy_map: dict[str, Type[IPredictor]] = {}

    @classmethod
    def register(cls, name: str, model_cls: Type[IPredictor]):
        if not issubclass(model_cls, IPredictor):
            raise TypeError(f"{model_cls} must inherit from IPredictor")
        cls.strategy_map[name] = model_cls

    @classmethod
    def create(cls, name: str, **kwargs) -> IPredictor:
        model_cls = cls.strategy_map.get(name)
        if not model_cls:
            raise ValueError(f"Model '{name}' is not registered.")
        return model_cls(**kwargs)
