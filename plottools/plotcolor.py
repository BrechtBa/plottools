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
basecolors = {
    'a': (179./255,216./255,233./255),
    'b': ( 55./255,100./255,178./255),
    'g': ( 75./255,184./255, 86./255),
    'k': ( 51./255, 51./255, 51./255),
    'l': (145./255,216./255,127./255),
    'o': (244./255,150./255, 16./255),
    'p': (127./255, 35./255,133./255),
    'r': (244./255, 70./255, 31./255),
    'y': (245./255,246./255,104./255)
}

lightcolors = {
    'a': (207./255,230./255,241./255),
    'b': (102./255,141./255,208./255),
    'g': (125./255,204./255,133./255),
    'k': (102./255,102./255,102./255),
    'l': (180./255,229./255,167./255),
    'o': (247./255,181./255, 86./255),
    'p': (197./255, 63./255,205./255),
    'r': (247./255,120./255, 91./255),
    'y': (250./255,251./255,180./255)
}
    
longnames = {
    'black': 'k',
    'purple': 'p',
    'blue': 'b',
    'green': 'g',
    'red': 'r',
    'orange': 'o',
    'lime': 'l',
    'aqua': 'a',
    'yellow': 'y'
}
    
basecycle = ['b','r','g','o','y','p','l','a','k']


################################################################################
# Colorscheme class 
################################################################################
class Colorscheme(object):
    def __init__(self,colors=basecolors,longnames=longnames,cycle=basecycle):
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
        self.longnames = longnames
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
            if key in self.longnames:
                key = self.longnames[key]
            
            self.currentindex = self.cycle.index(key)+1
            return self.colors[key]

                   
               
################################################################################
# create default color schemes
################################################################################
color = Colorscheme()
lightcolor = Colorscheme(colors=lightcolors)
