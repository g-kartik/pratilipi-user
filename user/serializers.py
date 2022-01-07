from rest_framework import serializers
from django.contrib.auth import get_user_model

LipiUser = get_user_model()


class LipiUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = LipiUser
        fields = ['first_name', 'last_name', 'email', 'phone_number']


class LipiVerifyUserSerializer(serializers.Serializer):
    user_ids = serializers.ListField(child=serializers.IntegerField(), allow_empty=False, allow_null=False)
