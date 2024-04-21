import logging

import grpc

from src.models.ensemble_model import EnsembleModel
from src.rpc import *


class Classifier(classifier_pb2_grpc.NewsClassifierServicer):
    model = EnsembleModel()

    def ClassifyNews(
        self,
        request: classifier_pb2.NewsClassificationRequest,
        context: grpc.aio.ServicerContext,
    ) -> classifier_pb2.NewsClassificationReply:
        prediction = self.model.predict(request.text)
        return classifier_pb2.NewsClassificationReply(categories=prediction)


async def serve() -> None:
    server = grpc.aio.server()
    classifier_pb2_grpc.add_NewsClassifierServicer_to_server(Classifier(), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()
