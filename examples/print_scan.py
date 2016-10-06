import matplotlib.pyplot as plt
import plottools as pt


order = {
    'k': 0,
    'p': 1,
    'b': 2,
    'r': 3,
    'g': 4,
    'o': 5,
    'y': 6
}

pt.color.prepare_print_scan(pt.color.default.colors,order=order)
plt.savefig('print_scan_default.jpg')

# print the image and then scan it
pt.color.analyse_print_scan('print_scan_default_inkjet.jpg',pt.color.default.colors,order=order)

pt.color.analyse_print_scan('print_scan_default_laserjet.jpg',pt.color.default.colors,order=order)

plt.show()
