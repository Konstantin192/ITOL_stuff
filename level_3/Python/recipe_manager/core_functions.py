import os
from recipe import Recipe
import json


def add_recipe(recipe_list):
    title = input("Enter recipe title: ")
    ingredients = []
    instructions = []

    new_recipe = Recipe(title, ingredients, instructions)

    new_recipe.add_ingredients()
    new_recipe.add_instructions()

    recipe_list.append(new_recipe)

    print("Recipe added")
    # return recipe_list


def view_recipes(recipe_list):
    print("\nCurrent recipes:")

    for recipe in recipe_list:
        print(f"{(recipe_list.index(recipe) + 1)}. {recipe.title}")

    print() # Purely to make console more readable


def search_recipe_titles(recipe_list):
    result_list = list()
    title = input("\nEnter recipe title: ")

    for recipe in recipe_list:
        if title.lower() in recipe.title.lower():
            result_list.append(recipe)

    # view_recipes(result_list)

    return result_list


def search_recipe_ingredients(recipe_list):
    result_list = list()
    ingredient = input("Enter ingredient name: ").lower()

    # for recipe in recipe_list:
    #     if ingredient.lower() in map(str.lower, recipe.ingredients_list):
    #         result_list.append(recipe)

    for recipe in recipe_list:
        recipe_ingredients = map(str.lower, recipe.ingredients_list)

        # The filter function is passing the variable "recipe_ingredients" to the lambda function as a
        # parameter "recipe_ingredients_list"
        if any(filter(lambda recipe_ingredients_list: ingredient in recipe_ingredients_list, recipe_ingredients)):
            result_list.append(recipe)

    # view_recipes(result_list)

    return result_list


def delete_recipe(recipe_list, recipe_index):
    recipe_title = recipe_list[recipe_index].title

    print(f"\nRecipe {recipe_title} deleted")

    recipe_list.pop(recipe_index)
    view_recipes(recipe_list)
    # return recipe_list


def save_recipes(recipe_list):
    recipe_list_file_path = "recipe_list.txt"
    recipe_list_file_exists = os.path.isfile(recipe_list_file_path)

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


def load_recipes(recipe_list):
    recipe_list_path = "recipe_list.txt"
    recipe_list_file_exists = os.path.isfile(recipe_list_path)
    recipe_list_file_size = None

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


def find_recipe_index(recipe_list, recipe_title):
    recipe_index = None

    for recipe in recipe_list:
        if recipe_title == recipe.title:
            recipe_index = recipe_list.index(recipe)
            break

    return recipe_index