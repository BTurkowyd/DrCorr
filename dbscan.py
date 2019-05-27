from sklearn.cluster import DBSCAN
import numpy as np

import methods
import gui

class DBSCAN_class:
    def __init__(self, rois, eps, minPts):
        self.x_min = rois[0, 0]
        self.y_min = rois[0, 1]
        self.x_max = rois[1, 0]
        self.y_max = rois[1, 1]
        self.eps = eps
        self.minPts = minPts
        self.db_rois = []
        self.particle_ids = []
    
    def run_dbscan(self):
        for i, p in enumerate(methods.particles):
            if self.x_min < p.x < self.x_max and self.y_min < p.y < self.y_max:
                self.db_rois.append([p.x, p.y])
                self.particle_ids.append(i)

        self.db_rois = np.asarray(self.db_rois)
        self.clustering = DBSCAN(self.eps, self.minPts).fit(self.db_rois)

        for ids, point in zip(self.particle_ids, self.clustering.labels_):
            methods.particles[ids].dbscan = point

    def write(self, order):
        with open("DBSCAN_roi" + str(order) + ".txt", "w") as f:
            for ids in self.particle_ids:
                f.write("%.2f %.2f %.0f\n" % (methods.particles[ids].x, methods.particles[ids].y, methods.particles[ids].dbscan))