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
    @staticmethod
    def reset_R():
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
    @staticmethod
    def reset_L():
        GPIO.output(15, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
    @staticmethod
    def set_R_forward():
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)
    @staticmethod
    def set_L_forward():
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(16, GPIO.LOW)
    @staticmethod
    def set_R_back():
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.HIGH)
    @staticmethod
    def set_L_back():
        GPIO.output(15, GPIO.LOW)
        GPIO.output(16, GPIO.HIGH)

class lock:
    @staticmethod
    def car_forward():
        my_motor = motor()
        my_motor.set_L_forward()
        my_motor.set_R_forward()
    @staticmethod
    def car_back():
        my_motor = motor()
        my_motor.set_L_back()
        my_motor.set_R_back()
    @staticmethod
    def car_stop():
        my_motor = motor()
        my_motor.reset_L()
        my_motor.reset_R()
commands = {
    'UFL':motor.set_L_forward,
    'USL':motor.reset_L,
    'UBL':motor.set_L_back,
    'UFR':motor.set_R_forward,
    'USR':motor.reset_R,
    'UBR':motor.set_R_back,
    'LKF':lock.car_forward,
    'LKS':lock.car_stop,
    'LKB':lock.car_stop,
}


def main():
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
    while True:
        socket_con,(client_ip, client_port) = socket_tcp.accept()
        print("Connection accepted from %s." % client_ip)
        socket_con.send("Welcome to RPi TCP server!")
        while True:
            try:
                data = socket_con.recv(1024)
                commands[data]()
                socket_con.send(data)
                print(data)
            except:
                print("Still On Line")
                break
            else:
                continue
        socket_con.close()

    socket_tcp.close()

if __name__ == "__main__":
    init()
    main()
    GPIO.cleanup()
