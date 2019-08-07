from rest_framework import serializers

from ..models import (
    Generation,
    Kinds,
    Attribute,
    Monster,
    List
)


class GenerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generation
        fields = ['id', 'title']

class KindsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kinds
        fields = ['id', 'title']

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ['id', 'title']

class MonsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster
        fields = ['id', 'title', 'image']

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['id', 'gener', 'attri', 'kind', 'prev', 'monster', 'skill', 'desc', 'price']
