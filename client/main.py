from getinfo import sys_monitor
from getprocess import proc_monitor
from server import main
import requests, socket, random, platform, subprocess, sys


if sys.platform == "linux" or sys.platform == "linux2":
        output = str(subprocess.check_output('iwgetid')).split(' ')
        val = output[len(output)-1].replace('ESSID:','').replace('"', '')
        ssid = val[:-3]
elif sys.platform == 'darwin':
        process = subprocess.Popen(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport','-I'], stdout=subprocess.PIPE)
        out, err = process.communicate()
        process.wait()
        out = out.splitlines()
        ssid = out[12].split(" ")[1]
elif sys.platform == 'win32':
        data = subprocess.check_output("netsh wlan show interfaces")
        data = str(data)
        data = data.split('\ r\ n'.replace(' ', ''))
        ssid = ''
        for x in range(len(data)):
            if ' SSID' in data[x]:
                ssid = data[x].replace(' ', '').replace('SSID:', '')host = socket.gethostbyname(socket.gethostname())
host = socket.gethostbyname(socket.gethostname())
port = random.randint(10000, 10100)
r = requests.post(f'http://192.168.1.100:8080/api/computers/{platform.uname().node}/ipPort', json={'ip': host, 'port': port})
main(host=host, port=port)


sys_monitor()
proc_monitor()
