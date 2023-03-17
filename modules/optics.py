from sklearn.cluster import OPTICS
import numpy as np

class OPTICS_class:
    def __init__(self, rois, particles, minPts, max_eps, fileFormat):
        self.max_eps = max_eps
        self.minPts = minPts
        self.optics_rois = []
        self.particle_ids = []
        self.order = []
        self.rois = rois
        self.fileFormat = fileFormat
        self.particles = particles

    def run_optics(self):
        if self.fileFormat == "RapidSTORM":
            for i, p in enumerate(self.rois):
                self.optics_rois.append([p[0], p[1]])
                self.particle_ids.append(i)
        else:
            for i, p in self.rois.iterrows():
                self.optics_rois.append([p["x [nm]"], p["y [nm]"]])
                self.particle_ids.append(i)

        # for i, p in enumerate(methods.particles):
        #     if self.x_min < p.x < self.x_max and self.y_min < p.y < self.y_max:
        #         self.optics_rois.append([p.x, p.y])
        #         self.particle_ids.append(i)
        
        self.optics_rois = np.asarray(self.optics_rois)
        self.clustering = OPTICS(int(self.minPts), self.max_eps).fit(self.optics_rois)

        for ids, label, rd in zip(self.particle_ids, self.clustering.labels_, self.clustering.reachability_):
            self.particles[ids].optics = label
            self.particles[ids].optics_rd = rd
        
        for order in self.clustering.ordering_:
            self.order.append(self.particles[order].optics_rd)

        self.core_ordered = self.clustering.reachability_[self.clustering.ordering_]

    def write(self, order):
        with open("OPTICS_roi_" + str(order) + ".txt", "w") as f:

            for i in range(len(self.optics_rois)):
                f.write("%.2f %.2f %.0f %.2f\n" % (self.optics_rois[i, 0], self.optics_rois[i, 1], self.clustering.labels_[i], self.clustering.reachability_[i]))
            # for ids in self.particle_ids:
            #     f.write("%.2f %.2f %.0f %.2f\n" % (methods.particles[ids].x, methods.particles[ids].y, methods.particles[ids].optics, methods.particles[ids].optics_rd))
        
        np.savetxt("OPTICS_RDs_roi_" + str(order) + ".txt", self.core_ordered, '%.2f')

        print("OPTICS done")