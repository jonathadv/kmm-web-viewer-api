from attr import has
from rest_framework import serializers
from kmm.models import Kmmtransactions, Kmmsplits, Kmmpayees, Kmmaccounts

from enum import Enum


class AccountType(Enum):
    ASSET = "9"
    LIABILITY = "10"  # passivo
    INCOME = "12"
    EXPENSE = "13"
    EQUITY = "16"  # ação ordinaria


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
    account = serializers.SerializerMethodField()
    payee = serializers.SerializerMethodField()
    amount = serializers.SerializerMethodField()
    currency = serializers.SerializerMethodField()
    memo = serializers.SerializerMethodField()
    splits = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()

    def get_status(self, obj):
        splits = [x for x in obj.kmmsplits_set.all() if x.splitid == 1]
        if splits:
            split = splits[0]
            status = {"N": "normal", "S": "scheduled"}
            return status.get(split.txtype, "unknown")
        return None

    def get_splits(self, obj):
        splits = [
            {"id": x.id, "value": x.valueformatted, "account": x.accountid.accountname}
            for x in obj.kmmsplits_set.all()
        ]
        return splits

    def get_type(self, obj):
        splits = [x for x in obj.kmmsplits_set.all() if x.splitid == 1]
        if splits:
            split = splits[0]
            account_type = None

            for t in AccountType:
                if t.value == split.accountid.accounttype:
                    account_type = t.name
                    break

            return account_type
        return None

    def get_account(self, obj):
        split = [x for x in obj.kmmsplits_set.all() if x.splitid == 0][0]
        return split.accountid.accountname

    def get_payee(self, obj):
        splits = [x for x in obj.kmmsplits_set.all() if x.splitid == 1]
        if splits:
            split = splits[0]
            if hasattr(split, "payeeid"):
                return split.payeeid.name
        return None

    def get_amount(self, obj):
        split = [x for x in obj.kmmsplits_set.all() if x.splitid == 0][0]
        return split.valueformatted

    def get_currency(self, obj):
        return obj.currencyid

    def get_memo(self, obj):
        splits = [x for x in obj.kmmsplits_set.all() if x.splitid == 1]
        if splits:
            split = splits[0]
            return split.memo
        return None

    class Meta:
        model = Kmmtransactions
        fields = (
            "id",
            "status",
            "type",
            "memo",
            "currency",
            "account",
            "payee",
            "amount",
            "entrydate",
            "postdate",
            "splits",
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
            "id",
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
