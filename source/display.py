# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Robert\Repos\OurRecipes\source\display.ui'
#
# Created: Wed Apr 18 22:50:52 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(1097, 649)
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.table_Recipes = QtGui.QTableWidget(self.tab_2)
        self.table_Recipes.setGeometry(QtCore.QRect(340, 40, 721, 531))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.table_Recipes.setFont(font)
        self.table_Recipes.setObjectName("table_Recipes")
        self.table_Recipes.setColumnCount(7)
        self.table_Recipes.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table_Recipes.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_Recipes.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_Recipes.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.table_Recipes.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.table_Recipes.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.table_Recipes.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.table_Recipes.setHorizontalHeaderItem(6, item)
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(50, 20, 46, 13))
        self.label.setObjectName("label")
        self.combo_Chef = QtGui.QComboBox(self.tab_2)
        self.combo_Chef.setGeometry(QtCore.QRect(90, 20, 141, 22))
        self.combo_Chef.setObjectName("combo_Chef")
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 51, 16))
        self.label_2.setObjectName("label_2")
        self.combo_Appliance = QtGui.QComboBox(self.tab_2)
        self.combo_Appliance.setGeometry(QtCore.QRect(90, 50, 141, 22))
        self.combo_Appliance.setObjectName("combo_Appliance")
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(120, 90, 81, 16))
        self.label_3.setObjectName("label_3")
        self.spin_PrepLow = QtGui.QSpinBox(self.tab_2)
        self.spin_PrepLow.setGeometry(QtCore.QRect(30, 90, 71, 22))
        self.spin_PrepLow.setMaximum(9999)
        self.spin_PrepLow.setObjectName("spin_PrepLow")
        self.spin_PrepHigh = QtGui.QSpinBox(self.tab_2)
        self.spin_PrepHigh.setGeometry(QtCore.QRect(210, 90, 71, 22))
        self.spin_PrepHigh.setMaximum(9999)
        self.spin_PrepHigh.setProperty("value", 9999)
        self.spin_PrepHigh.setObjectName("spin_PrepHigh")
        self.spin_CookHigh = QtGui.QSpinBox(self.tab_2)
        self.spin_CookHigh.setGeometry(QtCore.QRect(210, 130, 71, 22))
        self.spin_CookHigh.setMaximum(9999)
        self.spin_CookHigh.setProperty("value", 9999)
        self.spin_CookHigh.setObjectName("spin_CookHigh")
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(120, 130, 81, 16))
        self.label_4.setObjectName("label_4")
        self.spin_CookLow = QtGui.QSpinBox(self.tab_2)
        self.spin_CookLow.setGeometry(QtCore.QRect(30, 130, 71, 22))
        self.spin_CookLow.setMaximum(9999)
        self.spin_CookLow.setObjectName("spin_CookLow")
        self.list_IngredientsFilter = QtGui.QListWidget(self.tab_2)
        self.list_IngredientsFilter.setGeometry(QtCore.QRect(20, 230, 291, 341))
        self.list_IngredientsFilter.setObjectName("list_IngredientsFilter")
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(690, 20, 46, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(130, 210, 61, 16))
        self.label_6.setObjectName("label_6")
        self.button_Search = QtGui.QPushButton(self.tab_2)
        self.button_Search.setGeometry(QtCore.QRect(240, 580, 71, 23))
        self.button_Search.setObjectName("button_Search")
        self.button_ViewIngredients = QtGui.QPushButton(self.tab_2)
        self.button_ViewIngredients.setGeometry(QtCore.QRect(884, 580, 101, 23))
        self.button_ViewIngredients.setObjectName("button_ViewIngredients")
        self.button_ViewRecipes = QtGui.QPushButton(self.tab_2)
        self.button_ViewRecipes.setGeometry(QtCore.QRect(990, 580, 75, 23))
        self.button_ViewRecipes.setObjectName("button_ViewRecipes")
        self.button_EditRecipe = QtGui.QPushButton(self.tab_2)
        self.button_EditRecipe.setGeometry(QtCore.QRect(450, 580, 101, 23))
        self.button_EditRecipe.setObjectName("button_EditRecipe")
        self.button_DeleteRecipe = QtGui.QPushButton(self.tab_2)
        self.button_DeleteRecipe.setGeometry(QtCore.QRect(340, 580, 101, 23))
        self.button_DeleteRecipe.setObjectName("button_DeleteRecipe")
        self.spin_CookLow_3 = QtGui.QSpinBox(self.tab_2)
        self.spin_CookLow_3.setGeometry(QtCore.QRect(30, 170, 71, 22))
        self.spin_CookLow_3.setMaximum(9999)
        self.spin_CookLow_3.setObjectName("spin_CookLow_3")
        self.spin_CookHigh_2 = QtGui.QSpinBox(self.tab_2)
        self.spin_CookHigh_2.setGeometry(QtCore.QRect(210, 170, 71, 22))
        self.spin_CookHigh_2.setMaximum(9999)
        self.spin_CookHigh_2.setProperty("value", 9999)
        self.spin_CookHigh_2.setObjectName("spin_CookHigh_2")
        self.label_14 = QtGui.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(120, 170, 81, 16))
        self.label_14.setObjectName("label_14")
        TabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.text_output = QtGui.QTextBrowser(self.tab_3)
        self.text_output.setGeometry(QtCore.QRect(380, 40, 691, 561))
        self.text_output.setObjectName("text_output")
        self.list_Viewing = QtGui.QListWidget(self.tab_3)
        self.list_Viewing.setGeometry(QtCore.QRect(30, 40, 331, 561))
        self.list_Viewing.setObjectName("list_Viewing")
        self.label_viewing = QtGui.QLabel(self.tab_3)
        self.label_viewing.setGeometry(QtCore.QRect(30, 20, 46, 13))
        self.label_viewing.setObjectName("label_viewing")
        self.label_Output = QtGui.QLabel(self.tab_3)
        self.label_Output.setGeometry(QtCore.QRect(380, 20, 51, 16))
        self.label_Output.setObjectName("label_Output")
        TabWidget.addTab(self.tab_3, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.combo_ApplianceNewRecipe = QtGui.QComboBox(self.tab)
        self.combo_ApplianceNewRecipe.setGeometry(QtCore.QRect(80, 440, 141, 22))
        self.combo_ApplianceNewRecipe.setObjectName("combo_ApplianceNewRecipe")
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(40, 410, 46, 13))
        self.label_8.setObjectName("label_8")
        self.spin_CookNewRecipe = QtGui.QSpinBox(self.tab)
        self.spin_CookNewRecipe.setGeometry(QtCore.QRect(80, 520, 71, 22))
        self.spin_CookNewRecipe.setObjectName("spin_CookNewRecipe")
        self.combo_ChefNewRecipe = QtGui.QComboBox(self.tab)
        self.combo_ChefNewRecipe.setGeometry(QtCore.QRect(80, 410, 141, 22))
        self.combo_ChefNewRecipe.setObjectName("combo_ChefNewRecipe")
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(20, 520, 61, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(20, 450, 51, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(20, 480, 61, 16))
        self.label_11.setObjectName("label_11")
        self.spin_PrepNewRecipe = QtGui.QSpinBox(self.tab)
        self.spin_PrepNewRecipe.setGeometry(QtCore.QRect(80, 480, 71, 22))
        self.spin_PrepNewRecipe.setObjectName("spin_PrepNewRecipe")
        self.label_12 = QtGui.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(40, 90, 46, 13))
        self.label_12.setObjectName("label_12")
        self.line_NameNewRecipe = QtGui.QLineEdit(self.tab)
        self.line_NameNewRecipe.setGeometry(QtCore.QRect(80, 90, 261, 20))
        self.line_NameNewRecipe.setObjectName("line_NameNewRecipe")
        self.label_13 = QtGui.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(10, 120, 61, 16))
        self.label_13.setObjectName("label_13")
        self.text_DescriptionNewRecipe = QtGui.QTextEdit(self.tab)
        self.text_DescriptionNewRecipe.setGeometry(QtCore.QRect(80, 120, 261, 271))
        self.text_DescriptionNewRecipe.setObjectName("text_DescriptionNewRecipe")
        self.spin_ServingsNewRecipe = QtGui.QSpinBox(self.tab)
        self.spin_ServingsNewRecipe.setGeometry(QtCore.QRect(80, 560, 71, 22))
        self.spin_ServingsNewRecipe.setObjectName("spin_ServingsNewRecipe")
        self.label_15 = QtGui.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(20, 560, 61, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtGui.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(370, 80, 91, 20))
        self.label_16.setObjectName("label_16")
        self.combo_IngredientTypeNewRecipe = QtGui.QComboBox(self.tab)
        self.combo_IngredientTypeNewRecipe.setGeometry(QtCore.QRect(470, 80, 231, 22))
        self.combo_IngredientTypeNewRecipe.setObjectName("combo_IngredientTypeNewRecipe")
        self.label_17 = QtGui.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(370, 30, 201, 20))
        self.label_17.setObjectName("label_17")
        self.line_IngredientAddToDB = QtGui.QLineEdit(self.tab)
        self.line_IngredientAddToDB.setGeometry(QtCore.QRect(560, 30, 241, 20))
        self.line_IngredientAddToDB.setObjectName("line_IngredientAddToDB")
        self.button_AddIngredientToDB = QtGui.QPushButton(self.tab)
        self.button_AddIngredientToDB.setGeometry(QtCore.QRect(1000, 40, 31, 23))
        self.button_AddIngredientToDB.setObjectName("button_AddIngredientToDB")
        self.label_18 = QtGui.QLabel(self.tab)
        self.label_18.setGeometry(QtCore.QRect(370, 330, 51, 16))
        self.label_18.setObjectName("label_18")
        self.text_NewStep = QtGui.QTextEdit(self.tab)
        self.text_NewStep.setGeometry(QtCore.QRect(430, 330, 601, 41))
        self.text_NewStep.setObjectName("text_NewStep")
        self.label_19 = QtGui.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(350, 380, 101, 20))
        self.label_19.setObjectName("label_19")
        self.button_AddNewStep = QtGui.QPushButton(self.tab)
        self.button_AddNewStep.setGeometry(QtCore.QRect(1040, 340, 31, 23))
        self.button_AddNewStep.setObjectName("button_AddNewStep")
        self.label_20 = QtGui.QLabel(self.tab)
        self.label_20.setGeometry(QtCore.QRect(370, 120, 61, 20))
        self.label_20.setObjectName("label_20")
        self.combo_UnitTypeNewRecipe = QtGui.QComboBox(self.tab)
        self.combo_UnitTypeNewRecipe.setGeometry(QtCore.QRect(470, 120, 111, 22))
        self.combo_UnitTypeNewRecipe.setObjectName("combo_UnitTypeNewRecipe")
        self.combo_UnitNewRecipe = QtGui.QComboBox(self.tab)
        self.combo_UnitNewRecipe.setGeometry(QtCore.QRect(470, 160, 111, 22))
        self.combo_UnitNewRecipe.setObjectName("combo_UnitNewRecipe")
        self.label_21 = QtGui.QLabel(self.tab)
        self.label_21.setGeometry(QtCore.QRect(370, 160, 41, 20))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtGui.QLabel(self.tab)
        self.label_22.setGeometry(QtCore.QRect(370, 200, 51, 20))
        self.label_22.setObjectName("label_22")
        self.table_AddedIngredients = QtGui.QTableWidget(self.tab)
        self.table_AddedIngredients.setGeometry(QtCore.QRect(720, 100, 351, 171))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.table_AddedIngredients.setFont(font)
        self.table_AddedIngredients.setObjectName("table_AddedIngredients")
        self.table_AddedIngredients.setColumnCount(3)
        self.table_AddedIngredients.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table_AddedIngredients.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_AddedIngredients.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_AddedIngredients.setHorizontalHeaderItem(2, item)
        self.button_RemoveIngredient = QtGui.QPushButton(self.tab)
        self.button_RemoveIngredient.setGeometry(QtCore.QRect(720, 280, 101, 23))
        self.button_RemoveIngredient.setObjectName("button_RemoveIngredient")
        self.label_23 = QtGui.QLabel(self.tab)
        self.label_23.setGeometry(QtCore.QRect(850, 80, 101, 20))
        self.label_23.setObjectName("label_23")
        self.double_AmountNewRecipe = QtGui.QDoubleSpinBox(self.tab)
        self.double_AmountNewRecipe.setGeometry(QtCore.QRect(470, 200, 81, 22))
        self.double_AmountNewRecipe.setMaximum(9999.99)
        self.double_AmountNewRecipe.setObjectName("double_AmountNewRecipe")
        self.pushButton_5 = QtGui.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(370, 250, 111, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.button_DeleteStep = QtGui.QPushButton(self.tab)
        self.button_DeleteStep.setGeometry(QtCore.QRect(430, 580, 81, 23))
        self.button_DeleteStep.setObjectName("button_DeleteStep")
        self.button_MoveStepUp = QtGui.QPushButton(self.tab)
        self.button_MoveStepUp.setGeometry(QtCore.QRect(990, 580, 81, 23))
        self.button_MoveStepUp.setObjectName("button_MoveStepUp")
        self.button_MoveStepDown = QtGui.QPushButton(self.tab)
        self.button_MoveStepDown.setGeometry(QtCore.QRect(880, 580, 101, 23))
        self.button_MoveStepDown.setObjectName("button_MoveStepDown")
        self.table_CurrentSteps = QtGui.QTableWidget(self.tab)
        self.table_CurrentSteps.setGeometry(QtCore.QRect(430, 380, 641, 191))
        self.table_CurrentSteps.setObjectName("table_CurrentSteps")
        self.table_CurrentSteps.setColumnCount(2)
        self.table_CurrentSteps.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table_CurrentSteps.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_CurrentSteps.setHorizontalHeaderItem(1, item)
        self.table_CurrentSteps.horizontalHeader().setDefaultSectionSize(30)
        self.table_CurrentSteps.horizontalHeader().setMinimumSectionSize(30)
        self.table_CurrentSteps.horizontalHeader().setStretchLastSection(True)
        self.table_CurrentSteps.verticalHeader().setStretchLastSection(False)
        self.combo_UnitTypeNewRecipe_2 = QtGui.QComboBox(self.tab)
        self.combo_UnitTypeNewRecipe_2.setGeometry(QtCore.QRect(890, 10, 91, 22))
        self.combo_UnitTypeNewRecipe_2.setObjectName("combo_UnitTypeNewRecipe_2")
        self.label_24 = QtGui.QLabel(self.tab)
        self.label_24.setGeometry(QtCore.QRect(820, 10, 61, 20))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtGui.QLabel(self.tab)
        self.label_25.setGeometry(QtCore.QRect(840, 40, 41, 20))
        self.label_25.setObjectName("label_25")
        self.combo_UnitNewRecipe_2 = QtGui.QComboBox(self.tab)
        self.combo_UnitNewRecipe_2.setGeometry(QtCore.QRect(890, 40, 91, 22))
        self.combo_UnitNewRecipe_2.setObjectName("combo_UnitNewRecipe_2")
        self.button_Save = QtGui.QPushButton(self.tab)
        self.button_Save.setGeometry(QtCore.QRect(10, 10, 81, 23))
        self.button_Save.setObjectName("button_Save")
        self.label_SaveType = QtGui.QLabel(self.tab)
        self.label_SaveType.setGeometry(QtCore.QRect(100, 20, 91, 16))
        self.label_SaveType.setObjectName("label_SaveType")
        self.button_Discard = QtGui.QPushButton(self.tab)
        self.button_Discard.setGeometry(QtCore.QRect(10, 50, 81, 23))
        self.button_Discard.setObjectName("button_Discard")
        self.label_SaveType_2 = QtGui.QLabel(self.tab)
        self.label_SaveType_2.setGeometry(QtCore.QRect(100, 50, 261, 16))
        self.label_SaveType_2.setObjectName("label_SaveType_2")
        TabWidget.addTab(self.tab, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(2)
        QtCore.QObject.connect(self.button_Search, QtCore.SIGNAL("clicked()"), TabWidget.clickedSearch)
        QtCore.QObject.connect(self.button_DeleteRecipe, QtCore.SIGNAL("clicked()"), TabWidget.clickedDeleteRecipe)
        QtCore.QObject.connect(self.button_EditRecipe, QtCore.SIGNAL("clicked()"), TabWidget.clickedEditRecipe)
        QtCore.QObject.connect(self.button_ViewIngredients, QtCore.SIGNAL("clicked()"), TabWidget.clickedViewIngredients)
        QtCore.QObject.connect(self.button_ViewRecipes, QtCore.SIGNAL("clicked()"), TabWidget.clickedViewRecipes)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL("clicked()"), TabWidget.clickedAddIngredient)
        QtCore.QObject.connect(self.button_AddIngredientToDB, QtCore.SIGNAL("clicked()"), TabWidget.clickedIngredientAddToDatabase)
        QtCore.QObject.connect(self.button_RemoveIngredient, QtCore.SIGNAL("clicked()"), TabWidget.clickedRemoveIngredient)
        QtCore.QObject.connect(self.button_AddNewStep, QtCore.SIGNAL("clicked()"), TabWidget.clickedAddStep)
        QtCore.QObject.connect(self.button_DeleteStep, QtCore.SIGNAL("clicked()"), TabWidget.clickedDeleteStep)
        QtCore.QObject.connect(self.button_MoveStepDown, QtCore.SIGNAL("clicked()"), TabWidget.clickedMoveStepDown)
        QtCore.QObject.connect(self.button_MoveStepUp, QtCore.SIGNAL("clicked()"), TabWidget.clickedMoveStepUp)
        QtCore.QObject.connect(self.button_Save, QtCore.SIGNAL("clicked()"), TabWidget.clickedSave)
        QtCore.QObject.connect(self.button_Discard, QtCore.SIGNAL("clicked()"), TabWidget.clickedDiscard)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(QtGui.QApplication.translate("TabWidget", "TabWidget", None, QtGui.QApplication.UnicodeUTF8))
        self.table_Recipes.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("TabWidget", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.table_Recipes.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("TabWidget", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.table_Recipes.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("TabWidget", "Chef", None, QtGui.QApplication.UnicodeUTF8))
        self.table_Recipes.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("TabWidget", "Appliance", None, QtGui.QApplication.UnicodeUTF8))
        self.table_Recipes.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("TabWidget", "Prep Time", None, QtGui.QApplication.UnicodeUTF8))
        self.table_Recipes.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("TabWidget", "Cook Time", None, QtGui.QApplication.UnicodeUTF8))
        self.table_Recipes.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("TabWidget", "Servings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("TabWidget", "Chef:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("TabWidget", "Appliance:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("TabWidget", "<  Prep Time <", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("TabWidget", "<  Cook Time <", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("TabWidget", "Recipes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("TabWidget", "Ingredients", None, QtGui.QApplication.UnicodeUTF8))
        self.button_Search.setText(QtGui.QApplication.translate("TabWidget", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.button_ViewIngredients.setText(QtGui.QApplication.translate("TabWidget", "View Ingredients ", None, QtGui.QApplication.UnicodeUTF8))
        self.button_ViewRecipes.setText(QtGui.QApplication.translate("TabWidget", "View Recipes", None, QtGui.QApplication.UnicodeUTF8))
        self.button_EditRecipe.setText(QtGui.QApplication.translate("TabWidget", "Edit Recipe", None, QtGui.QApplication.UnicodeUTF8))
        self.button_DeleteRecipe.setText(QtGui.QApplication.translate("TabWidget", "Delete Recipe", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("TabWidget", "<  Servings <", None, QtGui.QApplication.UnicodeUTF8))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("TabWidget", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.label_viewing.setText(QtGui.QApplication.translate("TabWidget", "Viewing:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Output.setText(QtGui.QApplication.translate("TabWidget", "Recipes:", None, QtGui.QApplication.UnicodeUTF8))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("TabWidget", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("TabWidget", "Chef:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("TabWidget", "Cook Time: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("TabWidget", "Appliance:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("TabWidget", "Prep Time:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("TabWidget", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("TabWidget", "Description:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("TabWidget", "Servings:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("TabWidget", "Ingredient Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("TabWidget", "Add new ingredient type to database:", None, QtGui.QApplication.UnicodeUTF8))
        self.button_AddIngredientToDB.setText(QtGui.QApplication.translate("TabWidget", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("TabWidget", "New Step:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("TabWidget", "Current Steps:", None, QtGui.QApplication.UnicodeUTF8))
        self.button_AddNewStep.setText(QtGui.QApplication.translate("TabWidget", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("TabWidget", "Unit Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("TabWidget", "Unit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("TabWidget", "Amount:", None, QtGui.QApplication.UnicodeUTF8))
        self.table_AddedIngredients.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("TabWidget", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.table_AddedIngredients.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("TabWidget", "Amount", None, QtGui.QApplication.UnicodeUTF8))
        self.table_AddedIngredients.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("TabWidget", "Unit", None, QtGui.QApplication.UnicodeUTF8))
        self.button_RemoveIngredient.setText(QtGui.QApplication.translate("TabWidget", "Remove Ingredient", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("TabWidget", "Current Ingredients", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("TabWidget", "Add Ingredient", None, QtGui.QApplication.UnicodeUTF8))
        self.button_DeleteStep.setText(QtGui.QApplication.translate("TabWidget", "Delete Step", None, QtGui.QApplication.UnicodeUTF8))
        self.button_MoveStepUp.setText(QtGui.QApplication.translate("TabWidget", "Move Step Up", None, QtGui.QApplication.UnicodeUTF8))
        self.button_MoveStepDown.setText(QtGui.QApplication.translate("TabWidget", "Move Step Down", None, QtGui.QApplication.UnicodeUTF8))
        self.table_CurrentSteps.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("TabWidget", "No.", None, QtGui.QApplication.UnicodeUTF8))
        self.table_CurrentSteps.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("TabWidget", "Step", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("TabWidget", "Unit Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("TabWidget", "Unit:", None, QtGui.QApplication.UnicodeUTF8))
        self.button_Save.setText(QtGui.QApplication.translate("TabWidget", "SAVE", None, QtGui.QApplication.UnicodeUTF8))
        self.label_SaveType.setText(QtGui.QApplication.translate("TabWidget", "(As a new Recipe)", None, QtGui.QApplication.UnicodeUTF8))
        self.button_Discard.setText(QtGui.QApplication.translate("TabWidget", "Discard", None, QtGui.QApplication.UnicodeUTF8))
        self.label_SaveType_2.setText(QtGui.QApplication.translate("TabWidget", "(No changes to recipe book, start a fresh recipe)", None, QtGui.QApplication.UnicodeUTF8))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), QtGui.QApplication.translate("TabWidget", "Create/Edit", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TabWidget = QtGui.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.show()
    sys.exit(app.exec_())
