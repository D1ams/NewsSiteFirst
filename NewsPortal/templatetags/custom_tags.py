from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def get_url_isabsolute(context):
    d = context['request'].GET.copy()
    return bool(d)
