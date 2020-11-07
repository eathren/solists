from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()
@register.filter(is_safe=True)
@stringfilter
def upto(value, delimiter=None):
    return value.split(delimiter)[0].replace("days", "d").replace("day","d").replace("weeks","w").replace("week","w").replace("months","m").replace("minutes","m").replace("month","m").replace("minute","m").replace("\xa0","")