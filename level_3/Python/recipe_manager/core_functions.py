import os
from recipe import Recipe
import json


"""
Summary:
    Allows the user to specify details about the recipe they want added
Args:
    recipe_list (list): The list containing all of the data of all recipes (title, ingredients, instructions)
"""
def add_recipe(recipe_list):
    title = input("\nEnter recipe title: ")
    ingredients = []
    instructions = []

    new_recipe = Recipe(title, ingredients, instructions)

    new_recipe.add_ingredients()
    new_recipe.add_instructions()

    recipe_list.append(new_recipe)

    print("\nRecipe added")


"""
Summary:
    Provides the user with a list with the titles of all of the recipes currently in the recipe list
Args:
    recipe_list (list): The list containing all of the data of all recipes (title, ingredients, instructions)
"""
def view_recipes(recipe_list):
    print("\nCurrent recipes:")

    if len(recipe_list) == 0:
        print("Recipe list is empty")
    else:
        for recipe in recipe_list:
            print(f"{(recipe_list.index(recipe) + 1)}. {recipe.title}")


"""
Summary:
    Searches through the titles of all the recipes in the recipe list
Args:
    recipe_list (list): The list containing all of the data of all recipes (title, ingredients, instructions)
Returns:
    result_list (list): The list containing all of the data of all recipes found in the search
"""
def search_recipe_titles(recipe_list):
    result_list = list()
    title = input("\nEnter recipe title: ")

    for recipe in recipe_list:
        if title.lower() in recipe.title.lower():
            result_list.append(recipe)

    return result_list


"""
Summary:
    Searches through the ingredients of all the recipes in the recipe list
Args:
    recipe_list (list): The list containing all of the data of all recipes (title, ingredients, instructions)
Returns:
    result_list (list): The list containing all of the data of all recipes found in the search
"""
def search_recipe_ingredients(recipe_list):
    result_list = list()
    ingredient = input("\nEnter ingredient name: ").lower()

    for recipe in recipe_list:
        recipe_ingredients = map(str.lower, recipe.ingredients_list)

        # The filter function is passing the variable "recipe_ingredients" to the lambda function as a
        # parameter "recipe_ingredients_list"
        if any(filter(lambda recipe_ingredients_list: ingredient in recipe_ingredients_list, recipe_ingredients)):
            result_list.append(recipe)

    return result_list


"""
Summary:
    Removes a recipe from the recipe list
Args:
    recipe_list (list): The list containing all of the data of all recipes (title, ingredients, instructions)
"""
def delete_recipe(recipe_list, recipe_index):
    recipe_title = recipe_list[recipe_index].title

    print(f"\nRecipe {recipe_title} deleted")

    recipe_list.pop(recipe_index)
    view_recipes(recipe_list)


"""
Summary:
    Saves the recipes from the application recipe list to a text file
Args:
    recipe_list (list): The list containing all of the data of all recipes (title, ingredients, instructions)
"""
def save_recipes(recipe_list):
    recipe_list_file_path = "recipe_list.txt"
    recipe_list_file_exists = os.path.isfile(recipe_list_file_path)

    try:
        if not recipe_list_file_exists:
            with open(recipe_list_file_path, "w") as recipe_file:
                recipe_file.write("")
                recipe_file.close()

        if len(recipe_list) > 0:
            # Convert the objects of the recipe list to dictionaries so they can be put in a JSON format
            json_list = json.dumps([recipe.__dict__ for recipe in recipe_list])

            with open(recipe_list_file_path, "w") as recipe_file:
                recipe_file.write(json_list)
                recipe_file.close()
    except:
        print("\nERROR - The application encountered an error while attempting to save the recipe list. Please contact a system administrator.")


"""
Summary:
    Loads the recipes saved in the recipe list text file into the recipe list of the application
Args:
    recipe_list (list): The list containing all of the data of all recipes (title, ingredients, instructions)
"""
def load_recipes(recipe_list):
    recipe_list_path = "recipe_list.txt"
    recipe_list_file_exists = os.path.isfile(recipe_list_path)

    try:
        if recipe_list_file_exists:
            recipe_list_file_size = os.stat(recipe_list_path).st_size

            # Check if the recipe file is blank
            if recipe_list_file_size != 0:
                with open(recipe_list_path, "r") as recipe_file:
                    recipes_to_load = json.load(recipe_file)

                    for recipe in recipes_to_load:
                        recipe_load = Recipe(recipe["title"], recipe["ingredients_list"], recipe["instructions"])
                        recipe_list.append(recipe_load)

                    recipe_file.close()
    except:
        print("\nERROR - The application encountered an error when attempting to load recipe list. Please contact a system administrator.")


"""
Summary:
    Finds the index of a specified recipe within the recipe list
Args:
    recipe_list (list): The list containing all of the data of all recipes (title, ingredients, instructions)
    recipe_title (string): The title of the recipe for which to get the index
Returns:
    recipe_index (int): The index of the recipe within the recipe list
"""
def find_recipe_index(recipe_list, recipe_title):
    recipe_index = None

    for recipe in recipe_list:
        if recipe_title == recipe.title:
            recipe_index = recipe_list.index(recipe)
            break

    return recipe_index


"""
Summary:
    Logs errors along with their stack traces to an error log text file
Args:
    error_stack_trace (string): The error stack trace for the error
"""
def log_error(error_stack_trace):
    try:
        error_stack_trace = str(error_stack_trace)
        error_log_file_path = 'error_log.txt'

        with open(error_log_file_path, "a") as error_log_file:
            error_log_file.write(f"\n\n\n{error_stack_trace}")
            error_log_file.close()
    except:
        print("\nERROR - The application encountered an error while attempting to log an error. Please contact a system administrator.")
