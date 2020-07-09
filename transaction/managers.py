from rest_framework import serializers
from pruebatecnica.utils.exceptions import (GeneralError, ERROR_TRANSACTION)
from .displays import RespSerializerTransaction
from .models import Transaction
from account.models import Account
from pruebatecnica.utils.validators import validate_balance


class TransactionManager:

    @staticmethod
    def create(transaction_data):
        from_account = transaction_data['fromAccount']
        to_account = transaction_data['toAccount']
        amount = transaction_data['amount']
        new_transaction = {}
        user_from_account = Account.objects.get(account=from_account)
        user_to_account = Account.objects.get(account=to_account)
        try:
            if validate_balance(from_account, amount) != 'ok':
                return validate_balance(from_account, amount)
            user_from_account.balance = user_from_account.balance - amount
            user_from_account.save()
            user_to_account.balance = user_to_account.balance + amount
            user_to_account.save()
            new_transaction = Transaction.objects.create(
                fromAccount=from_account,
                toAccount=to_account,
                amount=amount,
            )
            new_transaction.save()
            return RespSerializerTransaction(new_transaction).data
        except Exception as e:
            user_from_account.balance = user_from_account.balance + amount
            user_from_account.save()
            user_to_account.balance = user_to_account.balance - amount
            user_to_account.save()
            new_transaction.delete()
            raise serializers.ValidationError(GeneralError(ERROR_TRANSACTION).error)
