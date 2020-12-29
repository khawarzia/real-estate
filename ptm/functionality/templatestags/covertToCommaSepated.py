from django import template

register = template.Library()   

from datetime import datetime


def covertToCommaSepated(value): # Only one argument.
    # print(value)
    # return datetime.strptime(value, "%m/%d/%Y")
    A = ''
    for i in range(0, len(value), 3):
        A.join(value[i:i+2])
    
register.filter(covertToCommaSepated)