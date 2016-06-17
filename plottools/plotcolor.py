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
    'k': ( 40./255, 40./255, 40./255),
    'n': (  0./255, 56./255,190./255),
    'p': (115./255, 45./255,145./255),
    'm': (186./255, 57./255,  0./255),
    'b': ( 33./255, 96./255,255./255),
    'g': ( 78./255,123./255, 43./255),
    'r': (224./255, 95./255, 86./255),
    't': ( 53./255,158./255,148./255),
    'o': (178./255,152./255, 22./255),
    'f': (214./255,144./255,198./255),
    'l': ( 99./255,205./255,107./255),
    'a': (119./255,211./255,189./255),
    'y': (205./255,220./255, 35./255) }

lightcolors = {
    'k': ( 60./255, 60./255, 60./255),
    'n': (  0./255, 68./255,230./255),
    'p': (139./255, 54./255,176./255),
    'm': (226./255, 69./255,  0./255),
    'b': ( 73./255,125./255,255./255),
    'g': ( 97./255,153./255, 53./255),
    'r': (230./255,127./255,120./255),
    't': ( 64./255,188./255,176./255),
    'o': (214./255,182./255, 26./255),
    'f': (225./255,173./255,213./255),
    'l': (129./255,215./255,136./255),
    'a': (149./255,221./255,204./255),
    'y': (213./255,226./255, 70./255) }
    
longnames = {
    'black': 'k',
    'navy': 'n',
    'purple': 'p',
    'maroon': 'm',
    'blue': 'b',
    'green': 'g',
    'red': 'r',
    'teal': 't',
    'olive': 'o',
    'fuchsia': 'f',
    'lime': 'l',
    'aqua': 'a',
    'yellow': 'y' }
    
basecycle = ['b','r','l','y','m','o','a','n','p','g','t','f','k']    


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
