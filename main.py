import sys
from random import randrange
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.qp = QPainter()
        self.initUI()

    def initUI(self):
        self.do_paint = False
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            self.qp.begin(self)
            self.draw(self.qp)
            self.qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        r = randrange(1, 100, 1)
        x = randrange(0, 400 - r, 1)
        y = randrange(0, 300 - r, 1)

        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x, y, r, r)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = App()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
