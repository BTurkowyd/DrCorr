# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:06:06 2018

@author: turkowyd
"""

class Particle:
    def __init__(self, x, y, t, I):
        self.x = x
        self.y = y
        self.t = t
        self.I = I
        
    def load_drift(self, drift):
        self.drift = drift.drift[int(self.t)]
        
    def apply_drift(self):
        self.new_x = self.x - self.drift[0]
        self.new_y = self.y - self.drift[1]