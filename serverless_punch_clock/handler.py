import json
from serverless_punch_clock.model.event import PunchClockEvent
from serverless_punch_clock.processor.event_processor import EventProcessor


def handle(event, context):
    body = json.loads(event['events'])
    event_model = PunchClockEvent(body)

    status = EventProcessor.process_event(event_model)

    response = {
        'statusCode': status,
        'context': str(context)
    }

    return response
