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
from numpy import loadtxt, shape, sqrt, zeros
from scipy import spatial
from scipy.optimize import curve_fit

from drift import Drift
from particle import Particle


refPt = list()
resize = None
image = None
particles = []


def number_gen():
    i = 1
    while True:
        yield i
        i += 1

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
    name = 'NeNA_loc_{0}.pdf'.format(k + 1)
    output_folder = os.path.dirname(os.path.realpath(localization))
    f, axarr = plt.subplots(1, sharex=False)
    axarr.bar(x, y, color='gray', edgecolor='black', width=Int)
    axarr.plot(x, NeNA_func, 'b')
    axarr.set_xlim([Min, Max])
    axarr.set_xlabel('loc_acc [nm]')
    axarr.set_ylabel('Intensity [a.u.]')
    # plt.savefig(str(output_folder) + "\\" + name, format='pdf')
    plt.savefig(os.path.join(output_folder, name), format='pdf')
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

def calc_NeNA(selections, localization, k, counting=0, nenaList=[]):
    selections = np.asarray(selections.fiducial)
    print(selections)
    max_frame = np.max(selections[:,2]) # this is only for rapidstorm format, not thunderstorm! You have to fix it!!!
    print(max_frame)
    length = shape(selections)[0]
    frames = zeros([length, 2])
    frames[:, 1] = selections[:, 2]
    tree = spatial.KDTree(frames[:, 0:2])
    d = zeros([length, 1])
    p = -1
    for i in range(length - 1):
        o = selections[i, 2]
        # j muss angeben,ob nächster Frame existent ist
        j = selections[i + 1, 2] - selections[i, 2]
        if selections[i, 2] < max_frame and o == p:
            d[i] = min_dist(selections[i, 0:3], temp_locs)
            p = o
        elif selections[i, 2] < max_frame and o > p:
            temp_locs = selections[tree.query_ball_point([0, o + 1], 0.1), 0:2]
            if np.shape(temp_locs)[0] > 0:
                d[i] = min_dist(selections[i, 0:3], temp_locs)
                p = o
        elif selections[i, 2] == max_frame:
            break
    print('\n')
    idx = d > 0
    NeNA_dist = d[idx]
    NeNA_acc, NeNA_err = plot_NeNA(NeNA_dist, localization, k)
    output_folder = os.path.dirname(os.path.realpath(localization))
    hd = "the average localization accuracy by NeNA is at %.1f [nm]" % (float(NeNA_acc[0]))
    outname = 'NeNA_loc_{0}_{1}.txt'.format(k + 1, counting)
    np.savetxt(os.path.join(output_folder, outname), NeNA_dist, fmt='%.5e', delimiter='   ', header=hd, comments='# ')
    nenaList.append(float(NeNA_acc[0]))
    return float(NeNA_acc[0])


def neNa(app, image_recon, localization, firstFrame=0, lastFrame=0, windowJump=0, windowSize=0):
    # try:
        # global image, resize, refPt

        # iy, ix, iz = shape(image)

        # if app.inputFormat.currentText() == "RapidSTORM":
        #     loc = loadtxt(image_recon)
        # else:
        #     loc = pd.read_csv(app.locfileName)

        # output_folder = os.path.dirname(os.path.realpath(localization))
        output_folder = os.path.dirname(os.path.realpath(app.locfileName))

        # regions = ROIs(refPt, ix, iy)
        # nena_regions = [NeNA(r, firstFrame, lastFrame, windowJump, windowSize, app.inputFormat.currentText()) for r in regions.rois]

        # app.statusBar.setText("Calculating NeNA values")

        # for n in nena_regions:
        #     n.nena_roi(loc, firstFrame, lastFrame, windowJump, windowSize)

        k = 0
        app.progressBar.setMaximum(len(image_recon.selections))
        app.progressBar.setValue(k)

        nena_values = []
        for i in range(len(image_recon.selections)):
            if (windowJump or windowSize) == 0:
                nena_values.append(calc_NeNA(image_recon.selections[i], localization, i))

            else:
                counting = 0
                nenaList = []
                nenaSeries = []
                for j in range(len(image_recon.selections)):
                    calc_NeNA(image_recon.selections, image_recon, i, counting, nenaList)
                    counting += 1
                np.savetxt(os.path.join(output_folder, 'NeNA_summary_', str(i), '.txt'), nenaList, fmt='%.5e')
                # np.savetxt(str(output_folder) + "\\NeNA_summary_" + str(i) + ".txt", nenaList, fmt='%.5e')
                nenaSeries.append(nenaList)
            

            k += 1
            app.progressBar.setValue(k)
        np.savetxt(os.path.join(output_folder, 'NeNA_summary_table.txt'), nena_values, fmt='%.2f')
        # np.savetxt(str(output_folder) + "\\NeNA_summary_table.txt", nena_values, fmt='%.2f')

        app.statusBar.setText("NeNA calculated!")
    # except:
    #     print("No ROIs selected")



