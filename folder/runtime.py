import typer, PySimpleGUI as sg, runtime

app = typer.Typer()

layout = [[sg.Text('parameter needed to run')],
          [sg.Button('OK'), sg.Exit()]]


@app.command()
def hello(enable: bool = False):
    if enable == True:
        runtime.start()
    elif enable == False:
        window = sg.Window('Error', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Exit' or event == "OK":
                break

        window.close()


if __name__ == "__main__":
    app()
