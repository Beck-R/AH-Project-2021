import socket
from threading import Thread
from zlib import compress
import platform
from mss import mss
import get_controls as name
import time, random, requests
import subprocess

WIDTH, HEIGHT = name.pgi.size()

if 'windows' in platform.uname().system.lower():
    try:
        subprocess.check_call('netsh.exe advfirewall set privateprofile state off')
    except:
        print('')
def retreive_screenshot(conn):
    with mss() as sct:
        # The region to capture
        rect = {'top': 0, 'left': 0, 'width': WIDTH-1, 'height': HEIGHT-1}

        while 'recording':
            # Capture the screen
            img = sct.grab(rect)
            # Tweak the compression level here (0-9)
            pixels = compress(img.rgb, 6)

            # Send the size of the pixels length
            size = len(pixels)
            size_len = (size.bit_length() + 7) // 8
            conn.send(bytes([size_len]))

            # Send the actual pixels length
            size_bytes = size.to_bytes(size_len, 'big')
            conn.send(size_bytes)
            #time.sleep(0.2)
            # Send pixels
            conn.sendall(pixels)



def main(host, port):
    global WIDTH
    global HEIGHT
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_addr = (host, port)
    sock.bind(s_addr)
    
    sock.listen(5)
    print('Server started.')
    while 'connected':
        conn, addr = sock.accept()
        print(conn)
        print('Client connected IP:', addr)
        conn.send((platform.uname().node + ';' + str(WIDTH) + ';' + str(HEIGHT)).encode('utf-8'))
        thread = Thread(target=retreive_screenshot, args=(conn,))
        thread.start()
        name.play = True
        name.automation()
    subprocess.check_call('netsh.exe advfirewall set privateprofile state on')
    name.play = False
    sock.close()
if __name__ == '__main__':
    host = socket.gethostbyname(socket.gethostname())
    port = random.randint(10000, 10100)
    r = requests.post(f'http://192.168.1.100:8080/api/computers/{platform.uname().node}/ipPort', json={'ip': host, 'port': port})
    main(host=host, port=port)
