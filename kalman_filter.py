import numpy as np

class Localizations:
	def __init__(self, data):
		self.x = data[:,0]
		self.y = data[:,1]
		self.global_var_x = np.nanstd(self.x)**2
		self.global_var_y = np.nanstd(self.y)**2
		self.means_x = np.zeros_like(self.x)
		self.means_y = np.zeros_like(self.y)
		self.vars_x = np.zeros_like(self.x)
		self.vars_y = np.zeros_like(self.y)
		self.aver_drift_x = 0
		self.aver_drift_y = 0

		for i in range(len(self.x)):
			try:
				self.aver_drift_x += self.x[i+1] - self.x[i]
				self.aver_drift_y += self.y[i+1] - self.y[i]
			except IndexError:
				pass

			if i < 1000:
				self.means_x[i] = np.nanmean(self.x[:1000+i])
				self.means_y[i] = np.nanmean(self.y[:1000+i])
				self.vars_x[i] = np.nanstd(self.x[:1000+i])**2
				self.vars_y[i] = np.nanstd(self.y[:1000+i])**2
			elif i < len(self.x) - 1000:
				self.means_x[i] = np.nanmean(self.x[i-1000:i+1000])
				self.means_y[i] = np.nanmean(self.y[i-1000:i+1000])
				self.vars_x[i] = np.nanstd(self.x[i-1000:i+1000])**2
				self.vars_y[i] = np.nanstd(self.y[i-1000:i+1000])**2
			else:
				self.means_x[i] = np.nanmean(self.x[i-1000:])
				self.means_y[i] = np.nanmean(self.y[i-1000:])
				self.vars_x[i] = np.nanstd(self.x[i-1000:])**2
				self.vars_y[i] = np.nanstd(self.y[i-1000:])**2
		# print("Loaded: %.2f, %.2f" % (self.aver_drift_x, self.aver_drift_y))
		self.aver_drift_x = self.aver_drift_x / len(self.x)
		self.aver_drift_y = self.aver_drift_y / len(self.y)
		# print("Loaded: %.2f, %.2f" % (self.aver_drift_x, self.aver_drift_y))


class KalmanFilterXY:
	def __init__(self, data):
		self.data = Localizations(data)

		self.measured_x = self.data.x
		self.measured_y = self.data.y

		self.var_x = self.data.global_var_x
		self.var_y = self.data.global_var_y

		self.measure_var_x = self.data.vars_x
		self.measure_var_y = self.data.vars_y

		self.predicted_x = np.zeros_like(self.data.means_x)
		self.predicted_y = np.zeros_like(self.data.means_y)

		self.kalman_gain_x = np.zeros_like(self.predicted_x)
		self.kalman_gain_y = np.zeros_like(self.predicted_y)

		self.corrected_x = np.zeros_like(self.predicted_x)
		self.corrected_y = np.zeros_like(self.predicted_y)

		self.global_var_x = []
		self.global_var_y = []


	def run(self):

		for i in range(1, len(self.kalman_gain_x)):

			self.predicted_x[i] = self.data.aver_drift_x + self.corrected_x[i-1]
			self.predicted_y[i] = self.data.aver_drift_y + self.corrected_y[i-1]

			self.kalman_gain_x[i] = self.var_x / (self.var_x + self.measure_var_x[i])
			self.kalman_gain_y[i] = self.var_y / (self.var_y + self.measure_var_y[i])

			self.corrected_x[i] = self.predicted_x[i] + self.kalman_gain_x[i]*(self.measured_x[i] - self.predicted_x[i])
			self.corrected_y[i] = self.predicted_y[i] + self.kalman_gain_y[i]*(self.measured_y[i] - self.predicted_y[i])

			self.var_x = self.var_x - self.kalman_gain_x[i] * self.var_x + np.abs(self.data.aver_drift_x)
			self.var_y = self.var_y - self.kalman_gain_x[i] * self.var_y + np.abs(self.data.aver_drift_y)

			self.global_var_x.append(self.var_x)
			self.global_var_y.append(self.var_y)

			# print("Kalman filter applied!")