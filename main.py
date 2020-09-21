import ufirebase as firebase
import machine
import utime
import gc
import micropython

URL = 'firebaseURL'
sair = 0


def troca_led(URL):
    if firebase.get(URL) == 1:
        print('acende led 1')
        print('apaga led 2')
    else:
        print('acende led 2')
        print('apaga led 1')


while sair != True:
    temp = 0
    for temp in range(0, 2):
        utime.sleep(15)
        gc.collect()
        troca_led(URL)
        utime.sleep(15)
        firebase.put(URL, temp)
        gc.collect()
        utime.sleep(15)
