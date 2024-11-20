from rest_framework import serializers

from .models import Toy


class ToysListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = (
            'id',
            'name',
            'price',
            'display_age',
            'image_url'
        )


class ToysDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = (
            'id',
            'name',
            'description',
            'price',
            'display_age',
            'image_url',
            'amazon_link'
        )
