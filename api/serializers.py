from rest_framework import serializers

from bitlyclone.models import ShortUrl


class ShortUrlListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortUrl
        fields = '__all__'

class ShortUrlDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortUrl
        fields = '__all__'