import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('dark_background')

def julia_set(h_range, w_range, max_iterations, t):
	y, x = np.ogrid[-1.4: 1.4: h_range*1j, -1.4: 1.4: w_range*1j]
	z_array = x + y*1j
	a = -0.29609091 + 0.00013*t + 0.62491j + 0.00013j*t
	iterations_till_divergence = max_iterations + np.zeros(z_array.shape)

	for i in range(max_iterations):
		z_array = z_array**2 + a 

		# make a boolean array for diverging indicies of z_array
		z_size_array = z_array * np.conj(z_array)
		divergent_array = z_size_array > 4

		iterations_till_divergence[divergent_array] = i

		# prevent overflow (numbers -> infinity) for diverging locations
		z_array[divergent_array] = 0 


	return iterations_till_divergence

for t in range(300):
	plt.imshow(julia_set(2000, 2000, 70 + 5*t, t), cmap='twilight')
	plt.axis('off')
	plt.savefig('{}.png'.format(t), dpi=300)
	plt.close()