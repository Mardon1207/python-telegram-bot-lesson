import json

data= {
    "like":0,
    "dislike":0
}
f = open('data.json','w+')
y=json.dumps(data)
f.write(y)

print(y)