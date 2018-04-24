import sqlite3 as DATABASE#using sqlite database
DB_LOCATION = 'db_recipes.sqlite'

### CONNECT TO DB ###
def queryDB(conn, query):
    return conn.execute(query)

def commitDB(conn):
    conn.commit()

def closeDB(conn):
    conn.close()

def openDB(db_location = DB_LOCATION):
    conn = DATABASE.connect(db_location)
    return conn

#columNames should be a string of comma seperated column names
#data should be a string of comma seperated values
def addRow(table, columNames, data):
    query = "INSERT INTO {} ({}) VALUES ({})".format(table, columNames, data)
    conn = openDB()
    queryDB(conn, query)
    commitDB(conn)
    closeDB(conn)

#id
#name
#description
#chefEnum
#applianceEnum
#prepTime
#cookTime
#servings
def getRecipes(query):
    conn = openDB(DB_LOCATION)
    cursor = queryDB(conn, query)

    recipes = []
    for row in cursor:
        recipes.append(row)

    closeDB(conn)
    return recipes

#id
#name
#unit
def getAllIngredientTypes():
    query = "SELECT * FROM IngredientTypes"

    conn = openDB(DB_LOCATION)
    cursor = queryDB(conn, query)

    ingredients = []
    for row in cursor:
        ingredients.append(row)

    closeDB(conn)
    return ingredients

#[id, type]
def getAllApplianceTypes():
    query = "SELECT * FROM ApplianceTypes"

    conn = openDB(DB_LOCATION)
    cursor = queryDB(conn, query)

    ingredients = []
    for row in cursor:
        ingredients.append(row)

    closeDB(conn)
    return ingredients

#[id, type]
def getAllChefTypes():
    query = "SELECT * FROM ChefTypes"

    conn = openDB(DB_LOCATION)
    cursor = queryDB(conn, query)

    ingredients = []
    for row in cursor:
        ingredients.append(row)

    closeDB(conn)
    return ingredients

def getAllMeasureUnits():
    query = "SELECT * FROM MeasurementUnits"

    conn = openDB(DB_LOCATION)
    cursor = queryDB(conn, query)

    ingredients = []
    for row in cursor:
        ingredients.append(row)

    closeDB(conn)
    return ingredients

#id
#recipeId
#ingredientType
#amount
def getIngredients(recipeId):
    query = "SELECT * FROM Ingredients WHERE recipeId = {}".format(recipeId)

    conn = openDB(DB_LOCATION)
    cursor = queryDB(conn, query)

    ingredients = []
    for row in cursor:
        ingredients.append(row)

    closeDB(conn)
    return ingredients

#id
#recipeId
#stepNumber
#text
def getSteps(recipeId):
    query = "SELECT * FROM Steps WHERE recipeId = {}".format(recipeId)

    conn = openDB(DB_LOCATION)
    cursor = queryDB(conn, query)

    steps = []
    for row in cursor:
        steps.append(row)

    closeDB(conn)
    return steps

#id
#name
#unit
def getIngredientType(ingredientId):
    query = "SELECT * FROM IngredientTypes WHERE id = {}".format(ingredientId)

    conn = openDB(DB_LOCATION)
    cursor = queryDB(conn, query)

    types = []
    for row in cursor:
        types.append(row)

    closeDB(conn)
    return types[0] #Hacky, just expect 1 unique result

#[id, type]
def getMeasurementUnit(typeId):
    query = "SELECT * FROM MeasurementUnits WHERE id = {}".format(typeId)

    conn = openDB(DB_LOCATION)
    cursor = queryDB(conn, query)

    types = []
    for row in cursor:
        types.append(row)

    closeDB(conn)
    return types[0] #Hacky, just expect 1 unique result

#[id, name]
def getApplianceType(applianceId):
    query = "SELECT * FROM ApplianceTypes WHERE id = {}".format(applianceId)

    conn = openDB(DB_LOCATION)
    cursor = queryDB(conn, query)

    types = []
    for row in cursor:
        types.append(row)

    closeDB(conn)
    return types[0] #Hacky, just expect 1 unique result

