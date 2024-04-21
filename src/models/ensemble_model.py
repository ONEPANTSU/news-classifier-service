from src.models.base_model import BaseModel


class EnsembleModel(BaseModel):
    """
    Ensemble includes MLP and TransformerEncoder
    """
    def __init__(self):
        super().__init__("models/ensemble.keras")

