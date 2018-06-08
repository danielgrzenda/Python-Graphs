import numpy as np
import matplotlib.pyplot as plt 
import math

def build_plot():
	n = [i for i in range(1,101)]
	plt.plot(n, constant(n), label='1')
	plt.plot(n, log_n(n), label='log(n)')
	plt.plot(n, n_log_n(n), label='nlog(n)')
	plt.plot(n, linear(n), label='n')
	plt.plot(n, n_squared(n), label='log(n^2)')
	plt.plot(n, exponential(n), label='log(2^n)')
	plt.legend(['1','log(n)','nlog(n)','n','log(n^2)','log(2^n)'])
	plt.title('Graph of the Common Big O')
	plt.xlabel('Size of N')
	plt.ylabel('Computation Complexity')
	plt.show()

def constant(n):
	return np.asarray([1 for _ in range(len(n))])

def log_n(n):
	return np.log(n)

def n_log_n(n):
	return n * np.log(n)

def linear(n):
	return n

def n_squared(n):
	return np.log(np.square(n))

def exponential(n):
	return np.log(np.exp2(n))

if __name__ == "__main__":
	build_plot()