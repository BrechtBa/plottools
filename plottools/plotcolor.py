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

import sys
import os
import matplotlib.pyplot as plt
from cycler import cycler

################################################################################
# Color definitions
################################################################################
# colors that look ok and have considerable contrast in grayscale
basecolors = {
    'a': (177./255,215./255,233./255),
    'b': ( 53./255, 97./255,172./255),
    'g': ( 65./255,163./255, 75./255),
    'k': ( 51./255, 51./255, 51./255),
    'l': (123./255,209./255,101./255),
    'o': (226./255,137./255, 11./255),
    'p': (115./255, 31./255,121./255),
    'r': (209./255, 47./255, 10./255),
    'y': (236./255,238./255, 14./255)
}

lightcolors = {
    'a': (206./255,230./255,241./255),
    'b': (100./255,140./255,207./255),
    'g': (104./255,195./255,113./255),
    'k': (102./255,102./255,102./255),
    'l': (168./255,225./255,153./255),
    'o': (246./255,171./255, 64./255),
    'p': (186./255, 51./255,194./255),
    'r': (246./255,100./255, 67./255),
    'y': (247./255,248./255,141./255)
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

                    
    def to_svg(self,filename):
        """
        converts the colorscheme to an svg file
        
        Arguments:
            filename: 	string, the file to write the svg file to
         
        Example:
            plottools.colors.to_svg('defaultcolors.svg')
        """
	
        # get the colors of the colorscheme
        colors = ['#{:02x}{:02x}{:02x}'.format(int(self.colors[k][0]*255),int(self.colors[k][1]*255),int(self.colors[k][2]*255)) for k in self.cycle]

        width = 100./len(self.cycle)
        x = [i*width for i in range(len(self.cycle))]
        
        # current path
        modulepath = os.path.dirname(sys.modules[__name__].__file__)

        # open the cs_blank svg file
        blank_file = open(os.path.join(modulepath,'cs_blank.svg'), 'r') 
        content = blank_file.read()
        blank_file.close()

        # find the rectangle template
        ind0 = content.find('    <rect')
        ind1 = content.find('  </g>')
        before = content[:ind0]
        after = content[ind1:]
        
        
        new_content = before
        for k,c,x in zip(self.cycle,colors,x):
            new_content = new_content + '    <rect\n       style="opacity:1;fill:{};fill-opacity:1;stroke:none;"\n       id="colorRectangle_{}"\n       width="{}"\n       height="100"\n       x="{}"\n       y="0" />\n'.format(c,k,width,x)

        new_content = new_content+after
        
        new_file = open(filename, 'w')
        new_file.write(new_content)
        new_file.close()

      
################################################################################
# create default color schemes
################################################################################
color = Colorscheme()
lightcolor = Colorscheme(colors=lightcolors)
