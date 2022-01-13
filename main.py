import sys
from PyQt5.QtWidgets import QApplication
from MainWindows import MainWindow

# Main ouvrant simplement la fenetre principale
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()

