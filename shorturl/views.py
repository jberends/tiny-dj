# Create your views here.
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

        Hit(short_url=shortener).save()

        return HttpResponseRedirect(shortener.long_url)
    except ShortUrl.DoesNotExist:
        raise Http404("This short link does not exist :'(")
