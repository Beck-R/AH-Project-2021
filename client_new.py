from socket import socket
from zlib import decompress
import pyautogui as pgi
import pygame, keyboard, time
import requests, json
import threading
from pynput.mouse import Listener

data = ''
WIDTH = 1920
HEIGHT = 1080
SC_WIDTH, SC_HEIGHT = pgi.size()
wh = [WIDTH, HEIGHT, SC_WIDTH, SC_HEIGHT]

def send_data():
    
    global data
    while True:
        try:
            print('hi')
            x, y = pgi.position()
            x = int(x * float(WIDTH/SC_WIDTH))
            y = int(y * float(HEIGHT/SC_HEIGHT))
            requests.post(f'http://192.168.1.100:8080/api/computers/{data}/sendCoordinates', json={'x': x, 'y': y})
            print('successfu post m')
            time.sleep(0.2)
        except:
            print('')

def send_keyboard():
    global data
    while True:
            try:
                key = keyboard.read_key()
                requests.post(f'http://192.168.1.100:8080/api/computers/{data}/sendKeys', json={"key": key})
            except:
                    print('')

def send_clicks():
    global data
    def on_click(x,y,button,pressed):
        print(x,y,button,pressed)
        if button == button.Left:
            buttonA = 'Left'
        if button == button.Right:
            buttonA = 'Right'
        requests.post(f'http://192.168.1.100:8080/api/computers/{data}/sendClicks', json={'button':buttonA, 'state':str(pressed)})
    with Listener(on_click=on_click) as listener:
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


def main(host='192.168.1.1', port=10044):
    global data
    global WIDTH
    global HEIGHT
    global SC_WIDTH
    global SC_HEIGHT
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    watching = True

    sock = socket()
    sock.connect((host, port))
    dataA = sock.recv(50).decode('utf-8')
    dataA = dataA.split(';')
    WIDTH = dataA[1]
    HEIGHT = dataA[2]
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
            img = pygame.image.fromstring(pixels, (WIDTH, HEIGHT), 'RGB')
            img = pygame.transform.scale(img, (SC_WIDTH, SC_HEIGHT))
            # Display the picture
            screen.blit(img, rect)
            pygame.display.flip()
            clock.tick(60)
    finally:
        sock.close()


if __name__ == '__main__':
    main()
    
