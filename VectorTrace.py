#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Malte Ehrlen malte@ehrlen.com

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

def lineArrowPlot(x, y, color=0.5, label=''):
	return plt.quiver(x[:-1], y[:-1], x[1:]-x[:-1], y[1:]-y[:-1], scale_units='xy', angles='xy', scale=1, color=color, label=label)
	

def putCursor(label, position, c):
	plt.annotate(label,
	xy=position, 
	xycoords='data',
	xytext=(position[0], position[1]+100), 
	textcoords='data', 
	size=20,
	color=c,
	arrowprops=dict(arrowstyle="fancy",
	connectionstyle="angle3", color='0.5'),
	)
