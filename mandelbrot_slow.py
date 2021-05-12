#! mandelbrot_slow.py
# a program to generate an image of the mandelbrot set.  
# Relatively slow, used for the purpose of clarifying what
# exactly is being plotted.

import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('dark_background')


def mandelbrot_set(h_range, w_range, max_iterations):
	y, x = np.ogrid[-1.4: 1.4: h_range*1j, -1.8: 1: w_range*1j]
	a_array = x + y*1j
	z_array = np.zeros(a_array.shape)
	iterations_till_divergence = max_iterations + np.zeros(a_array.shape)

	for h in range(h_range):
		for w in range(w_range):
			z = z_array[h][w]
			a = a_array[h][w]
			for i in range(max_iterations):
				z = z**2 + a
				if z * np.conj(z) > 4:
					iterations_till_divergence[h][w] = i
					break


	return iterations_till_divergence

plt.imshow(mandelbrot_set(800, 800, 30), cmap='twilight_shifted')
plt.axis('off')
plt.show()
plt.close()

