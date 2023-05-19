from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit)

from gui.MyCopy import NewCopy


class WinnerWindow(object):
    def __init__(self):
        self.my_copy = NewCopy()
        self.my_copy.name_window = "WinnerWindow"

    def ui(self, window, text):
        if not window.objectName():
            window.setObjectName("WinnerWindow")
        window.resize(530, 850)
        window.setStyleSheet("\n"
                             "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.507463 rgba(28, 17, 145, 255), stop:0.935 rgba(55, 170, 239, 255));\n"
                             "")
        self.central_widget = QWidget(window)
        self.central_widget.setObjectName("centralwidget")

        self.layout_widget = QWidget(self.central_widget)
        self.layout_widget.setObjectName("layoutWidget")
        self.layout_widget.setGeometry(QRect(10, 10, 510, 830))

        self.vertical_layout = QVBoxLayout(self.layout_widget)
        self.vertical_layout.setObjectName("verticalLayout")
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)

        self.text = QLabel(self.layout_widget)
        self.my_copy.new_lable(self.text, text, a=500, b=150)
        self.vertical_layout.addWidget(self.text)

        self.button_exit = QPushButton(self.layout_widget)
        self.my_copy.new_button(self.button_exit, "выход")
        self.vertical_layout.addWidget(self.button_exit)

        window.setCentralWidget(self.central_widget)
        window.setWindowTitle(QCoreApplication.translate("WinnerWindow", "Sea buttle game", None))
        QMetaObject.connectSlotsByName(window)



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = WinnerWindow()
    ui.ui(MainWindow, '[g[g')
    MainWindow.show()
    sys.exit(app.exec())
