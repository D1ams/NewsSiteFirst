from django import template

register = template.Library()

Curse_words = ['старший', 'зенит', 'причин']


@register.filter()
def censor(text):
    filtered_text = ''
    text = text.split()
    for word in text:
        if word.lower() in Curse_words:
            filtered_text += word[0]
            for _ in word[:-1]:
                filtered_text += '*'
        else:
            filtered_text += word
        filtered_text += ' '
    return filtered_text

