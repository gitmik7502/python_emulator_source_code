import keyboard

def mywait():
    keyboard.read_key()

def up():
    print("up")
def down():
    print("down")
def enter():
    print("enter")
def f10():
    print("f10")
def f12():
    print("f12")
def f6():
    print("f6")

keyboard.add_hotkey("up", up)
keyboard.add_hotkey("down", down)
keyboard.add_hotkey("enter", enter)
keyboard.add_hotkey("f10", f10)
keyboard.add_hotkey("f12", f12)
keyboard.add_hotkey("f6", f6)

print("""\033[1;mhello""")
while True:
    mywait()