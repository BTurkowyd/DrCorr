from numpy import zeros

class Fiducial2:

    def __init__(self, points, file_format):
        self.fiducial = []
        self.file_format = file_format

        if file_format == "RapidSTORM":
            for f in points:
                self.fiducial.append(f)
        else:
            for f in points.values:
                self.fiducial.append(f)
    
    def rel_drift(self):
        self.rel_x = []
        self.rel_y = []
        self.t = []
        self.intensity = []
        for i in range(len(self.fiducial)):
            if self.file_format == "RapidSTORM":
                self.temp_x = self.fiducial[i][0] - self.fiducial[0][0]
                self.temp_y = self.fiducial[i][1] - self.fiducial[0][1]
                self.temp_t = self.fiducial[i][2]
                self.temp_int = self.fiducial[i][3]
            else:
                self.temp_x = self.fiducial[i][2] - self.fiducial[0][2]
                self.temp_y = self.fiducial[i][3] - self.fiducial[0][3]
                self.temp_t = self.fiducial[i][1]
                self.temp_int = self.fiducial[i][5]

            self.rel_x.append(self.temp_x)
            self.rel_y.append(self.temp_y)
            self.t.append(self.temp_t)
            self.intensity.append(self.temp_int)

    def stretch_fiducials(self, loc, inputFormat):
        if inputFormat == "RapidSTORM":
            self.stretch = zeros((int(loc[-1,2])+1, 4))
        else:
            self.stretch = zeros((int(loc.values[-1,1])+1, 4))
 
        for x, y, t, intensity in zip(self.rel_x, self.rel_y, self.t, self.intensity):
            self.stretch[int(t), 0] = x
            self.stretch[int(t), 1] = y
            self.stretch[int(t), 2] = t
            self.stretch[int(t), 3] = intensity

        print("Fiducial stretched.")        