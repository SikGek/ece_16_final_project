"""
@author: Ramsin Khoshabeh
"""

from ECE16Lib.Communication import Communication
from ECE16Lib.CircularList import CircularList
from ECE16Lib.HRMonitor import HRMonitor
from time import sleep
import socket, pygame
import time


# Setup the Socket connection to the Space Invaders game
host = "127.0.0.1"
port = 65432
mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mySocket.connect((host, port))
mySocket.setblocking(False)

class PygameController:
  comms = None

  def __init__(self, serial_name, baud_rate):
    self.comms = Communication(serial_name, baud_rate)

  def run(self):
    # 1. make sure data sending is stopped by ending streaming
    self.comms.send_message("stop")
    self.comms.clear()

    # 2. start streaming orientation data
    input("Ready to start? Hit enter to begin.\n")
    self.comms.send_message("start")


    heartppg = 0                    # this is where we will store our heart rate data from arduino
    timeppg = 0
    header = 0
    fs = 50
    num_samples = 500
    command_list = []
    ppg = CircularList([], num_samples)
    times = CircularList([], num_samples)
    heart = HRMonitor(num_samples, fs, [])
    refresh_time = 1
    afk_list = []

    # 3. Forever collect orientation and send to PyGame until user exits
    print("Use <CTRL+C> to exit the program.\n")
    while True:
      message = self.comms.receive_message()

      if(message != None):
        command = None
        message = int(message)

        # want a counter for 30 seconds of afk, we exit the game
        if message == 0:
          afk_list.append(1)
        if len(afk_list) > 3000:
          command = "QUIT"

        # if message == 1:
        #   command = "UP"
        if message == 2:
          command = "FIRE"
          afk_list.clear()

        # appending the previous commands to a list so that we can decouple movement from firing
        elif message == 3:
          command = "LEFT"
          command_list.append(command)
          afk_list.clear()
        elif message == 4:
          command = "RIGHT"
          command_list.append(command)
          afk_list.clear()
        elif message == 5:
          command = "QUIT"
        print(command)
        if command is not None:
          # sending both previous and current move for decoupling and slightly smoother movement.
          mySocket.send(command.encode("UTF-8"))
          mySocket.send(command_list[-1].encode("UTF-8"))


if __name__== "__main__":
  serial_name = "COM4"
  baud_rate = 115200
  controller = PygameController(serial_name, baud_rate)

  try:
    controller.run()
  except(Exception, KeyboardInterrupt) as e:
    print(e)
  finally:
    print("Exiting the program.")
    controller.comms.send_message("stop")
    controller.comms.close()
    mySocket.send("QUIT".encode("UTF-8"))
    mySocket.close()

  input("[Press ENTER to finish.]")
