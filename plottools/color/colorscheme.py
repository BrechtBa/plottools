#!/usr/bin/env/ python
################################################################################
#    Copyright 2016 Brecht Baeten
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
# Colorscheme class 
################################################################################
class Colorscheme(object):
    """
    A colorscheme class useful for plotting
   
    """
    
    def __init__(self,colors,longnames=None,cycle=None):
        """
        defines a colorscheme object useful for plotting
        
        Parameters
        ----------
        colors : dict
            Dictionary of named colors as RGB (0-1) tupples
        
        longnames : dict, optional
            Dictionary of long names of the colors specified in colors
            
        cycle : list, optional
            List with the cycle order
        
        Examples
        --------
        >>> cs = Colorscheme({'r':(1.,0.,0.),'g':(0.,1.,0.),'b':(0.,0.,1.)},['b','g','r'])
        >>> print( cs[0] )
        >>> 
        >>> print( cs.next() )
        >>> print( cs.next() )
        >>> 
        >>> cs.reset_index()
        >>> print( cs.next() )
        """
        
        
        if longnames == None:
            longnames = {k:k for k in colors.keys()}
            
        if cycle == None:
            cycle = colors.keys()
            
            
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
        converts the colorscheme to an svg file with block of colors ordered
        according to the cycle
        
        parameters
        ----------
            filename : string
                the file to write the svg file to
         
        Examples
        --------
        >>>> plottools.colors.to_svg('defaultcolors.svg')
        
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

