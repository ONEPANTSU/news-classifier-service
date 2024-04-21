from src.models.base_model import BaseModel


class LSTMModel(BaseModel):
    def __init__(self):
        super().__init__("models/lstm.keras")