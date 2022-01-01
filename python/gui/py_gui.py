#! /usr/bin/env python

import sys
from guizero import App, PushButton, Text

app = App(title="My Sample Application")

def button_clicked():
    clicked_label.clear()
    clicked_label.append("Hello Button clicked!")

def exit_app():
    sys.exit()

Text(app, text="Click Below:")
button = PushButton(app, text="HERE", command=button_clicked)
button2 = PushButton(app, text="EXIT", command=exit_app)
clicked_label = Text(app, text="")

app.display()