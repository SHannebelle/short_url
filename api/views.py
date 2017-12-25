from rest_framework.generics import ListAPIView, RetrieveAPIView
from bitlyclone.models import ShortUrl
from .serializers import ShortUrlListSerializer, ShortUrlDetailSerializer



class ShortUrlDetailAPIView(RetrieveAPIView):
    queryset = ShortUrl.objects.all()
    serializer_class = ShortUrlDetailSerializer

class ShortUrlListAPIView(ListAPIView):
    queryset = ShortUrl.objects.all()
    serializer_class = ShortUrlListSerializer

