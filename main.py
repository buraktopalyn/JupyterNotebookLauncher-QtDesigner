import subprocess
import warnings
import sys
import os

from ui_appFrame import *  


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)  # pencere başlığını kaldır
        self.setAttribute(Qt.WA_TranslucentBackground)  # şeffaf pencere
        self.setWindowIcon(QIcon('images/logo.jpg'))  # logo
        self.setWindowTitle('jupyter notebook')

        self.ui.close.clicked.connect(lambda: self.closeapp())
        self.ui.mini.clicked.connect(lambda: self.showMinimized())
        self.flag = False
        self.ui.startstop.clicked.connect(lambda: self.control())

        warnings.filterwarnings("ignore")


        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.title.mouseMoveEvent = moveWindow


    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def closeapp(self):
        self.shutdownjupyter()
        sys.exit()

    def control(self):
        if self.flag:
            self.shutdownjupyter()
            self.flag = False
        else:
            self.runjupyter()
            self.flag = True

    def runjupyter(self):
        user = os.path.expanduser("~")
        baslat_komutu = f'cd {user} && jupyter notebook'
        subprocess.Popen(baslat_komutu, shell=True)
        self.ui.startstop.setText('DURDUR')

    def shutdownjupyter(self):
        sonlandir_komutu = 'taskkill /IM jupyter-notebook.exe /F'
        subprocess.call(sonlandir_komutu, shell=True)
        self.ui.startstop.setText('BASLAT')


# UYGULMAYI ÇALIŞTIRMA
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
