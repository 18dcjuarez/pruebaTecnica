from rest_framework import serializers
from pruebatecnica.utils.validators import (positive_number, find_account, validate_balance)
from .managers import TransactionManager


class CreateTransactionSerializer(serializers.Serializer):
    fromAccount = serializers.CharField(required=True)
    toAccount = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)

    class Meta:
        fields = ('fromAccount', 'toAccount', 'amount')

    def validate_amount(self, value):
        return positive_number(value)

    def validate_fromAccount(self, value):
        return find_account(value)

    def validate_toAccount(self, value):
        return find_account(value)

    def create(self, validated_data):
        transaction = TransactionManager.create(validated_data)
        return transaction
