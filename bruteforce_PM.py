import hid
import subprocess
import time
import serial



class server():
    def __init__(self):
        print("input path to wordlist: ")
        wordlist = input()
        self.__wordlist__ = wordlist
        self.__con__ = self.connection()

    def send_keys(self, word): #Send keystrokes to be sent via the RPI
        for word in self.__wordlist__:
            self.log_output(word)
            self.write(bytes(word))

    def connection(self): #Connect to RPI
        ser = serial.Serial('dev/ttyUSB0',
                        baudrate=115200,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE)
        return ser
    
    def log_output(word):
        print(word)


def __main__():
    new_server = server()
    new_server.open()
    if new_server.is_open():
        print("Connection Established\n")
        new_server.send_keys()