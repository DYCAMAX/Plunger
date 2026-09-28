import ffmpeg
from PyQt5.QtWidgets import QWidget

class convert(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Convert")
        self.resize(600, 400)

        ffmpeg.input("") # Valeur défini par l'utilisateur
        ffmpeg.output("dead.bik") # valeur défini par l'utilisateur
        ffmpeg.run()

