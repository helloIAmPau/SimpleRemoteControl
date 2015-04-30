#! /usr/bin/python

import pygtk
pygtk.require('2.0')
import gtk

import gestour
import notifications
import some_dialogs
import playlist_editor
import lyric

class myApplet():
  def __init__(self,applet):
    self.applet = applet
    self.myGestour=gestour.Gestour(self)
    self.Setup()
    self.myBubbles=notifications.myBubbles()

###################################################### Setup Main Widgets
  def Setup(self):
    self.MainConteiner = gtk.HBox()
    self.applet.add(self.MainConteiner)
    
    self.MenuBar = gtk.MenuBar()
    self.MenuBar.connect("button_press_event", self.DefSetupMenu)

    self.MpdButton = gtk.MenuItem("mpd")
    self.MenuBar.add(self.MpdButton)
    self.MainConteiner.add(self.MenuBar)

    self.DefButtonBar()
    self.DefMainMenu()
  
###################################################### Def Other Widgets
  def DefMainMenu(self):
    self.MainMenu = gtk.Menu()
    self.MpdButton.set_submenu(self.MainMenu)
    

    self.StopMenuItem = gtk.ImageMenuItem("Stop")
    self.StopMenuItemImage = gtk.Image()
    self.StopMenuItemImage.set_from_stock(gtk.STOCK_MEDIA_STOP,gtk.ICON_SIZE_BUTTON)
    self.StopMenuItem.set_image(self.StopMenuItemImage)
    self.StopMenuItem.connect("activate",self.myGestour.Stop)
    self.MainMenu.append(self.StopMenuItem)

    self.ShuffleMenuItem = gtk.CheckMenuItem("Shuffle")
    self.ShuffleMenuItem.connect("activate",self.myGestour.Shuffle)
    self.MainMenu.append(self.ShuffleMenuItem)

    self.RepeatMenuItem = gtk.CheckMenuItem("Repeat")
    self.RepeatMenuItem.connect("activate",self.myGestour.Repeat)
    self.MainMenu.append(self.RepeatMenuItem)

#    self.MainMenu.append(gtk.SeparatorMenuItem())

    self.PlaylistMenuItem = gtk.ImageMenuItem("Playlist Editor")
    self.PlaylistMenuItem.connect("activate",self.RunPlaylistEditor)
    self.MainMenu.append(self.PlaylistMenuItem)

    self.LyricMenuItem = gtk.ImageMenuItem("Fetch Lyric")
    self.LyricMenuItem.connect("activate",self.RunLyric)
#    self.MainMenu.append(self.LyricMenuItem)

    self.MainMenu.append(gtk.SeparatorMenuItem())

    self.KillMenuItem = gtk.ImageMenuItem("Kill Daemon")
    self.KillMenuItemImage = gtk.Image()
    self.KillMenuItemImage.set_from_stock("gtk-stop",gtk.ICON_SIZE_BUTTON)
    self.KillMenuItem.set_image(self.KillMenuItemImage)
    self.KillMenuItem.connect("activate",self.myGestour.KillMpd)
    self.MainMenu.append(self.KillMenuItem)
	
  def DefButtonBar(self):
    self.ButtonBar=gtk.HBox()
    self.MainConteiner.add(self.ButtonBar)

    self.PrevButton = gtk.Button()
    self.PrevButtonImage = gtk.Image()
    self.PrevButtonImage.set_from_stock(gtk.STOCK_MEDIA_PREVIOUS,gtk.ICON_SIZE_BUTTON)
    self.PrevButton.set_image(self.PrevButtonImage)
    self.PrevButton.set_relief(gtk.RELIEF_NONE)
    self.PrevButton.connect("clicked",self.myGestour.Prev)
    self.ButtonBar.add(self.PrevButton)

    self.PlayButton = gtk.Button()
    self.PlayButtonImage = gtk.Image()
    self.PlayButtonImage.set_from_stock(gtk.STOCK_MEDIA_PLAY,gtk.ICON_SIZE_BUTTON)
    self.PauseButtonImage = gtk.Image()
    self.PauseButtonImage.set_from_stock(gtk.STOCK_MEDIA_PAUSE,gtk.ICON_SIZE_BUTTON)
    self.PlayButton.set_relief(gtk.RELIEF_NONE)
    self.PlayButton.connect("clicked",self.myGestour.Play)
    self.ButtonBar.add(self.PlayButton)

    self.NextButton = gtk.Button()
    self.NextButtonImage = gtk.Image()
    self.NextButtonImage.set_from_stock(gtk.STOCK_MEDIA_NEXT,gtk.ICON_SIZE_BUTTON)
    self.NextButton.set_image(self.NextButtonImage)
    self.NextButton.set_relief(gtk.RELIEF_NONE)
    self.NextButton.connect("clicked",self.myGestour.Next)
    self.ButtonBar.add(self.NextButton)

  def DefSetupMenu(self,widget, event):
    if event.button == 3:
      widget.emit_stop_by_name("button_press_event")
      propxml="""
      <popup name="button3">
      <menuitem name="SetupItem" verb="Setup" label="_Configure Applet" pixtype="stock" pixname="gtk-setup"/>
      <menuitem name="AboutItem" verb="About" label="_About" pixtype="stock" pixname="gtk-about"/>
      </popup>"""
      verbs = [("Setup", self.RunConfig),("About", self.RunAbout)]
      self.applet.setup_menu(propxml,verbs,None)

    if event.button == 1:
      if not self.ButtonBar.props.visible:
        widget.emit_stop_by_name("button_press_event")
        self.myGestour.RunMpd()
      
###################################################### Other Functions
  def RunLyric(self,widget):
    lyricWindow=lyric.LyricWindow(self.myGestour)
    lyricWindow.run()

  def RunPlaylistEditor(self,widget):
    playlistWindow=playlist_editor.PlaylistEditor(self.myGestour)
    playlistWindow.run()

  def RunAbout(self,widget,event):
    dialog = some_dialogs.MyDialogs("About")
    dialog.start()
    dialog.destroy()

  def RunConfig(self,widget,event):
    dialog = some_dialogs.MyDialogs("Config",self.myGestour)
    response=dialog.start()
    if response == 99:
       self.myGestour.SaveConfig(dialog.AddressEntry.get_text(), dialog.PortEntry.get_text(), dialog.PasswordEntry.get_text(), dialog.NotificationEntry.get_active())
    dialog.destroy()


  def run(self):
    self.applet.show_all()
    self.myGestour.bootstrap()

