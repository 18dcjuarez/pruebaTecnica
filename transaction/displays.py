from rest_framework import serializers


class RespSerializerTransaction(serializers.Serializer):

    fromAccount = serializers.CharField()
    toAccount = serializers.CharField()
    amount = serializers.FloatField()
    sentAt = serializers.DateTimeField()

    class Meta:
        fields = ('fromAccount', 'toAccount', 'amount', 'sentAt')
