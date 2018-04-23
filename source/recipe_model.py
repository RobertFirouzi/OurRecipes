from time import sleep
import database

#TODO - don't use enums for Chef/Oven.  Load the name from the data base

#Index definitions
RECIPE_ID = 0
RECIPE_NAME = 1
RECIPE_DESCRIP = 2
RECIPE_CHEF = 3
RECIPE_APPLIANCE = 4
RECIPE_PREP = 5
RECIPE_COOK = 6
RECIPE_SERVE = 7

INGREDIENT_ID = 0
INGREDIENT_TYPE_ID = 0
INGREDIENT_NAME = 1
INGREDIENT_TYPE = 2
INGREDIENT_MEAS_UNIT = 2
INGREDIENT_AMOUNT = 3

MEASURE_ID = 0
MEASURE_TYPE = 1

STEP_ID = 0
STEP_RECIPE_ID = 1
STEP_STEP_NO = 2
STEP_TEXT = 3

CHEF_ID = 0
CHEF_NAME = 1

APPLIANCE_ID = 0
APPLIANCE_NAME = 1


class Chef:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Appliance:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class MeasureUnit:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class IngredientType:
    def __init__(self, id, name, measureUnit):
        self.id = id
        self.name = name
        self.measureUnit = measureUnit

class Ingredient:
    def __init__(self, id, ingredientType, amount):
        self.id = id
        self.ingredientType = ingredientType
        self.amount = amount

class RecipeStep:
    def __init__(self, id, stepNo, text):
        self.id = id
        self.stepNo = stepNo
        self.text = text

#Class passed in from controller contains filter rules.
#Default state is to select all recipes
class RecipeFilter:
    def __init__(self,
                 chef = Chef(1, 'NA'),
                 appliance = Appliance(1,'NA'),
                 prepTime = (0,9999),
                 cookTime = (0,9999),
                 servings = (0, 9999),
                 ingredientTypes = tuple()): #list of ingredient type ID's
        self.chef = chef
        self.appliance = appliance
        self.prepTime = prepTime
        self.cookTime = cookTime
        self.servings = servings
        self.ingredientTypes = ingredientTypes

class Recipe:
    def __init__(self,
                 id,
                 name,
                 description,
                 chef,
                 appliance,
                 prepTime,
                 cookTime,
                 servings,
                 ingredients,
                 recipeSteps,
                 pictures = None):

        self.id = id
        self.name = name
        self.description = description
        self.chef = chef
        self.appliance = appliance
        self.prepTime = prepTime
        self.cookTime = cookTime
        self.servings = servings
        self.ingredients = ingredients
        self.recipeSteps = recipeSteps
        self.pictures = pictures

class RecipeBookModel:
    def __init__(self):
        self.recipes = list()


    def loadRecipes(self):
        sqlQuery = "SELECT * FROM Recipes"
        recipe_rows = database.getRecipes(sqlQuery)

        recipes = list()
        for recipe_row in recipe_rows:
            step_rows = database.getSteps(recipe_row[RECIPE_ID])

            recipeSteps = list()
            for step_row in step_rows:
                recipeSteps.append(RecipeStep(step_row[STEP_ID], step_row[STEP_STEP_NO], step_row[STEP_TEXT]))

            ingredient_rows = database.getIngredients(recipe_row[RECIPE_ID])
            ingredients = list()
            for ingredient_row in ingredient_rows:
                ingredientTypeRow = database.getIngredientType(ingredient_row[INGREDIENT_TYPE])
                measurementUnitRow = database.getMeasurementUnit(ingredientTypeRow[INGREDIENT_MEAS_UNIT])
                measurementUnit = MeasureUnit(measurementUnitRow[MEASURE_ID], measurementUnitRow[MEASURE_TYPE])
                ingredientType = IngredientType(ingredientTypeRow[INGREDIENT_ID],
                                                ingredientTypeRow[INGREDIENT_NAME],
                                                measurementUnit)


                ingredients.append(Ingredient(ingredient_row[INGREDIENT_ID],
                                              ingredientType,
                                              ingredient_row[INGREDIENT_AMOUNT]))

            chef = database.getChefType(recipe_row[RECIPE_CHEF])
            appliance = database.getApplianceType(recipe_row[RECIPE_APPLIANCE])

            recipes.append(Recipe(recipe_row[RECIPE_ID],
                                  recipe_row[RECIPE_NAME],
                                  recipe_row[RECIPE_DESCRIP],
                                  Chef(chef[CHEF_ID], chef[CHEF_NAME]),
                                  Appliance(appliance[APPLIANCE_ID], appliance[APPLIANCE_NAME]),
                                  recipe_row[RECIPE_PREP],
                                  recipe_row[RECIPE_COOK],
                                  recipe_row[RECIPE_SERVE],
                                  ingredients,
                                  recipeSteps))

        self.recipes = recipes

    #Based on the filter object, retrun a list of recipes
    def getRecipesDict(self, recipeFilter):
        filteredRecipesDict = dict()


        for recipe in self.recipes:
            addRecipe = True
            if recipeFilter.chef.name != 'NA' and recipeFilter.chef.id != recipe.chef.id:
                addRecipe = False
            if recipeFilter.appliance.name != 'NA' and recipeFilter.appliance.id != recipe.appliance.id:
                addRecipe = False
            if  not (recipeFilter.prepTime[0] <= recipe.prepTime <= recipeFilter.prepTime[1]):
                addRecipe = False
            if  not (recipeFilter.cookTime[0] <= recipe.cookTime <= recipeFilter.cookTime[1]):
                addRecipe = False
            if  not (recipeFilter.servings[0] <= recipe.servings <= recipeFilter.servings[1]):
                addRecipe = False

            for filterType in recipeFilter.ingredientTypes:
                included = False
                for ingredient in recipe.ingredients:
                    if filterType.id == ingredient.ingredientType.id:
                        included = True
                        break
                if not included:
                    addRecipe = False
                    break

            if addRecipe:
                filteredRecipesDict[recipe.name] = recipe

        return filteredRecipesDict

    #return a list of ingredients from a list of recipes
    def getIngredients(self, recipes):
        allIngredients = list()

        for recipe in recipes:
            for ingredient in recipe.ingredients:
                allIngredients.append(ingredient)

        return allIngredients

    def addRecipe(self, recipe):
        recipeList =[]
        recipeList.append('"' + recipe.name + '"')
        recipeList.append('"' + recipe.description + '"')
        recipeList.append(recipe.chef.id)
        recipeList.append(recipe.appliance.id)
        recipeList.append(recipe.prepTime)
        recipeList.append(recipe.cookTime)
        recipeList.append(recipe.servings)
        database.addRecipe(recipeList)

        recipeId = database.getRecipeIDByName('"' +recipe.name+'"')[0]

        for step in recipe.recipeSteps:
            database.addRecipeStep([recipeId, step.stepNo, '"' + step.text + '"'], )

        for ingredient in recipe.ingredients:
            database.addIngredient([recipeId, ingredient.ingredientType.id, ingredient.amount])

    def deleteRecipe(self, recipeId):
        database.deleteRecipe(recipeId)

