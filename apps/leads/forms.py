import logging
from django import forms

logger = logging.getLogger(__name__)

REQUIRED_BY_SOURCE = {
    'main': ['name', 'email'],
    'contact-demo': ['name', 'email'],
    'contact-calc': ['name', 'email'],
    'product-question': ['name', 'email'],
}


def validate_lead_data(source: str, data: dict) -> list:
    """Возвращает список ошибок (пустой при успехе)."""
    errors = []
    required = REQUIRED_BY_SOURCE.get(source, ['name', 'email'])
    for field in required:
        if not (data.get(field) or '').strip():
            errors.append(f'Поле "{field}" обязательно.')
    return errors
