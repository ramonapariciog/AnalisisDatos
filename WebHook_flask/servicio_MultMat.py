import requests
import json
import numpy as np

def envia(link = "http://localhost:5000/send", ):
    headers={"Content-Type": "application/json"}
    data = {"Matrix": {"A": {"Array": np.random.randint(1,100, size=(10,5)).tolist(), "row": 10, "col": 5},
                       "B": {"Array": np.random.randint(1,100, size=(5,4)).tolist(), "row": 5, "col": 4}}}
    data = json.dumps(data)
    # peticion de operacion
    r = requests.post(link, headers=headers, data=data)
    mat = r.json()["result"][0]
    ro,c = r.json()["result"][1:]
    print(np.asarray(mat).reshape((ro,c)))
