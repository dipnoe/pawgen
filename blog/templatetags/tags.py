import datetime

from django import template

register = template.Library()


@register.filter()
def nice_date(date):
    if isinstance(date, datetime.datetime):
        return date.strftime("%d %b")
