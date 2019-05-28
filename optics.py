from sklearn.cluster import OPTICS
import numpy as np

import methods
import gui

class OPTICS_class:
    def __init__(self, rois, minPts=2, max_eps=np.inf):
        self.x_min = rois[0, 0]
        self.y_min = rois[0, 1]
        self.x_max = rois[1, 0]
        self.y_max = rois[1, 1]
        self.max_eps = max_eps
        self.minPts = minPts
        self.optics_rois = []
        self.particle_ids = []
        self.order = []

    def run_optics(self):
        for i, p in enumerate(methods.particles):
            if self.x_min < p.x < self.x_max and self.y_min < p.y < self.y_max:
                self.optics_rois.append([p.x, p.y])
                self.particle_ids.append(i)
        
        self.optics_rois = np.asarray(self.optics_rois)
        self.clustering = OPTICS(int(self.minPts), self.max_eps).fit(self.optics_rois)

        for ids, label, rd in zip(self.particle_ids, self.clustering.labels_, self.clustering.reachability_):
            methods.particles[ids].optics = label
            methods.particles[ids].optics_rd = rd
        
        for order in self.clustering.ordering_:
            self.order.append(methods.particles[order].optics_rd)

        self.rd_ordered = self.clustering.reachability_[self.clustering.ordering_]

    def write(self, order):
        with open("OPTICS_roi_" + str(order) + ".txt", "w") as f:
            for ids in self.particle_ids:
                f.write("%.2f %.2f %.0f %.2f\n" % (methods.particles[ids].x, methods.particles[ids].y, methods.particles[ids].optics, methods.particles[ids].optics_rd))
        
        np.savetxt("OPTICS_RDs_roi_" + str(order) + ".txt", self.rd_ordered, '%.2f')

        print("OPTICS done")