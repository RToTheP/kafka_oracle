from fastkafka.testing import Tester
import pytest

import ko.db as db
from ko.transform import Person, User, person_to_user

@pytest.mark.asyncio
async def test_transform_async():
    person = Person(first_name="Barry", last_name="McFarry")
    user = await person_to_user(person)
    assert user.user_name == "Barry.McFarry"


@pytest.mark.asyncio
async def test_app_transform(app):
    db.clear_users()

    msg = Person(id=1, first_name="Barry", last_name="McFarry")
    # Start Tester app and create InMemory Kafka broker for testing
    async with Tester(app) as tester:
        # Send Data message to input_data topic
        await tester.to_persons(msg)

    users = db.get_users()
    user_names = [ u[1] for u in users ]
    assert "Barry.McFarry" in user_names

    