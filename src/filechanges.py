#!/usr/bin/env python
from persist.database import init_sqlite

db_cursor = init_sqlite('data/db.sqlite3')

print(db_cursor.connection)
print(db_cursor.__doc__)
db_cursor.connection.close()
