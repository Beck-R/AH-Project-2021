from getinfo import sys_monitor
from getprocess import proc_monitor
from server import main
import requests, sockets

host = socket.gethostbyname(socket.gethostname())
port = random.randint(10000, 10100)
r = requests.post(f'http://192.168.1.100:8080/api/computers/{platform.uname().node}/ipPort', json={'ip': host, 'port': port})
main(host=host, port=port)


sys_monitor()
proc_monitor()
