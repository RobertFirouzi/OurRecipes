from PySide.QtCore import *
from PySide.QtGui import *
import display
from recipe_model import *

#TODO - Add types to database
#TODO - add ingredients to a grocery list


class MainWindow(QTabWidget, display.Ui_TabWidget):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        QApplication.setStyle(QStyleFactory.create("Plastique"))

        self.editingRecipe = None #If editing a recipe, reference here

        self.recipeBook = RecipeBookModel()
        self.recipeBook.loadRecipes()
        self.currentRecipes = self.recipeBook.getRecipesDict(RecipeFilter()) #initialize showing all recipes
        self.updateRecipesView()

        self.currentChefs = getChefTypesDict()
        self.currentAppliances = getApplianceTypesDict()
        self.currentIngredients = getIngredientTypesDict()
        self.currentMeasureUnits = getMeasureUnitsDict()

        self.refreshComboBoxes()
        self.refreshIngredientFilterList()

        self.setupTables()

        self.show()

    def setupTables(self):
        self.table_Recipes.setColumnWidth(0, 25)
        self.table_Recipes.setColumnWidth(1, 275)
        self.table_Recipes.setColumnWidth(2, 110)
        self.table_Recipes.setColumnWidth(3, 110)
        self.table_Recipes.setColumnWidth(4, 62)
        self.table_Recipes.setColumnWidth(5, 62)
        self.table_Recipes.setColumnWidth(5, 62)
        self.table_Recipes.setColumnWidth(6, 62)

        self.table_AddedIngredients.setColumnWidth(0,250)
        self.table_AddedIngredients.setColumnWidth(1, 55)
        self.table_AddedIngredients.setColumnWidth(2, 100)

    def refreshComboBoxes(self):
        for chef in self.currentChefs:
            self.combo_Chef.addItem(chef)
            self.combo_ChefNewRecipe.addItem(chef)

        #initialize boxes to NA
        index = self.combo_Chef.findText('NA', Qt.MatchFixedString)
        if index >= 0:
            self.combo_Chef.setCurrentIndex(index)

        index = self.combo_ChefNewRecipe.findText('NA', Qt.MatchFixedString)
        if index >= 0:
            self.combo_ChefNewRecipe.setCurrentIndex(index)

        for appliance in self.currentAppliances:
            self.combo_Appliance.addItem(appliance)
            self.combo_ApplianceNewRecipe.addItem(appliance)

        #initialize boxes to NA
        index = self.combo_Appliance.findText('NA', Qt.MatchFixedString)
        if index >= 0:
            self.combo_Appliance.setCurrentIndex(index)

        index = self.combo_ApplianceNewRecipe.findText('NA', Qt.MatchFixedString)
        if index >= 0:
            self.combo_ApplianceNewRecipe.setCurrentIndex(index)

        for ingredient in self.currentIngredients:
            self.combo_IngredientTypeNewRecipe.addItem(ingredient)

    def refreshIngredientFilterList(self):
        self.table_IngredientsFilter.setRowCount(0)

        for ingredient in self.currentIngredients:
            self.table_IngredientsFilter.insertRow(0)

            itemName = QTableWidgetItem()
            itemName.setText(ingredient)
            itemName.setFlags(Qt.ItemIsEnabled)  # makes the column not modifiable
            self.table_IngredientsFilter.setItem(0, 0, itemName)

            checkBoxSelect = QCheckBox()
            checkBoxSelect.setObjectName(ingredient)
            self.table_IngredientsFilter.setCellWidget(0, 1, checkBoxSelect)

    def updateRecipesView(self):
        #self.table_Recipes
        self.table_Recipes.setRowCount(0)
        for recipeName, recipe in self.currentRecipes.items():
            self.table_Recipes.insertRow(0)
            #select checkbox
            checkBoxSelect = QCheckBox()
            checkBoxSelect.setObjectName(recipeName)
            self.table_Recipes.setCellWidget(0, 0, checkBoxSelect)
            #name
            itemName = QTableWidgetItem()
            itemName.setText(recipe.name)
            itemName.setFlags(Qt.ItemIsEnabled)  # makes the column not modifiable
            self.table_Recipes.setItem(0, 1, itemName)
            #chef
            itemChef = QTableWidgetItem()
            itemChef.setText(recipe.chef.name)
            itemChef.setFlags(Qt.ItemIsEnabled)
            self.table_Recipes.setItem(0, 2, itemChef)
            #appliance
            itemAppl = QTableWidgetItem()
            itemAppl.setText(recipe.appliance.name)
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
        chef = self.currentChefs[self.combo_Chef.currentText()]
        appliance = self.currentAppliances[self.combo_Appliance.currentText()]
        filterIngredients = list()

        for i in range(self.table_IngredientsFilter.rowCount()):
            selectBox = self.table_IngredientsFilter.cellWidget(i, 1)
            if selectBox.checkState() == Qt.Checked:
                filterIngredients.append(self.currentIngredients[selectBox.objectName()])

        recfilter = RecipeFilter(chef,
                              appliance,
                              [int(self.spin_PrepLow.value()), int(self.spin_PrepHigh.value())],
                              [int(self.spin_CookLow.value()), int(self.spin_CookHigh.value())],
                              [int(self.spin_ServeLow.value()), int(self.spin_ServeHigh.value())],
                              filterIngredients)
        self.currentRecipes = self.recipeBook.getRecipesDict(recfilter)
        self.updateRecipesView()

    @Slot()
    def clickedDeleteRecipe(self):
        selectedRecipes = self.getSelectedRecipes()
        if len(selectedRecipes) > 1:
            self.label_deleteOne.setText('You may only delete one recipe at a time')
        elif len(selectedRecipes) == 0 :
            self.label_deleteOne.setText('You did not select any recipes to delete')
        elif len(selectedRecipes) == 1 :
            self.label_deleteOne.setText('')
            self.recipeBook.deleteRecipe(selectedRecipes[0].id)
            self.recipeBook.loadRecipes()
            self.clickedSearch()

    def getSelectedRecipes(self):
        selectedRecipes = list()

        for i in range(self.table_Recipes.rowCount()):
            selectBox = self.table_Recipes.cellWidget(i, 0)
            if selectBox.checkState() == Qt.Checked:
                selectedRecipes.append(self.currentRecipes[selectBox.objectName()])

        return selectedRecipes

    @Slot()
    def clickedEditRecipe(self):
        selectedRecipes = self.getSelectedRecipes()
        if len(selectedRecipes) > 1:
            self.label_deleteOne.setText('You may only edit one recipe at a time')
        elif len(selectedRecipes) == 0 :
            self.label_deleteOne.setText('You did not select any recipes to edit')
        elif len(selectedRecipes) == 1 :
            self.label_deleteOne.setText('')
            self.editingRecipe = self.currentRecipes[selectedRecipes[0].name]
            self.loadRecipeForEdit()

    @Slot()
    def clickedViewIngredients(self):
        pass

    @Slot()
    def clickedViewRecipes(self):
        pass

    @Slot()
    def clickedAddIngredient(self):
        ingredientType = self.currentIngredients[self.combo_IngredientTypeNewRecipe.currentText()]

        self.table_AddedIngredients.insertRow(0)

        itemName = QTableWidgetItem()
        itemName.setText(str(ingredientType.name))
        itemName.setFlags(Qt.ItemIsEnabled)  # makes the column not modifiable
        self.table_AddedIngredients.setItem(0, 0, itemName)

        itemAmount = QTableWidgetItem()
        itemAmount.setText(str(self.double_AmountNewRecipe.value()))
        itemAmount.setFlags(Qt.ItemIsEnabled)  # makes the column not modifiable
        self.table_AddedIngredients.setItem(0, 1, itemAmount)

        unitType = QTableWidgetItem()
        unitType.setText(str(ingredientType.measureUnit.name))
        unitType.setFlags(Qt.ItemIsEnabled)  # makes the column not modifiable
        self.table_AddedIngredients.setItem(0, 2, unitType)

    @Slot()
    def clickedIngredientAddToDatabase(self):
        pass

    @Slot()
    def clickedRemoveIngredient(self):
        index = self.spin_removeIngredient.value()
        tableSize = self.table_AddedIngredients.rowCount()
        if index <= tableSize:
            self.table_AddedIngredients.removeRow(index-1)

    @Slot()
    def clickedAddStep(self):
        text = self.text_NewStep.toPlainText()
        tableSize = self.table_CurrentSteps.rowCount()
        self.table_CurrentSteps.insertRow(tableSize)

        item = QTableWidgetItem()
        item.setText(text)
        item.setFlags(Qt.ItemIsEnabled)  # makes the column not modifiable
        self.table_CurrentSteps.setItem(tableSize, 0, item)

    @Slot()
    def clickedInsertStep(self):
        text = self.text_NewStep.toPlainText()
        tableSize = self.table_CurrentSteps.rowCount()
        insertPosition = self.spin_InstertSpot.value()
        if insertPosition < 0 or insertPosition > tableSize:
            insertPosition = tableSize

        self.table_CurrentSteps.insertRow(insertPosition)

        item = QTableWidgetItem()
        item.setText(text)
        item.setFlags(Qt.ItemIsEnabled)  # makes the column not modifiable
        self.table_CurrentSteps.setItem(insertPosition, 0, item)

    @Slot()
    def clickedDeleteStep(self):
        index = self.spin_removeStep.value()
        tableSize = self.table_CurrentSteps.rowCount()
        if index <= tableSize:
            self.table_CurrentSteps.removeRow(index-1)

    @Slot()
    def clickedSave(self):
        name = str(self.line_NameNewRecipe.text())
        description = str(self.text_DescriptionNewRecipe.toPlainText())
        chef = self.currentChefs[self.combo_ChefNewRecipe.currentText()]
        appliance = self.currentAppliances[self.combo_ApplianceNewRecipe.currentText()]
        prep = int(self.spin_PrepNewRecipe.value())
        cook = int(self.spin_CookNewRecipe.value())
        serve = int(self.spin_ServingsNewRecipe.value())

        ingredients = list()
        for i in range(self.table_AddedIngredients.rowCount()):
            ingtype = self.table_AddedIngredients.item(i, 0).text()
            ingredientType = self.currentIngredients[ingtype]
            amount = float(self.table_AddedIngredients.item(i, 1).text())
            ingredients.append(Ingredient(0,ingredientType,amount))

        steps = list()
        for i in range(self.table_CurrentSteps.rowCount()):
            text = self.table_CurrentSteps.item(i, 0).text()
            steps.append(RecipeStep(0,i+1,text))

        if name == '':
            self.label_uniqueName.setText('Enter a recipe name')
            return

        if self.editingRecipe is not None:
            self.recipeBook.deleteRecipe(self.editingRecipe.id)

        if not isRecipeNameInDB(name):
            recipe = Recipe(0, name, description, chef, appliance, prep, cook, serve, ingredients, steps)
            self.recipeBook.addRecipe(recipe)
            self.recipeBook.loadRecipes()
            self.clickedSearch()
            self.clearCreateForm()
        else:
            self.label_uniqueName.setText('Recipe name already in database, choose uniqe name')

    @Slot()
    def clickedDiscard(self):
        self.clearCreateForm()

    @Slot()
    def changedIngrediantAdd(self):
        ingredient = self.currentIngredients[self.combo_IngredientTypeNewRecipe.currentText()]
        self.label_measureUnit.setText(ingredient.measureUnit.name)

    def loadRecipeForEdit(self):
        self.label_SaveType.setText('Edit existing recipe: ' + str(self.editingRecipe.name))
        self.button_Save.setText('UPDATE')

        self.line_NameNewRecipe.setText(self.editingRecipe.name)
        self.text_DescriptionNewRecipe.setText(str(self.editingRecipe.description))
        self.label_uniqueName.setText('')

        index = self.combo_ChefNewRecipe.findText(self.editingRecipe.chef.name, Qt.MatchFixedString)
        if index >= 0:
            self.combo_ChefNewRecipe.setCurrentIndex(index)

        index = self.combo_ApplianceNewRecipe.findText(self.editingRecipe.appliance.name, Qt.MatchFixedString)
        if index >= 0:
            self.combo_ApplianceNewRecipe.setCurrentIndex(index)

        self.combo_IngredientTypeNewRecipe.setCurrentIndex(0)

        self.spin_PrepNewRecipe.setValue(self.editingRecipe.prepTime)
        self.spin_CookNewRecipe.setValue(self.editingRecipe.cookTime)
        self.spin_ServingsNewRecipe.setValue(self.editingRecipe.servings)
        self.double_AmountNewRecipe.setValue(0)
        self.spin_removeStep.setValue(1)
        self.spin_removeIngredient.setValue(1)

        self.table_AddedIngredients.setRowCount(0)
        self.text_NewStep.setText('')
        self.table_CurrentSteps.setRowCount(0)

        ingredientCount = 0
        for ingredient in self.editingRecipe.ingredients:
            self.table_AddedIngredients.insertRow(ingredientCount)
            itemName = QTableWidgetItem()
            itemName.setText(ingredient.ingredientType.name)
            itemName.setFlags(Qt.ItemIsEnabled)  # makes the column not modifiable
            self.table_AddedIngredients.setItem(ingredientCount, 0, itemName)

            itemAmount = QTableWidgetItem()
            itemAmount.setText(str(ingredient.amount))
            itemAmount.setFlags(Qt.ItemIsEnabled)  # makes the column not modifiable
            self.table_AddedIngredients.setItem(ingredientCount, 1, itemAmount)

            unitType = QTableWidgetItem()
            unitType.setText(ingredient.ingredientType.measureUnit.name)
            unitType.setFlags(Qt.ItemIsEnabled)  # makes the column not modifiable
            self.table_AddedIngredients.setItem(ingredientCount, 2, unitType)

            ingredientCount +=1

        stepCount = 0
        for step in self.editingRecipe.recipeSteps:
            self.table_CurrentSteps.insertRow(stepCount)
            item = QTableWidgetItem()
            item.setText(str(step.text))
            item.setFlags(Qt.ItemIsEnabled)  # makes the column not modifiable
            self.table_CurrentSteps.setItem(stepCount, 0, item)
            stepCount+=1

        self.setCurrentIndex(2) #Switch the tab to the edit tab

    def clearCreateForm(self):
        self.line_NameNewRecipe.setText('')
        self.text_DescriptionNewRecipe.setText('')
        self.label_uniqueName.setText('')

        index = self.combo_ChefNewRecipe.findText('NA', Qt.MatchFixedString)
        if index >= 0:
            self.combo_ChefNewRecipe.setCurrentIndex(index)

        index = self.combo_ApplianceNewRecipe.findText('NA', Qt.MatchFixedString)
        if index >= 0:
            self.combo_ApplianceNewRecipe.setCurrentIndex(index)

        self.combo_IngredientTypeNewRecipe.setCurrentIndex(0)

        self.spin_PrepNewRecipe.setValue(0)
        self.spin_CookNewRecipe.setValue(0)
        self.spin_ServingsNewRecipe.setValue(0)
        self.double_AmountNewRecipe.setValue(0)
        self.spin_removeStep.setValue(1)
        self.spin_removeIngredient.setValue(1)

        self.table_AddedIngredients.setRowCount(0)
        self.text_NewStep.setText('')
        self.table_CurrentSteps.setRowCount(0)

        self.editingRecipe = None
        self.label_SaveType.setText('As a new Recipe')
        self.button_Save.setText('SAVE')