from django import template

register = template.Library()   

from datetime import datetime


def covertToDate(value): # Only one argument.
    return datetime.strptime(value, "%a, %b %d %Y")
    
register.filter(covertToDate)