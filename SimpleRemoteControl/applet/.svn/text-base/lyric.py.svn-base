#! /usr/bin/python

import gtk
import urllib
import re

class LyricWindow():
  def __init__(self,gestour):
    self.gestour=gestour
    self.SetupWidgets()

#============================================= gtk stuffs

  def SetupWidgets(self):
    self.MainWindow=gtk.Window()
    
    self.MainConteiner=gtk.VBox()
    self.MainWindow.add(self.MainConteiner)

    self.Menubar=gtk.MenuBar()
    self.MainConteiner.pack_start(self.Menubar,False,False,0)

    self.File=gtk.MenuItem("_File")
    self.Menubar.add(self.File)
    
    self.FileMenu=gtk.Menu()
    self.File.set_submenu(self.FileMenu)

    self.Save=gtk.ImageMenuItem("_Save as txt")
    self.Save.connect("activate",self.save)
    self.FileMenu.append(self.Save)

    self.Exit=gtk.ImageMenuItem("E_xit")
    self.Exit.connect("activate",self.destroy)
    self.FileMenu.append(self.Exit)

    self.SongLabel=gtk.TextView()
    self.MainConteiner.add(self.SongLabel)

    self.Buffer=gtk.TextBuffer()
    self.SongLabel.set_buffer(self.Buffer)
  
  def save(self,widget):
    pass

  def destroy(self,widget):
    self.MainWindow.destroy()

  def run(self):
    self.GetLyric()
    self.MainWindow.show_all()

#===================================================== lyric stuff

  def GetLyric(self):
    info=self.gestour.MpdConnect()
    info=info.currentsong()
    artist=urllib.quote(info["artist"].lower().replace(' ','_'))
    title=urllib.quote(info["title"].lower().replace(' ','_'))
    print artist,title
    try:
      lyrics = urllib.urlopen('http://www.lyricsmode.com/lyrics/%s/%s/%s.html' % (artist[0],artist,title))
    except:
      text = "Could not connect to lyricsmode.com. Exiting..."
    else:
      text = lyrics.read().decode('latin-1').replace( u'\xb7','')
    p = re.compile(r'<[^<]*?/?>')
    text = p.sub('', text)
    p = re.compile(r'/<!--.*?-->/')
    text = p.sub('',text)

    self.Buffer.set_text(text)




