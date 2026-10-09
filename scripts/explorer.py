import os 
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon

class ExplorerFolders(QWidget):
 def __init__(self):
        super().__init__()
        self.title = 'Projects'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

 def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.model = QFileSystemModel()
        self.model.setrootPath('')
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        
        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)
        
        self.tree.setWindowTitle("Project")
        self.tree.resize(640, 480)
        
        ShitLayout = QVBoxLayout()
        ShitLayout.addWidget(self.tree)
        self.setLayout(ShitLayout)
        
        self.show()

