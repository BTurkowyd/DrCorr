# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 23:08:50 2018

@author: VerTislav
"""

import numpy as np


class NeNA:
    def __init__(self, rois, startFrame, endFrame, windowJump, windowSize):
        self.x_min = rois[0, 0]
        self.y_min = rois[0, 1]
        self.x_max = rois[1, 0]
        self.y_max = rois[1, 1]
        self.nena = list()
        self.startFrame = startFrame
        self.endFrame = endFrame
        self.windowJump = windowJump
        self.windowSize = windowSize

    def nena_roi(self, loc, firstFrame, lastFrame, windJump, windSize):
        if (windJump or windSize) == 0:
            for l in loc:
                if self.x_min < l[0] < self.x_max and self.y_min < l[1] < self.y_max:
                    self.nena.append(l)

            self.nena = np.asarray(self.nena)

        else:
            for i in range(firstFrame, lastFrame, windJump):
                self.nenaRAM = []
                for l in loc:
                    if self.x_min < l[0] < self.x_max and self.y_min < l[1] < self.y_max and i <= l[
                        2] < i + self.windowSize:
                        self.nenaRAM.append(l)
                self.nenaRAM = np.asarray(self.nenaRAM)
                self.nena.append(self.nenaRAM)
                print(len(self.nena))
