
from Adafruit_MotorHAT.Adafruit_PWM_Servo_Driver import PWM 
import os  

# 设置最大最小脉冲长度
servo_min = 90  # 4096的最小脉冲长度
servo_max = 2000   # 4096的最大脉冲长度
servo_mid = 365  # 4096的中间脉冲长度


class Arm():
    def __init__(self):
        self.x = 1000
        self.y = 1000 
        self.pwm = PWM(address=0x40, debug=False, i2c=None, i2c_bus=1)
        self.pwm.setPWMFreq(50)

    def down(self):
        if self.y >= 300:
            self.y -= 50
            self.pwm.setServoPulse(0,self.y)
   
    def up(self):
        if self.y <= 1500:
            self.y += 50
            self.pwm.setServoPulse(0,self.y)

    def close(self):
        if self.x <= 1500:
            self.x += 50
            self.pwm.setServoPulse(1,self.x)


    def open(self):
        if self.x >= 300:
             self.x -= 50
        self.pwm.setServoPulse(1,self.x)

