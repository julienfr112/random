import requests

from clickhouse_driver import Client
from datetime import date


c = Client("localhost")
c.execute("drop table if exists cache")
c.execute("create table cache(date Date,url String, content String) engine=MergeTree() partition by date order by url ")

url = "https://www.lemonde.fr"
content = requests.get("https://www.lemonde.fr").content

c.execute("insert into cache values", [(date.today(), url, content)])

print(c.execute("select * from cache"))
