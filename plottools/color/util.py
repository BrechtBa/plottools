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

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from colorspacious import cspace_converter  
from PIL import Image


def plot_colors(ax,coldict,order=None):
    n = len(coldict.keys())
    
    if order == None:
        order = {}
        for i,k in enumerate(coldict.keys()):
            order[k] = i
            
    for k,c in coldict.items():
        o = order[k]
        ax.add_patch(  patches.Rectangle( (o, 0), 1.0, 5.0, facecolor=c, edgecolor='none') )
        ax.text(o+0.5,2.5,k,ha='center')
        
    plt.xlim([0,n])
    plt.ylim([0,5])


# derived from matplotlib viscm
_sRGB1_to_JCh = cspace_converter('sRGB1', 'JCh')
_JCh_to_sRGB1 = cspace_converter('JCh', 'sRGB1')

def to_greyscale(sRGB1):
    JCh = _sRGB1_to_JCh(sRGB1)
    JCh[..., 1] = 0
    return _JCh_to_sRGB1(JCh)
    

def change_lightness_to_match_greyscale(col,grey):
    JCh = _sRGB1_to_JCh(col)
    Js = np.linspace(1e-6,100,20)
    gs = []
    
    for Ji in Js:
        JCh[..., 0] = Ji
        RGBi = _JCh_to_sRGB1(JCh)
        RGBi = np.clip(RGBi,0,1)
        gi = np.mean(to_greyscale(RGBi))
        
        gs.append(gi)

    J = np.interp(grey,gs,Js)
    JCh[..., 0] = J
    newcol = _JCh_to_sRGB1( JCh )
    newcol = np.clip(newcol,0,1)

    return newcol
  
  
  
  
def distribute_greyscale_spacing(colors_rgb,grey_min,grey_max,order=None,plot=False):
    # convert all colors ro greyscale and determine the order
    colors_grey_rgb = {}
    grey = []
    keys = []
    for k,c in colors_rgb.items():
        g = np.mean( to_greyscale(c) )
        keys.append(k)
        grey.append(g)
        colors_grey_rgb[k] = (g,g,g)
        

    # define the order
    if order == None:
        order = {}
        for i,o in enumerate(np.argsort(grey)):
            order[keys[o]] = i


    # rescale to greyscale min-max
    grey_edit = np.linspace(grey_min,grey_max,len(order.keys()))
    colors_edit_rgb = {}
    for k,c in colors_rgb.items():
        colors_edit_rgb[k] = change_lightness_to_match_greyscale(c,grey_edit[order[k]])

        
    # convert all colors ro greyscale and determine the order
    colors_edit_grey_rgb = {}
    for k,c in colors_edit_rgb.items():
        colors_edit_grey_rgb[k] = to_greyscale(c)  
        

    # print final colors
    if plot:
        for k,c in colors_edit_rgb.items():
            print( '\'{}\': ({:>3.0f}./255,{:>3.0f}./255,{:>3.0f}./255),'.format(k,c[0]*255,c[1]*255,c[2]*255))
           
        fig = plt.figure()
        ax1 = fig.add_subplot(221)
        plot_colors(ax1,colors_rgb,order)
        plt.title('original')
        
        ax2 = fig.add_subplot(223)
        plot_colors(ax2,colors_grey_rgb,order)

        ax3 = fig.add_subplot(222)
        plot_colors(ax3,colors_edit_rgb,order)
        plt.title('edited')
        
        ax4 = fig.add_subplot(224)
        plot_colors(ax4,colors_edit_grey_rgb,order)  
          
      
    return colors_edit_rgb


def prepare_print_scan(colors_rgb,order=None):

    colors_grey_rgb = {}

    for k,c in colors_rgb.items():
        colors_grey_rgb[k] = to_greyscale(c)

    fig = plt.figure(figsize=(16./2.54,24./2.54))
    ax1 = fig.add_subplot(211)
    plot_colors(ax1,colors_rgb,order)
    plt.title('color')

    ax2 = fig.add_subplot(212)
    plot_colors(ax2,colors_grey_rgb,order)  
    plt.title('greyscale')


