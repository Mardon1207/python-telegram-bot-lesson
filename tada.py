import json

f = open('data.json','r').read()
y=json.loads(f)

print(y)