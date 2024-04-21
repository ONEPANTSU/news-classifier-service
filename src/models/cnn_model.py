from src.models.base_model import BaseModel


class CNNModel(BaseModel):
    def __init__(self):
        super().__init__("models/cnn.keras")