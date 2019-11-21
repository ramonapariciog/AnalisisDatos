from flask import Flask, request
from funcionServ import multiplica
import json
app = Flask(__name__)



@app.route("/send", methods=["GET", "POST"])
def send():
    # print(dir(request))
    # print(request)
    if request.method == "POST":
        content = request.get_json()
        # subprocess.check_output(["python -c 'print 53+10'"], shell=True)
        matrices = content["Matrix"]
        response = multiplica(matrices["A"], matrices["B"])
        return json.dumps(response, indent=4)
    else:
        content = request.get_json()
        print(content)
        return "GET"

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
