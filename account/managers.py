from django.db import models
from rest_framework import serializers
from .models import Account
from pruebatecnica.utils.exceptions import (GeneralError, ERROR_OBJECT_NOT_CREATED)
from .displays import RespSerializerAccount


class AccountManager:

    @staticmethod
    def create(account_data):
        account = account_data['account']
        balance = account_data['balance']
        owner = account_data['owner']
        new_account = {}
        try:
            new_account = Account.objects.create(
                account=account,
                balance=balance,
                owner=owner
            )
            new_account.save()
            return RespSerializerAccount(new_account).data
        except Exception as e:
            new_account.delete()
            raise serializers.ValidationError(GeneralError(ERROR_OBJECT_NOT_CREATED).error)
