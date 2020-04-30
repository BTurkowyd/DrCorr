import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import LassoSelector
from matplotlib.path import Path
from fiducial2 import Fiducial2
from image_reconstruction2 import ImageReconstruction

class ImageReconstructionDrCorrection(ImageReconstruction):

    def __init__(self, data, intensity_threshold, file_format):
        super().__init__(data, intensity_threshold, file_format)

    def onselect(self, verts):
        self.face_colors = self.pts.get_facecolors()
        self.path = Path(verts)

        ind = np.nonzero(self.path.contains_points(self.pts.get_offsets()))[0]

        self.ind_list.append(ind)
        self.old_face_colors.append(self.face_colors[ind, :3])
        self.face_colors[ind, :3] = [0, 1, 0]
        self.ax.figure.canvas.draw_idle()

        if self.file_format == "RapidSTORM":
            selected_data = self.data[ind]
            selected_data = selected_data[selected_data[:,3] > self.intensity_threshold]
        else:
            selected_data = self.data.loc[ind]
            selected_data = selected_data[selected_data["intensity [photon]"] > self.intensity_threshold]            

        print(len(selected_data))
        self.selections.append(Fiducial2(selected_data, self.file_format))
        print("# fiducials: " + str(len(self.selections)))