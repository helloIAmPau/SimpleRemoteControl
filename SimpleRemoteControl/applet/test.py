#!/usr/bin/python
import gtk
import pygtk

def toggle_func (widget, *user_data):
    frame = user_data[0]
    if frame.props.visible:
        frame.hide ()
    else:
        frame.show ()
    
window = gtk.Window ()
vbox = gtk.VBox ()
button = gtk.Button ("Toggle")

frame = gtk.HBox ()
label = gtk.Label ("Some Text")

frame.add (label)
vbox.pack_start (frame)
vbox.pack_start (button)

window.add (vbox)
button.connect ("clicked", toggle_func, frame)
window.connect ("delete-event", gtk.main_quit)
window.show_all ()
gtk.main ()
