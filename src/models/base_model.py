from tensorflow import keras
import re
import string
import nltk
from nltk.corpus import stopwords
import pymorphy2

from src.models.utils import CATEGORIES


class BaseModel:
    def __init__(self, path):
        self.model = keras.models.load_model(path)

    def predict(self, text, threshold=0.3):
        standardized_text = self.__standardize(text)
        predictions = self.model.predict(standardized_text)
        return [
            CATEGORIES[i]
            for i, prediction in enumerate(predictions[0])
            if prediction >= threshold
        ]

    @staticmethod
    def __standardize(text, delete_stop_words=True):
        nltk.download("stopwords")
        morph = pymorphy2.MorphAnalyzer()
        stop_words = stopwords.words("russian")

        processing = re.sub(
            f"[{re.escape(string.punctuation)}]",
            "",
            text,
        )
        result = []
        if delete_stop_words:
            for stop_word in stop_words:
                processing = re.sub(
                    f" {stop_word} ",
                    " ",
                    processing,
                )
        lemmas = []
        for token in processing.split():
            lemmas.append(morph.parse(token)[0].normal_form)
        result.append(" ".join(lemmas))
        if len(result) % 50 == 0:
            print(len(result))
        return result
