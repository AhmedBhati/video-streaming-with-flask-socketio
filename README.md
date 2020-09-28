# video-streaming-with-flask-socketIO
Video Streaming is done with flask-socketio with production WSGI server 

#### Run the test.py file using the terminal and open the localhost 127.0.0.1:5000

In order to use eventlet or gevent for making asynchronous call instead of uWSGI download the dependency using pip3 and in the test.py file change

```python3
socketio.emit('image',json, broadcast=True)
```

A video is attached in the repository with the name videostreaming.mkv play the video to see the demonstration of the project
