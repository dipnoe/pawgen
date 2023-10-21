import datetime

from django import template

register = template.Library()


@register.filter()
def nice_date(date):
    if isinstance(date, datetime.datetime):
        return date.strftime("%d %b")


@register.simple_tag()
def mediapath(image):
    if image:
        return f'/media/{image}'
