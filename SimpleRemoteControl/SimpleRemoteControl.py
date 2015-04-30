#!/usr/bin/env python
#
# Simple Remote Control
# A simple controller for mpd player
#	created by Pasquale Boemio
#	boemianrapsodi@gmail.com

import gnomeapplet
import sys
import applet.ui as ui
import gtk


def Factory(applet,iid):
    myApplet=ui.myApplet(applet)
    myApplet.run()
    return gtk.TRUE

if len(sys.argv) == 2:
    if sys.argv[1] == "test": #Debug mode
        main_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        main_window.set_title("Python Applet")
        main_window.connect("destroy", gtk.main_quit)
        app = gnomeapplet.Applet()
        Factory(app,None)
        app.reparent(main_window)
        main_window.show_all()
        gtk.main()
        sys.exit()

#If called via gnome panel, run it in the proper way
if __name__ == '__main__':
    gnomeapplet.bonobo_factory("OAFIID:GNOME_SimpleRemoteControl_Factory", gnomeapplet.Applet.__gtype__, "hello", "0", Factory)

