FROM python:3.10

WORKDIR /news_classifier

COPY . .

RUN pip install -r requirements.txt

EXPOSE 50051

CMD ["python", "run.py"]