import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import colorsys



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

    
def rgb_to_gray(r,g,b):
    # CCIR 601
    return 0.2989*r + 0.5870*g + 0.1140*b
    
def change_lightness_to_match_grayscale(col,gray):
    h,l,s = colorsys.rgb_to_hls(col[0],col[1],col[2])

    ls = np.linspace(0,1,100)
    gs = []
    
    for li in ls:
        ri,gi,bi = colorsys.hls_to_rgb(h,li,s)
        gs.append(rgb_to_gray(ri,gi,bi))

        
    ll = np.interp(gray,gs,ls)

    newcol = colorsys.hls_to_rgb(h,ll,s)
    
    return newcol
  
  
  
  
def linearize_grayscale(colors_rgb,gray_min,gray_max,order={},plot=False):
    # convert all colors ro grayscale and determine the order
    colors_gray_rgb = {}
    gray = []
    keys = []
    for k,c in colors_rgb.items():
        g = rgb_to_gray(c[0],c[1],c[2])
        keys.append(k)
        gray.append(g)
        colors_gray_rgb[k] = (g,g,g)
        

    # define the order
    if order == {}:
        for i,o in enumerate(np.argsort(gray)):
            order[keys[o]] = i

      


    # rescale to grayscale min-max
    gray_edit = np.linspace(gray_min,gray_max,len(order.keys()))
    colors_edit_rgb = {}
    for k,c in colors_rgb.items():
        colors_edit_rgb[k] = change_lightness_to_match_grayscale(c,gray_edit[order[k]])

        
    # convert all colors ro grayscale and determine the order
    colors_edit_gray_rgb = {}
    for k,c in colors_edit_rgb.items():
        g = rgb_to_gray(c[0],c[1],c[2])
        colors_edit_gray_rgb[k] = (g,g,g)   
        

    # print final colors
    if plot:
        for k,c in colors_edit_rgb.items():
            print( '\'{}\': ({:>3.0f}./255,{:>3.0f}./255,{:>3.0f}./255),'.format(k,c[0]*255,c[1]*255,c[2]*255))
           
        fig = plt.figure()
        ax1 = fig.add_subplot(221)
        plot_colors(ax1,colors_rgb,order)
        plt.title('original')
        
        ax2 = fig.add_subplot(223)
        plot_colors(ax2,colors_gray_rgb,order)

        ax3 = fig.add_subplot(222)
        plot_colors(ax3,colors_edit_rgb,order)
        plt.title('edited')
        
        ax4 = fig.add_subplot(224)
        plot_colors(ax4,colors_edit_gray_rgb,order)  
          
      
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
    linearize_grayscale(colors_rgb,0.20,0.90,order=order,plot=True)

    print('\nlight colors:')
    linearize_grayscale(colors_rgb,0.40,0.95,order=order,plot=True)

    
    plt.show()
