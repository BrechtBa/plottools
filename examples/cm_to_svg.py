import matplotlib.pyplot as plt
import numpy as np
import plottools as pt


# viridis
pt.cm.cm_to_svg(plt.cm.viridis,'viridis.svg')

# hot water
pt.cm.cm_to_svg(pt.cm.hotwater,'hotwater.svg',stops=5)

