import core_functions
import os
import json
from core_functions import load_recipes, view_recipes, save_recipes
from recipe import Recipe
import menus

# ToDo Input validation
# Todo make functions for the input verifications ?
# ToDo Handling for everything when the recipe list is empty
# ToDo review all back to main menu while loops in menus / Am i continuously drilling down by calling main menu function at the end of a function ?
# Todo Error handling
# ToDo Make sure an option to go back to main menu is present wherever it needs to be
# Todo make sure there is even spacing between everything going on in the console
# Todo make sure all code follows the same logic for error input - either repeat menu after invalid input OR don't
# Todo decide whether to keep saving changes to the list only on app exit or update saved list after every change
def main():
    recipe_list = list()
    load_recipes(recipe_list)

    # core_functions.add_recipe(recipe_list,
    #                           "Salad",
    #                           ["cucumbers", "tomatoes", "cow cheese"],
    #                           ["cut ingredients", "mix ingredients"])
    # core_functions.add_recipe(recipe_list,
    #                           "Salmon with potatoes and carrots",
    #                           ["salmon fillet", "carrots", "potatoes"],
    #                           ["cut ingredients", "season ingredients", "put into air fryer"])
    # core_functions.add_recipe(recipe_list,
    #                           "Vegetable fried rice",
    #                           ["rice", "red onions", "bell peper", "spring onion", "frozen peas", "eggs", "soy sauce", "sesame seed oil"],
    #                           ["boil rice", "mix rice with vegetables and sauces", "put in air fryer"])

    menus.main_menu(recipe_list)


    save_recipes(recipe_list)

if __name__ == "__main__":
    main()

