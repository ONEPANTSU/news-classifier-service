from src.models.base_model import BaseModel
from src.models.utils.transformer_encoder import TransformerEncoder
from src.models.utils.positional_embedding import PositionalEmbedding


class TransformerModel(BaseModel):
    def __init__(self):
        super().__init__(
            "models/transformer.keras",
             custom_objects={
                "TransformerEncoder": TransformerEncoder,
                "PositionalEmbedding": PositionalEmbedding
            }
        )