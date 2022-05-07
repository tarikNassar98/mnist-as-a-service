import requests
from flask import Flask, send_file, request, render_template
app = Flask(__name__, static_url_path='')




@app.route("/")
def home():
    return render_template('index.html')


@app.route("/upload", methods=['POST'])
def hello_world():

    data = request.data

    client = boto3.client('s3')

    # with open('static/js/app.js', 'rb') as data:
    #     client.upload_fileobj(data, 'tarik-fp-bucket','my-key')
    prediction = requests.get(f'http://mnist-predictor-service:8080/predict', data=data)

    return prediction.json()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)

