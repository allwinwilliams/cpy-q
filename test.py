import sys
import os
import time

import signal
import keyboard

import Cpyq
import functions

# print("test")
cpy_obj=Cpyq.Cpyq()
# for i in range(10):
#     x=(i*i)%(i+3)
#     print(x,"\n")
#     c.add_front(x)
# for i in range(10):
#     print(c.del_front())
#


# def signal_handler(sig, frame):
#         print('You pressed Ctrl+C!')
#         sys.exit(0)
#
# signal.signal(signal.SIGINT, signal_handler)
# print('Press Ctrl+C')
# signal.pause()


    # sys.path.append(os.path.abspath("SO_site-packages"))
    #
    # recent_value = ""
    #
    # while True:
    #     tmp_value = functions.read_from_clipboard()
    #     if tmp_value != recent_value:
    #         recent_value = tmp_value
    #         Cpyq.add_front(recent_value)
    #



while True:

    try:

        if sys.platform == "linux" or sys.platform == "linux2":

            if keyboard.is_pressed('ctrl++shift+c'):
                print('You Pressed ctrl shift c!')

            elif keyboard.is_pressed('ctrl+shift+v'):
                print('You Pressed ctrl shift c!')

            elif keyboard.is_pressed('ctrl+c'):
                print('You Pressed ctrl c!')

            elif keyboard.is_pressed('ctrl+v'):
                print('You Pressed ctrl v!')

            elif keyboard.is_pressed('ctrl+z'):
                print('You Pressed ctrl z!')

            else:
                pass


        elif sys.platform == "darwin":


            if keyboard.is_pressed('cmd+shift+c'):
                print('You Pressed cmd shift c!')
                x=functions.read_from_clipboard()
                print(x)
                cpy_obj.add_front(x)
                keyboard.write("")

            elif keyboard.is_pressed('cmd+shift+v'):
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
        else:
            pass

    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        break
