# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Kmmaccounts(models.Model):
    id = models.CharField(unique=True, max_length=32, primary_key=True)
    institutionid = models.CharField(
        db_column="institutionId", max_length=32, blank=True, null=True
    )  # Field name made lowercase.
    parentid = models.CharField(
        db_column="parentId", max_length=32, blank=True, null=True
    )  # Field name made lowercase.
    lastreconciled = models.TextField(
        db_column="lastReconciled", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    lastmodified = models.TextField(
        db_column="lastModified", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    openingdate = models.DateField(
        db_column="openingDate", blank=True, null=True
    )  # Field name made lowercase.
    accountnumber = models.TextField(
        db_column="accountNumber", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    accounttype = models.CharField(
        db_column="accountType", max_length=16
    )  # Field name made lowercase.
    accounttypestring = models.TextField(
        db_column="accountTypeString", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    isstockaccount = models.CharField(
        db_column="isStockAccount", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    accountname = models.TextField(
        db_column="accountName", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    currencyid = models.CharField(
        db_column="currencyId", max_length=32, blank=True, null=True
    )  # Field name made lowercase.
    balance = models.TextField(blank=True, null=True)  # This field type is a guess.
    balanceformatted = models.TextField(
        db_column="balanceFormatted", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    transactioncount = models.TextField(
        db_column="transactionCount", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = "kmmAccounts"


class Kmmbudgetconfig(models.Model):
    id = models.CharField(unique=True, max_length=32, primary_key=True)
    name = models.TextField()
    start = models.DateField()
    xml = models.TextField(
        db_column="XML", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = "kmmBudgetConfig"


class Kmmcurrencies(models.Model):
    isocode = models.CharField(
        db_column="ISOcode", unique=True, max_length=3
    )  # Field name made lowercase.
    name = models.TextField()
    type = models.PositiveSmallIntegerField(blank=True, null=True)
    typestring = models.TextField(
        db_column="typeString", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    symbol1 = models.PositiveSmallIntegerField(blank=True, null=True)
    symbol2 = models.PositiveSmallIntegerField(blank=True, null=True)
    symbol3 = models.PositiveSmallIntegerField(blank=True, null=True)
    symbolstring = models.CharField(
        db_column="symbolString", max_length=255, blank=True, null=True
    )  # Field name made lowercase.
    partsperunit = models.CharField(
        db_column="partsPerUnit", max_length=24, blank=True, null=True
    )  # Field name made lowercase.
    smallestcashfraction = models.CharField(
        db_column="smallestCashFraction", max_length=24, blank=True, null=True
    )  # Field name made lowercase.
    smallestaccountfraction = models.CharField(
        db_column="smallestAccountFraction", max_length=24, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        db_table = "kmmCurrencies"


class Kmmfileinfo(models.Model):
    version = models.CharField(max_length=16, blank=True, null=True)
    created = models.DateField(blank=True, null=True)
    lastmodified = models.DateField(
        db_column="lastModified", blank=True, null=True
    )  # Field name made lowercase.
    basecurrency = models.CharField(
        db_column="baseCurrency", max_length=3, blank=True, null=True
    )  # Field name made lowercase.
    institutions = models.TextField(
        blank=True, null=True
    )  # This field type is a guess.
    accounts = models.TextField(blank=True, null=True)  # This field type is a guess.
    payees = models.TextField(blank=True, null=True)  # This field type is a guess.
    transactions = models.TextField(
        blank=True, null=True
    )  # This field type is a guess.
    splits = models.TextField(blank=True, null=True)  # This field type is a guess.
    securities = models.TextField(blank=True, null=True)  # This field type is a guess.
    prices = models.TextField(blank=True, null=True)  # This field type is a guess.
    currencies = models.TextField(blank=True, null=True)  # This field type is a guess.
    schedules = models.TextField(blank=True, null=True)  # This field type is a guess.
    reports = models.TextField(blank=True, null=True)  # This field type is a guess.
    kvps = models.TextField(blank=True, null=True)  # This field type is a guess.
    daterangestart = models.DateField(
        db_column="dateRangeStart", blank=True, null=True
    )  # Field name made lowercase.
    daterangeend = models.DateField(
        db_column="dateRangeEnd", blank=True, null=True
    )  # Field name made lowercase.
    hiinstitutionid = models.TextField(
        db_column="hiInstitutionId", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    hipayeeid = models.TextField(
        db_column="hiPayeeId", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    hiaccountid = models.TextField(
        db_column="hiAccountId", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    hitransactionid = models.TextField(
        db_column="hiTransactionId", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    hischeduleid = models.TextField(
        db_column="hiScheduleId", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    hisecurityid = models.TextField(
        db_column="hiSecurityId", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    hireportid = models.TextField(
        db_column="hiReportId", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    encryptdata = models.CharField(
        db_column="encryptData", max_length=255, blank=True, null=True
    )  # Field name made lowercase.
    updateinprogress = models.CharField(
        db_column="updateInProgress", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    budgets = models.TextField(blank=True, null=True)  # This field type is a guess.
    hibudgetid = models.TextField(
        db_column="hiBudgetId", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    logonuser = models.CharField(
        db_column="logonUser", max_length=255, blank=True, null=True
    )  # Field name made lowercase.
    logonat = models.TextField(
        db_column="logonAt", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    fixlevel = models.TextField(
        db_column="fixLevel", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = "kmmFileInfo"


class Kmminstitutions(models.Model):
    id = models.CharField(unique=True, max_length=32, primary_key=True)
    name = models.TextField()
    manager = models.TextField(blank=True, null=True)  # This field type is a guess.
    routingcode = models.TextField(
        db_column="routingCode", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    addressstreet = models.TextField(
        db_column="addressStreet", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    addresscity = models.TextField(
        db_column="addressCity", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    addresszipcode = models.TextField(
        db_column="addressZipcode", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    telephone = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        db_table = "kmmInstitutions"


class Kmmkeyvaluepairs(models.Model):
    kvptype = models.CharField(
        db_column="kvpType", max_length=16
    )  # Field name made lowercase.
    kvpid = models.CharField(
        db_column="kvpId", max_length=32, blank=True, null=True
    )  # Field name made lowercase.
    kvpkey = models.CharField(
        db_column="kvpKey", max_length=255
    )  # Field name made lowercase.
    kvpdata = models.TextField(
        db_column="kvpData", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = "kmmKeyValuePairs"


class Kmmpayees(models.Model):
    id = models.CharField(unique=True, max_length=32, primary_key=True)
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    reference = models.TextField(blank=True, null=True)  # This field type is a guess.
    email = models.TextField(blank=True, null=True)  # This field type is a guess.
    addressstreet = models.TextField(
        db_column="addressStreet", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    addresscity = models.TextField(
        db_column="addressCity", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    addresszipcode = models.TextField(
        db_column="addressZipcode", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    addressstate = models.TextField(
        db_column="addressState", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    telephone = models.TextField(blank=True, null=True)  # This field type is a guess.
    notes = models.TextField(blank=True, null=True)  # This field type is a guess.
    defaultaccountid = models.CharField(
        db_column="defaultAccountId", max_length=32, blank=True, null=True
    )  # Field name made lowercase.
    matchdata = models.TextField(
        db_column="matchData", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    matchignorecase = models.CharField(
        db_column="matchIgnoreCase", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    matchkeys = models.TextField(
        db_column="matchKeys", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = "kmmPayees"


class Kmmprices(models.Model):
    fromid = models.CharField(
        db_column="fromId", max_length=32
    )  # Field name made lowercase.
    toid = models.CharField(
        db_column="toId", max_length=32
    )  # Field name made lowercase.
    pricedate = models.DateField(db_column="priceDate")  # Field name made lowercase.
    price = models.TextField()
    priceformatted = models.TextField(
        db_column="priceFormatted", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    pricesource = models.TextField(
        db_column="priceSource", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = "kmmPrices"

    unique_together = (("fromid", "toid", "pricedate"),)


class Kmmreportconfig(models.Model):
    name = models.CharField(max_length=255)
    xml = models.TextField(
        db_column="XML", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    id = models.CharField(unique=True, max_length=32, primary_key=True)

    class Meta:
        db_table = "kmmReportConfig"


class Kmmschedulepaymenthistory(models.Model):
    schedid = models.CharField(
        db_column="schedId", max_length=32
    )  # Field name made lowercase.
    paydate = models.DateField(db_column="payDate")  # Field name made lowercase.

    class Meta:
        db_table = "kmmSchedulePaymentHistory"

    unique_together = (("schedid", "paydate"),)


class Kmmschedules(models.Model):
    id = models.CharField(unique=True, max_length=32, primary_key=True)
    name = models.TextField()
    type = models.TextField()  # This field type is a guess.
    typestring = models.TextField(
        db_column="typeString", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    occurence = models.PositiveSmallIntegerField()
    occurencemultiplier = models.PositiveSmallIntegerField(
        db_column="occurenceMultiplier"
    )  # Field name made lowercase.
    occurencestring = models.TextField(
        db_column="occurenceString", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    paymenttype = models.TextField(
        db_column="paymentType", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    paymenttypestring = models.TextField(
        db_column="paymentTypeString", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    startdate = models.DateField(db_column="startDate")  # Field name made lowercase.
    enddate = models.DateField(
        db_column="endDate", blank=True, null=True
    )  # Field name made lowercase.
    fixed = models.CharField(max_length=1)
    autoenter = models.CharField(
        db_column="autoEnter", max_length=1
    )  # Field name made lowercase.
    lastpayment = models.DateField(
        db_column="lastPayment", blank=True, null=True
    )  # Field name made lowercase.
    nextpaymentdue = models.DateField(
        db_column="nextPaymentDue", blank=True, null=True
    )  # Field name made lowercase.
    weekendoption = models.TextField(
        db_column="weekendOption"
    )  # Field name made lowercase. This field type is a guess.
    weekendoptionstring = models.TextField(
        db_column="weekendOptionString", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = "kmmSchedules"


class Kmmsecurities(models.Model):
    id = models.CharField(unique=True, max_length=32, primary_key=True)
    name = models.TextField()
    symbol = models.TextField(blank=True, null=True)  # This field type is a guess.
    type = models.PositiveSmallIntegerField()
    typestring = models.TextField(
        db_column="typeString", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    smallestaccountfraction = models.CharField(
        db_column="smallestAccountFraction", max_length=24, blank=True, null=True
    )  # Field name made lowercase.
    tradingmarket = models.TextField(
        db_column="tradingMarket", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    tradingcurrency = models.CharField(
        db_column="tradingCurrency", max_length=3, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        db_table = "kmmSecurities"


class Kmmsplits(models.Model):
    id = models.CharField(unique=True, max_length=32, primary_key=True)
    transactionid = models.CharField(
        db_column="transactionId", max_length=32
    )  # Field name made lowercase.
    txtype = models.CharField(
        db_column="txType", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    splitid = models.PositiveSmallIntegerField(
        db_column="splitId"
    )  # Field name made lowercase.
    # payeeid = models.CharField(
    #    db_column="payeeId", max_length=32, blank=True, null=True
    # )  # Field name made lowercase.
    payeeid = models.ForeignKey(
        Kmmpayees, db_column="payeeid", on_delete=models.DO_NOTHING
    )
    reconciledate = models.TextField(
        db_column="reconcileDate", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    action = models.CharField(max_length=16, blank=True, null=True)
    reconcileflag = models.CharField(
        db_column="reconcileFlag", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    value = models.TextField()
    valueformatted = models.TextField(
        db_column="valueFormatted", blank=True, null=True
    )  # Field name made lowercase.
    shares = models.TextField()
    sharesformatted = models.TextField(
        db_column="sharesFormatted", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    price = models.TextField(blank=True, null=True)
    priceformatted = models.TextField(
        db_column="priceFormatted", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    memo = models.TextField(blank=True, null=True)  # This field type is a guess.
    accountid = models.CharField(
        db_column="accountId", max_length=32
    )  # Field name made lowercase.
    checknumber = models.CharField(
        db_column="checkNumber", max_length=32, blank=True, null=True
    )  # Field name made lowercase.
    postdate = models.TextField(
        db_column="postDate", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    bankid = models.TextField(
        db_column="bankId", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = "kmmSplits"

    unique_together = (("transactionid", "splitid"),)


class Kmmtransactions(models.Model):
    id = models.CharField(unique=True, max_length=32, primary_key=True)
    txtype = models.CharField(
        db_column="txType", max_length=1, blank=True, null=True
    )  # Field name made lowercase.
    postdate = models.TextField(
        db_column="postDate", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    memo = models.TextField(blank=True, null=True)  # This field type is a guess.
    entrydate = models.TextField(
        db_column="entryDate", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    currencyid = models.CharField(
        db_column="currencyId", max_length=3, blank=True, null=True
    )  # Field name made lowercase.
    bankid = models.TextField(
        db_column="bankId", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = "kmmTransactions"
