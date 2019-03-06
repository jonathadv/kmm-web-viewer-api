# kmymoney-web-viewer
A web viewer for kMyMoney database


Open kmymoney with sqlite file:
```bash
kmymoney sql:/path/to/file/kmm.sqlite3?driver=QSQLITE
```

Changes `timestamp` fields to `date` fields in sqlite.

```sql
PRAGMA foreign_keys=off;
ALTER TABLE kmmTransactions RENAME TO _table1_old;

CREATE TABLE kmmTransactions (id varchar(32) NOT NULL, txType char(1), postDate date, memo mediumtext, entryDate date, currencyId char(3), bankId mediumtext, PRIMARY KEY (id));

INSERT INTO kmmTransactions (id, txType, postDate, memo, entryDate, currencyId, bankId)
  SELECT id, txType, postDate, memo, entryDate, currencyId, bankId
  FROM _table1_old;

DROP TABLE _table1_old;
  
PRAGMA foreign_keys=on;
```
