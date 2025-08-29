from recipe import Recipe


def add_recipe(recipe_list, title, ingredients, instructions):
    new_recipe = Recipe(title, ingredients, instructions)
    recipe_list.append(new_recipe)
    # return recipe_list

def view_recipes(recipe_list):
    for recipe in recipe_list:
        print(f"{(recipe_list.index(recipe) + 1)}. {recipe.title}")

    print() # Purely to make console more readable

def search_recipe_titles(recipe_list, title):
    result_list = list()

    for recipe in recipe_list:
        if title.lower() in recipe.title.lower():
            result_list.append(recipe)

    view_recipes(result_list)

def search_recipe_ingredients(recipe_list, ingredient):
    result_list = list()

    for recipe in recipe_list:
        if ingredient.lower() in map(str.lower, recipe.ingredients_list):
            result_list.append(recipe)

    view_recipes(result_list)

def delete_recipe(recipe_list, recipe_index):
    recipe_list.pop(recipe_index)
    view_recipes(recipe_list)
    # return recipe_list