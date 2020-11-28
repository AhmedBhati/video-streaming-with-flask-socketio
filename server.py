from flask import Flask, render_template, request
import eventlet
import socketio
import eventlet.wsgi

sio = socketio.Server()#async_mode=async_mode)
app = Flask(__name__)
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

dict1={}
i=0
@app.route('/')
def index():
	return render_template('file.html')

@sio.event()
def pingpong(sid):
	print("//////////////////////////")
	sio.emit("send_data", room=sid)

@sio.event
def connect(sid, data):	
	print("[INFO] Connect to the server")
	pingpong(sid)

@sio.event
def send(sid, data):
	global i
	if sid not in dict1:
		i+=1
		dict1[sid]=i
	key=dict1[sid]
	print("Reached here")
	sio.emit('response',{'key':key, 'data':data})
	pingpong(sid)

@sio.event
def disconnect(sid):
	print("[INFO] disconnected from the server")

if __name__ == '__main__':
	eventlet.wsgi.server(eventlet.listen(('0.0.0.0',5000)), app)
