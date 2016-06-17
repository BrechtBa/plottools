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
    'k': ( 13./255, 13./255, 13./255),
    'n': (  0./255, 30./255,104./255),
    'p': ( 77./255, 30./255, 92./255),
    'm': (140./255, 43./255,  0./255),
    'b': (  7./255, 79./255,255./255),
    'g': ( 66./255,105./255, 36./255),
    'r': (221./255, 79./255, 69./255),
    't': ( 49./255,145./255,136./255),
    'o': (167./255,145./255, 21./255),
    'f': (212./255,136./255,194./255),
    'l': ( 90./255,202./255, 98./255),
    'a': (115./255,209./255,187./255),
    'y': (205./255,220./255, 35./255) }

lightcolors = {
    'k': ( 33./255, 33./255, 33./255),
    'n': (  0./255, 42./255,144./255),
    'p': (103./255, 40./255,122./255),
    'm': (180./255, 55./255,  0./255),
    'b': ( 47./255,107./255,255./255),
    'g': ( 85./255,136./255, 46./255),
    'r': (227./255,111./255,103./255),
    't': ( 59./255,175./255,164./255),
    'o': (203./255,173./255, 25./255),
    'f': (222./255,166./255,209./255),
    'l': (120./255,212./255,126./255),
    'a': (145./255,219./255,201./255),
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
