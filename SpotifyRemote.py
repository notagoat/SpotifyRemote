#!/usr/bin/env python3
import os
command = " "
EndBool = False

print(" Spotify Terminal Remote! ")
print(" ________________________ ")
print("")

def cmdlist():
    print ("")
    print ("Spotify Remote for Linux")
    print ("Commands:"),
    print ("\n \t next: Next Track"),
    print ("\n \t previous: Previous Track"),
    print ("\n \t pause: Pause Playback"),
    print ("\n \t play: Resume Playback"),
    print ("\n \t help: Show list of commands")
    print ("\n \t end: Ends the program")
while (EndBool == False):
    command = input("Please enter a command: ")
    stem = "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player."
    if command == ("next"):
        os.system(stem + "Next")
    elif command == ("pause"):
        os.system(stem + "Pause")
    elif command == "previous":
        os.system(stem + "Previous")
    elif command == ("play"):
        os.system(stem + "Play")
    elif command == ("help"):
        cmdlist()
    elif command == ("end"):
        EndBool = True
    else:
        print("Command not valid. 'help' for a list of commands")
