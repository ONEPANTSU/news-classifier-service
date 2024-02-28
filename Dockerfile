FROM python:3.10

WORKDIR /news_classifier

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "run.py"]