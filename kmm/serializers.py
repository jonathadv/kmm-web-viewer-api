from rest_framework import serializers
from kmm.models import Kmmtransactions, Kmmsplits, Kmmpayees, Kmmaccounts


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


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    kmmsplits_set = SplitSerializer(many=True, read_only=True)

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
            "kmmsplits_set",
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


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kmmaccounts
        fields = (
            "institutionid",
            "parentid",
            "lastreconciled",
            "lastmodified",
            "openingdate",
            "accountnumber",
            "accounttype",
            "accounttypestring",
            "isstockaccount",
            "accountname",
            "description",
            "currencyid",
            "balance",
            "balanceformatted",
            "transactioncount",
        )
