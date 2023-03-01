import requests

# Call 2
# r = requests.post("http://127.0.0.1:8008/function_2/", 
#                   json=[{"value": 2, "color": "green"}, 
#                         {"function": "sum", "value": 3}])
# print(r.content, r.status_code, r.reason)

# Add A
# r = requests.post("http://127.0.0.1:8008/add/", 
#                   json={"value": 2, "color": "green"})
# print(r.content, r.status_code, r.reason)

# Add B
# r = requests.post("http://127.0.0.1:8008/add/", 
#                   json={"function": "sum", "value": 3})
# print(r.content, r.status_code, r.reason)

# Call 3
# r = requests.post("http://127.0.0.1:8008/function_3/1/1/")
# print(r.content, r.status_code, r.reason)