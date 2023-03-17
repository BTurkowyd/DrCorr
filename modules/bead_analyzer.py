from itertools import islice
import os
from PyQt5 import QtCore, QtWidgets
import numpy as np
from modules.drift import Drift
from matplotlib import pyplot as plt
import pandas as pd


class Ui_BeadAnalyzer(QtWidgets.QMainWindow):
    def setupUi(self, BeadAnalyzer, app, fiducials, particles):
        try:
            self.fiducials = fiducials
            self.particles = particles
            
        except AttributeError:
            print('No ROIs selected')

        self.mother_app = app

        BeadAnalyzer.setObjectName("Bead Analyzer")
        BeadAnalyzer.resize(400, 600)
        self.centralwidget = QtWidgets.QWidget(BeadAnalyzer)
        self.centralwidget.setObjectName("beadAnalyzerWidget")

        self.analayzeBeads = QtWidgets.QPushButton(self.centralwidget)
        self.analayzeBeads.setGeometry(QtCore.QRect(10, 520, 96, 32))
        self.analayzeBeads.setObjectName("analayzeBeads")
        self.analayzeBeads.clicked.connect(self.analyze_fiducials)

        self.applyDriftCorr = QtWidgets.QPushButton(self.centralwidget)
        self.applyDriftCorr.setGeometry(QtCore.QRect(120, 520, 96, 32))
        self.applyDriftCorr.setObjectName("applyDriftCorr")
        self.applyDriftCorr.clicked.connect(self.apply_drift_corr)

        self.quiteBeadsAnal = QtWidgets.QPushButton(self.centralwidget)
        self.quiteBeadsAnal.setGeometry(QtCore.QRect(290, 520, 96, 32))
        self.quiteBeadsAnal.setObjectName("quiteBeadsAnal")
        self.quiteBeadsAnal.clicked.connect(self.close)
        
        self.listOfFiducials = QtWidgets.QFrame(self.centralwidget)
        self.listOfFiducials.setGeometry(QtCore.QRect(10, 10, 381, 441))
        self.listOfFiducials.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listOfFiducials.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listOfFiducials.setObjectName("listOfFiducials")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.listOfFiducials)
        self.verticalScrollBar.setGeometry(QtCore.QRect(360, 0, 16, 441))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")

        self.fiducialCheckBoxes = []

        try:
            for i, _ in enumerate(self.fiducials):
                self.fiducialCheckBoxes.append(QtWidgets.QCheckBox(self.listOfFiducials))
                if i < 14:
                    self.fiducialCheckBoxes[-1].setGeometry(QtCore.QRect(10, 10 + i*30, 90, 20))
                elif i >= 14 and i < 28:
                    self.fiducialCheckBoxes[-1].setGeometry(QtCore.QRect(110, 10 + (i-14)*30, 90, 20))
                else:
                    self.fiducialCheckBoxes[-1].setGeometry(QtCore.QRect(210, 10 + (i-28)*30, 90, 20))

                self.fiducialCheckBoxes[-1].setObjectName("Fiducial" + str(i+1))
                self.fiducialCheckBoxes[-1].setChecked(True)
        except AttributeError:
            print('No ROIs selected')

        self.selectAll = QtWidgets.QPushButton(self.centralwidget)
        self.selectAll.setGeometry(QtCore.QRect(10, 460, 96, 32))
        self.selectAll.setObjectName("selectAll")
        self.selectAll.clicked.connect(self.select_all)
        self.on = True

        BeadAnalyzer.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(BeadAnalyzer)
        self.statusbar.setObjectName("statusbar")
        BeadAnalyzer.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(BeadAnalyzer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        BeadAnalyzer.setMenuBar(self.menubar)

        self.retranslateUi(BeadAnalyzer)
        QtCore.QMetaObject.connectSlotsByName(BeadAnalyzer)

    def retranslateUi(self, BeadAnalyzer):
        _translate = QtCore.QCoreApplication.translate
        BeadAnalyzer.setWindowTitle(_translate("BeadAnalyzer", "BeadAnalyzer"))
        self.analayzeBeads.setText(_translate("BeadAnalyzer", "Analyze"))
        self.quiteBeadsAnal.setText(_translate("BeadAnalyzer", "Close"))

        for i, f in enumerate(self.fiducialCheckBoxes):
            f.setText(_translate("BeadAnalyzer", "Fiducial " + str(i+1)))

        self.selectAll.setText(_translate("BeadAnalyzer", "Select All"))
        self.applyDriftCorr.setText(_translate("MainWindow", "Apply dr. corr."))

    
    def select_all(self):
        if self.on:
            for f in self.fiducialCheckBoxes:
                f.setChecked(False)
            self.on = False
        else:
            for f in self.fiducialCheckBoxes:
                f.setChecked(True)
            self.on = True
    
    def apply_drift_corr(self):
        self.selected_fiducials = []
        self.ids = []

        n = 1
        for f,ff in zip(self.fiducials, self.fiducialCheckBoxes):
                if ff.isChecked():
                    self.selected_fiducials.append(f)
                    self.ids.append(n)
                n += 1

        self.dr_corr_2(self.mother_app, self.selected_fiducials, self.particles, self.ids)
    
    def dr_corr_2(self, mother_app, fiducials, particles, fiducial_ids):
            output_folder = os.path.dirname(os.path.realpath(mother_app.locfileName))

            plt.savefig(os.path.join(output_folder, 'selected_rois.png'))
            # plt.savefig(output_folder + '\\' + 'selected_rois.png')

            plt.style.use('classic')

            if mother_app.inputFormat.currentText() == "RapidSTORM":
                loc = np.loadtxt(mother_app.locfileName)
            else:
                loc = pd.read_csv(mother_app.locfileName)

            k = 0
            mother_app.progressBar.setMaximum(len(fiducials))
            mother_app.progressBar.setValue(k)
            mother_app.statusBar.setText("Extracting fiducial markers")

            for f in fiducials:
                f.rel_drift()
                f.stretch_fiducials(loc, mother_app.inputFormat.currentText())
                k += 1
                mother_app.progressBar.setValue(k)

            drift = Drift(fiducials)

            k = 0
            mother_app.progressBar.setMaximum(len(loc))
            mother_app.progressBar.setValue(k)
            mother_app.statusBar.setText("Applying the drift correction")

            print("particles: " + str(len(particles)))
            for p in particles:
                p.load_drift(drift)
                p.apply_drift()
                k += 1
                if k % 1000 == 0:
                    mother_app.progressBar.setValue(k)
            mother_app.progressBar.setValue(k)    

            with open(mother_app.locfileName) as input_file:
                head = list(islice(input_file, 1))

            if mother_app.inputFormat.currentText() == "RapidSTORM":
                with open(os.path.join(output_folder, 'corrected_localizations.txt'), 'w') as final_file:
                # with open(app.locfileName.split('.')[0] + "_corrected.txt", "w") as final_file:
                    final_file.write(str(head[0]))
                    k = 0
                    mother_app.progressBar.setValue(k)
                    mother_app.progressBar.setMaximum(len(loc))
                    mother_app.statusBar.setText("Saving a new localization file")
                    for p in particles:
                        final_file.write('%1.1f %1.1f %1.0f %1.0f\n' % (p.new_x, p.new_y, p.t, p.I))
                        k += 1
                        if k % 1000 == 0:
                            mother_app.progressBar.setValue(k)
                    mother_app.progressBar.setValue(k)
            else:
                with open(os.path.join(output_folder, mother_app.locfileName.split('.')[0] + '_corrected.csv'), 'w') as final_file:
                    final_file.write('"id","frame","x [nm]","y [nm]","sigma [nm]","intensity [photon]","offset [photon]","bkgstd [photon]","chi2","uncertainty_xy [nm]"\n')
                    k = 0
                    mother_app.progressBar.setValue(k)
                    mother_app.progressBar.setMaximum(len(loc))
                    mother_app.statusBar.setText("Saving a new localization file")
                    for p in particles:
                        final_file.write("%1.0f,%1.0f,%1.5f,%1.5f,%1.5f,%1.5f,%1.5f,%1.5f,%1.5f,%1.5f\n" % (p.id, p.t, p.new_x, p.new_y, p.sigma, p.I, p.offset, p.bkgstd, p.chi2, p.uncertainty))
                        k += 1
                        if k % 1000 == 0:
                            mother_app.progressBar.setValue(k)
                    mother_app.progressBar.setValue(k)

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
            
            mother_app.statusBar.setText("Done!")
            print('DONE!!!')

            plt.close("all")    

    def analyze_fiducials(self):
        self.selected_fiducials = []
        self.ids = []

        n = 1
        for f,ff in zip(self.fiducials, self.fiducialCheckBoxes):
                if ff.isChecked():
                    self.selected_fiducials.append(f)
                    self.ids.append(n)
                n += 1

        self.analyze_fiducials_2(self.mother_app, self.selected_fiducials, self.ids)

    def analyze_fiducials_2(self, mother_app, fiducials, fiducial_ids):
            plt.style.use('classic')

            if mother_app.inputFormat.currentText() == "RapidSTORM":
                loc = np.loadtxt(mother_app.locfileName)
            else:
                loc = pd.read_csv(mother_app.locfileName)

            k = 0
            mother_app.progressBar.setMaximum(len(fiducials))
            mother_app.progressBar.setValue(k)
            mother_app.statusBar.setText("Extracting fiducial markers")

            for f in fiducials:
                f.rel_drift()
                f.stretch_fiducials(loc, mother_app.inputFormat.currentText())
                k += 1
                mother_app.progressBar.setValue(k)

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
