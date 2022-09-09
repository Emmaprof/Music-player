import PySimpleGUI as sg
import vlc

controls = [sg.Button("play"), sg.Button("pause"), sg.Button("stop")]

layout = [[sg.FileBrowse(key ="-MP3-", enable_events = True)],controls]
player = None

# create the window
window = sg.Window("MP3 Player", layout)

# CREATE AN EVENT LOOP
while True:
    event, values = window.read()
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break
    # presses the play button
    if event =="-MP3-":
        player = vlc.MediaPlayer(values["-MP3-"])
        player.play()
    if event == "play" and player is not None:
        player.play()
    if event == "pause" and player is not None:
        player.pause()
    if event == "stop" and player is not None:
        player.stop()


window.close()