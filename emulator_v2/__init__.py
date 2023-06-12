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
    os.system(f"python {filename}")


def usb(usbenabled, boothdd, bootpickenabled, defaultbootdevice, filename):
    os.system("cls")
    print("""MJD95 BOOT MENU

PLEASE SELECT ONE OF THE BELOW:
1. BOOT MSDOS 6.22 INSTALLER
2. BOOT MSDOS PROMPT
3. BOOT HDD
4. BOOT FLOPPY
""")
    I = input("YOUR ANSWER: ")

    if I == "3":
        if boothdd:
            hdd()
        else:
            print ("NO OPERATING SYSTEM FOUND, SHUTING DOWN.")
            time.sleep(5)
    elif I == "4":
        floppy(filename=filename)
    else:
        print("not a valid answer")
    if I == "1":
        boothdd = "1"
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("0% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("2% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("4% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("5% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("7% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("9% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("11% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("12% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("14% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("15% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("17% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("19% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("20% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("22% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("24% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("25% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("27% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("29% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("31% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("32% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("34% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("35% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("37% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("39% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("40% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("42% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("44% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("45% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("47% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("49% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("51% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("52% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("54% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("55% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("57% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("59% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("60% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("62% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("64% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("65% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("67% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("69% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("71% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("82% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("84% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("89% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("97% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("99% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("100% installed..")
        time.sleep(3)
        os.system("cls")
        print("installation complete!")
        print("restarting the pc in 7 seconds...")
        time.sleep(7)
        boothdd=True
        defaultbootdevice="hdd"
        start(usbenabled, boothdd, bootpickenabled, defaultbootdevice, filename)

    if I == "2":
        os.system("cls")
        print("loading BOOT.IMG")
        print()
        print("starting MS-DOS...")
        print()
        print()
        print("HIMEM is testing extended memory...done.")

        def DOS():
            command = input("c:\>")
            if command == "dir":
                os.system("dir")
                DOS()
            elif command == "reboot --enable-hdd":
                boothdd = "1"
                os.system("cls")
                start(usbenabled, boothdd, bootpickenabled, defaultbootdevice, filename)
            elif command == "winver":
                print("invalid command 'winver'")
                DOS()
            elif command == "WINVER":
                print("invalid command 'winver'")
                DOS()
            else:
                os.system(command)
                DOS()

        DOS()


def cd():
    os.system("cls")
    print("Welcome to the MS-DOS 6.22 setup!")
    print("please select one choice...")
    print()
    print("1. boot MS-DOS 6.22 setup or")
    print("2. boot MS-DOS 6.22 demo")
    why = input("")
    if why == "1":
        os.system("cls")
        boothdd = "1"
        print("sit back and relax while we install MS-DOS 6.22...")
        print("0% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("2% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("4% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("5% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("7% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("9% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("11% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("12% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("14% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("15% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("17% installed..")
        time.sleep(3)
        os.system("cls")
        print("sit back and relax while we install MS-DOS 6.22...")
        print("19% installed..")
        time.sleep(3)
        os.system("cls")
        print("FATAL ERROR")
        print("4208.CP_ NOT FOUND SYSTEM HALTED")
        os.system("pause >nul")
    else:
        print("loading BOOT.IMG")
        print("loading MS-DOS...")
        time.sleep(6)
        print("FATAL ERROR")
        print("DOSBOX.IMG NOT FOUND SYSTEM HALTED")
        os.system("pause >nul")


def hdd():
    os.system("cls")
    print("starting MS-DOS...")
    print()
    print()
    print("HIMEM is testing extended memory...done.")

    def DOS1(bootdisk, combineinstalled, patchinstalled, wininstalled, sudoinstalled, pythoninstalled):
        command = input("c:\>")
        if command == "dir":
            os.system("dir")
            DOS1(bootdisk, combineinstalled, patchinstalled, wininstalled, sudoinstalled, pythoninstalled)
        elif command == "bootdisk --createfile:boot.img --bootimage:command.com, boot.bat":
            bootdisk = "1"
            time.sleep(3)
            print("completed creating bootfile boot.img")
            DOS1(bootdisk, combineinstalled, patchinstalled, wininstalled, sudoinstalled, pythoninstalled)
        elif command == "bootdisk --bootfile:boot.img":
            if bootdisk == "1":
                print("loading boot.img...")
                time.sleep(6)
                os.system("boot.bat")
                os.system("color 07")
                os.system("cls")
                DOS1(bootdisk, combineinstalled, patchinstalled, wininstalled, sudoinstalled, pythoninstalled)
            else:
                print("can not find file boot.img")
                DOS1(bootdisk, combineinstalled, patchinstalled, wininstalled, sudoinstalled, pythoninstalled)
        elif command == "bootdisk --deletefile:boot.img":
            bootdisk = "0"
            time.sleep(3)
            print("completed deleting bootfile boot.img")
            DOS1(bootdisk, combineinstalled, patchinstalled, wininstalled, sudoinstalled, pythoninstalled)
        elif command == "winver":
            print("invalid command 'winver'")
            DOS1(bootdisk, combineinstalled, patchinstalled, wininstalled, sudoinstalled, pythoninstalled)
        elif command == "WINVER":
            print("invalid command 'winver'")
            DOS1(bootdisk, combineinstalled, patchinstalled, wininstalled, sudoinstalled, pythoninstalled)
        elif command == "HELP bootdisk":
            print("""
                            #########
                            help
                            #########
                            command
                            bootdisk
                            uses:

                            --createfile, creates a filename and an .img file out of specified files
                            --bootimage, uses the files named to make an .img file
                            --bootfile, executes given .img file
                            --deletefile, deletes an given .img file
                            examples:
                            To create and run a img file out of a batch file:
                            1. bootdisk --createfile:boot.img --bootimage:command.com, boot.bat 
                            2. bootdisk --bootfile:boot.img
                            To create and delete a img file out of a batch file:
                            1. bootdisk --createfile:boot.img --bootimage:command.com, boot.bat
                            2. bootdisk --deletefile:boot.img
                            press any key to continue to the MS-DOS prompt...""")
            key = input("")
            if key == "":
                DOS1(bootdisk, combineinstalled, patchinstalled, wininstalled, sudoinstalled, pythoninstalled)
            else:
                DOS1(bootdisk, combineinstalled, patchinstalled, wininstalled, sudoinstalled, pythoninstalled)
        elif command == "help bootdisk":
            print("""
                #########
                help
                #########
                command
                bootdisk
                uses:

                            --createfile, creates a filename and an .img file out of specified files
                            --bootimage, uses the files named to make an .img file
                            --bootfile, executes given .img file
                            --deletefile, deletes an given .img file

                examples:

                To create and run a img file out of a batch file:
                1. bootdisk --createfile:boot.img --bootimage:command.com, boot.bat 
                2. bootdisk --bootfile:boot.img

                To create and delete a img file out of a batch file:
                1. bootdisk --createfile:boot.img --bootimage:command.com, boot.bat
                2. bootdisk --deletefile:boot.img

                press any key to continue to the MS-DOS prompt...""")
            key = input("")
            if key == "":
                DOS1(bootdisk, combineinstalled, patchinstalled, wininstalled, sudoinstalled, pythoninstalled)
            else:
                DOS1(bootdisk, combineinstalled, patchinstalled, wininstalled, sudoinstalled, pythoninstalled)
        elif command == "installapp win95installer":
            os.system("cls")
            combineinstalled = "1"
            print("installing windows 95 installer...")
            print("\033[0;31m ━ \033[0m .01/1Gb 690.8 kB/s eta 0:00:10")
            time.sleep(1)
            os.system("cls")
            print("installing windows 95 installer...")
            print("\033[0;31m ━━━━━━━━ \033[0m .20/1GB 690.8 kB/s eta 0:00:2")
            time.sleep(1)
            os.system("cls")
            print("installing windows 95 installer...")
            print("\033[0;31m ━━━━━━━━━━━━ \033[0m .30/1GB 690.8 kB/s eta 0:00:01")
            time.sleep(.1)
            os.system("cls")
            print("installing windows 95 installer...")
            print("\033[0;31m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \033[0m .96/1GB 690.8 kB/s eta 0:00:00")
            time.sleep(1)
            os.system("cls")

            print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \033[0m 1/1GB 690.8 kB/s eta 0:00:00")
            print("extracting files...")
            time.sleep(1)
            print("extracted files")
            print("installed windows 95 installer")
            DOS1(bootdisk, combineinstalled, patchinstalled, wininstalled, sudoinstalled, pythoninstalled)
        elif command == "setup":
            if patchinstalled == "1":
                os.system("cls")
                wininstalled = "1"
                print("""windows 95 setup
━━━━━━━━━━━━━━━━
                      This will upgrade you MS-DOS 6.22 installation to windows 95                
                                     are you sure? 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 Y = Continue   F3 = EXIT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
                while 1:
                    if keyboard.is_pressed('F3'):
                        DOS1(bootdisk, combineinstalled, patchinstalled, wininstalled, sudoinstalled, pythoninstalled)
                    elif keyboard.is_pressed("Y"):
                        os.system("cls")
                        print("""windows 95 setup
━━━━━━━━━━━━━━━━━
                   ╔══════════════════════════╗
                   ║The drive is too large to ║
                   ║support windows 95. do you║
                   ║   enable large fat32?    ║
                   ╚══════════════════════════╝
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    F3 = EXIT Y = yes N = No
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
                    while "true":
                        if keyboard.is_pressed('F3'):
                            DOS1(bootdisk, combineinstalled, patchinstalled, wininstalled, sudoinstalled,
                                 pythoninstalled)
                        elif keyboard.is_pressed("n"):
                            DOS1(bootdisk, combineinstalled, patchinstalled, wininstalled, sudoinstalled,
                                 pythoninstalled)
                        elif keyboard.is_pressed("Y"):
                            os.system("cls")
                            print("""windows 95 setup
━━━━━━━━━━━━━━━━━
                   ╔══════════════════════════╗
                   ║     formatting disk      ║
                   ║                          ║
                   ║            0%            ║
                   ║                          ║
                   ╚══════════════════════════╝
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
                            time.sleep(12)
                            os.system("cls")
                            print("""windows 95 setup
━━━━━━━━━━━━━━━━━
                   ╔══════════════════════════╗
                   ║     formatting disk      ║
                   ║                          ║
                   ║           24%            ║
                   ║                          ║
                   ╚══════════════════════════╝
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
                            time.sleep(8)
                            os.system("cls")
                            print("""windows 95 setup
━━━━━━━━━━━━━━━━━
                   ╔══════════════════════════╗
                   ║     formatting disk      ║
                   ║                          ║
                   ║           50%            ║
                   ║                          ║
                   ╚══════════════════════════╝
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
                            time.sleep(4)
                            os.system("cls")
                            print("""windows 95 setup
━━━━━━━━━━━━━━━━━
                   ╔══════════════════════════╗
                   ║     formatting disk      ║
                   ║                          ║
                   ║           70%            ║
                   ║                          ║
                   ╚══════════════════════════╝
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
                            time.sleep(3)
                            os.system("cls")
                            print("""windows 95 setup
━━━━━━━━━━━━━━━━━
                       ╔══════════════════════════╗
                       ║     formatting disk      ║
                       ║                          ║
                       ║           99%            ║
                       ║                          ║
                       ╚══════════════════════════╝
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
                            os.system("cls")
                            print("""windows 95 setup
━━━━━━━━━━━━━━━━
                                  Press Enter To Restart 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ENTER = Restart
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
                            os.system("pause >nul")

                            boothdd = "1"
                            start(boothdd, bootdisk, combineinstalled, patchinstalled, wininstalled, sudoinstalled)
            elif patchinstalled == "0":
                print("Not Enough RAM For The Windows Setup")
                DOS1(bootdisk, combineinstalled, patchinstalled, wininstalled, sudoinstalled, pythoninstalled)
        elif command == "installapp 95patch":
            os.system("cls")
            patchinstalled = "1"
            print("installing 95patch...")
            print("\033[0;31m ━ \033[0m .01/10MB 690.8 kB/s eta 0:00:10")
            time.sleep(1)
            os.system("cls")
            print("installing 95patch...")
            print("\033[0;31m ━━━━━━━━ \033[0m .20/10MB 690.8 kB/s eta 0:00:2")
            time.sleep(1)
            os.system("cls")
            print("installing 95patch...")
            print("\033[0;31m ━━━━━━━━━━━━━━━━ \033[0m .50/10MB 690.8 kB/s eta 0:00:01")
            time.sleep(.1)
            os.system("cls")
            print("installing 95patch...")
            print("\033[0;31m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \033[0m .96/10MB 690.8 kB/s eta 0:00:00")
            time.sleep(1)
            os.system("cls")
            print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \033[0m 1/10MB 690.8 kB/s eta 0:00:00")
            print("extracting files...")
            time.sleep(1)
            print("extracted files")
            print("installed w95patch")
            DOS1(bootdisk, combineinstalled, patchinstalled, wininstalled, sudoinstalled, pythoninstalled)
        elif command == "exec(dlc.custom_dlc)":
            dlcs.exec()
        elif command == "win":
            if wininstalled == "1":
                print("""
                    This is an demo program
                    Made in Python!
                    By your favourite friend,
                    Mikolaj!
                    I hope you liked it!

                    Press enter to exit to
                    DOS prompt.""")
                os.system("pause")
                DOS1(bootdisk, combineinstalled, patchinstalled, wininstalled, sudoinstalled, pythoninstalled)
            else:
                print("windows is not installed...")
                DOS1(bootdisk, combineinstalled, patchinstalled, wininstalled, sudoinstalled, pythoninstalled) 
    def windows():
        print("""
            This is an demo program
            Made in Python!
            By your favourite friend,
            Mikolaj!
            I hope you liked it!
            Press enter to exit to
             DOS prompt... """)
        os.system("pause >nul")
        DOS1(bootdisk, combineinstalled, patchinstalled, wininstalled, sudoinstalled, pythoninstalled)

    if wininstalled == "0":
        DOS1(bootdisk, combineinstalled, patchinstalled, wininstalled, sudoinstalled, pythoninstalled)
    elif wininstalled == "1":
        windows()


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