#[id, name]
def getChefType(chefId):
    query = "SELECT * FROM ChefTypes WHERE id = {}".format(chefId)

    conn = openDB(DB_LOCATION)
    cursor = queryDB(conn, query)

    types = []
    for row in cursor:
        types.append(row)

    closeDB(conn)
    return types[0] #Hacky, just expect 1 unique result

#After adding a new recipe, need the entry so that can get the uniqe ID
def getRecipeIDByName(name):
    query = "SELECT * FROM Recipes WHERE name = {}".format(name)

    conn = openDB(DB_LOCATION)
    cursor = queryDB(conn, query)

    recipes = []
    for row in cursor:
        recipes.append(row)

    closeDB(conn)
    if recipes:
        return recipes[0] #Hacky, just expect 1 unique result
    return []

def deleteRecipe(recipeId):
    query = 'DELETE FROM Recipes WHERE id = ' +str(recipeId)
    conn = openDB()
    queryDB(conn, query)
    commitDB(conn)
    closeDB(conn)

    deleteIngredients(recipeId)
    deleteSteps(recipeId)
    deletePictures(recipeId)

def deleteIngredients(recipeId):
    query = 'DELETE FROM Ingredients WHERE recipeId = ' +str(recipeId)
    conn = openDB()
    queryDB(conn, query)
    commitDB(conn)
    closeDB(conn)

def deleteSteps(recipeId):
    query = 'DELETE FROM Steps WHERE recipeId = ' +str(recipeId)
    conn = openDB()
    queryDB(conn, query)
    commitDB(conn)
    closeDB(conn)

def deletePictures(recipeId):
    query = 'DELETE FROM Pictures WHERE recipeId = ' +str(recipeId)
    conn = openDB()
    queryDB(conn, query)
    commitDB(conn)
    closeDB(conn)

def addRecipe(recipe):
    columns = 'name,description,chefEnum,applianceEnum,prepTime,cookTime,servings'
    values = str(recipe[0]) + ',' \
             + str(recipe[1])  + ',' \
             + str(recipe[2])  + ',' \
             + str(recipe[3]) + ',' \
             + str(recipe[4]) + ',' \
             + str(recipe[5]) + ',' \
             + str(recipe[6])
    addRow('Recipes', columns , values)

def addRecipeStep(step):
    columns = 'recipeId,stepNumber,text'
    values = str(step[0]) + ',' \
             + str(step[1])  + ',' \
             + str(step[2])
    addRow('Steps', columns , values)

def addIngredient(ingredient):
    columns = 'recipeId,ingredientType,amount'
    values = str(ingredient[0]) + ',' \
             + str(ingredient[1])  + ',' \
             + str(ingredient[2])
    addRow('Ingredients', columns , values)

def addIngredientType(ingredientType):
    columns = 'name,unit'
    values = str(ingredientType[0]) + ',' \
             + str(ingredientType[1])
    addRow('IngredientTypes', columns , values)

def addChef(chef):
    columns = 'type'
    values = str(chef)
    addRow('ChefTypes', columns , values)

def addAppliance(appliance):
    columns = 'type'
    values = str(appliance)
    addRow('ApplianceTypes', columns , values)

def addMeasureUnit(measureUnit):
    columns = 'type'
    values = str(measureUnit)
    addRow('MeasurementUnits', columns , values)


if __name__ == '__main__':
    pass
    # ingType = ['"Onion"', '4', '1']
    # addIngredientType(ingType)
    # ing = ['1' , '3' , '1']
    # addIngredient(ing)
    # recipe = ['"testAddTacos"', '"a descript for a test add"', '2', '3', '10', '10' , '5']
    # addRecipe(recipe)
    # step = [3,3,'"fry the meat"']
    # addRecipeStep(step)
    # ing = ['3' , '3' , '1']
    # addIngredient(ing)
