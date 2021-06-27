from sklearn.cluster import DBSCAN
import numpy as np

import methods

class DBSCAN_class:
    def __init__(self, rois, eps, minPts, fileFormat="RapidSTORM"):
        self.eps = eps
        self.minPts = minPts
        self.db_rois = []
        self.particle_ids = []
        self.rois = rois
        self.fileFormat = fileFormat
    
    def run_dbscan(self):
        if self.fileFormat == "RapidStorm":
            for i, p in enumerate(self.rois):
                self.db_rois.append([p[0], p[1]])
                self.particle_ids.append(i)
        else:
            for i, p in self.rois.iterrows():
                self.db_rois.append([p["x [nm]"], p["y [nm]"]])
                self.particle_ids.append(i)

        # for i, p in enumerate(methods.particles):
        #     if self.x_min < p.x < self.x_max and self.y_min < p.y < self.y_max:
        #         self.db_rois.append([p.x, p.y])
        #         self.particle_ids.append(i)

        self.db_rois = np.asarray(self.db_rois)
        self.clustering = DBSCAN(self.eps, self.minPts).fit(self.db_rois)

        for ids, point in zip(self.particle_ids, self.clustering.labels_):
            methods.particles[ids].dbscan = point

    def write(self, order):
        with open("DBSCAN_roi" + str(order) + ".txt", "w") as f:
            # for ids in self.particle_ids:
            #     f.write("%.2f %.2f %.0f\n" % (methods.particles[ids].x, methods.particles[ids].y, methods.particles[ids].dbscan))

            for i in range(len(self.db_rois)):
                f.write("%.2f %.2f %.0f\n" % (self.db_rois[i, 0], self.db_rois[i, 1], self.clustering.labels_[i]))