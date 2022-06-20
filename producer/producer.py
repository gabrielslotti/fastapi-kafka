import asyncio
import json

from aiokafka import AIOKafkaProducer
from config import KAFKA_INSTANCE
from config import PROJECT_NAME
from fastapi import FastAPI
from loguru import logger

app = FastAPI(title=PROJECT_NAME)

loop = asyncio.get_event_loop()
aioproducer = AIOKafkaProducer(loop=loop,
                               client_id=PROJECT_NAME,
                               bootstrap_servers=KAFKA_INSTANCE)


@app.on_event("startup")
async def startup_event():
    await aioproducer.start()


@app.on_event("shutdown")
async def shutdown_event():
    await aioproducer.stop()


@app.post("/producer/{topicname}")
async def kafka_produce(msg: dict, topicname: str):
    await aioproducer.send(topicname, json.dumps(msg).encode("ascii"))
    response = {
        'msg': msg,
        'topicname': topicname
    }
    logger.info(response)
    return response
