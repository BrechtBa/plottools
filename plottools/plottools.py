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
import numpy as np
import itertools

def set_publication_rc():
    # figure
    plt.rc('figure', autolayout=True, figsize=(80/25.4,50/25.4))
    plt.rc('savefig', format='pdf', dpi=150, bbox='tight', pad_inches=0.01)
    # font
    plt.rc('font', family='serif', serif=['computer modern roman'], size=6)
    # axes
    plt.rc('axes', linewidth=0.4, labelsize=8)
    plt.rc('axes.formatter', useoffset=False)
    # legend
    plt.rc('legend', fontsize=8, frameon=True)
    # lines
    plt.rc('lines', linewidth=0.8,markersize=4)
    # patch
    plt.rc('patch', linewidth=0.4, edgecolor=(0.3,0.3,0.3))
    # text
    plt.rc('text', usetex=True)
    # ticks
    plt.rc('xtick.major', size=3, width=0.3, pad=3)
    plt.rc('ytick.major', size=3, width=0.3, pad=3)
    plt.rc('xtick.minor', size=2, width=0.3, pad=3)
    plt.rc('ytick.minor', size=2, width=0.3, pad=3)
    
    
def zoom_axes(fig,ax,zoom_x,zoom_y,axes_x,axes_y,box=True,box_color='k',box_alpha=0.8,connect=True,connect_color='k',connect_alpha=0.3,spacing=4,tick_width=20,tick_height=12):
    """
    Creates a new axes which zooms in on a part of a given axes.
    Axes limits should not be changed after a zoom axes has been added
    zoom_axes does not give the expected results when used on a subfigure

    Arguments:
        fig:        matplotlib figure
        ax:         matplotlib axes
        zoom_x:     list, specifying the zooming horizontal area
        zoom_y:     list, specifying the zooming vertical area
        axes_x:     list, specifying the new axes horizontal location in data coordinates
        axes_y:     list, specifying the new axes vertical location in data coordinates

    Returns:
        ax1:        a new axes

    Example:
        plottools.zoom_axes(fig,ax,[0.1,0.3],[1.0,1.2],[1.0,1.9],[1.5,2.0])
        
    """

    plt.tight_layout()
    ax1_p0 = (ax.transData + fig.transFigure.inverted()).transform_point((axes_x[0],axes_y[0]))
    ax1_p1 = (ax.transData + fig.transFigure.inverted()).transform_point((axes_x[1],axes_y[1]))

    ax1 = plt.axes([ax1_p0[0],ax1_p0[1],ax1_p1[0]-ax1_p0[0],ax1_p1[1]-ax1_p0[1]])

    ax1.set_xlim(zoom_x)
    ax1.set_ylim(zoom_y)

    plt.xticks(fontsize=4)
    plt.yticks(fontsize=4)
    ax1.tick_params(axis='x', pad=3)
    ax1.tick_params(axis='y', pad=2)

    if box:
        ax.plot([zoom_x[0],zoom_x[1],zoom_x[1],zoom_x[0],zoom_x[0]],[zoom_y[0],zoom_y[0],zoom_y[1],zoom_y[1],zoom_y[0]],color=box_color,alpha=box_alpha,linewidth=0.4)

    if connect:
        
        # define a box of points of the axes and the zoom
        zoom_xx = [zoom_x[0],zoom_x[0],zoom_x[1],zoom_x[1]]
        zoom_yy = [zoom_y[0],zoom_y[1],zoom_y[1],zoom_y[0]]
        axes_xx = [axes_x[0],axes_x[0],axes_x[1],axes_x[1]]
        axes_yy = [axes_y[0],axes_y[1],axes_y[1],axes_y[0]]
        
        # determine which points to connect
        if axes_x[1] < zoom_x[0]:
            # left
            if axes_y[0] > zoom_y[1]:
                # top
                p1 = 0
                p2 = 2
            elif axes_y[1] < zoom_y[0]:
                # bottom
                p1 = 1
                p2 = 3
            else:
                # center
                p1 = 2
                p2 = 3
        
        elif axes_x[0] > zoom_x[1]:
            # right
            if axes_y[0] > zoom_y[1]:
                # top
                p1 = 1
                p2 = 3
            elif axes_y[1] < zoom_y[0]:
                # bottom
                p1 = 0
                p2 = 2
            else:
                # center
                p1 = 0
                p2 = 1
                
        else:
            # center
            if axes_y[0] > zoom_y[1]:
                # top
                p1 = 0
                p2 = 3
            elif axes_y[1] < zoom_y[0]:
                # bottom
                p1 = 1
                p2 = 2
            else:
                # center, the axes is over the zoom
                p1 = 0
                p2 = 0

        
        line1 = ([zoom_xx[p1],axes_xx[p1]],[zoom_yy[p1],axes_yy[p1]])
        line2 = ([zoom_xx[p2],axes_xx[p2]],[zoom_yy[p2],axes_yy[p2]])
        
       
        # estimate the width and height of the ticks
        tick_width  = (ax.transData.inverted()).transform_point((tick_width,0))[0]-(ax.transData.inverted()).transform_point((0,0))[0]
        tick_height = (ax.transData.inverted()).transform_point((0,tick_height))[1]-(ax.transData.inverted()).transform_point((0,0))[1]
        spacing     = (ax.transData.inverted()).transform_point((spacing,0))[0]-(ax.transData.inverted()).transform_point((0,0))[0]
        
        # create fictional boxes around the axes where no lines should be
        box_axes_x = [ axes_x[0]-tick_width , axes_x[1]+spacing]
        box_axes_y = [ axes_y[0]-tick_height , axes_y[1]+spacing]
        
        box_zoom_x = [ zoom_x[0]-spacing , zoom_x[1]+spacing]
        box_zoom_y = [ zoom_y[0]-spacing , zoom_y[1]+spacing]
        

        
        # cut the lines inside the boxes
        t = np.linspace(0,1,100)
        
        line1_cut = line1
        line2_cut = line2
        for tt in t:
            x = line1[0][0]*(1-tt) + line1[0][1]*tt
            y = line1[1][0]*(1-tt) + line1[1][1]*tt
            if x <= box_zoom_x[0] or x >= box_zoom_x[1] or y <= box_zoom_y[0] or y >= box_zoom_y[1]:
                line1_cut[0][0] = x
                line1_cut[1][0] = y
                break
        
        for tt in t[::-1]:
            x = line1[0][0]*(1-tt) + line1[0][1]*tt
            y = line1[1][0]*(1-tt) + line1[1][1]*tt
            if (x <= box_axes_x[0] or x >= box_axes_x[1]) or (y <= box_axes_y[0] or y >= box_axes_y[1]):
                line1_cut[0][1] = x
                line1_cut[1][1] = y
                break
        
        for tt in t:
            x = line2[0][0]*(1-tt) + line2[0][1]*tt
            y = line2[1][0]*(1-tt) + line2[1][1]*tt
            if (x <= box_zoom_x[0] or x >= box_zoom_x[1]) or (y <= box_zoom_y[0] or y >= box_zoom_y[1]):
                line2_cut[0][0] = x
                line2_cut[1][0] = y
                break
        
        for tt in t[::-1]:
            x = line2[0][0]*(1-tt) + line2[0][1]*tt
            y = line2[1][0]*(1-tt) + line2[1][1]*tt
            if (x <= box_axes_x[0] or x >= box_axes_x[1]) or (y <= box_axes_y[0] or y >= box_axes_y[1]):
                line2_cut[0][1] = x
                line2_cut[1][1] = y
                break
                 
        # draw the connecting lines         
        ax.plot(line1_cut[0],line1_cut[1],color=connect_color,alpha=connect_alpha,linewidth=0.4)
        ax.plot(line2_cut[0],line2_cut[1],color=connect_color,alpha=connect_alpha,linewidth=0.4)
        

    return ax1

def set_style(style,axes=None):
    """
    
    Arguments:
        style:          string, style string 'verticalgridonly',
        axes=None:      matplotlib axes object
        
    Returns:
        
    Example:
        plottools.set_style()
    """
    
    if axes == None:
        axes = plt.gca()
        
    if style == 'verticalgridonly':
        # hide the spines except the bottom one
        axes.spines['top'].set_visible(False)
        # axes.spines['bottom'].set_visible(False)
        axes.spines['right'].set_visible(False)
        axes.spines['left'].set_visible(False)

        # show ticks only on the left bottom  
        axes.get_xaxis().tick_bottom()
        axes.get_yaxis().tick_left()
        
        # add horizontal lines
        yticks = axes.get_yticks()
        xlim = axes.get_xlim()
        
        for y in yticks:
            axes.plot(xlim, [y,y], '-', linewidth=0.5, color='k', alpha=0.3, zorder=-10)
                 
        axes.xaxis.set_tick_params(which='both', bottom='off', top='off', labelbottom='on', left='off', right='off', labelleft='on')
        axes.yaxis.set_tick_params(which='both', bottom='off', top='off', labelbottom='on', left='off', right='off', labelleft='on')         
                 
             