import json

# Deserialize
with open("file.json", "r") as f:
    a = json.load(f)

print(a), print(type(a))
