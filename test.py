from flask import Flask, render_template
from flask_socketio import SocketIO
from time import sleep
import cv2
import json
import base64
#cap=cv2.VideoCapture(0)  ##when removing debug=True or using gevent or eventlet uncomment this line and comment the cap=cv2.VideoCapture(0) in gen(json)
app = Flask(__name__)
app.config['SECRET_KEY'] = '78581099#lkjh'
socketio = SocketIO(app)

@app.route('/')
def index():
	return render_template('index.html')


@socketio.on('check')
def gen(json):
	cap=cv2.VideoCapture(0)	
	while(cap.isOpened()):
		ret,img=cap.read()
		if ret:
			img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
			frame = cv2.imencode('.jpg', img)[1].tobytes()
			frame= base64.encodebytes(frame).decode("utf-8")
			message(frame)
			socketio.sleep(0)
		else:
			break


def message(json, methods=['GET','POST']):
	print("Recieved message")
	socketio.emit('image', json )

if __name__== "__main__":
	socketio.run(app,debug=True, host='127.0.0.1', port=5000) 	
