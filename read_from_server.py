# script to read from server at ip address

LOCAL_IP = '192.168.1.70' # 192.168.1.70 #.23 is dead
TIMEOUT_TIME = .5 #seconds
COMMAND_OFF = '/LED/off'
COMMAND_ON = '/LED/on'
COMMAND_STATE = '/LED/state'
COMMAND_CLICK = '/click'

from time import time, sleep
from urllib.request import urlopen

def ask_esp32_server(command=''):
    try:
        # read from server
        # open url
        with urlopen(f'http://{LOCAL_IP}{command}', timeout=TIMEOUT_TIME) as f:
            # read data
            data = f.read()
            #convert to string
            data = data.decode('utf-8')
        return data
    except Exception as e:
        # print(f'Exception: {e}')
        return None

if __name__ == '__main__':
    cnt = 0
    while True:
        cnt += 1

        command = COMMAND_ON if cnt % 2 == 0 else COMMAND_OFF

        # #change led state    
        # sleep(1.5)
        # # read from server
        # # data = ask_esp32_server()
        # _ = ask_esp32_server(command) # send command
        # #sleep for 1 second
        # sleep(1.5)

        #send click command
        _ = ask_esp32_server(COMMAND_CLICK) # send command
        sleep(2.5)

        state = ask_esp32_server(COMMAND_STATE) # read data

        #remove all spaces and \n
        state = state.replace(' ', '').replace('\n', '') if state is not None else None

        # print data
        print(state)

        sleep(.5)


