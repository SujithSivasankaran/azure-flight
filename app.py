from flask import Flask,render_template,request
import requests,json,urllib
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/', methods=['POST','GET'])
def predict():

    features = [float(x) for x in request.form.values()]
    test = json.dumps({"data": features})
    headers = {'Content-Type': 'application/json'}
    service = 'http://162d376c-d9fa-4d8a-99ed-6c73e23206ff.centralus.azurecontainer.io/score'
    resp = requests.post(service, test, headers=headers)
    m = resp.json()[0]
    print(m)
    # flash(m)
    if (m>0):
        ans = "Flight is delayed"
    else:
        ans = "Flight is not delayed"
    return render_template('index.html', output = ans)


if __name__ == "__main__":
    app.run()









