from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt
class ITM_ArrowKey_Movement(QLineEdit): 
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Left:
            self.parent().focusPreviousChild()
        elif event.key() == Qt.Key.Key_Right:
            self.parent().focusNextChild()
        else:
            super().keyPressEvent(event)