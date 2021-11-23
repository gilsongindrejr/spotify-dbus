#!/bin/python3

import dbus

# instantiate session bus
bus = dbus.SessionBus()
# get object by bus name and object path
spotify = bus.get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2')
# create interface using spotify object and speccified dbus iterface
iface = dbus.Interface(spotify, dbus_interface='org.freedesktop.DBus.Properties')
# execute method get from specified interface
metadata = iface.Get('org.mpris.MediaPlayer2.Player', 'Metadata')
# get title and artist
title = metadata.get('xesam:title')
artist = metadata.get('xesam:artist')[0]
print(f'{title} - {artist}')

