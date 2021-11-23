#!/bin/python3

import dbus

# instantiate session bus
bus = dbus.SessionBus()
# get bus object with bus name and bus object path
spotify = bus.get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2')
# execute method play from spotify interface
play = spotify.Play(dbus_interface='org.mpris.MediaPlayer2.Player')

