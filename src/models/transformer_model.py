from src.models.base_model import BaseModel


class TransformerModel(BaseModel):
    def __init__(self):
        super().__init__("models/transformer.keras")