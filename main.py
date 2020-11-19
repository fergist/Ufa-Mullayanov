import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QColor, QPainter


class Ex(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.is_draw = False
        self.initUi()

    def initUi(self):
        self.pushButton.clicked.connect(self.click)

    def click(self):
        self.is_draw = True
        self.repaint()

    def paintEvent(self, event):
        if self.is_draw:
            dr = QPainter()
            dr.begin(self)
            self.draw(dr)

    def draw(self, painter):
        for i in range(randint(0, 5)):
            r = randint(0, 100)
            painter.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            painter.drawEllipse(randint(110, 580 - r), randint(30, 500 - r), r, r)


def main():
    app = QApplication(sys.argv)
    a = Ex()
    a.show()
    sys.exit(app.exec())