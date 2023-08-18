from logging import getLogger
from fastkafka import FastKafka
from pydantic import BaseModel, Field, NonNegativeFloat

import ko.db as db
from ko.transform import Person, person_to_user

class Data(BaseModel):
    data: NonNegativeFloat = Field(
        ..., example=0.5, description="Float data example"
    )

logger = getLogger("Demo Kafka app")

kafka_brokers = {
    "localhost": {
        "url": "localhost",
        "description": "local development kafka broker",
        "port": 29092,
    },
}

def create_app() -> FastKafka:
    app = FastKafka(
        title="Demo Kafka app",
        kafka_brokers=kafka_brokers,
    )

    @app.consumes(topic="input_data", auto_offset_reset="latest")
    async def on_input_data(msg: Data):
        logger.info(f"Got data: {msg.data}")
        await to_output_data(msg.data)


    @app.produces(topic="output_data")
    async def to_output_data(data: float) -> Data:
        processed_data = Data(data=data+1.0)
        return processed_data
    
    @app.consumes(topic="persons", auto_offset_reset="latest")
    async def on_person_transform(msg: Person):
        logger.info(f"Got person: {msg.first_name} {msg.last_name}")
        user = await person_to_user(msg)
        db.insert_user(user)

    return app

app = create_app()