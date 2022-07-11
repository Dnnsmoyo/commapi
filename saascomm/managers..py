#dashboard.managers.py

from datetime import datetime
from django.contrib.contenttypes.models import ContentType


class MyActionManager(ActionManager):
    @stream
    def mystream(self, obj, verb='posted', time=None):
    from actstream.managers import ActionManager, stream
        if time is None:
            time = datetime.now()
        return obj.actor_actions.filter(verb = verb, timestamp__lte = time)