def analyse_print_scan(scanfile,colors_rgb,order=None):

    im = Image.open(scanfile).convert('RGB')

    print(im.size)
    
    if order == None:
        order = {}
        for i,k in enumerate(coldict.keys()):
            order[k] = i

    

    width,height = im.size

    rgb_color = {}
    rgb_greyscale = {}
    for key in colors_rgb:
        # get the colors from the scan file
        x = int(0.20*width + 0.66*order[key]/len(order)*width)

        y = int(0.25*height)
        r = [ im.getpixel( (xi, yi) )[0] for xi in np.array(x)+np.arange(-int(0.02*width),int(0.02*width)) for yi in np.array(y)+np.arange(-int(0.02*height),int(0.02*height)) ]
        g = [ im.getpixel( (xi, yi) )[1] for xi in np.array(x)+np.arange(-int(0.02*width),int(0.02*width)) for yi in np.array(y)+np.arange(-int(0.02*height),int(0.02*height)) ]
        b = [ im.getpixel( (xi, yi) )[2] for xi in np.array(x)+np.arange(-int(0.02*width),int(0.02*width)) for yi in np.array(y)+np.arange(-int(0.02*height),int(0.02*height)) ]
        

        rgb_color[key] = (np.mean(r)/255,np.mean(g)/255,np.mean(b)/255)

        y = int(0.80*height)
        r = [ im.getpixel( (xi, yi) )[0] for xi in np.array(x)+np.arange(-int(0.02*width),int(0.02*width)) for yi in np.array(y)+np.arange(-int(0.02*height),int(0.02*height)) ]
        g = [ im.getpixel( (xi, yi) )[1] for xi in np.array(x)+np.arange(-int(0.02*width),int(0.02*width)) for yi in np.array(y)+np.arange(-int(0.02*height),int(0.02*height)) ]
        b = [ im.getpixel( (xi, yi) )[2] for xi in np.array(x)+np.arange(-int(0.02*width),int(0.02*width)) for yi in np.array(y)+np.arange(-int(0.02*height),int(0.02*height)) ]
        
        rgb_greyscale[key] = (np.mean(r)/255,np.mean(g)/255,np.mean(b)/255)


    fig = plt.figure(figsize=(16./2.54,24./2.54))
    ax1 = fig.add_subplot(211)
    plot_colors(ax1,rgb_color,order)
    plt.title('color')

    ax2 = fig.add_subplot(212)
    plot_colors(ax2,rgb_greyscale,order)  
    plt.title('greyscale')
    
    
    # compare the printed values with to_greyscale
    greyscales = {}
    for key,val in colors_rgb.items():
        greyscales[key] = np.mean(to_greyscale(val))

    greyscales_printed = {}
    for key,val in rgb_color.items():
        greyscales_printed[key] = np.mean(val)


    # rescale so first and last value are equal
    x  = np.array([order[key] for key in colors_rgb.keys()])
    y1 = np.array([greyscales[key] for key in colors_rgb.keys()])
    y2 = np.array([greyscales_printed[key] for key in colors_rgb.keys()])
    # rescale so first and last value are equal
    y2 = min(y1) + (y2-min(y2))*(max(y1)-min(y1))/(max(y2)-min(y2))

    plt.figure()
    plt.plot(x,y1,'o',color='b',label='greyscale')
    plt.plot(x,y2,'s',color='r',label='printed')

    for key in colors_rgb.keys():
        plt.text(order[key]+0.12,greyscales[key],key)

    plt.legend(loc='lower right')
    plt.xlim([-0.5,len(colors_rgb)-1+0.5])
    plt.ylim([-0.02,1.02])

if __name__ == '__main__':

    colors_rgb = {
        'r': (245./255, 82./255, 45./255),
        'o': (244./255,154./255, 26./255),
        'y': (242./255,244./255, 66./255),
        'g': ( 32./255, 81./255, 37./255),
        'l': ( 80./255,180./255, 54./255),
        'a': ( 95./255,173./255,209./255),
        'b': ( 31./255, 57./255,101./255),
        'p': (114./255, 31./255,119./255),
        'k': ( 49./255, 49./255, 49./255)
    }

    order = {
        'k': 0,
        'p': 1,
        'b': 2,
        'r': 3,
        'g': 4,
        'o': 5,
        'l': 6,
        'a': 7,
        'y': 8
    }

    print('\nbase colors:')
    distribute_greyscale_spacing(colors_rgb,0.20,0.90,order=order,plot=True)

    print('\nlight colors:')
    distribute_greyscale_spacing(colors_rgb,0.40,0.95,order=order,plot=True)

    
    plt.show()
