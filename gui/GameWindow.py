from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QTimer, Qt)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QHBoxLayout)

from gui.MyCopy import NewCopy


class GameWindow(object):
    def __init__(self):
        self.my_copy = NewCopy()
        self.my_copy.name_window = "GameWindow"

    def ui(self, window, text, field, size, timer=False):
        self.window = window
        if not window.objectName():
            window.setObjectName("GameWindow")
        window.resize(1070, 900)
        window.setStyleSheet("\n"
                             "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.507463 rgba(28, 17, 145, 255), stop:0.935 rgba(55, 170, 239, 255));\n"
                             "")
        self.central_widget = QWidget(window)
        self.central_widget.setObjectName("centralwidget")

        self.layout_widget = QWidget(self.central_widget)
        self.layout_widget.setObjectName("layoutWidget")
        self.layout_widget.setGeometry(QRect(10, 10, 1050, 880))

        self.vertical_layout = QVBoxLayout(self.layout_widget)
        self.vertical_layout.setObjectName("verticalLayout")
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.text_game = QLabel(self.layout_widget)
        self.my_copy.new_lable(self.text_game, text, a=500, b=150)
        self.text_game.setAlignment(Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.text_game)

        if timer:
            self.timer_label = QLabel(self.layout_widget)
            self.timer_label.setMaximumSize(90, 50)
            self.font = QFont()
            self.font.setFamilies([u"Arial"])
            self.font.setPointSize(35)
            self.font.setBold(True)
            self.timer_label.setFont(self.font)
            self.timer = QTimer()
            self.timer.start(1000)  # 1 second
            self.horizontalLayout.addWidget(self.timer_label)
        else:
            self.button_exit_game = QPushButton(self.layout_widget)
            self.my_copy.new_button(self.button_exit_game, "ВЫХОД")
            self.button_exit_game.setMaximumSize(150, 50)
            self.horizontalLayout.addWidget(self.button_exit_game)

        self.vertical_layout.addLayout(self.horizontalLayout)

        self.field_game = QLabel(self.layout_widget)
        self.my_copy.new_lable(self.field_game, field, a=500, b=500, size=size)
        self.vertical_layout.addWidget(self.field_game)

        self.text_enter_game = QLineEdit(self.layout_widget)
        self.text_enter_game.setObjectName("text_enter_game")
        self.vertical_layout.addWidget(self.text_enter_game)

        self.button_enter_game = QPushButton(self.layout_widget)
        self.my_copy.new_button(self.button_enter_game, "ВВОД")
        self.vertical_layout.addWidget(self.button_enter_game)

        window.setCentralWidget(self.central_widget)
        window.setWindowTitle(QCoreApplication.translate("GameWindow", "Sea buttle game", None))
        QMetaObject.connectSlotsByName(window)
