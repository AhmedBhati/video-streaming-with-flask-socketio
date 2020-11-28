from flask import Flask, render_template, request
from flask_socketio import SocketIO
import socketio
import cv2
import json
import base64
from time import sleep
cap=cv2.VideoCapture(0)
sio = socketio.Client(engineio_logger=True)
i=0;

@sio.event
def connect():
	print("CONNECTED")

@sio.event
def send_data():
	while(cap.isOpened()):
		ret,img=cap.read()
		if ret:
			img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
			frame = cv2.imencode('.jpg', img)[1].tobytes()
			frame= base64.encodebytes(frame).decode("utf-8")
			message(frame)
			sleep(0)
		else:
			break

def message(json):
	print("/////////////////////////////500")
	#sio.emit('send',str(i))
	sio.emit('send',json)

@sio.event
def disconnect():
	print("DISCONNECTED")

if __name__ == '__main__':
	#sio.connect('http://192.168.0.108:5000') ## uncomment this line when the server is on remote system change the ip address with the ip address 
	#of the system where the server is running.
	sio.connect('0.0.0.0:5000')
	sio.wait()
