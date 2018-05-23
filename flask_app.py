#!/usr/bin/python
from flask import Flask,request
from werkzeug import secure_filename
import requests
import os

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World"

@app.route("/tts",methods=['GET','POST'])
def tts():
    if request.method == 'POST':
        f = request.files['fileInput']
        f.save(secure_filename(f.filename))
        os.system("./tamil-tts.sh --run --gen-mp3 --source "+f.filename)
        filename = f.filename
        filename = filename.split('.')[0]
        audioFile = filename+".mp3"
        print("Initiating MP3 upload")
        files = {'ttsAudio':open(audioFile,'rb')}
        url = 'http://127.0.0.1/tts/getMp3'
        r = requests.post(url,files=files)
        print(r.content)
        return 'Success'


if __name__ == '__main__':
    app.run(debug=True)
