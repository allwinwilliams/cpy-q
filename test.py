import sys
import os
import time

import signal
import keyboard

import Cpyq
import functions

cpy_obj=Cpyq.Cpyq()

while True:

    try:

        if sys.platform == "darwin":


            if keyboard.is_pressed('cmd+alt+c'):
                print('You Pressed cmd shift c!')
                x=functions.read_from_clipboard()
                print(x)
                cpy_obj.add_front(x)
                keyboard.write("")

            elif keyboard.is_pressed('cmd+alt+v'):
                print('You Pressed cmd shift v!')
                print(cpy_obj.del_front())
                keyboard.write("")

            elif keyboard.is_pressed('cmd+c'):
                print('You Pressed cmd c!')
                x=functions.read_from_clipboard()
                print("text to clipboard: ", x)
                cpy_obj.add_front(x)
                keyboard.write("")
                functions.write_to_clipboard("")

            elif keyboard.is_pressed('cmd+v'):
                print('You Pressed cmd v!')
                x=cpy_obj.del_back()
                print("to be pasted: ",x)
                # keyboard.write("delete")
                keyboard.write(x)
                keyboard.write("")

            elif keyboard.is_pressed('cmd+z'):
                print('You Pressed cmd z!')
                keyboard.write("")

            else:
                pass

        elif sys.platform == "linux" or sys.platform == "linux2":
            pass

        else:
            pass

    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        break
