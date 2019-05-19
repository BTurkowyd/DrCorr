# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:06:40 2018

@author: turkowyd
"""
from numpy import array, sort

class ROIs:
    def __init__(self, refPt, ix, iy):
        self.refPt = refPt
        self.fids = []
        self.rois = []
        self.region = []
        
        for ref in self.refPt:
                self.fids.append(list(ref))
                
        for i in range(len(self.fids)):
            for j in range(2):
                self.fids[i][j] = 10 * self.fids[i][j]
        
        for i in range(len(self.fids)):
            self.fids[i][0] = self.fids[i][0] * float(ix/1260)
            self.fids[i][1] = self.fids[i][1] * float(iy/1080)
                    
                
        for i in range(0, len(self.fids), 2):
            self.rois.append(array([[self.fids[i][0], self.fids[i][1]],
                                 [self.fids[i+1][0], self.fids[i+1][1]]]))
    
        for r in self.rois:
            for i in range(2):
                r[:,i] = sort(r[:,i])