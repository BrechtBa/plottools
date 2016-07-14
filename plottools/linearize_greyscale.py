import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import colorsys
from colorspacious import cspace_converter  
  


def plot_colors(ax,coldict,order={}):
    n = len(coldict.keys())
    
    if order == {}:
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
    h,l,s = colorsys.rgb_to_hls(col[0],col[1],col[2])

    ls = np.linspace(0,1,100)
    gs = []
    
    for li in ls:
        ri,gi,bi = colorsys.hls_to_rgb(h,li,s)
        gs.append(np.mean(to_greyscale((ri,gi,bi))))

        
    ll = np.interp(grey,gs,ls)

    newcol = colorsys.hls_to_rgb(h,ll,s)
    
    return newcol
  
  
  
  
def linearize_greyscale(colors_rgb,grey_min,grey_max,order={},plot=False):
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
    if order == {}:
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
    linearize_greyscale(colors_rgb,0.20,0.90,order=order,plot=True)

    print('\nlight colors:')
    linearize_greyscale(colors_rgb,0.40,0.95,order=order,plot=True)

    
    plt.show()
