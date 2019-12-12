from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.crugi = []
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawCrug(qp)
        qp.end()

    def drawCrug(self, qp):
        width = randint(50, 200)
        qp.setBrush(QColor(255, 255, 0))
        self.crugi.append((randint(width, self.width() - width), randint(width, self.height() - width), width, width))
        for crug in self.crugi:
            qp.drawEllipse(*crug)


app = QApplication([])
ex = Window()
ex.show()
app.exec_()
