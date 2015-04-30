import pynotify

class myBubbles():
  def __init__(self):
    self.ApplicationName="Simple Remote Control"
    pynotify.init("SimpleRemoteControl")
  
  def CreateBubble(self,message):
    self.ShowMessage(message)

  def ShowMessage(self,message):
    self.bubble=pynotify.Notification(self.ApplicationName, message)
    self.bubble.show()
