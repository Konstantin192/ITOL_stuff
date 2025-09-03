import core_functions

def main_menu(recipe_list):
    print("Welcome to Recipe Manager")
    print("1. View Recipes")
    print("2. Add Recipes")
    print("3. Edit Recipes")
    print("4. Delete Recipes")
    print("5. Exit")

    option_selected = int(input("\n What would you like to do? : "))

    match option_selected:
        case 1:
            core_functions.view_recipes(recipe_list)
        case 2:
            core_functions.add_recipe(recipe_list)
