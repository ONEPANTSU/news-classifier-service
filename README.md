# 📰 News Classifier Service

## 📖 Description:
The gRPC API for getting ru-news category by neural network model predictions. It could be used as a microservice for Recommender Systems.

This API uses the fully connected MLP model, which includes 2 hidden layers with ReLU activation function: the first layer has 512 neurons and the second layer has 256 neurons. This structure is capable of processing unordered sets of tokens. In this case, bigrams are used as a token, which allow local order information to be input into the "bag of words". In addition, the degree of importance of token a in a given context is added to the vector representation using TF-IDF normalization.

The output of the model is a fully connected layer of 12 neurons, each of which applies a sigmoidal activation function and corresponds to a particular class of neurons
| Precision | Recall | F1-score | AUC-ROC | AUC-PR |
| --------- | ------ | -------- | ------- | ------ |
| 78 %      | 59,6 % | 55,2 %   | 92,7 %  | 75,3 % |

## ▶️ Run:
The service will run on port 50051
```
docker-compose build
docker-compose up
```
## 😗 Creating a client:

Use file `client_example.py` as an example of gRPC client. Also you need to have files from dir `src/rpc/` 
