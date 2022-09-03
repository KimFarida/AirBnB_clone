
import json

a = {"name": "Larvine", "age":22}

# serialization
with open("file.json", "w") as f:
    json.dump(a, f)


