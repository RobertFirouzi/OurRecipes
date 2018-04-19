from PySide.QtCore import *
from PySide.QtGui import *
import display


class MainWindow(QTabWidget, display.Ui_TabWidget):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        QApplication.setStyle(QStyleFactory.create("WindowsVista"))

        self.show()


    @Slot()
    def clickedSearch(self):
        pass

    @Slot()
    def clickedDeleteRecipe(self):
        pass

    @Slot()
    def clickedEditRecipe(self):
        pass

    @Slot()
    def clickedViewIngredients(self):
        pass

    @Slot()
    def clickedViewRecipes(self):
        pass

    @Slot()
    def clickedAddIngredient(self):
        pass

    @Slot()
    def clickedIngredientAddToDatabase(self):
        pass

    @Slot()
    def clickedRemoveIngredient(self):
        pass

    @Slot()
    def clickedAddStep(self):
        pass

    @Slot()
    def clickedDeleteStep(self):
        pass

    @Slot()
    def clickedMoveStepDown(self):
        pass

    @Slot()
    def clickedMoveStepUp(self):
        pass

    @Slot()
    def clickedSave(self):
        pass

    @Slot()
    def clickedDiscard(self):
        pass