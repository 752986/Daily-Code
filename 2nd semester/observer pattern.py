import weakref
from typing import Callable, Any

class Event:
    class Delegate:
        def __init__(self):
            self.subject: weakref.ref[object]
            self.called: Callable[[object, list[Any]], None]

    def __init__(self):
        self.subscriptions: list[Event.Delegate] = []

    def subscribe(self, )

    def emit(self, eventargs: list[Any]):
        for i in self.subscriptions:
            i.subject.(i.called)()

