# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:08:03 2018

@author: turkowyd
"""
from numpy import empty, concatenate, nan, nanmean, shape, isnan, array, savetxt, linspace, nanstd
from kalman_filter import KalmanFilterXY
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt

class Drift:
    def __init__(self, fiducials):
        self.fiducials = fiducials
        self.longest = 0
        self.window = 101
        
        for f in self.fiducials:
            if len(f.stretch) > self.longest:
                self.longest = int(len(f.stretch))
                
        self.rel_x = empty((self.longest, 1))
        self.rel_y = empty((self.longest, 1))
        
        for f in self.fiducials:
                self.rel_x = concatenate((self.rel_x, f.stretch[:,:1]), axis = 1)
                self.rel_y = concatenate((self.rel_y, f.stretch[:,1:2]), axis = 1)
        
        self.rel_x = self.rel_x[:,1:]
        self.rel_y = self.rel_y[:,1:]
        
        rows, columns =  shape(self.rel_x)
        
        for i in range(rows):
            for j in range(columns):
                if self.rel_x[i,j] == 0:
                    self.rel_x[i,j] = nan
                if self.rel_y[i,j] == 0:
                    self.rel_y[i,j] = nan
                
        self.av_rel_x = nanmean(self.rel_x, axis = 1)  
        self.av_rel_y = nanmean(self.rel_y, axis = 1)

        self.std_rel_x = nanstd(self.rel_x, axis = 1)  
        self.std_rel_y = nanstd(self.rel_y, axis = 1)
        
        self.smooth_x = self.av_rel_x
        self.smooth_y = self.av_rel_y

        self.smooth_std_x = self.std_rel_x
        self.smooth_std_y = self.std_rel_y
        
        for i in range(len(self.smooth_x)):
            if isnan(self.smooth_x[i]) == True:
                self.smooth_x[i] = 0
            if isnan(self.smooth_std_x[i]) == True:
                self.smooth_std_x[i] = 0

        for i in range(len(self.smooth_y)):
            if isnan(self.smooth_y[i]) == True:
                self.smooth_y[i] = 0
            if isnan(self.smooth_std_y[i]) == True:
                self.smooth_std_y[i] = 0

        self.smooth_x = savgol_filter(self.smooth_x, self.window, 2, mode= 'mirror')
        self.smooth_y = savgol_filter(self.smooth_y, self.window, 2, mode= 'mirror')
    
        self.smooth_std_x = savgol_filter(self.smooth_std_x, self.window, 2, mode= 'mirror')
        self.smooth_std_y = savgol_filter(self.smooth_std_y, self.window, 2, mode= 'mirror')
                
        self.t = array(range(len(self.smooth_x)))
        
        self.drift = array(list(zip(self.smooth_x, self.smooth_y, self.t)))