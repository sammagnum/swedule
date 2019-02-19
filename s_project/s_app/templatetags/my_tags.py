from django import template

register = template.Library()


@register.filter
def fixtime(num):
    if num == 0:
        return 12
    if num > 24:
        return num % 25 + 1
    if num > 12:
        return num % 13 + 1
    return num


@register.filter
def flip(flag):
    if flag is "False":
        return "True"
    return "False"
