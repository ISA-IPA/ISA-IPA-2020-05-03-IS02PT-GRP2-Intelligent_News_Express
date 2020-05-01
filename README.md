# ISA-CA1-Intelligent-News-express

New York Times - Tagui

BBC News - API

StraitTimes - Tagui

Today Online - Tagui

--

Library:
pip install apscheduler==2.1.2
pip install sqlite3


SQL query
```
CREATE TABLE "site" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT NOT NULL UNIQUE,
	"base_url"	TEXT NOT NULL
);

CREATE TABLE "news" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"site_id"	INTEGER,
	"create_date"	TEXT,
	"title"	TEXT,
	"url"	TEXT,
	"summary"	TEXT,
	FOREIGN KEY("site_id") REFERENCES "site"("id")
);
```

![](images/cloud_word_output_2.png?raw=true)

