import requests, platform, json, time
import pyautogui as pgi
from pynput.keyboard import Key, Controller

keyboard = Controller()
pgi.FAILSAFE = False
play = True
pc = platform.uname().node
def automation():
    global pc
    global play
    while play:
        data = requests.get(f'http://192.168.1.100:8080/api/computers/{pc}/getCoordinates').json()
        #print(data)
        x = data['x']
        y = data['y']
        pgi.moveTo(x, y)
        #print('x',x, 'y', y)
        keys = requests.get(f'http://192.168.1.100:8080/api/computers/{pc}/getKeys').json()
        listKeys = keys['keys']
        for x in listKeys:
            if x != '':
                print(str(x))
                if str(x) == "'a'":
                    #print('in')
                    pgi.press('a')
                    #print('a')
                elif str(x) == "'b'":
                    pgi.press('b')
                elif x == "'c'":
                    pgi.press('c')
                elif x == "'d'":
                    pgi.press('d')
                elif x == "'e'":
                    pgi.press('e')
                elif x == "'f'":
                    pgi.press('f')
                elif x == "'g'":
                    pgi.press('g')
                elif x == "'h'":
                    pgi.press('h')
                elif x == "'i'":
                    pgi.press('i')
                elif x == "'j'":
                    pgi.press('j')
                elif x == "'k'":
                    pgi.press('k')
                elif x == "'l'":
                    pgi.press('l')
                elif x == "'m'":
                    pgi.press('m')
                elif x == "'n'":
                    pgi.press('n')
                elif x == "'o'":
                    pgi.press('o')
                elif x == "'p'":
                    pgi.press('p')
                elif x == "'q'":
                    pgi.press('q')
                elif x == "'r'":
                    pgi.press('r')
                elif x == "'s'":
                    pgi.press('s')
                elif x == "'t'":
                    pgi.press('t')
                elif x == "'u'":
                    pgi.press('u')
                elif x == "'v'":
                    pgi.press('v')
                elif x == "'w'":
                    pgi.press('w')
                elif x == "'x'":
                    pgi.press('x')
                elif x == "'y'":
                    pgi.press('y')
                elif x == "'z'":
                    pgi.press('z')
                elif x == "'A'":
                    pgi.press('A')
                elif x == "'B'":
                    pgi.press('B')
                elif x == "'C'":
                    pgi.press('C')
                elif x == "'D'":
                    pgi.press('D')
                elif x == "'E'":
                    pgi.press('E')
                elif x == "'F'":
                    pgi.press('F')
                elif x == "'G'":
                    pgi.press('G')
                elif x == "'H'":
                    pgi.press('H')
                elif x == "'I'":
                    pgi.press('I')
                elif x == "'J'":
                    pgi.press('J')
                elif x == "'K'":
                    pgi.press('K')
                elif x == "'L'":
                    pgi.press('L')
                elif x == "'M'":
                    pgi.press('M')
                elif x == "'N'":
                    pgi.press('N')
                elif x == "'O'":
                    pgi.press('O')
                elif x == "'P'":
                    pgi.press('P')
                elif x == "'Q'":
                    pgi.press('Q')
                elif x == "'R'":
                    pgi.press('R')
                elif x == "'S'":
                    pgi.press('S')
                elif x == "'T'":
                    pgi.press('T')
                elif x == "'U'":
                    pgi.press('U')
                elif x == "'V'":
                    pgi.press('V')
                elif x == "'W'":
                    pgi.press('W')
                elif x == "'X'":
                    pgi.press('X')
                elif x == "'Y'":
                    pgi.press('Y')
                elif x == "'Z'":
                    pgi.press('Z')
                elif x == 'Key.alt' or x == 'Key.alt_gr' or x == 'Key.alt_r' or x == 'Key.alt_l':
                    pgi.press('alt')
                elif str(x) == 'Key.backspace':
                    pgi.press('backspace')
                elif x == 'Key.caps_lock':
                    pgi.press('capslock')
                elif x == 'Key.cmd' or x=='Key.cmd_l' or x=="Key.cmd_r":
                    pgi.press('command')
                elif x == 'Key.ctrl' or x=="Key.ctrl_l" or x=='Key.ctrl_r':
                    pgi.press('ctrl')
                elif x == 'Key.delete':
                    pgi.press('delete')
                elif x == 'Key.down':
                    pgi.press('down')
                elif x == 'Key.end':
                    pgi.press('end')
                elif x == 'Key.enter':
                    pgi.press('enter')
                elif x == 'Key.esc':
                    pgi.press('esc')
                elif x == 'Key.f1':
                    pgi.press('f1')
                elif x == 'Key.f2':
                    pgi.press('f2')
                elif x == 'Key.f3':
                    pgi.press('f3')
                elif x == 'Key.f4':
                    pgi.press('f4')
                elif x == 'Key.f5':
                    pgi.press('f5')
                elif x == 'Key.f6':
                    pgi.press('f6')
                elif x == 'Key.f7':
                    pgi.press('f7')
                elif x == 'Key.f8':
                    pgi.press('f8')
                elif x == 'Key.f9':
                    pgi.press('f9')
                elif x == 'Key.f10':
                    pgi.press('f10')
                elif x == 'Key.f11':
                    pgi.press('f11')
                elif x == 'Key.f12':
                    pgi.press('f12')
                elif x == 'Key.f13':
                    pgi.press('f13')
                elif x == 'Key.f14':
                    pgi.press('f14')
                elif x == 'Key.f15':
                    pgi.press('f15')
                elif x == 'Key.f16':
                    pgi.press('f16')
                elif x == 'Key.f17':
                    pgi.press('f17')
                elif x == 'Key.f18':
                    pgi.press('f18')
                elif x == 'Key.f19':
                    pgi.press('f19')
                elif x == 'Key.f20':
                    pgi.press('f20')
                elif x == 'Key.home':
                    pgi.press('home')
                elif x == 'Key.insert':
                    pgi.press('insert')
                elif x == 'Key.left':
                    pgi.press('left')
                elif x == 'Key.media_next':
                    pgi.press('nexttrack')
                elif x == 'Key.media_play_pause':
                    pgi.press('playpause')
                elif x == 'Key.media_previous':
                    pgi.press('prevtrack')
                elif x == 'Key.media_volume_down':
                    pgi.press('volumnedown')
                elif x == 'Key.media_volume_mute':
                    pgi.press('volumemute')
                elif x == 'Key.media_volume_up':
                    pgi.press('volumeup')
                elif x == 'Key.menu':
                    pgi.press('menu')
                elif x == 'Key.num_lock':
                    pgi.press('numlock')
                elif x == 'Key.page_down':
                    pgi.press('pagedown')
                elif x == 'Key.page_up':
                    pgi.press('pageup')
                elif x == 'pause':
                    pgi.press('pause')
                elif x == 'Key.right':
                    pgi.press('right')
                elif x == 'Key.scroll_lock':
                    pgi.press('scrolllock')
                elif x == 'Key.print_screen':
                    pgi.press('printscreen')
                elif x == 'Key.shift' or x=='Key.shift_l' or x=='Key.shift_r':
                    pgi.press('shift')
                elif x == "Key.space":
                    pgi.press('space')
                elif x == 'Key.tab':
                    pgi.press('tab')
                elif x == "Key.up":
                    pgi.press('up')
                elif x == "'\ x1a'".replace(' ', ''):
                    pgi.hotkey('ctrl', 'z')
                elif x == "'\ x18'".replace(' ', ''):
                    pgi.hotkey('ctrl', 'x')
                elif x == "'\ x03'".replace(' ', ''):
                    pgi.hotkey('ctrl', 'c')
                elif x == "'\ x16'".replace(' ', ''):
                    pgi.hotkey('ctrl', 'v')
                elif x == "'\ x02'".replace(' ', ''):
                    pgi.hotkey('ctrl', 'b')
                elif x == "'\ x0e'".replace(' ', ''):
                    pgi.hotkey('ctrl', 'n')
                elif x == "'\ r'".replace(' ', ''):
                    pgi.hotkey('ctrl', 'm')
                elif x == "'\ x01'".replace(' ', ''):
                    pgi.hotkey('ctrl', 'a')
                elif x == "'\ x13'".replace(' ', ''):
                    pgi.hotkey('ctrl', 's')
                elif x == "'\ x04'".replace(' ', ''):
                    pgi.hotkey('ctrl', 'd')
                elif x == "'\ x06'".replace(' ', ''):
                    pgi.hotkey('ctrl', 'f')
                elif x == "'\ x07'".replace(' ', ''):
                    pgi.hotkey('ctrl', 'g')
                elif x == "'\ x08'".replace(' ', ''):
                    pgi.hotkey('ctrl', 'h')
                elif x == "'\ x0b'".replace(' ', ''):
                    pgi.hotkey('ctrl', 'k')
                elif x == "'\ x0c'".replace(' ', ''):
                    pgi.hotkey('ctrl', 'l')
                elif x == "'\ x11'".replace(' ', ''):
                    pgi.hotkey('ctrl', 'q')
                elif x == "'\ x17'".replace(' ', ''):
                    pgi.hotkey('ctrl', 'w')
                elif x == "'\ x05'".replace(' ', ''):
                    pgi.hotkey('ctrl', 'e')
                elif x == "'\ x12'".replace(' ', ''):
                    pgi.hotkey('ctrl', 'r')
                elif x == "'\ x14'".replace(' ', ''):
                    pgi.hotkey('ctrl', 't')
                elif x == "'\ x19'".replace(' ', ''):
                    pgi.hotkey('ctrl', 'y')
                elif x == "'\ x15'".replace(' ', ''):
                    pgi.hotkey('ctrl', 'v')
                elif x == "'\ t'".replace(' ', ''):
                    pgi.hotkey('ctrl', 'i')
                elif x == "'\ n'".replace(' ', ''):
                    pgi.hotkey('ctrl', 'j')
                elif x == "'\  x0f'".replace(' ', ''):
                    pgi.hotkey('ctrl', 'o')
                elif x == "'\ x10'".replace(' ', ''):
                    pgi.hotkey('ctrl', 'p')
                elif x == "'1'":
                    pgi.press('1')
                elif x == "'2'":
                    pgi.press('2')
                elif x == "'3'":
                    pgi.press('3')
                elif x == "'4'":
                    pgi.press('4')
                elif x == "'5'":
                    pgi.press('5')
                elif x == "'6'":
                    pgi.press('6')
                elif x == "'7'":
                    pgi.press('7')
                elif x == "'8'":
                    pgi.press('8')
                elif x == "'9'":
                    pgi.press('9')
                elif x == "'0'":
                    pgi.press('0')
                elif x == "'!'":
                    pgi.press('!')
                elif x == "'@'":
                    pgi.press('@')
                elif x == "'#'":
                    pgi.press('#')
                elif x == "'$'":
                    pgi.press('$')
                elif x == "'%'":
                    pgi.press('%')
                elif x == "'^'":
                    pgi.press('^')
                elif x == "'&'":
                    pgi.press('&')
                elif x == "'*'":
                    pgi.press('*')
                elif x == "'('":
                    pgi.press('(')
                elif x == "')'":
                    pgi.press(')')
                elif x == "'-'":
                    pgi.press('-')
                elif x == "'_'":
                    pgi.press('_')
                elif x == "'+'":
                    pgi.press('+')
                elif x == "'='":
                    pgi.press('=')
                elif x == "'`'":
                    pgi.press('`')
                elif x == "'~'":
                    pgi.press('~')
                elif x == "'{'":
                    pgi.press('{')
                elif x == "'}'":
                    pgi.press('}')
                elif x == "'['":
                    pgi.press('[')
                elif x == "']'":
                    pgi.press(']')
                elif x == "':'":
                    pgi.press(':')
                elif x == "';'":
                    pgi.press(';')
                elif x == "'<'":
                    pgi.press('<')
                elif x == "'<>'":
                    pgi.press('<>')
                elif x == "'?'":
                    pgi.press('?')
                elif x == "'/'":
                    pgi.press('/')
                elif x == "','":
                    pgi.press(',')
                elif x == "'.'":
                    pgi.press('.')
                elif x == "'\ \ '".replace(' ', ''):
                    pgi.press('\ '.replace(' ', ''))
                elif x == "'|'":
                    pgi.press('|')

        clicks = requests.get(f'http://192.168.1.100:8080/api/computers/{pc}/getClicks').json()
        listClicks = clicks['clicks']
        for x in listClicks:
            #print('x',x)
            if x != '':
                if x['state'] == 'True':
                    pgi.mouseDown(button=x['button'])
                if x['state'] == 'False':
                    pgi.mouseUp(button=x['button'])

        time.sleep(0.5)
