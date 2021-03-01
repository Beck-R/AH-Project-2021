import subprocess, time, requests, platform, json
import psutil


node = platform.uname().node
def proc_monitor():
    while True:

        data = {}
        #structure {"app name": [cpu usage, memory usage, pid]}
        cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Id'
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        for line in proc.stdout:
            if not line.decode()[0].isspace():
                p = psutil.Process(int(line.decode().rstrip()))
                p.cpu_percent(interval=1)
                #time.sleep(0.1)
                data[p.name()] = [p.cpu_percent(interval=1), p.memory_percent(), int(line.decode().rstrip())]

        r = requests.post(f'http://openaccess.space:8080/api/computers/{node}/getProcesses', json=(data))
        time.sleep(10)
