#!/usr/bin/python
################################################################################
#    Copyright 2015 Brecht Baeten
#    This file is part of plottools.
#
#    plottools is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    plottools is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with plottools.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

import matplotlib.pyplot as plt
from cycler import cycler

################################################################################
# Color definitions
################################################################################
# colors that look ok and have considerable contrast in grayscale
basecolors = {'b': ( 69./255,128./255,215./255),
			  'o': (255./255,172./255,103./255),
			  'g': ( 40./255,186./255, 72./255),
			  'r': (165./255, 30./255, 33./255),
			  'k': ( 81./255, 79./255, 82./255),
			  'p': (123./255, 90./255,174./255),
			  'd': ( 90./255, 22./255, 25./255),
			  'y': (185./255,174./255, 85./255)}

lightcolors = {'b': ( 99./255,148./255,221./255),
			   'o': (235./255,185./255,135./255),
			   'g': ( 44./255,206./255, 80./255),
			   'r': (217./255, 47./255, 50./255),
			   'k': (111./255,108./255,113./255),
			   'p': (140./255,111./255,184./255),
			   'd': (136./255, 33./255, 38./255),
			   'y': (190./255,180./255, 98./255)}

basecycle = ['b','o','g','r','k','p','d','y']	


################################################################################
# Colorscheme class 
################################################################################
class Colorscheme(object):
	def __init__(self,colors=basecolors,cycle=basecycle):
		"""
		defines a colorscheme object useful for plotting
		
		Arguments:
		colors: dict, dictionary of named colors as RGB (0-1) tupples
		cycle:  list, list with the cycle order
		
		Example:
		cs = Colorscheme({'r':(1.,0.,0.),'g':(0.,1.,0.),'b':(0.,0.,1.)},['b','g','r'])
		print( cs[0] )
		
		print( cs.next() )
		print( cs.next() )
		
		cs.reset_index()
		print( cs.next() )
		"""
		
		self.colors = colors
		self.cycle = cycle
		self.currentindex = 0

	def next(self):
		"""
		get the next color in the cycle
		"""
		c = self.colors[self.cycle[self.currentindex]]
		self.currentindex += 1
		if self.currentindex >= len(self.cycle):
			self.currentindex = 0
			
		return c
		
	def reset_index(self):
		"""
		resets the current color index to 0
		"""
		
		self.currentindex = 0
	
	def set_as_default(self):
		"""
		sets the colorscheme as the default color cycle in matplotlib figures
		"""
		
		plt.rc('axes',prop_cycle=cycler('color', [self.colors[c] for c in self.cycle]) )
		
	def __getitem__(self,key):
		if isinstance(key,int):
			self.currentindex = key+1
			return self.colors[self.cycle[key]]
		else:
			self.currentindex = self.cycle.index(key)+1
			return self.colors[key]

				   
			   
################################################################################
# create default color schemes
################################################################################
color = Colorscheme()
lightcolor = Colorscheme(colors=lightcolors)
