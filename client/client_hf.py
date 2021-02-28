from socket import socket
from zlib import decompress
import pyautogui as pgi
import pygame, time
import requests
import threading
#from pynput.mouse import Listener
import pynput

data = ''
WIDTH = 1920
HEIGHT = 1080
SC_WIDTH, SC_HEIGHT = pgi.size()
wh = [WIDTH, HEIGHT, SC_WIDTH, SC_HEIGHT]

def send_data():
    
    global data
    while True:
        try:
            #print('hi')
            x, y = pgi.position()
            x = int(x * float(WIDTH/SC_WIDTH))
            y = int(y * float(HEIGHT/SC_HEIGHT))
            requests.post(f'http://192.168.1.100:8080/api/computers/{data}/sendCoordinates', json={'x': x, 'y': y})
            print('successfu post m')
            #time.sleep(0.2)
        except:
            print('')

def send_keyboard():
    global data
    def on_press(key):
        requests.post(f'http://192.168.1.100:8080/api/computers/{data}/sendKeys', json={'key': str(key)})
    with pynput.keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def send_clicks():
    global data
    def on_click(x,y,button,pressed):
        print(x,y,button,pressed)
        buttonA = 'left'
        if str(button) == 'Button.left':
            buttonA = 'left'
        if str(button) == 'Button.right':
            buttonA = 'right'
        requests.post(f'http://192.168.1.100:8080/api/computers/{data}/sendClicks', json={'button':buttonA, 'state':str(pressed)})
    with pynput.mouse.Listener(on_click=on_click) as listener:
        listener.join()

def recvall(conn, length):
    """ Retreive all pixels. """

    buf = b''
    while len(buf) < length:
        data = conn.recv(length - len(buf))
        if not data:
            return data
        buf += data
    return buf


def main(host, port):
    global data
    global WIDTH
    global HEIGHT
    global SC_WIDTH
    global SC_HEIGHT
    pygame.init()
    screen = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))
    clock = pygame.time.Clock()

    watching = True

    sock = socket()
    sock.connect((host, port))
    dataA = sock.recv(50).decode('utf-8')
    dataA = dataA.split(';')
    WIDTH = int(dataA[1])
    HEIGHT = int(dataA[2])
    data = dataA[0]
    x = threading.Thread(target=send_data)
    x.start()
    y = threading.Thread(target=send_keyboard)
    y.start()
    z = threading.Thread(target=send_clicks)
    z.start()

    print(data)
    try:
        while watching:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    watching = False
                    break

            # Retreive the size of the pixels length, the pixels length and pixels
            size_len = int.from_bytes(sock.recv(1), byteorder='big')
            size = int.from_bytes(sock.recv(size_len), byteorder='big')
            pixels = decompress(recvall(sock, size))

            # Create the Surface from raw pixels
            print(WIDTH, HEIGHT)
            img = pygame.image.fromstring(pixels, (WIDTH-1, HEIGHT-1), 'RGB')
            img = pygame.transform.scale(img, (SC_WIDTH, SC_HEIGHT))
            # Display the picture
            screen.blit(img, (0,0))
            pygame.display.flip()
            clock.tick(60)
    finally:
        sock.close()


if __name__ == '__main__':
    r = requests.get('http://192.168.1.100:8080/api/computers/listOfConnectedDevices').json()
    lDevices = r['list']
    dDevices = {}
    for i in range(len(lDevices)):
        dDevices[i] = lDevices[i]
        print(i, lDevices[i])
    choice = int(input('Please Enter No. corresponding to the device you want to control: '))
    d = requests.get(f'http://192.168.1.100:8080/api/computers/{lDevices[choice]}/getIpPort').json()
    print(d)
    main(host=d['ip'], port=int(d['port']))
    
