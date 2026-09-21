import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QPushButton, QVBoxLayout,
    QFileDialog, QLabel, 
    QHBoxLayout, QSpacerItem, 
    QSizePolicy, QMainWindow, 
)
from settings import Preference
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


# Specification de la fénétre
class ModFramework (QMainWindow):
    def __init__(self):

        super().__init__()
        self.setWindowTitle("Rabbids Mod Framework")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(
        QIcon("/images/Rabbids Mod Framework icon.png")
        )

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        label = QLabel("Please select a file, you want to replace")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        
        menu_bar = self.menuBar()                          
        file_menu = menu_bar.addMenu("File")

        ouvrir_action = file_menu.addAction("Open")
        ouvrir_action.triggered.connect(self.open_file)

        ouvrir_action = file_menu.addAction("Compile")
        ouvrir_action.triggered.connect(self.open_file)

        quitter_action = file_menu.addAction("Quitter")
        quitter_action.triggered.connect(self.close)

        options_menu = menu_bar.addMenu("Settings")

        son_action = options_menu.addAction("Preference")
        son_action.triggered.connect(self.open_preference)

        aide_menu = menu_bar.addMenu("Help")
        aide_menu.addAction("À propos")

        aide_menu = menu_bar.addMenu("About Us")
        aide_menu.addAction("À propos")

        central_widget.setLayout(layout)

    def open_file(self):
      file, _ = QFileDialog.getOpenFileName(self, "Choose a file", ".", "Big File (*.bf *.)")

    def open_preference(self):
      self.preference = Preference()
      self.preference.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModFramework()
    window.show()
    sys.exit(app.exec_())
