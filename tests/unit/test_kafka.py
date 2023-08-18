from fastkafka.testing import Tester
import pytest

from ko.app import Data

msg = Data(
    data=0.1,
)

@pytest.mark.asyncio
async def test_fastkafka(app):
    # Start Tester app and create InMemory Kafka broker for testing
    async with Tester(app) as tester:
        # Send Data message to input_data topic
        await tester.to_input_data(msg)

        # Assert that the kafka_app responded with incremented data in output_data topic
        await tester.awaited_mocks.on_output_data.assert_awaited_with(
            Data(data=1.1), timeout=2
        )
