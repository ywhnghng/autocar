#!/user/bin/env python
import RPi.GPIO as GPIO
import socket
import time
import sys

def init():
     GPIO.setmode(GPIO.BOARD)
     GPIO.setup(11, GPIO.OUT)
     GPIO.setup(13, GPIO.OUT)
     GPIO.setup(15, GPIO.OUT)
     GPIO.setup(16, GPIO.OUT)

class motor:
    def reset_R(self):
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
    def reset_L(self):
        GPIO.output(15, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
    def set_R_forward(self):
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)
    def set_L_forward(self):
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(16, GPIO.LOW)
    def set_R_back(self):
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.HIGH)
    def set_L_back(self):
        GPIO.output(15, GPIO.LOW)
        GPIO.output(16, GPIO.HIGH)

class lock:
    def car_forward(self):
        my_motor = motor()
        my_motor.set_L_forward()
        my_motor.set_R_forward()
    def car_back(self):
        my_motor = motor()
        my_motor.set_L_back()
        my_motor.set_R_back()
    def car_stop(self):
        my_motor = motor()
        my_motor.reset_L()
        my_motor.reset_R()


def server():
     HOST_IP = "192.168.1.1"
     HOST_PORT = 8888
     print("Starting socket: TCP...")
     # 1.create socket object:socket=socket.socket(family,type)
     socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     print("TCP server listen @ %s:%d!" % (HOST_IP, HOST_PORT))
     host_addr = (HOST_IP, HOST_PORT)
     # 2.bind socket to addr:socket.bind(address)
     socket_tcp.bind(host_addr)
     # 3.listen connection request:socket.listen(backlog)
     socket_tcp.listen(5)
     # 4.waite for client:connection,address=socket.accept()
     socket_con,(client_ip, client_port) = socket_tcp.accept()
     print("Connection accepted from %s." % client_ip)
     socket_con.send("Welcome to RPi TCP server!")

if __name__ == "__main__":
     init()
     while True:
          data =

    GPIO.cleanup()
def server():
     HOST_IP = "192.168.1.1"
     HOST_PORT = 8888
     print("Starting socket: TCP...")
     # 1.create socket object:socket=socket.socket(family,type)
     socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     print("TCP server listen @ %s:%d!" % (HOST_IP, HOST_PORT))
     host_addr = (HOST_IP, HOST_PORT)
     # 2.bind socket to addr:socket.bind(address)
     socket_tcp.bind(host_addr)
     # 3.listen connection request:socket.listen(backlog)
     socket_tcp.listen(1)
     # 4.waite for client:connection,address=socket.accept()
     socket_con, (client_ip, client_port) = socket_tcp.accept()
     print("Connection accepted from %s." % client_ip)
     socket_con.send("Welcome to RPi TCP server!")
     data = socket_con.recv()