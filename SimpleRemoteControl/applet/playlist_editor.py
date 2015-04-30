#! /usr/bin/python

import gtk
import gobject

class PlaylistEditor():
  def __init__(self,gestour):
    self.gestour=gestour
    self.SetupWidgets()
    self.CurrentTrack = 0
    self.CurrentSongInformation()


  def SetupWidgets(self):
    self.MainWindow=gtk.Window()
    self.MainWindow.set_title("SimpleRemoteControl - Playlist Editor")
    self.MainWindow.set_default_size(550,400)
    self.MainWindow.set_resizable(False)

    self.MainConteiner=gtk.VBox()
    self.MainWindow.add(self.MainConteiner)

    self.InfoConteiner=gtk.HBox()
    self.MainConteiner.pack_start(self.InfoConteiner,expand=False, fill=False, padding=0)

    self.AlbumArt=gtk.Image()
    self.AlbumArt.set_from_stock("gtk-media-play",gtk.ICON_SIZE_DIALOG)
    self.InfoConteiner.pack_start(self.AlbumArt,expand=True, fill=False, padding=0)

    self.InfoBox=gtk.VBox()
    self.InfoConteiner.pack_start(self.InfoBox,expand=True, fill=False, padding=0)
    
    self.SongLabel=gtk.Label("Song")
    self.InfoBox.pack_start(self.SongLabel, expand=False, fill=False, padding=5)
    
    self.ArtistRow=gtk.HBox()
    self.InfoBox.pack_start(self.ArtistRow, expand=False, fill=False, padding=5)
    self.byLabel=gtk.Label("by ")
    self.ArtistRow.pack_start(self.byLabel, expand=False, fill=False, padding=0)
    self.ArtistLabel=gtk.Label("Artist")
    self.ArtistRow.pack_start(self.ArtistLabel, expand=False, fill=False, padding=0)
    
    
    self.AlbumRow=gtk.HBox()
    self.InfoBox.pack_start(self.AlbumRow, expand=False, fill=False, padding=5)
    self.fromLabel=gtk.Label("from ")
    self.AlbumRow.pack_start(self.fromLabel, expand=False, fill=False, padding=0)
    self.AlbumLabel=gtk.Label("Album")
    self.AlbumRow.pack_start(self.AlbumLabel, expand=False, fill=False, padding=0)

    
    self.MainNotebook=gtk.Notebook()
    self.MainConteiner.pack_start(self.MainNotebook,expand=True, fill=True, padding=0)

    self.PlaylistConteiner=gtk.VBox()
    self.MainNotebook.append_page(self.PlaylistConteiner,gtk.Label("Playlist"))

  def CurrentSongInformation(self):
    player=self.gestour.MpdConnect()
    if player != "connection error":
      if self.CurrentTrack != player.status()["songid"]:
	info=player.currentsong()
	self.CurrentTrack = player.status()["songid"]
	try:
          self.ArtistLabel.set_label(info["artist"])
	except:
          self.ArtistLabel.set_label("Unknow")
	try:
	  self.SongLabel.set_label(info["title"])
	except:
          self.SongLabel.set_label("Unknow")
	try:
	  self.AlbumLabel.set_label(info["album"])
	except:
	  self.AlbumLabel.set_label("Unknow")
    self.iterate_handler=gobject.timeout_add(2000, self.CurrentSongInformation)


  def run(self):
    self.MainWindow.show_all()
