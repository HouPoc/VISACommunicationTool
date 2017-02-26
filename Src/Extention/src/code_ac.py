from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


def search (key):
    result = None
    return result


def get_data(model):
    # Searching through the Doc
    # Result shows in a dictionary structure
    result = {"alpha": 0, "apple": 1, "agree": 2}
    icon_address = ['..\..\Src\Img\A.png', '..\..\Src\Img\E.png','..\..\Src\Img\O.png']
    index = 0;
    for cmd, value in result.items():
        item = QStandardItem(cmd)
        item.setIcon(QIcon(icon_address[value]))
        model.insertRow(index, item)
        index += 1


class CodeAC:
    def __init__(self, input_line):
        self.completer = QCompleter()
        input_line.setCompleter(self.completer)
        self.model = QStandardItemModel()
        self.input_line = input_line;

    def active_script(self):
        get_data(self.model)
        self.completer.setModel(self.model)
        self.completer.activated.connect(self.tip_balloon)

    def tip_balloon(self, text):
        # selected highlight item
        self.input_line.setToolTip(text)


