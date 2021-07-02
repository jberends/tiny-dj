from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.viewsets import ModelViewSet

from shorturl.models import ShortUrl


class ShortUrlSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShortUrl
        fields = '__all__'


class ShortUrlViewSet(ModelViewSet):
    """
    API endpoint for the URL shortener
    """
    queryset = ShortUrl.objects.all()
    serializer_class = ShortUrlSerializer
