from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1164, 905)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(584, 430, 31, 23))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.crugi = []
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawCrug(qp)
        qp.end()

    def drawCrug(self, qp):
        width = randint(50, 200)
        a = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.crugi.append(((randint(width, self.width() - width), randint(width, self.height() - width), width, width), a))
        for crug, a in self.crugi:
            qp.setBrush(a)
            qp.drawEllipse(*crug)


app = QApplication([])
ex = Window()
ex.show()
app.exec_()
