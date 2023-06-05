from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLabel)

from gui.MyCopy import NewCopy


class SaveWindow(object):
    def __init__(self):
        self.my_copy = NewCopy()
        self.my_copy.name_window = "SaveWindow"

    def ui(self, window):
        if not window.objectName():
            window.setObjectName(u"SaveWindow")
        window.resize(340, 150)
        window.setStyleSheet(u"\n"
                             "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.507463 rgba(28, 17, 145, 255), stop:0.935 rgba(55, 170, 239, 255));\n"
                             "")
        self.central_widget = QWidget(window)
        self.central_widget.setObjectName("centralwidget")

        self.layout_widget = QWidget(self.central_widget)
        self.layout_widget.setObjectName("layoutWidget")
        self.layout_widget.setGeometry(QRect(10, 10, 320, 120))

        self.vertical_layout = QVBoxLayout(self.layout_widget)
        self.vertical_layout.setObjectName("verticalLayout")
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)

        self.field_game = QLabel(self.layout_widget)
        self.my_copy.new_lable(self.field_game, 'сохранить игру?', a=200, b=50)
        self.vertical_layout.addWidget(self.field_game)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName('horizontalLayout')

        self.button_yes = QPushButton(self.layout_widget)
        self.my_copy.new_button(self.button_yes, 'да')
        self.vertical_layout.addWidget(self.button_yes)

        self.button_no = QPushButton(self.layout_widget)
        self.my_copy.new_button(self.button_no, 'нет')
        self.vertical_layout.addWidget(self.button_no)

        self.horizontalLayout.addWidget(self.button_yes)
        self.horizontalLayout.addWidget(self.button_no)

        self.vertical_layout.addLayout(self.horizontalLayout)

        window.setCentralWidget(self.central_widget)
        window.setWindowTitle(QCoreApplication.translate('MainWindow', 'Sea buttle game', None))
        QMetaObject.connectSlotsByName(window)
