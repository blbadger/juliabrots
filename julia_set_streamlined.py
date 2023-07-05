import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('dark_background')

def julia_set(h_range, w_range, max_iterations, t):
	y, x = np.ogrid[-1.4: 1.4: h_range*1j, -1.4: 1.4: w_range*1j]
	z_array = x + y*1j
	c_value = -0.29609091 + 0.00013*t + 0.62491j + 0.00013j*t
	iterations_until_divergence = max_iterations + np.zeros(z_array.shape)

	# create array of all True
	not_already_diverged = iterations_until_divergence < 10000

	# create array of all False
	diverged_in_past = iterations_until_divergence > 10000

	for i in range(max_iterations):
		z_array = z_array**2 + c_value

		# make a boolean array for diverging indices of z_array
		z_size_array = z_array * np.conj(z_array)
		diverging = z_size_array > 4
		diverging_now = diverging & not_already_diverged
		iterations_until_divergence[diverging_now] = i
		not_already_diverged = np.invert(diverging_now) & not_already_diverged

		# prevent overflow (values headed towards infinity) for diverging locations
		diverged_in_past = diverged_in_past | diverging_now
		z_array[diverged_in_past] = 0


	return iterations_until_divergence

for t in range(300):
	plt.imshow(julia_set(2000, 2000, 70 + 5*t, t), cmap='twilight')
	plt.axis('off')
	plt.savefig('{}.png'.format(t), dpi=300)
	plt.close()

