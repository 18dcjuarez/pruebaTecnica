from rest_framework import serializers
from pruebatecnica.utils.exceptions import (ERROR_VALUE_LESS_THAN_CERO, ERROR_ACCOUNT_ALREADY_EXIST,
                                            ERROR_OWNER_ALREADY_EXIST, ERROR_ACCOUNT_DONT_EXIST,
                                            ERROR_OWNER_DONT_EXIST, ERROR_MIN_BALANCE, GeneralError)
from account.models import Account


def positive_number(value):
    if value < 0:
        raise serializers.ValidationError(ERROR_VALUE_LESS_THAN_CERO)
    return value


def account_exist(account):
    if Account.objects.filter(account=account).exists():
        raise serializers.ValidationError(ERROR_ACCOUNT_ALREADY_EXIST)
    else:
        return account


def owner_exist(owner):
    if Account.objects.filter(owner=owner).exists():
        raise serializers.ValidationError(ERROR_OWNER_ALREADY_EXIST)
    else:
        return owner


def get_by_account(account):
    if Account.objects.filter(account=account).exists():
        return Account.objects.get(account=account)
    else:
        raise serializers.ValidationError(ERROR_ACCOUNT_DONT_EXIST)


def get_by_owner(owner):
    if Account.objects.filter(owner=owner).exists():
        return Account.objects.get(owner=owner)
    else:
        raise serializers.ValidationError(ERROR_OWNER_DONT_EXIST)


def find_account(account):
    if Account.objects.filter(account=account).exists():
        return account


def validate_balance(from_account, amount):
    from_user = Account.objects.get(account=from_account)
    if from_user.balance - amount <= -500.0:
        return ERROR_MIN_BALANCE
    else:
        return 'ok'
