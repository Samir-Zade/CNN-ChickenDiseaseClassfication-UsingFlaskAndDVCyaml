from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from src.cnnClassifier.utils.common import decodeImage #decode the image
from src.cnnClassifier.pipeline.predict import PredictionPipeline


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

#initialize the flask
app = Flask(__name__)
CORS(app)

#creating the client
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

#default route
@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

#train page route
@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("dvc repro") ###change from python main.py###
    return "Training done successfully!"

#predict page route
@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080) #local host
    # app.run(host='0.0.0.0', port=8080) #for AWS
    # app.run(host='0.0.0.0', port=80) #for AZURE