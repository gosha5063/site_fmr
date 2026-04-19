import json
import logging

from django.conf import settings
from django.core.mail import send_mail

from .models import Lead

logger = logging.getLogger(__name__)


def notify_new_lead(lead: Lead) -> None:
    recipient = getattr(settings, 'LEADS_NOTIFICATION_EMAIL', '') or ''
    if not recipient:
        logger.warning('LEADS_NOTIFICATION_EMAIL не задан — письмо о заявке не отправлено')
        return

    subject = f'Новая заявка с сайта #{lead.id} ({lead.source})'
    lines = [
        f'Источник формы: {lead.source}',
        f'Номер заявки в базе: {lead.id}',
        f'Email в форме: {lead.email}',
        f'Телефон в форме: {lead.phone}',
        '',
        'Все поля формы:',
        json.dumps(lead.payload, ensure_ascii=False, indent=2),
    ]
    body = '\n'.join(lines)
    try:
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [recipient],
            fail_silently=False,
        )
    except Exception:
        logger.exception('Не удалось отправить письмо о заявке #%s', lead.id)
