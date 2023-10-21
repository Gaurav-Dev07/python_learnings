
import json

# json to python
x_json = '{"name": "gaurav","age": 24}'
x_dict = json.loads(x_json)
print(x_dict)
print(type(x_dict))

# python object to json
y_dict = {
    "name": "aniket",
    "age": 22
}

y_json = json.dumps(y_dict,indent=2)
print(y_json)
print(type(y_json))
