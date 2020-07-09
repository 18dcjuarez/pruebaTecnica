from rest_framework import serializers
from .models import Account


class RespSerializerAccount(serializers.Serializer):

    account = serializers.CharField()
    balance = serializers.FloatField()
    owner = serializers.CharField()
    createdAt = serializers.DateTimeField()

    class Meta:
        fields = ('account', 'balance', 'owner', 'createdAt')
