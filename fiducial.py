# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:07:23 2018

@author: turkowyd
"""
from numpy import zeros
from kalman_filter import KalmanFilterXY

class Fiducial:
    def __init__(self, rois, int_thres):
        self.x_min = rois[0,0]
        self.y_min = rois[0,1]
        self.x_max = rois[1,0]
        self.y_max = rois[1,1]
        self.int_thres = float(int_thres)
        self.fiducial = []
        
    def extract_fiducial(self, loc, inputFormat):
        if inputFormat == "RapidSTORM":
            for l in loc:
                if l[3] >= self.int_thres and self.x_min < l[0] < self.x_max and self.y_min < l[1] < self.y_max:
                    self.fiducial.append(l)
        else:
            for l in loc.values:
                if l[5] >= self.int_thres and self.x_min < l[2] < self.x_max and self.y_min < l[3] < self.y_max:
                    self.fiducial.append(l)
    
    def rel_drift(self, inputFormat):
        self.rel_x = []
        self.rel_y = []
        self.t = []
        self.intensity = []
        for i in range(len(self.fiducial)):
            if inputFormat == "RapidSTORM":
                self.temp_x = self.fiducial[i][0] - self.fiducial[0][0]
                self.temp_y = self.fiducial[i][1] - self.fiducial[0][1]
                self.temp_t = self.fiducial[i][2]
                self.temp_int = self.fiducial[i][3]
            else:
                self.temp_x = self.fiducial[i][2] - self.fiducial[0][2]
                self.temp_y = self.fiducial[i][3] - self.fiducial[0][3]
                self.temp_t = self.fiducial[i][1]
                self.temp_int = self.fiducial[i][5]
            self.rel_x.append(self.temp_x)
            self.rel_y.append(self.temp_y)
            self.t.append(self.temp_t)
            self.intensity.append(self.temp_int)
                  
    def stretch_fiducials(self, loc, inputFormat):
        if inputFormat == "RapidSTORM":
            self.stretch = zeros((int(loc[-1,2])+1, 4))
        else:
            self.stretch = zeros((int(loc.values[-1,1])+1, 4))
            
        for x, y, t, intensity in zip(self.rel_x, self.rel_y, self.t, self.intensity):
            self.stretch[int(t), 0] = x
            self.stretch[int(t), 1] = y
            self.stretch[int(t), 2] = t
            self.stretch[int(t), 3] = intensity
        # self.kalman_stretch = KalmanFilterXY(self.stretch[:,:2])
        # print("Kalman")
        # self.kalman_stretch.run()
        # self.stretch[:,0] = self.kalman_stretch.corrected_x
        # self.stretch[:,1] = self.kalman_stretch.corrected_y