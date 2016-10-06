import matplotlib.pyplot as plt
import plottools as pt



pt.color.prepare_print_scan(pt.color.default.colors)
plt.savefig('print_scan_default.jpg')

# print the image and then scan it
pt.color.analyse_print_scan('print_scan_default_inkjet.jpg',pt.color.default.colors)

pt.color.analyse_print_scan('print_scan_default_laserjet.jpg',pt.color.default.colors)

plt.show()
