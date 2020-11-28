# Video Streaming with Flask SocketIO
Video Streaming is done with flask-socketio with production WSGI server 

## Transmitting video frames with Flask SocketIO

In order to use eventlet or gevent for making asynchronous call instead of uWSGI download the dependency using pip3 and in the test.py file change

```python3
socketio.emit('image',json, broadcast=True)
```

#### Run the test.py file using the terminal and open the localhost http://127.0.0.1:5000

A video is attached in the repository with the name videostreaming.mkv play the video to see the demonstration of the project.

## Demonstration of client sending video frames to server on Different system/Same system in the network.

In order to send video frames from single server to client see the server.py and client.py. Currently this code can only display video frames from two clients but with some modification in javascript code it will be possible to do for many clients, will make the required changes in some time. See the demo videos of remote_server_client1 and remote_server_client2 for the output demonstration. In remote_server_client2, first client is on a remote system and second client and server is on the same system in the network. In remote-server_client1 the server and client are both on different systems in the same network.

#### Run the server.py file and client.py file and open http://0.0.0.0:5000 on browser.
