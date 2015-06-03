import datetime
from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    return value.replace(arg,"*")

@register.filter
def lower(value):
    return value.lower()

# {{ current_time %Y-%m-%d %H:%M:%S }}

@register.tag(name='current_time')
def do_current_time(parser,token):
    try:
        tag_name,format_string = token.split_contents()
    except:
        raise template.TemplateSyntaxError("syntax")

    return CurrentTimeNode(format_string[1:-1])

class CurrentTimeNode(template.Node):
    def __init__(self, format_string):
        self.format_string = str(format_string)

    def render(self, context):
        now = datetime.datetime.now()
        return now.strftime(self.format_string)
