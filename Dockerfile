FROM python:3.10

WORKDIR /news_classifier

COPY ./src .
COPY ./run.py .
COPY ./requirements.txt .
COPY ./models/ensemble.keras ./models

RUN pip install -r requirements.txt

EXPOSE 50051

CMD ["python", "run.py"]