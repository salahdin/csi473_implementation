from django.core.exceptions import ValidationError
from datetime import date

def validate_reservation_date(value):
    if value > date.today():
        raise ValidationError("invalid date")
    else:
        return value