from enum import Enum
import database

#TODO - add to GIT!

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
INGREDIENT_UNIT_TYPE = 2
INGREDIENT_UNIT = 3
INGREDIENT_AMOUNT = 3

STEP_ID = 0
STEP_RECIPE_ID = 1
STEP_STEP_NO = 2
STEP_TEXT = 3

class UnitTypeEnum(Enum):
    NONE = 0
    NA = 1
    VOLUME = 2
    MASS = 3
    QUANTITY = 4

class MassEnum(Enum):
    NONE = 0
    NA = 1
    OUNCE = 2
    POUND = 3
    MILLIGRAM = 4
    GRAM = 5
    KILOGRAM = 6

class VolumeEnum(Enum):
    NONE = 0
    NA = 1
    TEASPOON = 2
    TABLESPOON = 3
    FLUID_OUNCE = 4
    GILL = 5
    CUP = 6
    PINT = 7
    QUART = 8
    GALLON = 9
    MILLILITER = 10
    LITER = 11

class ChefEnum(Enum):
    NONE = 0
    NA = 1
    ASHLEY = 2
    ROBERT = 3

class ApplianceEnum(Enum):
    NONE = 0
    NA = 1
    OVEN = 2
    COOKTOP = 3
    CROCKPOT = 4
    GRILL = 5
    OTHER = 6

class Ingredient:
    def __init__(self, id, name, typeID, unitType, unit, amount):
        self.id = id
        self.name = name
        self.typeID = typeID
        self.unitType = unitType
        self.unit = unit
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
                 chefEnum = ChefEnum.NA,
                 applianceEnum = ApplianceEnum.NA,
                 prepTime = (0,9999),
                 cookTime = (0,9999),
                 servings = (0, 9999),
                 ingredientsTypes = tuple()): #list of ingredient type ID's
        self.chefEnum = chefEnum
        self.applianceEnum = applianceEnum
        self.prepTime = prepTime
        self.cookTime = cookTime
        self.servings = servings
        self.ingredientsTypes = ingredientsTypes

class Recipe:
    def __init__(self,
                 id,
                 name,
                 description,
                 chefEnum,
                 applianceEnum,
                 prepTime,
                 cookTime,
                 servings,
                 ingredients,
                 recipeSteps,
                 pictures = None):

        self.id = id
        self.name = name
        self.description = description
        self.chefEnum = chefEnum
        self.applianceEnum = applianceEnum
        self.prepTime = prepTime
        self.cookTime = cookTime
        self.servings = servings
        self.ingredients = ingredients
        self.recipeSteps = recipeSteps
        self.pictures = pictures

class RecipeBookModel:
    def __init__(self):
        self.recipes = list()


    def loadRecipes(self, filters = tuple()):
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
                ingredientType = database.getIngredientType(ingredient_row[INGREDIENT_TYPE])
                unitTypeEnum = UnitTypeEnum(ingredientType[INGREDIENT_UNIT_TYPE])

                if unitTypeEnum == UnitTypeEnum.MASS:
                    unitEnum = MassEnum(ingredientType[INGREDIENT_UNIT])

                elif unitTypeEnum == UnitTypeEnum.VOLUME:
                    unitEnum = VolumeEnum(ingredientType[INGREDIENT_UNIT])

                elif unitTypeEnum == UnitTypeEnum.QUANTITY:
                    unitEnum = MassEnum(1) #the unit is NA

                else:
                    unitEnum = MassEnum(1)

                ingredients.append(Ingredient(ingredient_row[INGREDIENT_ID],
                                              ingredientType[INGREDIENT_NAME],
                                              ingredientType[INGREDIENT_TYPE_ID],
                                              unitTypeEnum,
                                              unitEnum,
                                              ingredient_row[INGREDIENT_AMOUNT]))

            recipes.append(Recipe(recipe_row[RECIPE_ID],
                                  recipe_row[RECIPE_NAME],
                                  recipe_row[RECIPE_DESCRIP],
                                  ChefEnum(recipe_row[RECIPE_CHEF]),
                                  ApplianceEnum(recipe_row[RECIPE_APPLIANCE]),
                                  recipe_row[RECIPE_PREP],
                                  recipe_row[RECIPE_COOK],
                                  recipe_row[RECIPE_SERVE],
                                  ingredients,
                                  recipeSteps))

        self.recipes = recipes

    #Based on the filter object, retrun a list of recipes
    def getRecipes(self, recipeFilter):
        filteredRecipes = list()

        for recipe in self.recipes:
            addRecipe = True
            if recipeFilter.chefEnum != ChefEnum.NA and recipeFilter.chefEnum != recipe.chefEnum:
                addRecipe = False
            if recipeFilter.applianceEnum != ApplianceEnum.NA and recipeFilter.applianceEnum != recipe.applianceEnum:
                addRecipe = False
            if  not (recipeFilter.prepTime[0] <= recipe.prepTime <= recipeFilter.prepTime[1]):
                addRecipe = False
            if  not (recipeFilter.cookTime[0] <= recipe.cookTime <= recipeFilter.cookTime[1]):
                addRecipe = False
            if  not (recipeFilter.servings[0] <= recipe.servings <= recipeFilter.servings[1]):
                addRecipe = False

            for filterType in recipeFilter.ingredientsTypes:
                included = False
                for ingredient in recipe.ingredients:
                    if filterType == ingredient.typeID:
                        included = True
                        break
                if not included:
                    addRecipe = False
                    break

            if addRecipe:
                filteredRecipes.append(recipe)

        return filteredRecipes

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
        recipeList.append(recipe.chefEnum.value)
        recipeList.append(recipe.applianceEnums.value)
        recipeList.append(recipe.prepTime)
        recipeList.append(recipe.cookTime)
        recipeList.append(recipe.servings)
        database.addRecipe(recipeList)

        recipeId = database.getRecipeByName(recipe.name)[0]

        for step in recipe.recipeSteps:
            database.addRecipeStep([recipeId, step.stepNo, '"' + step.text + '"'], )

        for ingredient in recipe.ingredients:
            database.addIngredient([recipeId, ingredient.typeID, ingredient.amount])

    def deleteRecipe(self, recipeId):
        database.deleteRecipe(recipeId)


if __name__ == '__main__':
    recipeBook = RecipeBookModel()
    recipeBook.loadRecipes()
    recipeBook.deleteRecipe(3)

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


