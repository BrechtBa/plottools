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
    'a': (175./255,214./255,232./255)
    'b': ( 54./255,100./255,177./255)
    'g': ( 66./255,168./255, 77./255)
    'k': ( 51./255, 51./255, 51./255)
    'l': (126./255,210./255,104./255)
    'o': (244./255,152./255, 23./255)
    'p': (153./255, 42./255,160./255)
    'r': (245./255, 87./255, 51./255)
    'y': (241./255,243./255, 53./255)
}

lightcolors = {
    'a': (204./255,229./255,240./255)
    'b': (101./255,141./255,208./255)
    'g': (107./255,197./255,116./255)
    'k': (102./255,102./255,102./255)
    'l': (167./255,224./255,152./255)
    'o': (247./255,183./255, 91./255)
    'p': (204./255, 86./255,211./255)
    'r': (248./255,132./255,106./255)
    'y': (248./255,249./255,154./255)
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
