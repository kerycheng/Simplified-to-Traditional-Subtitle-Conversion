import sys
from PyQt5 import QtWidgets

from main import subtitle_conversion

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = subtitle_conversion()
    window.show()
    sys.exit(app.exec_())