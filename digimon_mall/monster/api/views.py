from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from ..models import (
    Generation,
    Kinds,
    Attribute,
    Monster,
    List
)
from .serializers import (
    GenerationSerializer,
    KindsSerializer,
    AttributeSerializer,
    MonsterSerializer,
    ListSerializer
)


class GenerationViewSet(viewsets.ModelViewSet):
    queryset = Generation.objects.all()
    serializer_class = GenerationSerializer

    @action(detail=True)
    def mons(self, request, *args, **kwargs):
        gener = self.get_object()
        serializer = ListSerializer(gener.monsters.all(), many=True)
        return Response(serializer.data)

class KindsViewSet(viewsets.ModelViewSet):
    queryset = Kinds.objects.all()
    serializer_class = KindsSerializer

class AttributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer

class MonsterViewSet(viewsets.ModelViewSet):
    queryset = Monster.objects.all()
    serializer_class = MonsterSerializer

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
