import feedparser

d = feedparser.parse('http://hatena.ne.jp/hotentry/it.rss')

for entry in d.entries:
    print(entry,link,entry.title)