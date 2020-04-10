import matplotlib
import matplotlib.pyplot as plt
import numpy as np
filenames = ["usa","slovenia", "iran", "germany"]

def read_data(filename):
	old_data = open(filename+"_actual.txt", "r")
	old_array = old_data.readlines()

	data = open(filename+"_forecast.txt", "r")
	data_array = old_array + ["\n"] + data.readlines()

	# Now we split based off of \n: Code based off of 
	# https://www.geeksforgeeks.org/python-split-list-into-lists-by-particular-value/
	idx_list = [idx + 1 for idx, val in enumerate(data_array) if val == '\n']
	split_data = [data_array[i:j] for i,j in zip([0] + idx_list,
		idx_list + ([len(data_array)] if idx_list[-1] != len(data_array) else [] ))]
	return split_data

def plot_forecasts():
	fig, ax = plt.subplots(2,2)
	i = 0
	for row in range(len(ax)):
		for col in range(len(ax)):
			ax[row,col].set_yscale('log')
			split_data = read_data(filenames[i])
			for curve in split_data:
				curve = [h.split() for h in curve]
				dates = [h[0] for h in curve[0:-1]]
				forecasts = [float(h[1]) for h in curve[0:-1]]
				ax[row,col].set(xlabel = 'Date', ylabel='Confirmed Cases', 
					title = filenames[i].capitalize() + " Case Graph" )
				ax[row,col].plot(dates, forecasts)				
			i+=1
			plt.savefig('forecast.png')

plot_forecasts()