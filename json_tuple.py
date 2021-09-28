import json
f = open('plan_teste.json')
data = json.load(f)
f.close()
print(tuple(data.items()))