from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import LipiUserSerializer, LipiVerifyUserSerializer, LipiVerifyUserResponseSerializer

LipiUser = get_user_model()


@method_decorator(name='destroy', decorator=extend_schema(operation_id="Method deletes a user"))
@method_decorator(name='partial_update', decorator=extend_schema(operation_id="Method partially updates the "
                                                                              "details of a user"))
@method_decorator(name='update', decorator=extend_schema(operation_id="Method updates the details of a user"))
@method_decorator(name='retrieve', decorator=extend_schema(operation_id="Method retrieves the details of a user"))
@method_decorator(name='list', decorator=extend_schema(operation_id="Method returns a list of users"))
@method_decorator(name='create', decorator=extend_schema(operation_id="Method creates a user"))
class LipiAPIViewSet(ModelViewSet):
    queryset = LipiUser.objects.all()
    serializer_class = LipiUserSerializer

    @extend_schema(operation_id="Given a list of user ids method returns a  list of invalid user ids",
                   request=LipiVerifyUserSerializer, responses={'200': LipiVerifyUserResponseSerializer})
    @action(methods=['POST'], detail=False)
    def verify(self, request):
        serializer = LipiVerifyUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_ids = serializer.validated_data['user_ids']
            valid_user_ids = LipiUser.objects.filter(pk__in=user_ids).values_list('pk', flat=True)
            invalid_user_ids = [_id for _id in user_ids if _id not in valid_user_ids]
            return Response(data=LipiVerifyUserResponseSerializer(invalid_user_ids).data, status=status.HTTP_200_OK)
