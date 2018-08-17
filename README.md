# VectorTrace
Python vector trace plot using numpy and pyplot. This is useful for plotting vectorcardiograms (VECG)

Usage: 
(Assuming that Imat is a 2D array of a vectorcardiogram, and the respective timings like tmax and qwave have been defined)
  ```python
  from lineArrowPlot import lineArrowPlot
  
  lineArrowPlot(Imat[:,0], Imat[:,1], color='k')
	plt.xlabel('Current ((A*(mu0*4pi)*10^6', size=20)
	plt.ylabel('Current ((A*(mu0*4pi)*10^6', size=20)
	plt.title(ID, size=30)
	plt.annotate("R-peak, "+str((rpeak+1)*2)+"ms",
	xy=(Imat[rpeak,0], Imat[rpeak,1]), xycoords='data',
	xytext=(Imat[rpeak,0], Imat[rpeak,1]), textcoords='data', size=20,
	arrowprops=dict(arrowstyle="fancy",
	connectionstyle="angle3", color='0.5'),
	)
	plt.annotate("T-max, "+str((tmax+1)*2)+"ms",
	xy=(Imat[tmax,0], Imat[tmax,1]), xycoords='data',
	xytext=(Imat[tmax,0], Imat[tmax,1]), textcoords='data', size=20,
	arrowprops=dict(arrowstyle="fancy",
	connectionstyle="angle3", color='0.5'),
	)
	if pwaveexists:
		plt.annotate("Q-wave, "+str((qwave+1)*2)+"ms",
		xy=(Imat[qwave,0], Imat[qwave,1]), xycoords='data',
		xytext=(Imat[qwave,0], Imat[qwave,1]), textcoords='data', size=20,
		arrowprops=dict(arrowstyle="fancy",
		connectionstyle="angle3", color='0.5'),
		)
	fig = plt.gcf()
	fig.set_size_inches(15.5, 15.5, forward=True)
	ax = plt.gca()
	ax.grid()
	ax.set_aspect('equal')
  plt.show()
  ```
![example vectorcardiogram trace][example]

[example]: https://github.com/malteehrlen/VectorTrace/blob/master/HK_DEMO%20_PSEUDO_0.png "example vectorcardiogram trace"
