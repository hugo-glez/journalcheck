#! /usr/bin/env python3
# Copyright (c) 2019 Hugo Gonzalez @hugo_glez
#
# This file is part of JournalCheck
# (see github.com/hugo-glez/journalcheck).

# License: 3-clause BSD, see https://opensource.org/licenses/BSD-3-Clause
#
"""
This is the gui interface for the project. It is based on a PySimpleGUI pattern
for a simple window. It uses libjc to retrieve the information.

"""

import PySimpleGUI as sg
import libjc

# All the stuff inside your window.
layout = [  [sg.Text('Look if a journal is in the JCR index, and the quartile')],
            [sg.Text('ISSN of the journal'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')],
            [sg.Text(size=(40,3), key='tResult')],
            [sg.Image(filename="",key='iResult')],
            [sg.Text('Powered by SCIMAGO https://www.scimagojr.com')]
            ]

# Create the Window
window = sg.Window('Journal Check', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    (v,im) = libjc.getinfo(values[0])
    window['tResult'].update(v)
    window['iResult'].update(data=im)

window.close()
