import subprocess
from time import sleep
from external.NWW import NWW
import PyQt5
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QPlainTextEdit,
                             QVBoxLayout, QWidget)
from PyQt5.QtCore import QProcess


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.embed_widget = None
        self.embed_window = None
        self.layout = QVBoxLayout()
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        # On instancie NWW
        self.start_process_ww()
        # On attend que la fenetre s'ouvre
        sleep(0.5)
        # On capture la fenetre une fois ouverte
        self.start_process_capture()

    @staticmethod
    def start_process_ww():
        # Meme principe qu'en java
        app = NWW.ApplicationTemplate.start(NWW.String("NasaWorldWindTemplate"), NWW.AppFrame)

    def start_process_capture(self):
        # xwininfo permet de recuperer l'id de la fenetre correspondant au titre
        proc = subprocess.Popen(["xwininfo -tree -root | grep \"NasaWorldWindTemplate\" | awk '{print $1}'"],
                                stdout=subprocess.PIPE,
                                shell=True)
        (out2, err2) = proc.communicate()

        # Recuperation de la fenetre
        self.embed_window = QtGui.QWindow.fromWinId(int(out2, 16))
        self.embed_window.setFlags(PyQt5.QtCore.Qt.FramelessWindowHint)
        self.embed_widget = QtWidgets.QWidget.createWindowContainer(self.embed_window)
        self.embed_widget.setAttribute(PyQt5.QtCore.Qt.WA_DeleteOnClose
                                       & PyQt5.QtCore.Qt.WA_NativeWindow
                                       & PyQt5.QtCore.Qt.WA_NoSystemBackground)
        self.embed_widget.setMinimumHeight(800)
        self.embed_widget.setMinimumWidth(1400)
        self.layout.addWidget(self.embed_widget)
        self.embed_widget.show()