def isRecipeNameInDB(recipeName):
    recipe = database.getRecipeIDByName('"' +recipeName+'"')
    if recipe:
        return True
    else:
        return False


def getChefTypesDict():
    chefDict = dict()
    chefRows = database.getAllChefTypes()

    for row in chefRows:
        chefDict[row[CHEF_NAME]] = Chef(row[CHEF_ID], row[CHEF_NAME])

    return chefDict

def getApplianceTypesDict():
    applianceDict = dict()
    applianceRows = database.getAllApplianceTypes()

    for row in applianceRows:
        applianceDict[row[APPLIANCE_NAME]] = Appliance(row[APPLIANCE_ID], row[APPLIANCE_NAME])

    return applianceDict

def getIngredientTypesDict():
    ingredientDict = dict()
    ingredientRows = database.getAllIngredientTypes()

    for row in ingredientRows:
        measureUnitRow = database.getMeasurementUnit(row[INGREDIENT_MEAS_UNIT])
        ingredientDict[row[INGREDIENT_NAME]] = IngredientType(row[INGREDIENT_ID],
                                                row[INGREDIENT_NAME],
                                                MeasureUnit(measureUnitRow[MEASURE_ID], measureUnitRow[MEASURE_TYPE]))

    return ingredientDict

def getMeasureUnitsDict():
    measureDict = dict()
    measureRows = database.getAllMeasureUnits()

    for row in measureRows:
        measureDict[row[MEASURE_TYPE]] = MeasureUnit(row[MEASURE_ID], row[MEASURE_TYPE])

    return measureDict


if __name__ == '__main__':
    recipeBook = RecipeBookModel()
    recipeBook.loadRecipes()
    recipes = recipeBook.getRecipesDict(RecipeFilter())

    print(getIngredientTypesDict())


    # filter1 = RecipeFilter(ChefEnum.NA,
    #                        ApplianceEnum.NA,
    #                        (0,9999),
    #                        (0,9999),
    #                        (0,9999),
    #                        tuple())
    #
    # filter2 = RecipeFilter()
    # filter3 = RecipeFilter(ChefEnum.ASHLEY)
    # filter4 = RecipeFilter(ChefEnum.ROBERT)
    # filter5 = RecipeFilter(applianceEnum=ApplianceEnum.GRILL)
    # filter6 = RecipeFilter(ChefEnum.ASHLEY, applianceEnum=ApplianceEnum.GRILL)
    #
    # search1 = recipeBook.getRecipes(filter1)
    # search2 = recipeBook.getRecipes(filter2)
    # search3 = recipeBook.getRecipes(filter3)
    # search4 = recipeBook.getRecipes(filter4)
    # search5 = recipeBook.getRecipes(filter5)
    # search6 = recipeBook.getRecipes(filter6)
    #
    # ingredientTypes = (1,4,)
    # filter7 = RecipeFilter(ingredientsTypes=ingredientTypes)
    # search7 = recipeBook.getRecipes(filter7)

    print('complete')


