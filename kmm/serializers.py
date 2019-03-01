from rest_framework import serializers
from kmm.models import Kmmtransactions, Kmmsplits, Kmmpayees


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kmmtransactions
        fields = (
            "id",
            "txtype",
            "postdate",
            "memo",
            "entrydate",
            "currencyid",
            "bankid",
        )


class SplitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kmmsplits
        fields = (
            "transactionid",
            "txtype",
            "splitid",
            "payeeid",
            "reconciledate",
            "action",
            "reconcileflag",
            "value",
            "valueformatted",
            "shares",
            "sharesformatted",
            "price",
            "priceformatted",
            "memo",
            "accountid",
            "checknumber",
            "postdate",
            "bankid",
        )


class PayeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kmmpayees
        fields = (
            "name",
            "reference",
            "email",
            "addressstreet",
            "addresscity",
            "addresszipcode",
            "addressstate",
            "telephone",
            "notes",
            "defaultaccountid",
            "matchdata",
            "matchignorecase",
            "matchkeys",
        )
