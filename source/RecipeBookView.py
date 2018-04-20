from PySide.QtCore import *
from PySide.QtGui import *
import display
from recipe_model import *

#TODO chefs not an enum, just a string
#TODO appliace/chef add to database and pull by ID
#TODO chef and appliance combo,load from DB

class ApplianceEnum(Enum):
    NONE = 0
    NA = 1
    OVEN = 2
    COOKTOP = 3
    CROCKPOT = 4
    GRILL = 5
    OTHER = 6

APPLIANCE_NAME = {0: 'None',
                  1: 'NA',
                  2: 'Oven',
                  3: 'Cooktop',
                  4: 'Crockpot',
                  5: 'Grill',
                  6: 'Other'}

class MainWindow(QTabWidget, display.Ui_TabWidget):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        QApplication.setStyle(QStyleFactory.create("Plastique"))

        self.recipeBook = RecipeBookModel()
        self.recipeBook.loadRecipes()
        self.currentRecipes = self.recipeBook.getRecipes(RecipeFilter()) #initialize showing all recipes
        self.updateRecipesView()

        self.setupTables()
        self.show()

    def setupTables(self):
        self.table_Recipes.setColumnWidth(0, 25)
        self.table_Recipes.setColumnWidth(1, 275)
        self.table_Recipes.setColumnWidth(2, 110)
        self.table_Recipes.setColumnWidth(3, 110)
        self.table_Recipes.setColumnWidth(4, 62)
        self.table_Recipes.setColumnWidth(5, 62)
        self.table_Recipes.setColumnWidth(6, 62)

    def updateRecipesView(self):
        #self.table_Recipes
        self.table_Recipes.setRowCount(0)
        for recipe in self.currentRecipes:
            self.table_Recipes.insertRow(0)
            #select checkbox
            checkBoxSelect = QCheckBox()
            checkBoxSelect.setObjectName(str(recipe.id))
            self.table_Recipes.setCellWidget(0, 0, checkBoxSelect)
            #name
            itemName = QTableWidgetItem()
            itemName.setText(recipe.name)
            itemName.setFlags(Qt.ItemIsEnabled)  # makes the column not modifiable
            self.table_Recipes.setItem(0, 1, itemName)
            #chef
            if recipe.chefEnum == ChefEnum.ASHLEY:
                chef = 'Ashley'
            elif recipe.chefEnum == ChefEnum.ROBERT:
                chef = 'Robert'
            else:
                chef = 'NA'

            itemChef = QTableWidgetItem()
            itemChef.setText(chef)
            itemChef.setFlags(Qt.ItemIsEnabled)
            self.table_Recipes.setItem(0, 2, itemChef)
            #appliance
            itemAppl = QTableWidgetItem()
            itemAppl.setText(APPLIANCE_NAME[recipe.applianceEnum.value])
            itemAppl.setFlags(Qt.ItemIsEnabled)
            self.table_Recipes.setItem(0, 3, itemAppl)
            #Prep
            itemPrep = QTableWidgetItem()
            itemPrep.setText(str(recipe.prepTime))
            itemPrep.setFlags(Qt.ItemIsEnabled)
            self.table_Recipes.setItem(0, 4, itemPrep)
            #Cook
            itemCook = QTableWidgetItem()
            itemCook.setText(str(recipe.cookTime))
            itemCook.setFlags(Qt.ItemIsEnabled)
            self.table_Recipes.setItem(0, 5, itemCook)
            #Servings
            itemServe = QTableWidgetItem()
            itemServe.setText(str(recipe.servings))
            itemServe.setFlags(Qt.ItemIsEnabled)
            self.table_Recipes.setItem(0, 6, itemServe)


    @Slot()
    def clickedSearch(self):
        if self.combo_Chef.currentText() == 'Ashley':
            chef = ChefEnum.ASHLEY
        elif self.combo_Chef.currentText() == 'Robert':
            chef = ChefEnum.ROBERT
        else:
            chef = ChefEnum.NA

        if self.combo_Appliance.currentText() == 'None':
            appl = ApplianceEnum.NONE
        elif self.combo_Appliance.currentText() == 'Oven':
            appl = ApplianceEnum.OVEN
        elif self.combo_Appliance.currentText() == 'Cooktop':
            appl = ApplianceEnum.COOKTOP
        elif self.combo_Appliance.currentText() == 'Crockpot':
            appl = ApplianceEnum.CROCKPOT
        elif self.combo_Appliance.currentText() == 'Grill':
            appl = ApplianceEnum.GRILL
        elif self.combo_Appliance.currentText() == 'Other':
            appl = ApplianceEnum.OTHER
        else:
            appl = ApplianceEnum.NA


        filter = RecipeFilter(chef,
                              appl,
                              [int(self.spin_PrepLow.value()), int(self.spin_PrepHigh.value())],
                              [int(self.spin_CookLow.value()), int(self.spin_CookHigh.value())],
                              [int(self.spin_ServeLow.value()), int(self.spin_ServeHigh.value())],
                              [])
        self.currentRecipes = self.recipeBook.getRecipes(filter)
        self.updateRecipesView()

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