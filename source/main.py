import sys
from PySide.QtGui import *
import RecipeBookView

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RecipeBookView.MainWindow()

    app.exec_()
    sys.exit()