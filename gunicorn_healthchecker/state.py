class State():
  def __new__(cls):
    if not hasattr(cls,'instance'):
      cls.workers = 0
      cls.idle = 0
      cls.healthy = True
      cls.busy = False
      cls.availability = 1
      cls.instance = super(State, cls).__new__(cls)
    return cls.instance
  
  def dict(self):
    return self.__dict__