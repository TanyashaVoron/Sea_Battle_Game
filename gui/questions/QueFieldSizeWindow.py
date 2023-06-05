from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QPushButton, QVBoxLayout, QWidget, QLabel)

from gui.MyCopy import NewCopy


class FieldSizeWindow(object):
    def __init__(self):
        self.my_copy = NewCopy()
        self.my_copy.name_window = "fieldSizeWindow"

    def ui(self, window):
        if not window.objectName():
            window.setObjectName("fieldSizeWindow")
        window.resize(320, 200)
        window.setStyleSheet("\n"
                             "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.507463 rgba(28, 17, 145, 255), stop:0.935 rgba(55, 170, 239, 255));\n"
                             "")
        self.central_widget = QWidget(window)
        self.central_widget.setObjectName("centralwidget")

        self.que = QLabel(self.central_widget)
        self.my_copy.new_lable(self.que, 'pазмер поля')

        self.layout_widget = QWidget(self.central_widget)
        self.layout_widget.setObjectName("layoutWidget")
        self.layout_widget.setGeometry(QRect(10, 60, 300, 120))

        self.vertical_layout = QVBoxLayout(self.layout_widget)
        self.vertical_layout.setObjectName("verticalLayout")
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)

        self.button_size_field_10 = QPushButton(self.layout_widget)
        self.my_copy.new_button(self.button_size_field_10, "10")
        self.vertical_layout.addWidget(self.button_size_field_10)

        self.button_size_field_15 = QPushButton(self.layout_widget)
        self.my_copy.new_button(self.button_size_field_15, "15")
        self.vertical_layout.addWidget(self.button_size_field_15)

        self.button_size_field_20 = QPushButton(self.layout_widget)
        self.my_copy.new_button(self.button_size_field_20, "20")
        self.vertical_layout.addWidget(self.button_size_field_20)

        window.setCentralWidget(self.central_widget)
        window.setWindowTitle(QCoreApplication.translate("fieldSizeWindow", "Sea buttle game", None))
        QMetaObject.connectSlotsByName(window)
