import matplotlib.pyplot as plt
import plottools as pt



pt.cs.prepare_print_scan(pt.color.colors)
plt.savefig('print_scan_default.jpg')

# print the image and then scan it
pt.cs.analyse_print_scan('print_scan_default_inkjet.jpg',pt.color.colors)

pt.cs.analyse_print_scan('print_scan_default_laserjet.jpg',pt.color.colors)

plt.show()
