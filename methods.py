# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 16:31:13 2018

@author: VerTislav
"""

import os
from itertools import islice

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from cv2 import (EVENT_LBUTTONDOWN, EVENT_LBUTTONUP, FONT_HERSHEY_SIMPLEX,
                 LINE_AA, destroyAllWindows, imread, imshow, imwrite,
                 namedWindow, putText)
from cv2 import rectangle as rectangler
from cv2 import resize as resizer
from cv2 import setMouseCallback, waitKey
from numpy import loadtxt, shape, sqrt, zeros
from scipy import spatial
from scipy.optimize import curve_fit

from drift import Drift
from fiducial import Fiducial
from kalman_filter import KalmanFilterXY
from nena import NeNA
from particle import Particle
from rois import ROIs

refPt = list()
resize = None
image = None

def min_dist(point, locs):
    d = sqrt(np.square(locs[:, 0] - point[0]) + np.square(locs[:, 1] - point[1]))
    return np.min(d)


def Area(r, y):
    Areaf = abs(np.trapz(y, r))
    return Areaf

def plot_NeNA(NeNA_dist, localization, k):
    Min = 0
    Max = 150
    Int = 1
    Inc = (Max - Min) / Int
    x = np.arange(Min, Max, Int, dtype='float')
    y = np.histogram(NeNA_dist, bins=int(Inc), range=(Min, Max), density=True)[0]
    acc, acc_err = CFit_resultsCorr(x, y)
    NeNA_func = CFunc2dCorr(x, acc[0], acc[1], acc[2], acc[3], acc[4], acc[5])
    name = 'NeNA_lac_{0}.pdf'.format(k + 1)
    output_folder = os.path.dirname(os.path.realpath(localization))
    f, axarr = plt.subplots(1, sharex=False)
    axarr.bar(x, y, color='gray', edgecolor='black', width=Int)
    axarr.plot(x, NeNA_func, 'b')
    axarr.set_xlim([Min, Max])
    axarr.set_xlabel('loc_acc [nm]')
    axarr.set_ylabel('Intensity [a.u.]')
    plt.savefig(str(output_folder) + "\\" + name, format='pdf')
    plt.close()
    return acc, acc_err

def CFunc2dCorr(r, a, rc, w, F, A, O):
    y = (r / (2 * a * a)) * np.exp((-1) * r * r / (4 * a * a)) * A + (F / (w * np.sqrt(np.pi / 2))) * np.exp(
        -2 * ((r - rc) / w) * ((r - rc) / w)) + O * r
    return y

def CFit_resultsCorr(r, y):
    A = Area(r, y)
    p0 = np.array([10.0, 15, 100, (A / 2), (A / 2), ((y[98] / 200))])
    popt, pcov = curve_fit(CFunc2dCorr, r, y, p0)
    return popt, pcov

def calc_NeNA(locs, localization, k, counting=0, nenaList=[]):
    max_frame = np.max(locs[:, 2])
    length = shape(locs)[0]
    frames = zeros([length, 2])
    frames[:, 1] = locs[:, 2]
    tree = spatial.KDTree(frames[:, 0:2])
    d = zeros([length, 1])
    p = -1
    for i in range(length - 1):
        o = locs[i, 2]
        # j muss angeben,ob nächster Frame existent ist
        j = locs[i + 1, 2] - locs[i, 2]
        if locs[i, 2] < max_frame and o == p:
            d[i] = min_dist(locs[i, 0:3], temp_locs)
            p = o
        elif locs[i, 2] < max_frame and o > p:
            temp_locs = locs[tree.query_ball_point([0, o + 1], 0.1), 0:2]
            if np.shape(temp_locs)[0] > 0:
                d[i] = min_dist(locs[i, 0:3], temp_locs)
                p = o
        elif locs[i, 2] == max_frame:
            break
    print('\n')
    idx = d > 0
    NeNA_dist = d[idx]
    NeNA_acc, NeNA_err = plot_NeNA(NeNA_dist, localization, k)
    output_folder = os.path.dirname(os.path.realpath(localization))
    hd = "the average localization accuracy by NeNA is at %.1f [nm]" % (float(NeNA_acc[0]))
    outname = 'NeNA_lac_{0}_{1}.txt'.format(k + 1, counting)
    np.savetxt(str(output_folder) + "\\" + outname, NeNA_dist, fmt='%.5e', delimiter='   ', header=hd, comments='# ')
    nenaList.append(float(NeNA_acc[0]))
    return nenaList

def neNa(app, localization, image_png, firstFrame=0, lastFrame=0, windowJump=0, windowSize=0):
    global image, resize, refPt

    iy, ix, iz = shape(image)

    if app.inputFormat.currentText() == "RapidSTORM":
        loc = loadtxt(localization)
    else:
        loc = pd.read_csv(app.locfileName)

    output_folder = os.path.dirname(os.path.realpath(localization))

    regions = ROIs(refPt, ix, iy)
    nena_regions = [NeNA(r, firstFrame, lastFrame, windowJump, windowSize, app.inputFormat.currentText()) for r in regions.rois]

    app.statusBar.setText("Calculating NeNA values")

    for n in nena_regions:
        n.nena_roi(loc, firstFrame, lastFrame, windowJump, windowSize)

    k = 0
    app.progressBar.setMaximum(len(nena_regions))
    app.progressBar.setValue(k)

    for i in range(len(nena_regions)):
        if (windowJump or windowSize) == 0:
            calc_NeNA(nena_regions[i].nena, localization, i)

        else:
            counting = 0
            nenaList = []
            nenaSeries = []
            for j in range(len(nena_regions[i].nena)):
                calc_NeNA(nena_regions[i].nena[j], localization, i, counting, nenaList)
                counting += 1
            np.savetxt(str(output_folder) + "\\NeNA_summary_" + str(i) + ".txt", nenaList, fmt='%.5e')
            nenaSeries.append(nenaList)
        
        k += 1
        app.progressBar.setValue(k)
    
    app.statusBar.setText("NeNA calculated!")

def dr_corr(app):
    global image, resize, refPt

    iy, ix, iz = shape(image)

    if app.inputFormat.currentText() == "RapidSTORM":
        loc = loadtxt(app.locfileName)
        particles = [Particle(p[0], p[1], p[2], p[3]) for p in loc]
    else:
        loc = pd.read_csv(app.locfileName)
        particles = [Particle(p[2], p[3], p[1], p[5], p[0], p[4], p[6], p[7], p[8], p[9]) for p in loc.values]

    regions = ROIs(refPt, ix, iy)

    fiducials = [Fiducial(r, app.fidu_intensity) for r in regions.rois]

    k = 0
    app.progressBar.setMaximum(len(fiducials))
    app.progressBar.setValue(k)
    app.statusBar.setText("Extracting fiducial markers")

    for f in fiducials:
        f.extract_fiducial(loc, app.inputFormat.currentText())
        f.rel_drift(app.inputFormat.currentText())
        f.stretch_fiducials(loc, app.inputFormat.currentText())
        k += 1
        app.progressBar.setValue(k)

    drift = Drift(fiducials)

    k = 0
    app.progressBar.setMaximum(len(loc))
    app.progressBar.setValue(k)
    app.statusBar.setText("Applying the drift correction")

    for p in particles:
        p.load_drift(drift)
        p.apply_drift()
        k += 1
        if k % 1000 == 0:
            app.progressBar.setValue(k)
    app.progressBar.setValue(k)    

    with open(app.locfileName) as input_file:
        head = list(islice(input_file, 1))

    if app.inputFormat.currentText() == "RapidSTORM":
        with open(app.locfileName.split('.')[0] + "_corrected.txt", "w") as final_file:
            final_file.write(str(head[0]))
            k = 0
            app.progressBar.setValue(k)
            app.progressBar.setMaximum(len(loc))
            app.statusBar.setText("Saving a new localization file")
            for p in particles:
                final_file.write('%1.1f %1.1f %1.0f %1.0f\n' % (p.new_x, p.new_y, p.t, p.I))
                k += 1
                if k % 1000 == 0:
                    app.progressBar.setValue(k)
            app.progressBar.setValue(k)
    else:
        with open(app.locfileName.split('.')[0] + "_corrected.csv", "w") as final_file:
            final_file.write('"id","frame","x [nm]","y [nm]","sigma [nm]","intensity [photon]","offset [photon]","bkgstd [photon]","chi2","uncertainty_xy [nm]"\n')
            k = 0
            app.progressBar.setValue(k)
            app.progressBar.setMaximum(len(loc))
            app.statusBar.setText("Saving a new localization file")
            for p in particles:
                final_file.write("%1.0f,%1.0f,%1.1f,%1.1f,%1.1f,%1.1f,%1.1f,%1.1f,%1.1f,%1.1f\n" % (p.id, p.t, p.new_x, p.new_y, p.sigma, p.I, p.offset, p.bkgstd, p.chi2, p.uncertainty))
                k += 1
                if k % 1000 == 0:
                    app.progressBar.setValue(k)
            app.progressBar.setValue(k)

    output_folder = os.path.dirname(os.path.realpath(app.locfileName))
    with open(output_folder + "\\" + "drift_trace.txt", "w") as drift_file:
        for dx, dy in zip(drift.smooth_x, drift.smooth_y):
            drift_file.write('%1.3f\t%1.3f\n' % (dx, dy))
    
    app.statusBar.setText("Done!")
    print('DONE!!!')

def display_image(app):
    global image, resize, refPt

    def click_and_crop(event, x, y, flags, param):
        global refPt
        if event == EVENT_LBUTTONDOWN:
            refPt.append((x, y))

        elif event == EVENT_LBUTTONUP:
            refPt.append((x, y))
            rectangler(resize, refPt[-2], refPt[-1], (0, 255, 0), 2)
            imshow("image", resize)

    # load the image, clone it, and setup the mouse callback function
    image = imread(app.imgFileName)
    clone = image.copy()
    namedWindow("image")
    iy, ix, iz = shape(image)
    resize = resizer(image, (1260, 1080))
    setMouseCallback("image", click_and_crop)
    if len(refPt) > 0:
        for i in range(0,len(refPt), 2):
            rectangler(resize, refPt[i], refPt[i+1], (0, 255, 0), 2)

    # keep looping until the 'q' key is pressed
    while True:
        # display the image and wait for a keypress
        imshow("image", resize)
        key = waitKey(1) & 0xFF

        # if the 'r' key is pressed, reset the cropping region
        if key == ord("r"):
            remove_single_roi()

        # if the 'x' key is pressed, reset all ROIs
        if key == ord("x"):
            remove_all_rois()

        # if the 'c' key is pressed, break from the loop
        elif key == ord("c"):
            destroyAllWindows()
            app.statusBar.setText("ROI ({}) saved".format(int(len(refPt)/2)))
            break

def remove_single_roi():
    global refPt, resize
    del refPt[-2:]
    resize = resizer(image, (1260, 1080))

    for i in range(0,len(refPt), 2):
        rectangler(resize, refPt[i], refPt[i+1], (0, 255, 0), 2)

def remove_all_rois():
    global refPt, resize
    refPt = list()
    resize = resizer(image, (1260, 1080))
