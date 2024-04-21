from src.models.base_model import BaseModel
from src.models.custom_objects.transformer_encoder import TransformerEncoder
from src.models.custom_objects.positional_embedding import PositionalEmbedding


class EnsembleModel(BaseModel):
    """
    Ensemble includes MLP and TransformerEncoder
    """
    def __init__(self):
        super().__init__(
            "models/ensemble.keras",
            custom_objects={
                "TransformerEncoder": TransformerEncoder,
                "PositionalEmbedding": PositionalEmbedding
            }
        )


