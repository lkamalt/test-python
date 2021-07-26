from PyQt5 import QtWidgets
import sys

from myapp import MyApp

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    cd = MyApp()
    cd.show()
    app.exec_()
