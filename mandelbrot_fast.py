#! python3
# A program to display the mandelbrot set, based on the numpy 
# quickstart tutorial found here (https://numpy.org/devdocs/user/quickstart.html)

import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('dark_background')

def mandelbrot_set(h_range, w_range, max_iterations, t):
	y, x = np.ogrid[1.6: -1.6: h_range*1j, -2.2: 1.4: w_range*1j]
	a_array = x + y*1j		#
	z_array = np.zeros(a_array.shape) 
	iterations_till_divergence = max_iterations + np.zeros(a_array.shape)

	# make an array with all elements set to 'True'
	not_already_diverged = a_array < 1000

	for i in range(max_iterations):
		# mandelbrot equation
		z_array = z_array**2 + a_array + np.exp(3.1415j * t/150)/3

		# make a boolean array for diverging indicies of z_array
		z_size_array = z_array * np.conj(z_array)
		divergent_array = z_size_array > 4
		diverging_now = divergent_array & not_already_diverged

		iterations_till_divergence[diverging_now] = i
		# prevent overflow (numbers -> infinity) for diverging locations
		z_array[divergent_array] = 0

		# prevent the a point from diverging again in future iterations
		not_already_diverged = np.invert(diverging_now) & not_already_diverged


	return iterations_till_divergence

plt.imshow(mandelbrot_set(2000, 2000, 70), cmap='twilight_shifted')
plt.axis('off')
plt.savefig('mandelbrot_corrected.png', dpi=300)
plt.close()
