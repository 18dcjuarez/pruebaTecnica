from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from pruebatecnica.utils.responses import create_response
from .serializers import CreateAccountSerializer
from .models import Account
from .displays import RespSerializerAccount
from pruebatecnica.utils.validators import (get_by_account, get_by_owner)
import coreapi
from rest_framework.schemas import AutoSchema


class AccountViewSchema(AutoSchema):

    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post']:
            extra_fields = [
                coreapi.Field('account'),
                coreapi.Field('balance'),
                coreapi.Field('owner'),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class AccountViewSet(viewsets.ViewSet):

    schema = AccountViewSchema()

    def create(self, request):
        serializer = CreateAccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            result = serializer.create(serializer.validated_data)
            return create_response(True, 201, result, '', 0)
        except Exception as err:
            return create_response(False, 500, {}, err, 0)

    def list(self, request):
        accounts = Account.objects.all()
        serializer = RespSerializerAccount(accounts, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def get_by_account(self, request, pk):
        user_account = get_by_account(pk)
        return Response(
            status=HTTP_200_OK,
            data={'balance': {
                'account': user_account.account,
                'balance': user_account.balance,
                'owner': user_account.owner,
                'createdAt': user_account.createdAt
            }}
        )

    @action(detail=True, methods=['GET'])
    def get_by_owner(self, request, pk):
        user_account = get_by_owner(pk)
        return Response(
            status=HTTP_200_OK,
            data={'balance': {
                'account': user_account.account,
                'balance': user_account.balance,
                'owner': user_account.owner,
                'createdAt': user_account.createdAt
            }}
        )


