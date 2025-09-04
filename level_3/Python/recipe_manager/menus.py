import core_functions

def main_menu(recipe_list):
    application_exit = False

    while not application_exit:
        print("\nWelcome to Recipe Manager")
        print("1. View Recipes")
        print("2. Add Recipes")
        print("3. Edit Recipes")
        print("4. Delete Recipes")
        print("5. Search Recipes")
        print("0. Exit")

        option_selected = int(input("\nWhat would you like to do? : "))

        match option_selected:
            # View recipes
            case 1:
                recipe_view_menu(recipe_list)
            # Add recipes
            case 2:
                recipe_add_menu(recipe_list)
            # Edit recipes
            case 3:
                recipe_edit_menu(recipe_list)
            # Delete recipes
            case 4:
                recipe_delete_menu(recipe_list)
            # Search recipes
            case 5:
                recipe_search_menu(recipe_list)
            # Exit
            case 0:
                application_exit = True


def recipe_view_menu(recipe_list):
    back_to_main_menu = False;

    while not back_to_main_menu:
        core_functions.view_recipes(recipe_list)
        selected_recipe = int(input("\nSelect recipe to view: "))
        recipe_list[selected_recipe - 1].view_recipe_details()

        print("\nOptions: ")
        print("1. View more Recipes")
        print("2. Back to Main Menu")
        option_select = int(input("\nWhat would you like to do? : "))

        if option_select == 2:
            back_to_main_menu = True


def recipe_add_menu(recipe_list):
    back_to_main_menu = False

    while not back_to_main_menu:
        core_functions.add_recipe(recipe_list)

        print("\nOptions: ")
        print("1. Add more Recipes")
        print("2. Main Menu")
        selected_option = int(input("\nWhat would you like to do? : "))

        if selected_option == 2:
            back_to_main_menu = True


def recipe_edit_menu(recipe_list):
    back_to_main_menu = False

    while not back_to_main_menu:
        core_functions.view_recipes(recipe_list)
        selected_recipe = int(input("\nSelect recipe to edit: "))
        recipe_list[selected_recipe - 1].view_recipe_details()

        print("Recipe edit options: ")
        print("1. Change title")
        print("2. Edit ingredients")
        print("3. Edit instructions")
        selected_edit = int(input("\nWhat would you like to do? : "))

        recipe_edit_submenu(recipe_list, selected_recipe, selected_edit)

        print("\nOptions: ")
        print("1. Edit more recipes")
        print("2. Main Menu")
        selected_option = int(input("\nWhat would you like to do? : "))

        if selected_option == 2:
            back_to_main_menu = True


def recipe_edit_submenu(recipe_list, selected_recipe, selected_edit):
    match selected_edit:
        # Change recipe title
        case 1:
            recipe_list[selected_recipe - 1].change_title()
        # Edit recipe ingredients
        case 2:
            print("\nIngredient edit options:")
            print("1. Add ingredients")
            print("2. Remove ingredients")
            print("3. Change ingredients")
            selected_ingredient_edit = int(input("\nWhat would you like to do? : "))

            match selected_ingredient_edit:
                case 1:
                    recipe_list[selected_recipe - 1].add_ingredients()
                case 2:
                    recipe_list[selected_recipe - 1].remove_ingredients()
                case 3:
                    recipe_list[selected_recipe - 1].change_ingredients()
        # Edit recipe instructions
        case 3:
            print("\nInstruction edit options:")
            print("1. Add instructions")
            print("2. Remove instructions")
            print("3. Change instructions")
            selected_instruction_edit = int(input("\nWhat would you like to do? : "))

            match selected_instruction_edit:
                case 1:
                    recipe_list[selected_recipe - 1].add_instructions()
                case 2:
                    recipe_list[selected_recipe - 1].remove_instructions()
                case 3:
                    recipe_list[selected_recipe - 1].change_instructions()


def recipe_delete_menu(recipe_list):
    back_to_main_menu = False

    while not back_to_main_menu:
        print("\nCurrent recipes")
        core_functions.view_recipes(recipe_list)
        selected_recipe_delete = int(input("\nWhich would you like to delete? : "))

        core_functions.delete_recipe(recipe_list, selected_recipe_delete - 1)

        print("\nOptions: ")
        print("1. Delete more recipes")
        print("2. Back to Main Menu")
        selected_option = int(input("\nWhat would you like to do? : "))

        if selected_option == 2:
            back_to_main_menu = True


def recipe_search_menu(recipe_list):
    back_to_main_menu = False

    while not back_to_main_menu:
        print("\nRecipe search options: ")
        print("1. Search by Title")
        print("2. Search by Ingredients")
        selected_search = int(input("\nWhat would you like to do? : "))

        if selected_search == 1:
            core_functions.search_recipe_titles(recipe_list)
        else:
            core_functions.search_recipe_ingredients(recipe_list)

        print("\nOptions: ")
        print("1. Search more recipes")
        print("2. Back to Main Menu")
        selected_option = int(input("\nWhat would you like to do? : "))

        if selected_option == 2:
            back_to_main_menu = True