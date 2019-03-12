from django.views.generic import View
from django.http import HttpRequest, HttpResponseRedirect

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


class IndexView(View):
    def get(self, request: Request, *args, **kwargs):
        return HttpResponseRedirect("/static/index.html")


class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = (
        Kmmtransactions.objects.prefetch_related("kmmsplits_set")
        .prefetch_related("kmmsplits_set__payeeid")
        .prefetch_related("kmmsplits_set__accountid")
        .all().order_by("-id")
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
        transactions = Kmmtransactions.objects.filter(kmmsplits__accountid=pk).order_by("-id")
        page = self.paginate_queryset(transactions)
        if page:
            serializer = TransactionSerializer(page, many=True)
            return self.get_paginated_response(data=serializer.data)

        serializer = TransactionSerializer(transactions, many=True)
        return Response(data=serializer.data)
