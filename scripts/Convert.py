import ffmpeg
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class convert(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Convert")
        self.resize(1000, 600)

        central_widget = QWidget()
        label = QLabel("(Important) you need RAD Video Tools on your computer, for convert file")
        label.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addLayout(layout)
        

