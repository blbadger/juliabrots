import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('dark_background')

def logistic_boundaries(h_range, w_range, max_iterations, t):
	y, x = np.ogrid[-0.5/(2**(t/15)): 0.5/(2**(t/15)): h_range*1j, 0/(2**(t/15)): 1/(2**(t/15)): w_range*1j]
	starting_point = x + y*1j
	x_array = starting_point
	r = 3
	# x_array = np.zeros(r_array.shape) + starting_point

	iterations_until_divergence = max_iterations + np.zeros(starting_point.shape)
	not_already_diverged = iterations_until_divergence < 10000

	for i in range(max_iterations):
		x_array = x_array * r * (1 - x_array)

		# make a boolean array for diverging indicies of z_array
		x_size_array = x_array * np.conj(x_array)
		diverging = x_size_array > 100
		diverging_now = diverging & not_already_diverged
		iterations_until_divergence[diverging_now] = i
		not_already_diverged = np.invert(diverging_now) & not_already_diverged

		# prevent overflow (numbers -> infinity) for diverging locations
		x_array[diverging_now] = 0 

	return iterations_until_divergence

for t in range(0, 1):
	plt.imshow(logistic_boundaries(2000, 2000, 50, t), cmap='twilight', extent=[0/(2**(t/15)), 1/(2**(t/15)), -0.5/(2**(t/15)), 0.5/(2**(t/15))])
	plt.axis('off')
	plt.savefig('{}.png'.format(t), bbox_inches='tight', dpi=300)
	plt.close()
	break


