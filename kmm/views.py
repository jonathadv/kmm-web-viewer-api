from rest_framework import viewsets
from kmm.models import Kmmtransactions, Kmmsplits
from kmm.serializers import TransactionSerializer, SplitSerializer


class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = Kmmtransactions.objects.all()
    serializer_class = TransactionSerializer


class SplitsViewSet(viewsets.ModelViewSet):
    queryset = Kmmsplits.objects.all()
    serializer_class = SplitSerializer