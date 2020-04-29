import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import LassoSelector
from matplotlib.path import Path
from fiducial2 import Fiducial2

class ImageReconstruction:

    def __init__(self, data, intensity_threshold):
        self.data = np.loadtxt(data)
        self.intensity_threshold = intensity_threshold
        self.fiducials = []

        plt.style.use('dark_background')

        self.subplot_kw = dict(xlim=(0, np.max(self.data[:,0])), ylim=(0, np.max(self.data[:,1])), autoscale_on=False)
        _, self.ax = plt.subplots(subplot_kw=self.subplot_kw)

        self.pts = self.ax.scatter(self.data[:, 0], self.data[:, 1], s=1, c=np.log(self.data[:, 3]), cmap='hot', linewidths=0)

        self.lasso = LassoSelector(self.ax, self.onselect, button=3)

        plt.axis('off')
        plt.show()

        
    def onselect(self, verts):
        self.face_colors = self.pts.get_facecolors()
        self.path = Path(verts)

        ind = np.nonzero(self.path.contains_points(self.pts.get_offsets()))[0]
        self.face_colors[ind, :3] = [0, 1, 0]
        self.ax.figure.canvas.draw_idle()

        selected_data = self.data[ind]
        selected_data = selected_data[selected_data[:,3] > self.intensity_threshold]

        print(len(selected_data))

        self.fiducials.append(Fiducial2(selected_data))

