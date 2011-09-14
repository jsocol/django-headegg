from random import choice
import re

try:
    from django.conf import settings
except ImportError:
    settings = None


if hasattr(settings, 'HEADEGG_QUOTES'):
    QUOTES = settings.HEADEGG_QUOTES
else:
    QUOTES = (
        ('Zoidberg', 'Why not Zoidberg?'),
    )


class HeadEgg(object):
    def process_response(self, request, response):
        key, value = choice(QUOTES)
        safe_key = 'X-' + re.sub(r'\W+', '-', key)
        response[safe_key] = value
        return response
