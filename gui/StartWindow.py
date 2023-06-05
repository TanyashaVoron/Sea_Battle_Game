from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QPushButton, QVBoxLayout, QWidget)

from gui.MyCopy import NewCopy


class StartWindow(object):
    def __init__(self):
        self.button = NewCopy()
        self.button.name_window = "MainWindow"

    def ui(self, window, is_saved_game):
        if not window.objectName():
            window.setObjectName(u"MainWindow")
        if is_saved_game:
            window.resize(360, 230)
        else:
            window.resize(250, 150)
        window.setStyleSheet(u"\n"
                             "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.507463 rgba(28, 17, 145, 255), stop:0.935 rgba(55, 170, 239, 255));\n"
                             "")
        self.central_widget = QWidget(window)
        self.central_widget.setObjectName(u"centralwidget")

        self.layout_widget = QWidget(self.central_widget)
        self.layout_widget.setObjectName(u"layoutWidget")
        if is_saved_game:
            self.layout_widget.setGeometry(QRect(10, 10, 340, 210))
        else:
            self.layout_widget.setGeometry(QRect(10, 10, 234, 120))

        self.vertical_layout = QVBoxLayout(self.layout_widget)
        self.vertical_layout.setObjectName(u"verticalLayout")
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)

        if is_saved_game:
            self.button_save = QPushButton(self.layout_widget)
            self.button.new_button(self.button_save, "восстановить игру")
            self.vertical_layout.addWidget(self.button_save)

        self.button_start = QPushButton(self.layout_widget)
        self.button.new_button(self.button_start, "start")
        self.vertical_layout.addWidget(self.button_start)

        self.button_exit = QPushButton(self.layout_widget)
        self.button.new_button(self.button_exit, "exit")
        self.vertical_layout.addWidget(self.button_exit)

        window.setCentralWidget(self.central_widget)
        window.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sea buttle game", None))
        QMetaObject.connectSlotsByName(window)
