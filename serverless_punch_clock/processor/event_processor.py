

class EventProcessor:

    def __init__(self):
        pass

    @classmethod
    def process_event(cls, event_model):
        print(f'processing_event: {event_model}')
        return 200
