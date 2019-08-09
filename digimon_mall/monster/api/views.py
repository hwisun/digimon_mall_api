from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import transaction

from ..models import (
    Generation,
    Kinds,
    Attribute,
    Monster,
    List,
    UserMonster
)
from .serializers import (
    GenerationSerializer,
    KindsSerializer,
    AttributeSerializer,
    MonsterSerializer,
    ListSerializer,
    UserMonsterSerializer
)


class GenerationViewSet(viewsets.ModelViewSet):
    queryset = Generation.objects.all()
    serializer_class = GenerationSerializer

    @action(detail=True)
    def mons(self, request, *args, **kwargs):
        gener = self.get_object()
        serializer = ListSerializer(gener.monsters.all(), many=True, context=self.get_serializer_context())
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['POST'])
    def purchase(self, request, *args, **kwargs):
        list = self.get_object()
        user = request.user
        if list.price > user.point:
            return Response(status=status.HTTP_402_PAYMENT_REQUIRED)
        user.point -= list.price
        user.save()
        try:
            user_mon = UserMonster.objects.get(user=user, list=list)
        except UserMonster.DoesNotExist:
            user_mon = UserMonster(user=user, list=list)
        user_mon.count += 1
        user_mon.save()

        serializer = UserMonsterSerializer(user.monsters.all(), many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    @action(detail=False, methods=['POST'], url_path='purchase')
    @transaction.atomic()
    def purchase_items(selfs, request, *args, **kwargs):
        mons = request.data['mons']
        user = request.user

        sid = transaction.savepoint()
        for i in mons:
            mons = mons.objects.get(id=i['mon_id'])
            count = int(i['count'])

            if mons.price * count > user.point:
                transaction.savepoint_rollback(sid)
                return Response(status=status.HTTP_402_PAYMENT_REQUIRED)
            user.point -= mons.price
            user.save()
            try:
                user_mons = UserMonster.objects.get(user=user, item=item)
            except UserMonster.DoesNotExist:
                user_mons = UserMonster(user=user, item=item)
            user_mons.count += count
            user_mons.save()
        transaction.savepoint_commit(sid)
        serializer = UserMonsterSerializer(user.items.all(), many=True, context=self.get_serializer_context())
        return Response(serializer.data)
