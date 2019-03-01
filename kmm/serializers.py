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
    pay_to = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    # kmmsplits_set = SplitSerializer(many=True, read_only=True)
    amount = serializers.SerializerMethodField()
    transaction_type = serializers.SerializerMethodField()

    def get_transaction_type(self, obj):
        split = obj.kmmsplits_set.all().filter(splitid=1)[0]
        type_options = {"N": "normal", "S": "scheduled"}
        account_type = None

        for t in AccountType:
            if t.value == split.accountid.accounttype:
                account_type = t.name

        result = {
            "type": type_options.get(split.txtype, "unknown"),
            "value_type": account_type,
        }

        return result

    def get_account(self, obj):
        split = obj.kmmsplits_set.all().filter(splitid=0)[0]
        return split.accountid.accountname

    def get_pay_to(self, obj):
        split = obj.kmmsplits_set.all().filter(splitid=1)[0]
        return split.payeeid.name

    def get_category(self, obj):
        split = obj.kmmsplits_set.all().filter(splitid=1)[0]
        return split.accountid.accountname

    def get_amount(self, obj):
        split = obj.kmmsplits_set.all().filter(splitid=1)[0]
        return split.valueformatted

    class Meta:
        model = Kmmtransactions
        fields = (
            "id",
            "transaction_type",
            "memo",
            "currencyid",
            "account",
            "pay_to",
            "category",
            "amount",
            # "kmmsplits_set",
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
