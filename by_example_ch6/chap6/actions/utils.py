from django.contrib.contenttypes.models import ContentType
from .models import Action
import datetime
from django.utils import timezone


def create_action(user, verb, target=None):
    # check for any similiar action made in the last minute
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    similiar_actions = Action.objects.filter(
        user_id=user.id,
        verb=verb,
        timestamp_gte=last_minute
    )

    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similiar_actions = similiar_actions.filter(
            target_ct=target_ct,
            target_id=target.id,
        )
    if not similiar_actions:
        # no existing actions found
        actions = Action(user=user, verb=verb, target=target)
        actions.save()
        return True
    return False
