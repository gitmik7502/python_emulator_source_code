import os
import PySimpleGUI as sg
import keyboard
import time
import dlcs
import winsound
from pathlib import Path

defaultbootdevice = "cd"
usbenabled = False
bootpickenabled = False
boothdd = False
bootdisk = "0"
sudoinstalled = "0"
combineinstalled = "0"
patchinstalled = "0"
wininstalled = "0"
sudoinstalled = "0"
pythoninstalled = "0"
os.system("mode con cols=93 lines=32")
def hdd(): ...
def usb(): ...
def cd(): ...

def selfloppyimg():
    layout = [
        [
            sg.Input(key='-INPUT-'),
            sg.FileBrowse(file_types=(("Python Files", "*.py"),)),
            sg.Button("Open")
        ]
    ]

    window = sg.Window('floppy image setter', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Open':
            filename = values['-INPUT-']
            if Path(filename).is_file():
                try:
                    window.close()
                    return filename
                except Exception as e:
                    print("Error: ", e)

    window.close()


def configure():
    import PySimpleGUI as sg

    usbenabled = False
    boothdd = False
    bootpickenabled = False
    defaultbootdevice = "cd"
    layout = [[sg.Checkbox('USB Activated', default=False, key="-USB-")],
              [sg.Checkbox('HDD Enabled (MS-DOS Installed)', default=False, key="HDDENABLED")],
              [sg.Checkbox('Boot Picker Enabled', default=False, key="bootpick")],
              [sg.Text('Default Boot Device: '), sg.InputText(default_text="cd", key="default")],
              [sg.Text("set floppy image: "), sg.Button("..."), sg.Text(text="not selected", key="out")],
              [sg.Text("                   "), sg.Button("Save And Exit")]]

    window = sg.Window('Configuration Menu', layout, size=(400, 270))

    while True:
        event, values = window.read()
        text_elem = window['out']
        if event == sg.WIN_CLOSED or event == "Save And Exit":
            if values["-USB-"]: usbenabled = True
            if values["HDDENABLED"]: boothdd = True
            if values["bootpick"]: bootpickenabled = True
            if values["default"] == "cd":
                defaultbootdevice = "cd"
                break
            elif values["default"] == "floppy":
                defaultbootdevice = "floppy"
                break
            elif values["default"] == "hdd":
                if values["HDDENABLED"]:
                    defaultbootdevice = "hdd"
                    break
                else:
                    print("Config Error: HDD Is Not Activated, Configurations Are Not Saved.")
                    break
            elif values["default"] == "usb":
                if values["-USB-"]:
                    defaultbootdevice = "usb"
                    break
                else:
                    print("Config Error: USB Is Not Activated, Configurations Are Not Saved.")
                    break
            else:
                print("Config Error: Invalid Default Boot Device,  Configurations Are Not Saved.")
                break

        if event == "...":
            winout = selfloppyimg()
            window['out'].Update(winout)
            text_elem.update(font='Helvitica 6 bold italic')
    print("current default bootdevice: " + defaultbootdevice)

    window.close()
    os.system("cls")
    try:
        boot(usbenabled, boothdd, bootpickenabled, defaultbootdevice, filename=winout)
    except:
        boot(usbenabled, boothdd, bootpickenabled, defaultbootdevice, filename=None)


def test(filename, usbenabled):
    if not usbenabled:
        print()
        print()
        print("pick bootdevice")
        print()
        print("1. hdd")
        print("2. cd/dvd")
        print("3. floppy")
        pick = input("")
        if pick == "1":
            hdd()
        elif pick == "2":
            cd()
        elif pick == "3":
            floppy(filename)
    elif usbenabled:
        print()
        print()
        print("pick bootdevice")
        print()
        print("1. hdd")
        print("2. usb")
        print("3. cd/dvd")
        print("4. floppy")
        pick = input("")
        if pick == "1":
            hdd()
        elif pick == "2":
            usb(usbenabled, boothdd, bootpickenabled, defaultbootdevice, filename)
        elif pick == "3":
            cd()
        elif pick == "4":
            floppy(filename)


def start_menu():
    print("this is still under development")


def floppy(filename):
    floppy_file = open(filename, 'r')
    exec(floppy_file.read())

def start(usbenabled, boothdd, bootpickenabled, defaultbootdevice, filename):
    if bootpickenabled:
        if usbenabled:
            print("""

























           press F12 to enter setup      press ESC to enter bootpicker




""")
            time.sleep(3)  # Stop code for 3 seconds
            if keyboard.is_pressed("F12"):
                print("entering setup...")
                time.sleep(1)
                start_menu()
            elif keyboard.is_pressed('ESC'):
                if bootpickenabled:
                    print("entering bootmenu...")
                    time.sleep(1)
                    test(filename, usbenabled=usbenabled)
                else:
                    pass
            else:
                if defaultbootdevice == "cd":
                    cd()
                elif defaultbootdevice == "hdd":
                    hdd()
                elif defaultbootdevice == "floppy":
                    floppy(filename)
                elif defaultbootdevice == "usb":
                    usb(usbenabled, boothdd, bootpickenabled, defaultbootdevice, filename)
        else:
            print("""

























           press F12 to enter setup      press ESC to enter bootpicker




""")
            time.sleep(3)  # Stop code for 3 seconds
            if keyboard.is_pressed("F12"):
                print("entering setup...")
                time.sleep(1)
                start_menu()
            elif keyboard.is_pressed('ESC'):
                if bootpickenabled:
                    print("entering bootmenu...")
                    time.sleep(1)
                    test(filename, usbenabled=usbenabled)
                else:
                    pass
            else:
                if defaultbootdevice == "cd":
                    cd()
                elif defaultbootdevice == "hdd":
                    hdd()
                elif defaultbootdevice == "floppy":
                    floppy(filename)
    else:
        if usbenabled:
            print("""

























                       press F12 to enter setup




            """)
            time.sleep(3)  # Stop code for 3 seconds
            if keyboard.is_pressed("F12"):
                print("entering setup...")
                time.sleep(1)
                start_menu()
            else:
                if defaultbootdevice == "cd":
                    cd()
                elif defaultbootdevice == "hdd":
                    hdd()
                elif defaultbootdevice == "floppy":
                    floppy(filename)
                elif defaultbootdevice == "usb":
                    usb(usbenabled, boothdd, bootpickenabled, defaultbootdevice, filename)
        else:
            print("""
















 








                       press F12 to enter setup




            """)
            time.sleep(3)  # Stop code for 3 seconds
            if keyboard.is_pressed("F12"):
                print("entering setup...")
                time.sleep(1)
                start_menu()
            else:
                if defaultbootdevice == "cd":
                    cd()
                elif defaultbootdevice == "hdd":
                    hdd()
                elif defaultbootdevice == "floppy":
                    floppy(filename)
   

def boot(usbenabled, boothdd, bootpickenabled, defaultbootdevice, filename):
    pc_state = "Powered Off."
    os.system("title MS-98 [" + pc_state + "] - SeaBios Emulator")
    print(f"""Your PC Is Currently:
{pc_state}

press Ctrl and R to start it or
press Ctrl and S to open settings.
""")
    while 1:
        if keyboard.is_pressed("CTRL+R"):  # Press Control And R To Start It.
            pc_state = "Powering On..."
            time.sleep(2)
            os.system("cls")
            os.system("title MS-98 [" + pc_state + "] - SeaBios Emulator ")
            print(f"""Your PC Is Currently:
{pc_state}.
""")
            time.sleep(2)
            os.system("title MS-98 [Powered On..] - SeaBios Emulator")
            os.system("cls")
            start(usbenabled, boothdd, bootpickenabled, defaultbootdevice, filename)
        elif keyboard.is_pressed("CTRL+S"):
            configure()


boot(usbenabled, boothdd, bootpickenabled, defaultbootdevice, filename=None)
