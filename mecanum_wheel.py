# -*- coding: utf-8 -*-
# Mecanum wheel

import serial

# ###############################
#
#     y
#    ^
#    |
#    |     /A-----B\
#    |      |     |
#    |      |     |
#    |     \C-----D/
#    |
#    -------->x
#
################################


class MecanumWheel():
    def __init__(self, serial_dev='/dev/ttyUSB0'):
        self.min_pwm = 500 
        self.max_pwm = 1800 

        self.ser = serial.Serial(serial_dev, 9600)
        self.ser.read_all()
        self.last_vx = 0 
        self.last_vy = 0
        self.last_rotate = 0 


    def control(self, vx, vy, rotate):
        if vx == self.last_vx and vy == self.last_vy and rotate == self.last_vy:
            return

        print("vx , vy , rotate = ==== ", vx, vy, rotate)
        va = (vx + vy ) * 1200 - rotate * 800 
        vc = (-vx + vy ) * 1200 - rotate * 800 
        vd = ( vx + vy ) * 1200 + rotate * 800 
        vb = (-vx + vy ) * 1200 + rotate * 800 

        if va > 1400:
            va = 1400
        elif va < -1400:
            va = -1400

        if vb > 1400:
            vb = 1400
        elif vb < -1400:
            vb = -1400

        if vc > 1400:
            vc = 1400
        elif vc < -1400:
            vc = -1400

        if vd > 1400:
            vd = 1400
        elif vd < -1400:
            vd = -1400

        va = int(va * 127 / 1400)
        vb = int(vb * 127 / 1400)
        vc = int(vc * 127 / 1400)
        vd = int(vd * 127 / 1400)

        print(va, vb, vc, vd)

        sz_sent = bytearray(4)

        sz_sent[0] = va  if va >= 0 else 256 + va 
        sz_sent[1] = vb  if vb >= 0 else 256 + vb 
        sz_sent[2] = vc  if vc >= 0 else 256 + vc 
        sz_sent[3] = vd  if vd >= 0 else 256 + vd 

        self.ser.write(b'S')
        self.ser.write(sz_sent)
              

    def left(self):
        self.ser.write(b'd')

    def right(self):
        self.ser.write(b'b')

    def up(self):
        self.ser.write(b'A') 

    def down(self):
        self.ser.write(b'E') 

    def left_up(self):
        self.ser.write(b'H')  

    def right_up(self):
        self.ser.write(b'B')  

    def left_down(self):
        self.ser.write(b'F') 

    def right_down(self):
        self.ser.write(b'D')  

    def stop(self):
        self.ser.write(b'Z') 

    def rotate(self):
        self.ser.write(b'C') 
    
    def rotate_r(self):
        self.ser.write(b'G') 



