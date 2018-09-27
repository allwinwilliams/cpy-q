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

            if keyboard.is_pressed('+1+c'):
                pass
                
            elif keyboard.is_pressed('+2+c'):
                pass

            elif keyboard.is_pressed('+1+v'):
                pass

            elif keyboard.is_pressed('alt+c'):
                print('You Pressed alt c!')
                x=functions.read_from_clipboard()
                print("text to clipboard: ", x)
                cpy_obj.add_front(x)
                keyboard.write("")
                functions.write_to_clipboard("")
                cpy_obj.show()

            elif keyboard.is_pressed('alt+v'):
                print('You Pressed ctrl v!')
                x=cpy_obj.del_front()
                print("to be pasted: ",x)
                # keyboard.write("delete")
                keyboard.write(x)
                keyboard.write("")
                cpy_obj.show()

            if keyboard.is_pressed('ctrl+shift+c'):
                print('You Pressed alt c!')
                x=functions.read_from_clipboard()
                print("text to clipboard: ", x)
                cpy_obj.add_front(x)
                keyboard.write("")
                functions.write_to_clipboard("")
                cpy_obj.show()

            elif keyboard.is_pressed('ctrl+shift+v'):
                print('You Pressed ctrl v!')
                x=cpy_obj.del_front()
                print("to be pasted: ",x)
                # keyboard.write("delete")
                keyboard.write(x)
                keyboard.write("")
                cpy_obj.show()


            elif keyboard.is_pressed('cmd+c'):
                print('You Pressed cmd c!')
                x=functions.read_from_clipboard()
                print("text to clipboard: ", x)
                cpy_obj.add_back(x)
                keyboard.write("")
                functions.write_to_clipboard("")
                cpy_obj.show()

            elif keyboard.is_pressed('cmd+v'):
                print('You Pressed cmd v!')
                x=cpy_obj.get_back()
                print("to be pasted: ",x)
                # keyboard.write("delete")
                keyboard.write(x)
                keyboard.write("")
                cpy_obj.show()

            elif keyboard.is_pressed('cmd+z'):
                print('You Pressed cmd z!')
                cpy_obj.clear()
                keyboard.write("")
                cpy_obj.show()

            else:
                pass

        elif sys.platform == "linux" or sys.platform == "linux2":
            pass

        else:
            pass

    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        break
