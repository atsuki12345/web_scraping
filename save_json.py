import json
cities = [
    {'rank':1,'city':'Shanghai','population':1234567890},
    {'rank':2,'city':'Beigin','population':1234567},
    {'rank':3,'city':'Tokyo','population':7890}
]

print(json.dumps(cities,ensure_ascii=False,indent=2))