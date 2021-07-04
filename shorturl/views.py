# Create your views here.
import json
import re
from pprint import pprint
from typing import Iterable
from typing import Pattern

from django.http import Http404
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from shorturl.models import Hit
from shorturl.models import ShortUrl


def home_view(request):
    return HttpResponse('Hello World')


def redirect_url_view(request: HttpRequest, shortened_part: str):
    try:
        shortener = ShortUrl.objects.get(short_url=shortened_part)

        def _get_fields_from_meta(meta: dict, fields: Iterable) -> dict:
            """
            Retrieve fields from a dictionary.

            You may provide a valid regex
            """
            d = {}

            regexptrn = '|'.join([f'({field})' for field in fields])
            matcher: Pattern[str] = re.compile(regexptrn, flags=re.IGNORECASE)

            for key, val in meta.items():
                if matcher.match(key):
                    d[key] = val

            return d

        meta = _get_fields_from_meta(
            request.META,
            [
                'REMOTE_ADDR', 'REQUEST_METHOD', 'PATH_INFO', 'QUERY_STRING',
                'REMOTE_ADDR', 'CONTENT_TYPE', 'HTTP_HOST', 'HTTP_USER_AGENT',
                'HTTP_ACCEPT', 'HTTP_.*',
            ]
        )

        hit = Hit(short_url=shortener, remote_addr=request.META['REMOTE_ADDR'])
        pprint(json.dumps(meta, ensure_ascii=True, indent=2))
        hit.request_meta = meta
        hit.save()

        return HttpResponseRedirect(shortener.long_url)
    except ShortUrl.DoesNotExist:
        raise Http404("This short link does not exist :'(")
