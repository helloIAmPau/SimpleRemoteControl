#! /usr/bin/python

import mpd
import socket
import os
import getpass

import gobject

class Gestour():
  def __init__(self,thing):
    self.thing = thing
    self.CurrentTrack = 0

#################################################### Config Files

  def LoadConfig(self):
    self.ConfigFile="/home/%s/.config/simpleremotecontrol" % (getpass.getuser())
    try:
      Config=open(self.ConfigFile,"r")
    except:
      self.SaveConfig("127.0.0.1","6600","","True")
      self.LoadConfig()
    else:
      text = Config.read().split("\n")
      self.MPDServerAddress=text[0].split(":")[1]
      self.MPDServerPort=text[1].split(":")[1]
      self.MPDServerPassword=text[2].split(":")[1]
      self.ActiveNotify=text[3].split(":")[1]

  def SaveConfig(self,server,port,password,notify):
    string="""address:%s
port:%s
password:%s
notify:%s""" % (server,port,password,notify)
    Config=open(self.ConfigFile,"w")
    Config.write(string)
    Config.close()

##################################################### Player Block
  def MpdConnect(self):
    self.LoadConfig()
    try:
      player=mpd.MPDClient()
      player.connect(self.MPDServerAddress,self.MPDServerPort)
    except socket.error:
      return "connection error"
    else:
      return player

  def MpdDisconnect(self,player):
    try:
      player.close()
      player.disconnect()
    except:
      pass


  def KillMpd(self,null):
    try:
      output=os.system("mpd --kill")
    except:
      print output
    self.restart()

  def RunMpd(self):
    try:
      output=os.system("mpd")
    except:
      print output
    self.restart()

  def Stop(self,widget=None,event=None):
    player=self.MpdConnect()
    if player != "connection error":
      player.stop()
      self.MpdDisconnect(player)
    self.restart()

  def Play(self,widget=None,event=None):
    player=self.MpdConnect()
    if player != "connection error":
      if player.status()["state"] == "play":
        player.pause()
      else:
        player.play()
      self.MpdDisconnect(player)
    self.restart()

  def Next(self,widget=None,event=None):
    player=self.MpdConnect()
    if player != "connection error":
      player.next()
      self.MpdDisconnect(player)

  def Prev(self,widget=None,event=None):
    player=self.MpdConnect()
    if player != "connection error":
      player.previous()
      self.MpdDisconnect(player)

  def Shuffle(self,widget=None,event=None):
    player=self.MpdConnect()
    if player != "connection error":
      if player.status()["random"] == '1':
        player.random(0)
      else:
        player.random(1)
      self.MpdDisconnect(player)
    self.restart()

  def Repeat(self,widget=None,event=None):
    player=self.MpdConnect()
    if player != "connection error":
      if player.status()["repeat"] == '1':
        player.repeat(0)
      else:
        player.repeat(1)
      self.MpdDisconnect(player)
    self.restart()

###################################################### Must be a thread

  def restart(self):
    try:
      gobject.source_remove(self.iterate_handler)
    except:
      pass
    finally:
      self.bootstrap()

  def bootstrap(self):
    player=self.MpdConnect()
    if player == "connection error":
      self.SetWidgets(False,player)
    else:
      self.SetWidgets(True,player)
      if self.ActiveNotify == "True":
	try:
	  now=player.status()["songid"]
	except:
          pass
	else:
          if self.CurrentTrack != now:
            self.CurrentTrack = player.status()["songid"]
	    try:
              text="%s by %s"  % (player.currentsong()["title"],player.currentsong()["artist"])
            except:
	      text=player.currentsong()["file"]
	    self.thing.myBubbles.CreateBubble(text)
      self.MpdDisconnect(player)
    self.iterate_handler=gobject.timeout_add(1000, self.bootstrap)

  def SetWidgets(self, state, player):
    if state == True:
      self.thing.ButtonBar.show()
      if player.status()["state"] == "play":
	self.thing.PlayButton.set_image(self.thing.PauseButtonImage)
      else:
	self.thing.PlayButton.set_image(self.thing.PlayButtonImage)
      if player.status()["random"] == '1':
	self.thing.ShuffleMenuItem.set_active(True)
      else:
        self.thing.ShuffleMenuItem.set_active(False)
      if player.status()["repeat"] == '1':
	self.thing.RepeatMenuItem.set_active(True)
      else:
        self.thing.RepeatMenuItem.set_active(False)
    else:
      self.thing.ButtonBar.hide()
	
