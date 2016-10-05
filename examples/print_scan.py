import matplotlib.pyplot as plt
import plottools as pt


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

pt.color.prepare_print_scan(pt.color.default.colors,order=order)
plt.savefig('print_color_default.jpg')


pt.color.analyse_print_scan('scan_color_default.jpg',pt.color.default.colors,order=order)

plt.show()
