from flask import Flask, render_template, Response, request, redirect, url_for
from flask_api import status

import json



app = Flask(__name__)

@app.route('/')
def index():
    cameras= []
    devices = load_devices()
    print(devices)
    for camara in devices:
        cameras.append(camara)
    cameras.pop()
    context = {
        'cameras':cameras,
        'devices': devices['camera'],
        'height_min': '120',
        'height_max': '800',
        'width_min': '300',
        'width_max': '10000',
    }
    return render_template('index.html', **context)

    
@app.route('/cutter', methods=['POST'])
def cutter():
    print(request.form)
    content = {'succes': 'your content here'}
    return content, status.HTTP_201_CREATED

@app.route('/cameras', methods=['POST'])    
def cam():
    print('posting')
    print(request.form)
    name=request.form['disp']
    devices = load_devices()
    print (devices)
    devices['camera']= name
    print(devices)
    save_config(devices)
    return  redirect(url_for('index'))

def load_devices():
    json_data = json.load(open('devices.json'))
    return json_data


def save_config(cameras_data):
    with open('devices.json', 'w') as fp:
        json.dump(cameras_data, fp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
