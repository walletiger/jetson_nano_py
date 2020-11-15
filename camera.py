import cv2 
import traceback 
import threading 
import queue

class JetCamera():
    def __init__(self, cap_w, cap_h, cap_fps):
        #self.cap_orig_w, self_cap_orig_h = 3264, 2464 # 21 fps 
        #self.cap_orig_w, self_cap_orig_h = 1920, 1080 # 30 fps 
        self.cap_orig_w, self.cap_orig_h = 1280, 720 # 60/120 fps 
        self.cap_orig_fps = 60 
        self.cap_out_w = cap_w
        self.cap_out_h = cap_h 
        self.cap_out_fps = cap_fps 
        
        self.cap_str = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=%d, height=%d, format=(string)NV12, framerate=(fraction)%d/1 '\
                '! nvvidconv ! video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx '\
                '! videorate ! video/x-raw, framerate=(fraction)%d/1 '\
                '! videoconvert !  video/x-raw, format=BGR !  appsink sync=false ' \
                % (self.cap_orig_w, self.cap_orig_h, self.cap_orig_fps, self.cap_out_w, self.cap_out_h, self.cap_out_fps)

        self.cap = None 

    def open(self):
        if self.cap:
            return True 
        try:
            #print(self.cap_str)
            self.cap = cv2.VideoCapture(self.cap_str, cv2.CAP_GSTREAMER)
        except:
            traceback.print_exc()

        return self.cap is not None 


    def read(self):
        if not self.cap:
            return None, None 
        
        try:
            ret, img = self.cap.read()
        except:
            traceback.print_exc()

        return ret, img 

    def close(self):

        try:
            if self.cap:
                self.cap.release()
            self.cap = None 
        except:
            pass 
