import requests, platform, json, time
import pyautogui as pgi

pc = platform.uname().node
def automation():
    global pc
    while True:
        data = requests.get(f'http://192.168.1.100:8080/api/computers/{pc}/getCoordinates').json()
        print(data)
        x = data['x']
        y = data['y']
        pgi.moveTo(x, y)
        print('x',x, 'y', y)
        keys = requests.get(f'http://192.168.1.100:8080/api/computers/{pc}/getKeys').json()
        listKeys = keys['keys']
        for x in listKeys:
            pgi.keyDown(x)
            pgi.keyUp(x)
        clicks = requests.get(f'http://192.168.1.100:8080/api/computers/{pc}/getClicks').json()
        listClicks = clicks['clicks']
        for x in listClicks:
            if x != '':
                print('state', x['state'], 'button', x['button'])

        time.sleep(0.5)
