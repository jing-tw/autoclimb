'''
The picuture button module.
'''
from PySide2 import QtGui
from PySide2.QtWidgets import QAbstractButton
from PySide2.QtGui import QPainter

class PicButton(QAbstractButton):
    '''
    The picture button class.
    '''
    def __init__(self, pixmap, parent=None):
        super(PicButton, self).__init__(parent)
        self.pixmap = pixmap
        self.enter = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)

        if self.enter:
            #painter.begin(self)
            self.draw_rect(painter, event.rect())
            #painter.end()

    def draw_rect(self, painter, rec):
        '''
        Draw rectangle on button.
        '''
        painter.setBrush(QtGui.QColor(000, 000, 255, 255/4))
        painter.drawRect(rec.left(), rec.top(), rec.width(), rec.height())

    def enterEvent(self, event):
        del event
        self.enter = True
        self.update()

    def leaveEvent(self, event):
        del event
        self.enter = False
        self.update()

    def sizeHint(self):
        return self.pixmap.size()
        