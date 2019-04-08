
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QAbstractButton, QDesktopWidget
from PySide2.QtGui import QPixmap, QPainter

class PicButton(QAbstractButton):
    def __init__(self, pixmap, parent=None):
        super(PicButton, self).__init__(parent)
        self.pixmap = pixmap
        self.enter = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)

        if self.enter:
            qp = QtGui.QPainter()
            qp.begin(self)
            self.drawRectangles(qp, event.rect())
            qp.end()

    def drawRectangles(self, qp, rec):
        qp.setBrush(QtGui.QColor(000, 000, 255, 255/4))
        qp.drawRect(rec.left(), rec.top(), rec.width(), rec.height())

    def enterEvent(self, event):
        self.enter = True
        self.update()

    def leaveEvent(self, event):
        self.enter = False
        self.update()

    def sizeHint(self):
        return self.pixmap.size()