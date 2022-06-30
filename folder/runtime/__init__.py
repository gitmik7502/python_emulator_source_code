import os

def start():
    a = open("systemfiles/core.dll", "r")
    if a.read(3) == "dll":
        a = open("systemfiles/emulatorVM.dll", "r")
        if a.read(3) == "dll":
            a = open("systemfiles/x86core.dll", "r")
            if a.read(3) == "dll":
                a = open("systemfiles/runtime.dll", "r")
                if a.read(3) == "dll":
                    print("all dlls are present!")
                    os.system("md %temp%\execute")
                    os.system("copy systemfiles\old.execute.dll %temp%\execute\execute.exe")
                    os.system("cls")
                    os.system("%temp%\execute\execute.exe")