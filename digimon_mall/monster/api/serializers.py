from rest_framework import serializers

from ..models import (
    Generation,
    Kinds,
    Attribute,
    Monster,
    List,
    UserMonster
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
    gener = GenerationSerializer()
    attri = AttributeSerializer()
    kind = KindsSerializer()
    prev = MonsterSerializer()
    monster = MonsterSerializer()
    class Meta:
        model = List
        fields = ['id', 'gener', 'attri', 'kind', 'prev', 'monster', 'skill', 'desc', 'price']

class UserMonsterSerializer(serializers.ModelSerializer):
    list = ListSerializer()

    class Meta:
        model = UserMonster
        fields = ['list', 'user', 'count', 'times']

