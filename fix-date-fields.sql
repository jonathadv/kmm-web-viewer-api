PRAGMA foreign_keys=off;
------------------------


ALTER TABLE kmmAccounts RENAME TO _kmmAccounts_old;
CREATE TABLE kmmAccounts (
        id varchar(32) NOT NULL,
        institutionId varchar(32),
        parentId varchar(32),
        lastReconciled date,
        lastModified date,
        openingDate date,
        accountNumber mediumtext,
        accountType varchar(16) NOT NULL,
        accountTypeString mediumtext,
        isStockAccount char(1),
        accountName mediumtext,
        description mediumtext,
        currencyId varchar(32),
        balance mediumtext,
        balanceFormatted mediumtext,
        transactionCount bigint unsigned,
        PRIMARY KEY (id));
INSERT INTO kmmAccounts (id, institutionId, parentId, lastReconciled, lastModified, openingDate,
                         accountNumber, accountType, accountTypeString, isStockAccount, accountName,
                         description, currencyId, balance, balanceFormatted, transactionCount)
SELECT id, institutionId, parentId, lastReconciled, lastModified, openingDate,
       accountNumber, accountType, accountTypeString, isStockAccount, accountName,
       description, currencyId, balance, balanceFormatted, transactionCount
FROM _kmmAccounts_old;
DROP TABLE _kmmAccounts_old;

-----------------------------------------------------------------------

ALTER TABLE kmmTransactions RENAME TO _kmmTransactions_old;
CREATE TABLE kmmTransactions (id varchar(32) NOT NULL, txType char(1), postDate date, memo mediumtext, entryDate date, currencyId char(3), bankId mediumtext, PRIMARY KEY (id));
INSERT INTO kmmTransactions (id, txType, postDate, memo, entryDate, currencyId, bankId)
  SELECT id, txType, postDate, memo, entryDate, currencyId, bankId
  FROM _kmmTransactions_old;
DROP TABLE _kmmTransactions_old;

-----------------------------------------------------------------------

ALTER TABLE kmmSplits RENAME TO _kmmSplits_old;

CREATE TABLE kmmSplits (
    transactionId varchar ( 32 ) NOT NULL,
    txType char ( 1 ),
    splitId smallint unsigned NOT NULL,
    payeeId varchar ( 32 ),
    reconcileDate date,
    action varchar ( 16 ),
    reconcileFlag char ( 1 ),
    "value" text NOT NULL,
    valueFormatted text,
    shares text NOT NULL,
    sharesFormatted mediumtext,
    price text,
    priceFormatted mediumtext,
    memo mediumtext,
    accountId varchar ( 32 ) NOT NULL,
    costCenterId varchar ( 32 ),
    checkNumber varchar ( 32 ),
    postDate date,
    bankId mediumtext,
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT );

INSERT INTO kmmSplits (id,
 transactionId, txType, splitId, payeeId, reconcileDate, action, reconcileFlag, "value", valueFormatted, shares,
 sharesFormatted, price, priceFormatted, memo, accountId, costCenterId, checkNumber, postDate, bankId)
    SELECT id,transactionId, txType, splitId, payeeId, reconcileDate, action, reconcileFlag, "value", valueFormatted, shares,
    sharesFormatted, price, priceFormatted, memo, accountId, costCenterId, checkNumber, postDate, bankId
    FROM _kmmSplits_old;
DROP TABLE _kmmSplits_old

----------------------------------------------------------------------



------------------------
PRAGMA foreign_keys=on;