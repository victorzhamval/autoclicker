import multiprocessing
import time
import mouse

class Autoclicker:

  def __process(self, cps, button):
    print("Auto-clicker started")
    delay = 1 / int(cps)
    while (True):
      mouse.click(button)
      print("Click")
      time.sleep(delay)

  def start(self, cps, button):
    self.task = multiprocessing.Process(target=self.__process, args=(cps, button))
    self.task.start()

  def stop(self):
    self.task.terminate()
    print("Stop...")