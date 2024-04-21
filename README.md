# 📰 News Classifier Service

## 📖 Description:
The gRPC API for getting ru-news category by neural network model predictions. It could be used as a microservice for Recommender Systems.

There are some available models architectures:
- **MLP model**

| Precision | Recall | F1-score | AUC-ROC | AUC-PR |
| --------- |--------|----------|---------|--------|
| 78 %      | 59.6 % | 55.2 %   | 92.7 %  | 75.3 % |

- **CNN model**

| Precision | Recall | F1-score | AUC-ROC | AUC-PR |
|-----------|--------|----------|---------|--------|
| 82.3 %    | 29.5 % | 53.2 %   | 88.4 %  | 64.7 % |

- **LSTM model**

| Precision | Recall | F1-score | AUC-ROC | AUC-PR |
|-----------|--------|----------|---------|--------|
| 78.1 %    | 44,6 % | 34.8 %   | 90,7 %  | 68.1 % |

- **TransformerEncoder**

| Precision | Recall | F1-score | AUC-ROC | AUC-PR |
|-----------|--------|----------|---------|--------|
| 75.7 %    | 49.8 % | 43.8 %   | 93 %    | 73 %   |

- **Ensemble of MLP and TransformerEncoder**

| Precision | Recall | F1-score | AUC-ROC | AUC-PR |
|-----------|--------|----------|---------|--------|
| 80.7 %    | 54,6 % | 55,8 %   | 93,5 %  | 76,6 % |



The output of the model is a fully connected layer of 12 neurons, each of which applies a sigmoidal activation function and corresponds to a particular class of neurons


This API uses the **Ensemble** by default.


## ▶️ Run:
The service will run on port 50051
```
docker-compose build
docker-compose up
```
## 😗 Creating a client:

Use file `client_example.py` as an example of gRPC client. Also you need to have files from dir `src/rpc/` 
