#! /usr/bin/python

import gtk


class MyDialogs():

  def __init__(self, kind, gestour=None):
    self.kind = kind
    self.gestour=gestour
    self.CreateDialog()

  def CreateDialog(self):
    if self.kind=="About":
      self.dialog=gtk.AboutDialog()
      self.dialog.set_name("SimpleRemoteControl")
      self.dialog.set_version("0.99develop")
      self.dialog.set_comments("This version is only for develop. The stable versions are on the site")
      self.dialog.set_website("http://code.google.com/p/simplerc/")
      self.dialog.set_authors(("From an idea and devoleped by:","Pasquale Boemio <boemianrapsodi@gmail.com>",))
    elif self.kind=="Config":
      self.dialog=gtk.Dialog(title="SimpleRemoteControl Setup",buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_REJECT,gtk.STOCK_OK,99))
      
      address=self.gestour.MPDServerAddress
      port=self.gestour.MPDServerPort
      password=self.gestour.MPDServerPassword
      if self.gestour.ActiveNotify == "True":
	notify=1
      else:
	notify=0

      self.MPDFrame=gtk.Frame("MPD Configuration")
      self.MPDBody=gtk.VBox()
      self.MPDFrame.add(self.MPDBody)
      
      self.AddressLine=gtk.HBox()
      self.MPDBody.add(self.AddressLine)
      self.AddressLabel=gtk.Label("Server Address:")
      self.AddressLine.add(self.AddressLabel)
      self.AddressEntry=gtk.Entry()
      self.AddressEntry.set_text(address)
      self.AddressLine.add(self.AddressEntry)

      self.PortLine=gtk.HBox()
      self.MPDBody.add(self.PortLine)
      self.PortLabel=gtk.Label("Server Port:")
      self.PortLine.add(self.PortLabel)
      self.PortEntry=gtk.Entry()
      self.PortEntry.set_text(port)
      self.PortLine.add(self.PortEntry)

      self.PasswordLine=gtk.HBox()
      self.MPDBody.add(self.PasswordLine)
      self.PasswordLabel=gtk.Label("Password:")
      self.PasswordLine.add(self.PasswordLabel)
      self.PasswordEntry=gtk.Entry()
      self.PasswordEntry.set_visibility(False)
      self.PasswordEntry.set_text(password)
      self.PasswordLine.add(self.PasswordEntry)

      self.dialog.vbox.add(self.MPDFrame)

      self.NotificationEntry=gtk.CheckButton("Notify on song change?")
      self.NotificationEntry.set_active(notify)
      self.dialog.vbox.add(self.NotificationEntry)
      
      self.dialog.show_all()

  def destroy(self):
    self.dialog.destroy()

  def start(self):
    response=self.dialog.run()
    return response
