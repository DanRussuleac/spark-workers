from flask import Flask, request
import requests
import json
app = Flask(__name__)

def get_api_key() -> str:
    return "ya29.a0AfB_byDwVIn1T-ozCZStxn0Ib28O6lbCw1FImerMoNnBvuZ2cH6LTcVqVFhQiLZp1JP72lr73NeTHMYVzfL70cPKIJUlw5OFRYDqF9giw0VFe0717cCWoyUCtgtmtR22Gm6hv7aPR_KwwqpWBoEKgC46-w53pNFo1KXA1QjROSZF0LlU9DhQc_1z5bqc2clRFAjtpDBYaPBcCqAMgc6pZgR-UFcGojTKzkSe4kiHpFqcABagLj5R49NX6wNwobwWaFCPDlCn5PsK4_nmn47Wd3eow6fKrEPf248YPtpWHmL2GvH_8iR4ExPz7a5shqO9ucD947plCLZybnXt46gbRTcWQZSz6FR4aFwPNy4DbaDTUCHCKx1HfPYhpEIpwX9E4XKucQ6imJbs33PEu7u05AFDKp0NnQaCgYKAWUSARASFQHGX2MiOrU-0prMi4yBIccYY3IjCw0421"

@app.route("/")
def hello():
    return "Add workers to the Spark cluster with a POST request to add"

@app.route("/test")
def test():
    return get_api_key()

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return "Use POST to add"  # replace with form template
    else:
        token = get_api_key()
        ret = addWorker(token, request.form['num'])
        return ret

def addWorker(token, num):
    with open('payload.json') as p:
        tdata = json.load(p)
    tdata['name'] = 'slave' + str(num)
    data = json.dumps(tdata)
    url = 'https://www.googleapis.com/compute/v1/projects/arched-media-400313/zones/europe-west1-b/instances'
    headers = {"Authorization": "Bearer " + token}
    resp = requests.post(url, headers=headers, data=data)
    if resp.status_code == 200:
        return "Done"
    else:
        print(resp.content)
        return "Error\n" + resp.content.decode('utf-8') + '\n\n\n' + data

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
