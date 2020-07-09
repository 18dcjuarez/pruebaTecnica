from rest_framework import serializers
from pruebatecnica.utils.validators import (positive_number, account_exist, owner_exist)
from .managers import AccountManager


class CreateAccountSerializer(serializers.Serializer):
    account = serializers.CharField(required=True)
    balance = serializers.FloatField(required=True)
    owner = serializers.CharField(required=True)

    class Meta:
        fields = ('account', 'balance', 'owner')

    def validate_balance(self, value):
        return positive_number(value)

    def validate_account(self, value):
        return account_exist(value)

    def validate_owner(self, value):
        return owner_exist(value)

    def create(self, validated_data):
        account = AccountManager.create(validated_data)
        return account
