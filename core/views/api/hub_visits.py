from django.conf import settings
from django.http import JsonResponse

from ...utils.recurse_api import get_hub_visits_for_today


def hub_visits(request):
    """
    Returns a JSON response containing the number of visits to the hub.
    """
    hub_visits_for_today = get_hub_visits_for_today(settings.RC_ACCESS_TOKEN)
    return JsonResponse({"hub_visits_for_today": hub_visits_for_today})