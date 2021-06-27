import sys
from PyQt5.QtCore import Qt, QSignalMapper
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.window().setStyleSheet("background-color: #D3BDE9;"
                                    "border-width: 2px;"
                                    "border-radius: 10px;"
                                    "border-color: beige;"
                                    )
        grid = QGridLayout(self)
        mapper = QSignalMapper(self)

        buttons = (
            ('(', ')', '<-', 'CLR'),
            ('1', '2', '3', '+'),
            ('4', '5', '6', '-'),
            ('7', '8', '9', '*'),
            ('0', '.', '=', '/'),
        )
        self.line = QLineEdit()
        self.line.setAlignment(Qt.AlignRight)
        font = self.line.font()
        font.setPointSize(30)
        self.line.setFont(font)
        self.line.setStyleSheet("background-color: #D3BDE9;"
                                    "border-style: outset;"
                                    "border-width: 2px;"
                                    "border-radius: 10px;"
                                    "border-color: beige;"
                                    "font: bold 30px;"
                                    "min-width: 10em;"

                                    )
        grid.addWidget(self.line, 0, 0, 1, 4)

        for row in range(5):
            for col in range(4):
                button = QPushButton(buttons[row][col])
                button.setFont(font)
                button.setStyleSheet("""
                                    QPushButton{
                                    background-color: #7F4CB2;
                                    border-style: outset;
                                    border-width: 2px;
                                    border-radius: 10px;
                                    border-color: beige;
                                    font: bold 20px;
                                    padding: 15px}
                                    QPushButton:pressed{background-color: white;}
                                    """)

                grid.addWidget(button, row + 1, col)
                button.clicked.connect(mapper.map)
                mapper.setMapping(button, button.text())
        mapper.mapped[str].connect(self.on_mapped)
        self.errorLine = QLabel()
        font2 = self.line.font()
        font2.setPointSize(15)
        self.errorLine.setFont(font2)
        self.errorLine.setFixedHeight(25)
        grid.addWidget(self.errorLine, 6, 0, 1, 4)

    def on_mapped(self, val):
        if val == 'CLR':
            self.line.clear()
            return
        txt = self.line.text()
        if val == '=':
            try:
                self.line.setText(str(round(eval(txt), 3)))
                self.errorLine.setText('')
            except Exception:
                self.errorLine.setText(str('Я не могу это обработать'))
        elif val == '<-':
            self.line.setText(txt[:-1])
        else:
            self.line.setText(txt + val)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
