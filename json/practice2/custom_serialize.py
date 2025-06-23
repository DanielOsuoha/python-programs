import json
from event import Event
from datetime import datetime
def custom_serialize(name, date_time):
    pass

if __name__ == "__main__":
    event = Event("Hackathon", datetime.now)
    print(event.time)
    # value = json.dumps(event, default=custom_serialize)
    # print(value)