def dr_corr_2(app, fiducials, fiducial_ids):
        output_folder = os.path.dirname(os.path.realpath(app.locfileName))

        plt.savefig(os.path.join(output_folder, 'selected_rois.png'))
        # plt.savefig(output_folder + '\\' + 'selected_rois.png')

        plt.style.use('classic')

        if app.inputFormat.currentText() == "RapidSTORM":
            loc = loadtxt(app.locfileName)
        else:
            loc = pd.read_csv(app.locfileName)

        k = 0
        app.progressBar.setMaximum(len(fiducials))
        app.progressBar.setValue(k)
        app.statusBar.setText("Extracting fiducial markers")

        for f in fiducials:
            f.rel_drift()
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
            with open(os.path.join(output_folder, 'corrected_localizations.txt'), 'w') as final_file:
            # with open(app.locfileName.split('.')[0] + "_corrected.txt", "w") as final_file:
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
            with open(os.path.join(output_folder, app.locfileName.split('.')[0] + '_corrected.csv'), 'w') as final_file:
                final_file.write('"id","frame","x [nm]","y [nm]","sigma [nm]","intensity [photon]","offset [photon]","bkgstd [photon]","chi2","uncertainty_xy [nm]"\n')
                k = 0
                app.progressBar.setValue(k)
                app.progressBar.setMaximum(len(loc))
                app.statusBar.setText("Saving a new localization file")
                for p in particles:
                    final_file.write("%1.0f,%1.0f,%1.5f,%1.5f,%1.5f,%1.5f,%1.5f,%1.5f,%1.5f,%1.5f\n" % (p.id, p.t, p.new_x, p.new_y, p.sigma, p.I, p.offset, p.bkgstd, p.chi2, p.uncertainty))
                    k += 1
                    if k % 1000 == 0:
                        app.progressBar.setValue(k)
                app.progressBar.setValue(k)

        with open(os.path.join(output_folder, 'beads_st_devs.txt'), 'w') as beads_stdevs:
            for i, f in enumerate(fiducials):
                beads_stdevs.write('Fiducial %s\t%1.3f\t%1.3f\n' % (fiducial_ids[i], np.std(f.stretch[:,0]-drift.smooth_x), np.std(f.stretch[:,1]-drift.smooth_y)))
        
        
        # Drift trace figure
        drift_trace_figure = plt.figure()
        drift_trace_x = drift_trace_figure.add_subplot(211)
        drift_trace_y = drift_trace_figure.add_subplot(212)
        
        for i, f in enumerate(fiducials):
            drift_trace_x.plot(f.stretch[:,2], f.stretch[:,0], '-', linewidth=1, label="Fiducial " + str(fiducial_ids[i]), alpha=0.5)
            drift_trace_y.plot(f.stretch[:,2], f.stretch[:,1], '-', linewidth=1, label="Fiducial " + str(fiducial_ids[i]), alpha=0.5)
            
            with open(os.path.join(output_folder, 'Fiducial_' + str(fiducial_ids[i]) + '.txt'), 'w') as fiducial_wobbling:
                for dx, dy in zip(f.stretch[:,0]-drift.smooth_x, f.stretch[:,1]-drift.smooth_y):
                    fiducial_wobbling.write('%1.3f\t%1.3f\n' % (dx, dy))

        drift_trace_x.plot(drift.t, drift.smooth_x, 'k-', label='X-drift', linewidth=2)
        drift_trace_y.plot(drift.t, drift.smooth_y, 'k-', label='Y-drift', linewidth=2)

        drift_trace_x.plot(drift.t, drift.smooth_x - drift.smooth_std_x, 'k-', linewidth=1)
        drift_trace_x.plot(drift.t, drift.smooth_x + drift.smooth_std_x, 'k-', linewidth=1)
        drift_trace_x.grid(True)

        drift_trace_x.set_xlabel('Frame')
        drift_trace_x.set_ylabel('X-Drift (nm)')
        drift_trace_x.legend()

        drift_trace_y.plot(drift.t, drift.smooth_y + drift.smooth_std_y, 'k-', linewidth=1)
        drift_trace_y.plot(drift.t, drift.smooth_y - drift.smooth_std_y, 'k-', linewidth=1)
        drift_trace_y.grid(True)

        drift_trace_y.set_xlabel('Frame')
        drift_trace_y.set_ylabel('Y-Drift (nm)')
        drift_trace_y.legend()
        drift_trace_figure.savefig(os.path.join(output_folder, 'drift_trace.png'))

        # Fiducial standard error plot
        fid_std_err_figure = plt.figure()
        fid_std_err_x = fid_std_err_figure.add_subplot(211)
        fid_std_err_y = fid_std_err_figure.add_subplot(212)

        fid_std_err_x.plot(drift.t, drift.smooth_std_x/np.sqrt(len(fiducials)), 'k-', linewidth=1)
        fid_std_err_x.set_xlabel('Frame')
        fid_std_err_x.set_ylabel('X-SE (nm)')
        fid_std_err_x.grid(True)

        fid_std_err_y.plot(drift.t, drift.smooth_std_y/np.sqrt(len(fiducials)), 'k-', linewidth=1)
        fid_std_err_y.set_xlabel('Frame')
        fid_std_err_y.set_ylabel('Y-SE (nm)')
        fid_std_err_y.grid(True)
        fid_std_err_figure.savefig(os.path.join(output_folder,'fiducial_st_err.png'))
        

        with open(os.path.join(output_folder, 'drift_trace.txt'), "w") as drift_file:
            for dx, dy in zip(drift.smooth_x, drift.smooth_y):
                drift_file.write('%1.3f\t%1.3f\n' % (dx, dy))
        
        app.statusBar.setText("Done!")
        print('DONE!!!')

        plt.close("all")    

