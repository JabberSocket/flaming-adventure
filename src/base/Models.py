import Events

class Model:
  def __init__(self,_id):
    self._id = _id 

  def notify( self, event ):
    return True 

  def getId(self):
    return self._id

class Map(Model):
  def __init__(self, _id):
      self._id = _id

  def notify(self, event):
    return True

  def getStrRep(self):
    return "."

class Player(Model):
  def __init__(self, _id):
      self._id = _id
      self.name = "Flarg"
      self.health = 10.0

  def notify(self, event):
    return True

  def getName(self):
    return self.name

  def setName(self, name):
    self.name = name

  def getHealth(self):
    return self.health

  def setHealth(self, health):
    self.health = health
