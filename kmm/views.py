from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from kmm.models import Kmmtransactions, Kmmsplits, Kmmpayees, Kmmaccounts
from kmm.serializers import (
    TransactionSerializer,
    SplitSerializer,
    PayeeSerializer,
    AccountSerializer,
)


class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = (
        Kmmtransactions.objects.prefetch_related("kmmsplits_set")
        .prefetch_related("kmmsplits_set__payeeid")
        .prefetch_related("kmmsplits_set__accountid")
        .all()
    )
    serializer_class = TransactionSerializer


class SplitsViewSet(viewsets.ModelViewSet):

    queryset = Kmmsplits.objects.all()
    serializer_class = SplitSerializer


class PayeeViewSet(viewsets.ModelViewSet):
    queryset = Kmmpayees.objects.all()
    serializer_class = PayeeSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Kmmaccounts.objects.all()
    serializer_class = AccountSerializer

    @action(detail=True, url_path="transactions", methods=["get"], name="list user groups")
    def transactions(self, request: Request, pk):
        transactions = Kmmtransactions.objects.filter(kmmsplits__accountid=pk)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(data=serializer.data)
