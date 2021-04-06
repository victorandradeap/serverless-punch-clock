

class Event:

    def __init__(self, event_id, event_type):
        self._event_id = event_id
        self._event_type = event_type

    @property
    def event_id(self):
        return self._event_id

    @property
    def event_type(self):
        return self._event_type


class PunchClockEvent(Event):

    EVENT_TYPE = 'PUNCH_CLOCK'

    def __init__(self, event_body):
        super().__init__(event_body['id'], self.EVENT_TYPE)

    def __str__(self):
        return f'ID: {self.event_id} - Type: {self.event_type}'
