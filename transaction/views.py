from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from pruebatecnica.utils.responses import create_response
from pruebatecnica.utils.exceptions import ERROR_MIN_BALANCE
from .serializers import CreateTransactionSerializer
from .models import Transaction
from .displays import RespSerializerTransaction
from pruebatecnica.utils.validators import (get_by_account, get_by_owner)
import coreapi
from rest_framework.schemas import AutoSchema
from django.db.models import Q


class TransactionViewSchema(AutoSchema):

    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post']:
            extra_fields = [
                coreapi.Field('fromAccount'),
                coreapi.Field('toAccount'),
                coreapi.Field('amount'),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class TransactionViewSet(viewsets.ViewSet):

    schema = TransactionViewSchema()

    def create(self, request):
        serializer = CreateTransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            result = serializer.create(serializer.validated_data)
            if result == ERROR_MIN_BALANCE:
                return create_response(False, 400, result, '', 0)
            return create_response(True, 201, result, '', 0)
        except Exception as err:
            return create_response(False, 500, {}, err, 0)

    def list(self, request):
        accounts = Transaction.objects.all()
        serializer = RespSerializerTransaction(accounts, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def all_transactions(self, request, pk):
        user_transactions = Transaction.objects.filter(fromAccount=pk) | Transaction.objects.filter(toAccount=pk)
        serializer = RespSerializerTransaction(user_transactions, many=True)
        return Response(
            status=HTTP_200_OK,
            data=serializer.data
        )

    @action(detail=True, methods=['GET'])
    def made_transactions(self, request, pk):
        user_transactions = Transaction.objects.filter(fromAccount=pk)
        serializer = RespSerializerTransaction(user_transactions, many=True)
        return Response(
            status=HTTP_200_OK,
            data=serializer.data
        )

    @action(detail=True, methods=['GET'])
    def recibed_transactions(self, request, pk):
        user_transactions = Transaction.objects.filter(toAccount=pk)
        serializer = RespSerializerTransaction(user_transactions, many=True)
        return Response(
            status=HTTP_200_OK,
            data=serializer.data
        )