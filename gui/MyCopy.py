from PySide6.QtCore import (QCoreApplication, QRect)
from PySide6.QtGui import QFont


class NewCopy:
    def __init__(self):
        self.size = {10: 35, 15: 23, 20: 15}
        self.name_window = ''
        self.button_configuration = (u"QPushButton {\n"
                                     "color: rgb(53, 23, 99);\n"
                                     "background-color: rgb(231, 235, 235);\n"
                                     "border: 1px solid rgba(255, 255, 255, 40); \n"
                                     "border-radius: 7px;\n"
                                     "width: 230px;\n"
                                     "height: 50px;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "color: rgb(237, 241, 241);\n"
                                     "background-color: rgba(231, 235, 235, 80);\n"
                                     "}\n"
                                     "QPushButton:pressed {\n"
                                     "color: rgb(237, 241, 241);\n"
                                     "background-color: rgba(231, 235, 235, 10);\n"
                                     "}")
        self.font = QFont()
        self.font.setFamilies([u"Arial"])
        self.font.setPointSize(35)
        self.font.setBold(True)

    def new_button(self, button, text):
        button.setObjectName(text)
        button.setFont(self.font)
        button.setStyleSheet(self.button_configuration)
        button.setText(QCoreApplication.translate(self.name_window, text, None))

    def new_lable(self, lable, text, x=10, y=10, a=300, b=50, size=10):
        lable.setObjectName(text)
        lable.setGeometry(QRect(x, y, a, b))
        self.font.setPointSize(self.size[size])
        lable.setFont(self.font)
        lable.setText(QCoreApplication.translate(self.name_window, f"  {text}", None))
