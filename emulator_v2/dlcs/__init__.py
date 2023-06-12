# coding=utf-8
import os

try:
    from python import *
except:
    print("python dlc not installed")
try:
    from sudo import *
except:
    print("sudo dlc not installed")
try:
    from custom_dlc import *
except:
    print("custom dlc not found")

def sudo_command(opptype, libery):
    try:
        sudo1(opptype=opptype, libery=libery)
    except:
        print("'sudo' is not recognized as an internal or external command.")
def exec_lib():
    exec()


