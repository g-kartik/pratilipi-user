from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from .serializers import LipiUserSerializer, LipiVerifyUserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

LipiUser = get_user_model()


class LipiAPIViewSet(ModelViewSet):
    queryset = LipiUser.objects.all()
    serializer_class = LipiUserSerializer

    @action(methods=['POST'], detail=False)
    def verify(self, request):
        serializer = LipiVerifyUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_ids = serializer.validated_data['user_ids']
            valid_user_ids = LipiUser.objects.filter(pk__in=user_ids).values_list('pk', flat=True)
            invalid_user_ids = [_id for _id in user_ids if _id not in valid_user_ids]
            return Response(data={'invalid_user_ids': invalid_user_ids}, status=status.HTTP_200_OK)
