from tensorflow import keras
import re
import string
import nltk
from nltk.corpus import stopwords
import pymorphy2


class Model:
    def __init__(self, path):
        self.model = keras.models.load_model(path)
        self.CATEGORIES = (
            "Криминал",
            "Культура",
            "Экономика",
            "Происшествие",
            "Политика",
            "Наука",
            "Шоу-бизнес",
            "Общество",
            "Спорт",
            "Транспорт",
            "Вооружённый конфликт",
            "Погода",
        )

    def predict(self, text, threshold=0.3):
        text = self.standardize([text])
        predictions = self.model.predict([text])
        return [
            self.CATEGORIES[i]
            for i, prediction in enumerate(predictions[0])
            if prediction >= threshold
        ]

    @staticmethod
    def standardize(input_text, delete_stop_words=True):
        nltk.download("stopwords")
        morph = pymorphy2.MorphAnalyzer()
        stop_words = stopwords.words("russian")

        processing = [re.sub(
            f"[{re.escape(string.punctuation)}]",
            "",
            text,
        ) for text in input_text]
        result = []
        for text in processing:
            if delete_stop_words:
                for stop_word in stop_words:
                    text = re.sub(
                        f" {stop_word} ",
                        " ",
                        text,
                    )
            lemmas = []
            for token in text.split():
                lemmas.append(morph.parse(token)[0].normal_form)
            result.append(" ".join(lemmas))
            if len(result) % 50 == 0:
                print(len(result))
        return result
