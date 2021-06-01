import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import LassoSelector
from matplotlib.path import Path
from fiducial2 import Fiducial2
import pandas as pd

class ImageReconstruction:

    def __init__(self, data, intensity_threshold, file_format):
        if file_format == "RapidSTORM":
            self.data = np.loadtxt(data)
        else:
            self.data = pd.read_csv(data)

        self.intensity_threshold = intensity_threshold
        self.selected_regions = []
        self.selections = []
        self.old_face_colors = []
        self.ind_list = []
        self.file_format = file_format
        self.fiducial_order = 1
        self.fiducial_texts = []

        plt.style.use('dark_background')

        if self.file_format == "RapidSTORM":
            self.subplot_kw = dict(xlim=(0, np.max(self.data[:,0])), ylim=(0, np.max(self.data[:,1])), autoscale_on=False)
            _, self.ax = plt.subplots(subplot_kw=self.subplot_kw)
            self.pts = self.ax.scatter(self.data[:, 0], self.data[:, 1], s=1, c=np.log(self.data[:, 3]), cmap='hot', linewidths=0)
        else:
            self.subplot_kw = dict(xlim=(0, np.max(self.data["x [nm]"])), ylim=(0, np.max(self.data["y [nm]"])), autoscale_on=False)
            _, self.ax = plt.subplots(subplot_kw=self.subplot_kw)
            self.pts = self.ax.scatter(self.data["x [nm]"], self.data["y [nm]"], s=1, c=np.log(self.data["intensity [photon]"]), cmap='hot', linewidths=0)            

        self.lasso = LassoSelector(self.ax, self.onselect, button=3)

        # plt.axis('off')
        plt.tight_layout()
        plt.gca().invert_yaxis()
        plt.show(block=False)

        
    def onselect(self, verts):
        self.face_colors = self.pts.get_facecolors()
        self.path = Path(verts)
        print(np.mean(self.path.vertices[:,0]), np.mean(self.path.vertices[:,1]))

        ind = np.nonzero(self.path.contains_points(self.pts.get_offsets()))[0]

        self.ind_list.append(ind)
        self.old_face_colors.append(self.face_colors[ind, :3])
        self.face_colors[ind, :3] = [0, 1, 0]
        self.fiducial_texts.append(plt.text(np.mean(self.path.vertices[:,0])-500, np.mean(self.path.vertices[:,1])-500, str(self.fiducial_order), c='g'))
        self.ax.figure.canvas.draw_idle()

        if self.file_format == "RapidSTORM":
            selected_data = self.data[ind]
        else:
            selected_data = self.data.loc[ind]

        print(len(selected_data))
        self.fiducial_order += 1

        self.selected_regions.append(selected_data)
        # self.selections.append(Fiducial2(selected_data, self.intensity_threshold, self.file_format))
        print("# fiducials: " + str(len(self.selected_regions)))

    def create_fiducials(self, intensity_threshold):
        self.selections = []
        for sr in self.selected_regions:
            self.selections.append(Fiducial2(sr, intensity_threshold, self.file_format))



    def del_last_selection(self):
        self.selections = self.selections[:-1]
        self.selected_regions = self.selected_regions[:-1]

        ind = self.ind_list[-1]
        face_colors = self.old_face_colors[-1]

        self.face_colors[ind, :3] = face_colors
        self.ax.figure.canvas.draw_idle()
        self.ind_list = self.ind_list[:-1]
        self.old_face_colors = self.old_face_colors[:-1]
        self.ax.figure.canvas.draw_idle()
        print("# fiducials: " + str(len(self.selections)))
        self.fiducial_texts[-1].remove()
        self.fiducial_texts = self.fiducial_texts[:-1]
        self.fiducial_order -= 1


    def del_all_selections(self):
        self.selections = []
        self.selected_regions = []

        for ind, face_colors in zip(self.ind_list, self.old_face_colors):
            self.face_colors[ind, :3] = face_colors
            self.ax.figure.canvas.draw_idle()
        
        self.ind_list = []
        self.old_face_colors = []
        self.ax.figure.canvas.draw_idle()
        print("# fiducials: " + str(len(self.selections)))
        for txt in self.fiducial_texts:
            txt.remove()
        self.fiducial_texts = []
        self.fiducial_order = 1
