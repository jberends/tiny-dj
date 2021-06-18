from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.viewsets import ModelViewSet

from urlshortener.models import ShortUrl


class UrlShortenerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShortUrl
        fields = "__all__"


class UrlShortenerViewSet(ModelViewSet):
    """
    API endpoint for the URL shortener
    """
    queryset = ShortUrl.objects.all()
    serializer_class = UrlShortenerSerializer
