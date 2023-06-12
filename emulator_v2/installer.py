import PySimpleGUI as sg
layout = [  [sg.Text("            Welcome To The EmuQemu Setup!")],     # Part 2 - The Layout
            [sg.Text("                 ")],
            [sg.Text("                 This Will Guide You Though The Setup")],
            [sg.Text("                 for EmuQemu!")],
            [sg.Text("                 Press Next To Continue.")],
            [sg.Text("")],
            [sg.Text("")],
            [sg.Text("")],
            [sg.Text("")],
            [sg.Text("")],
            [sg.Text("")],
            [sg.Text("")],
            [sg.Button("Close"), sg.Text("                                                                     "), sg.Button('Next')] ]

# Create the window
window = sg.Window('Emulator Setup', layout, size=(400, 350))      # Part 3 - Window Defintion

# Display and interact with the Window
event, values = window.read()                   # Part 4 - Event loop or Window.read call


# Finish up by removing from the screen
window.close()