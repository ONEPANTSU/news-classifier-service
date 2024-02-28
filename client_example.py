import asyncio
import logging

import grpc
from src.rpc import *

texts = [
    """
    В Москве полицейские нашли и изъяли спецоборудование и камеру, установленную напротив Минобороны РФ. Позже оказалось, что, вероятно, техника принадлежит ФСБ.

О странной находке полиции рассказал сотрудник управляющей компании дома на Фрунзенской набережной. Он обнаружил камеру на штативе во время планового обхода чердака. 

На место выехали оперативники и забрали оборудование. Изначально полицейские заподозрили подготовку диверсии, и даже начали свою проверку, но их успокоили сотрудники ФСБ — по данным «Базы», сотрудники спецслужб сообщили, что оборудование принадлежит им.
    """
]


async def run() -> None:
    for i, txt in enumerate(texts):
        async with grpc.aio.insecure_channel("localhost:50051") as channel:
            stub = classifier_pb2_grpc.NewsClassifierStub(channel)
            response = await stub.ClassifyNews(classifier_pb2.NewsClassificationRequest(text=txt))
        print(str(i) + str(response.categories))


if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(run())