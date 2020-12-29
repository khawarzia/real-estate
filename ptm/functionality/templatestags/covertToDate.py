from django import template

register = template.Library()   

from datetime import datetime


def covertToDate(value): # Only one argument.
    # print(value)
    try:
        return datetime.strptime(value, "%m/%d/%Y")
    except ValueError:
        return value
    
register.filter(covertToDate)