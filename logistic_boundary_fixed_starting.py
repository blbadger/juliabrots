import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('dark_background')

def logistic_boundaries(h_range, w_range, max_iterations, t):
	y, x = np.ogrid[-10/(2**(t/15)) - 0.00002: 10/(2**(t/15)) + 0.00002: h_range*1j, -10/(2**(t/15)) + 3.58354: 10/(2**(t/15)) + 3.58358: w_range*1j]
	r_array = x + y*1j
	starting_point = 0.5
	x_array = np.zeros(r_array.shape) + starting_point

	iterations_until_divergence = max_iterations + np.zeros(r_array.shape)
	not_already_diverged = iterations_until_divergence < 10000

	for i in range(max_iterations):
		x_array = x_array * r_array * (1 - x_array)

		# make a boolean array for diverging indices of z_array
		x_size_array = x_array * np.conj(x_array)
		diverging = x_size_array > 100
		diverging_now = diverging & not_already_diverged
		iterations_until_divergence[diverging_now] = i
		not_already_diverged = np.invert(diverging_now) & not_already_diverged

		# prevent overflow (numbers -> infinity) for diverging locations
		x_array[diverging_now] = 0 

	return iterations_until_divergence

for t in range(0, 1):
	plt.imshow(logistic_boundaries(2000, 2000, 50 + int(5*t), t), cmap='twilight_shifted', extent=[-10/(2**(t/15)) + 3.583564, 10/(2**(t/15)) + 3.583564, -10/(2**(t/15)), 10/(2**(t/15))])
	plt.axis('off')
	# plt.show()
	plt.savefig('{}.png'.format(t), bbox_inches='tight', dpi=300)
	plt.close()
	
