# journalcheck
A simple python gui program to check if a journal is in JCR.

## This project started as a way to solve three issues:
1. Quick consult a journal's ISSN for JCR and quartile
1. How to create a desktop application in python
1. Creating an imageApp (working on this)

# How does it work?
I'm using smago web site to get information about the ISSN, then another query
for the image of the quartil and the area of the journal.

Then to create the GUI, I uses PySimpleGUI, since it is very easy to use for
simple applications.

Now I'm in the process to create executables for different platforms as windows.

# Installation 
get the requirements
> pip3 install -r requirements.txt

Sometimes you need the package python3-tk to run it.

Then run the gui
> python3 gui.py
