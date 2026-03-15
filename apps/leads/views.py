import json
import logging
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .forms import validate_lead_data
from .models import Lead

logger = logging.getLogger(__name__)


@require_http_methods(['POST'])
def submit_lead(request):
    try:
        body = json.loads(request.body)
    except (json.JSONDecodeError, TypeError):
        return JsonResponse({'ok': False, 'error': 'invalid_json'}, status=400)

    source = (body.get('source') or '').strip()
    data = body.get('data')
    if not source:
        return JsonResponse({'ok': False, 'error': 'source_required'}, status=400)
    if not isinstance(data, dict):
        data = {}

    errors = validate_lead_data(source, data)
    if errors:
        return JsonResponse({'ok': False, 'errors': errors}, status=400)

    try:
        lead = Lead(
            source=source,
            payload=data,
            email=(data.get('email') or '').strip()[:254],
            phone=(data.get('phone') or '').strip()[:64],
        )
        lead.save()
    except Exception as e:
        logger.exception('Ошибка сохранения заявки: %s', e)
        return JsonResponse({'ok': False, 'error': 'save_failed'}, status=500)

    return JsonResponse({'ok': True})
