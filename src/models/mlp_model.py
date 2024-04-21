from src.models.base_model import BaseModel


class MLPModel(BaseModel):
    def __init__(self):
        super().__init__("models/mlp.keras")