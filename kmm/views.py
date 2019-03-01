from rest_framework import viewsets
from kmm.models import Kmmtransactions, Kmmsplits, Kmmpayees
from kmm.serializers import TransactionSerializer, SplitSerializer, PayeeSerializer


class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = Kmmtransactions.objects.all()
    serializer_class = TransactionSerializer


class SplitsViewSet(viewsets.ModelViewSet):
    queryset = Kmmsplits.objects.all()
    serializer_class = SplitSerializer


class PayeeViewSet(viewsets.ModelViewSet):
    queryset = Kmmpayees.objects.all()
    serializer_class = PayeeSerializer