def analyze_fiducials_2(app, fiducials, fiducial_ids):
        plt.style.use('classic')

    # try:
        # global image, resize, refPt

        # imwrite(app.locfileName.split('.')[0] + "selected_ROIs.png", resize)

        if app.inputFormat.currentText() == "RapidSTORM":
            loc = loadtxt(app.locfileName)
        else:
            loc = pd.read_csv(app.locfileName)

        # with open(app.locfileName.split('.')[0] + '\\rois.roi', 'wb') as file:
        #     pickle.dump(regions, file)

        k = 0
        app.progressBar.setMaximum(len(fiducials))
        app.progressBar.setValue(k)
        app.statusBar.setText("Extracting fiducial markers")

        for f in fiducials:
            f.rel_drift()
            f.stretch_fiducials(loc, app.inputFormat.currentText())
            k += 1
            app.progressBar.setValue(k)

        drift = Drift(fiducials)

        drift_traces_plot = plt.figure()
        lines_x = []
        lines_y = []
        for i, f in enumerate(fiducials):
            plt.subplot(211)
            line_x = plt.plot(f.stretch[:,2], f.stretch[:,0], '-', linewidth=1, label="Fiducial " + str(fiducial_ids[i]), alpha=0.5)
            lines_x.append(line_x)
            plt.subplot(212)
            line_y = plt.plot(f.stretch[:,2], f.stretch[:,1], '-', linewidth=1, label="Fiducial " + str(fiducial_ids[i]), alpha=0.5)
            lines_y.append(line_y)
        
        plt.subplot(211)
        plt.plot(drift.t, drift.smooth_x, 'k-', label='X-drift', linewidth=2)
        plt.subplot(212)
        plt.plot(drift.t, drift.smooth_y, 'k-', label='Y-drift', linewidth=2)

        plt.subplot(211)
        plt.plot(drift.t, drift.smooth_x + drift.smooth_std_x, 'k-', linewidth=1)
        plt.plot(drift.t, drift.smooth_x - drift.smooth_std_x, 'k-', linewidth=1)
        plt.grid(True)

        plt.xlabel('Frame')
        plt.ylabel('X-Drift (nm)')
        legend_x = plt.legend(fancybox=True, shadow=True)

        plt.subplot(212)
        plt.plot(drift.t, drift.smooth_y + drift.smooth_std_y, 'k-', linewidth=1)
        plt.plot(drift.t, drift.smooth_y - drift.smooth_std_y, 'k-', linewidth=1)
        plt.grid(True)

        plt.xlabel('Frame')
        plt.ylabel('Y-Drift (nm)')
        legend_y = plt.legend(fancybox=True, shadow=True)

        lined_y = {}
        lined_x = {}

        for legline_x, origline_x, legline_y, origline_y in zip(legend_x.get_lines(), lines_x, legend_y.get_lines(), lines_y):
            legline_x.set_picker(True)
            lined_x[legline_x] = origline_x

            legline_y.set_picker(True)
            lined_y[legline_y] = origline_y

        def on_pick_x(event):
            try:
                legline = event.artist
                origline_x = lined_x[legline]
                for o in origline_x:
                    visible = not o.get_visible()
                    o.set_visible(visible)
                    legline.set_alpha(1.0 if visible else 0.2)
                    drift_traces_plot.canvas.draw()
            except KeyError:
                pass
        
        def on_pick_y(event):
            try:
                legline = event.artist
                origline_y = lined_y[legline]
                for o in origline_y:        
                    visible = not o.get_visible()
                    o.set_visible(visible)
                    legline.set_alpha(1.0 if visible else 0.2)
                    drift_traces_plot.canvas.draw()
            except KeyError:
                pass

        drift_traces_plot.canvas.mpl_connect('pick_event', on_pick_x)
        drift_traces_plot.canvas.mpl_connect('pick_event', on_pick_y)

        plt.figure()
        plt.subplot(211)
        plt.plot(drift.t, drift.smooth_std_x/np.sqrt(len(fiducials)), 'k-', linewidth=1)
        plt.xlabel('Frame')
        plt.ylabel('X-SE (nm)')
        plt.grid(True)

        plt.subplot(212)
        plt.plot(drift.t, drift.smooth_std_y/np.sqrt(len(fiducials)), 'k-', linewidth=1)
        plt.xlabel('Frame')
        plt.ylabel('Y-SE (nm)')
        plt.grid(True)

        corrected_drifts_plot = plt.figure()

        corr_lines_x = []
        corr_lines_y = []
        for i, f in enumerate(fiducials):
            plt.subplot(211)
            corr_line_x = plt.plot(f.stretch[:,2], f.stretch[:,0]-drift.smooth_x, '-', linewidth=1, label="Fiducial " + str(fiducial_ids[i]), alpha=0.5)
            corr_lines_x.append(corr_line_x)
            plt.subplot(212)
            corr_line_y = plt.plot(f.stretch[:,2], f.stretch[:,1]-drift.smooth_y, '-', linewidth=1, label="Fiducial " + str(fiducial_ids[i]), alpha=0.5)
            corr_lines_y.append(corr_line_y)

        plt.subplot(211)
        plt.xlabel("Frame")
        plt.ylabel("dX (nm)")
        plt.grid(True)
        corr_legend_x = plt.legend(fancybox=True, shadow=True)

        plt.subplot(212)
        plt.xlabel("Frame")
        plt.ylabel("dY (nm)")
        plt.grid(True)
        corr_legend_y = plt.legend(fancybox=True, shadow=True)

        corr_lined_y = {}
        corr_lined_x = {}

        for corr_legline_x, corr_origline_x, corr_legline_y, corr_origline_y in zip(corr_legend_x.get_lines(), corr_lines_x, corr_legend_y.get_lines(), corr_lines_y):
            corr_legline_x.set_picker(True)
            corr_lined_x[corr_legline_x] = corr_origline_x

            corr_legline_y.set_picker(True)
            corr_lined_y[corr_legline_y] = corr_origline_y

        def corr_on_pick_x(event):
            try:
                legline = event.artist
                corr_origline_x = corr_lined_x[legline]
                for o in corr_origline_x:
                    visible = not o.get_visible()
                    o.set_visible(visible)
                    legline.set_alpha(1.0 if visible else 0.2)
                    corrected_drifts_plot.canvas.draw()
            except KeyError:
                pass
        
        def corr_on_pick_y(event):
            try:
                legline = event.artist
                corr_origline_y = corr_lined_y[legline]
                for o in corr_origline_y:        
                    visible = not o.get_visible()
                    o.set_visible(visible)
                    legline.set_alpha(1.0 if visible else 0.2)
                    corrected_drifts_plot.canvas.draw()
            except KeyError:
                pass

        corrected_drifts_plot.canvas.mpl_connect('pick_event', corr_on_pick_x)
        corrected_drifts_plot.canvas.mpl_connect('pick_event', corr_on_pick_y)

        plt.show()

    # except:
    #     pass

def load_particles(app):
    try:
        global image, resize, refPt, particles

        if app.inputFormat.currentText() == "RapidSTORM":
            loc = loadtxt(app.locfileName)
            particles = [Particle(p[0], p[1], p[2], p[3]) for p in loc]
        else:
            loc = pd.read_csv(app.locfileName)
            particles = [Particle(p[2], p[3], p[1], p[5], p[0], p[4], p[6], p[7], p[8], p[9]) for p in loc.values]
    except:
        print("Localization file not loaded")
class NeNACalculation():
    def __init__(self, parent, app, image_recon, localization,  firstFrame=0, lastFrame=0, windowJump=0, windowSize=0):
        self.app = app
        self.image_recon = image_recon
        self.localization = localization
        self.first_frame = firstFrame
        self.last_frame = lastFrame
        self.window_jump = windowJump
        self.window_size = windowSize
        # super().__init__()
    def run(self):
        neNa(self.app, self.image_recon, self.localization, self.first_frame, self.last_frame, self.window_jump, self.window_size)
