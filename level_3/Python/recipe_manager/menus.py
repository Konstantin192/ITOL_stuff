import core_functions
import input_validation

def main_menu(recipe_list):
    application_exit = False
    valid_inputs = [1, 2, 3, 4, 5, 0]

    while not application_exit:
        input_validated = False

        print("\nWelcome to Recipe Manager")
        print("1. View Recipes")
        print("2. Add Recipes")
        print("3. Edit Recipes")
        print("4. Delete Recipes")
        print("5. Search Recipes")
        print("0. Exit")

        while not input_validated:
            option_selected = input("\nWhat would you like to do? : ")

            input_validated = input_validation.menu_input_validation(option_selected, valid_inputs)

            if input_validated:
                match int(option_selected):
                    # View recipes
                    case 1:
                        recipe_view_menu(recipe_list)
                    # Add recipes
                    case 2:
                        recipe_add_menu(recipe_list)
                    # Edit recipes
                    case 3:
                        recipe_edit_menu_list(recipe_list)
                    # Delete recipes
                    case 4:
                        recipe_delete_menu(recipe_list)
                    # Search recipes
                    case 5:
                        recipe_search_menu(recipe_list)
                    # Exit
                    case 0:
                        application_exit = True
            else:
                print("\nInvalid input. Please try again.")


def recipe_view_menu(recipe_list):
    back_to_main_menu = False;
    valid_menu_inputs = [1, 2]

    while not back_to_main_menu:
        menu_input_validated = False
        recipe_input_validated = False
        core_functions.view_recipes(recipe_list)

        while not recipe_input_validated:
            selected_recipe = input("\nSelect recipe to view: ")

            recipe_input_validated = input_validation.recipe_input_validation(selected_recipe, recipe_list)

            if recipe_input_validated:
                recipe_list[int(selected_recipe) - 1].view_recipe_details()
            else:
                print("\nInvalid input. Please try again.")

        while not menu_input_validated:
            print("\nOptions: ")
            print("1. View more Recipes")
            print("2. Back to Main Menu")
            option_select = input("\nWhat would you like to do? : ")

            menu_input_validated = input_validation.menu_input_validation(option_select, valid_menu_inputs)

            if menu_input_validated:
                if int(option_select) == 2:
                    back_to_main_menu = True
            else:
                print("\nInvalid input. Please try again.")


def recipe_add_menu(recipe_list):
    back_to_main_menu = False
    valid_inputs = [1, 2]

    while not back_to_main_menu:
        core_functions.add_recipe(recipe_list)
        input_validated = False

        while not input_validated:
            print("\nOptions: ")
            print("1. Add more Recipes")
            print("2. Main Menu")
            selected_option = input("\nWhat would you like to do? : ")

            input_validated = input_validation.menu_input_validation(selected_option, valid_inputs)

            if input_validated:
                if int(selected_option) == 2:
                    back_to_main_menu = True
            else:
                print("\nInvalid input. Please try again.")


# This menu is used for editing recipes when the user is presented with the list of all recipes and has to select one
def recipe_edit_menu_list(recipe_list):
    back_to_main_menu = False
    valid_edit_inputs = [1, 2, 3]
    valid_options_inputs = [1, 2]

    while not back_to_main_menu:
        recipe_input_validated = False
        edit_input_validated = False
        options_input_validated = False

        core_functions.view_recipes(recipe_list)

        while not recipe_input_validated:
            selected_recipe = input("\nSelect recipe to edit: ")

            recipe_input_validated = input_validation.recipe_input_validation(selected_recipe, recipe_list)

            if recipe_input_validated:
                recipe_list[int(selected_recipe) - 1].view_recipe_details()
            else:
                print("\nInvalid input. Please try again.")

        print("\nRecipe edit options: ")
        print("1. Change title")
        print("2. Edit ingredients")
        print("3. Edit instructions")

        while not edit_input_validated:
            selected_edit = input("\nWhat would you like to do? : ")

            edit_input_validated = input_validation.menu_input_validation(selected_edit, valid_edit_inputs)

            if edit_input_validated:
                recipe_edit_submenu(recipe_list, int(selected_recipe), int(selected_edit))
            else:
                print("\nInvalid input. Please try again.")

        print("\nOptions: ")
        print("1. Edit more recipes")
        print("2. Main Menu")

        while not options_input_validated:
            selected_option = input("\nWhat would you like to do? : ")

            options_input_validated = input_validation.menu_input_validation(selected_option, valid_options_inputs)

            if options_input_validated:
                if int(selected_option) == 2:
                    # ToDo Figure out how control flow should work here
                    back_to_main_menu = True
            else:
                print("\nInvalid input. Please try again.")


# This menu is used to edit a recipe when the user is currently viewing the full details of that recipe after a search
def recipe_edit_menu_direct(recipe_list, recipe_index):
    back_to_previous_menu = False
    valid_edit_inputs = [1, 2, 3]
    valid_options_inputs = [1, 2]

    while not back_to_previous_menu:
        edit_input_validated = False
        options_input_validated = False

        print("\nRecipe edit options: ")
        print("1. Change title")
        print("2. Edit ingredients")
        print("3. Edit instructions")

        while not edit_input_validated:
            selected_edit = input("\nWhat would you like to do? : ")

            edit_input_validated = input_validation.menu_input_validation(selected_edit, valid_edit_inputs)

            if edit_input_validated:
                # Why is index +1 here instead of -1 ? - In all other places where an index is used to get a specific
                # recipe from a list they are  -1 because user selection is being translated to the corresponding list
                # index. In this instance however the previously called "find_recipe_index" function has already gotten
                # the translated index. As the below called function is also called by the original recipe_edit_menu
                # function , which passes user inputs, it has to translate them to the corresponding list index which if
                # done to the index being passed by the current function would mean that the list index would be 1 lower
                # than it should be thus targeting a wrong recipe. Hence the +1 to counteract that.
                recipe_edit_submenu(recipe_list, recipe_index + 1, int(selected_edit))
            else:
                print("\nInvalid input. Please try again.")

        print("\nOptions: ")
        print("1. Edit recipe further")
        print("2. Back to Recipe Search Menu")
        # In order to implement this I have to make it so the recipe list is updated after every change
        # print("3. Back to search submenu")

        while not options_input_validated:
            selected_option = input("\nWhat would you like to do? : ")

            options_input_validated = input_validation.menu_input_validation(selected_option, valid_options_inputs)

            if options_input_validated:
                if int(selected_option) == 1:
                    edit_input_validated = False
                else:
                    # ToDo Figure out how control flow should work here
                    back_to_previous_menu = True
            else:
                print("\nInvalid input. Please try again.")


def recipe_edit_submenu(recipe_list, selected_recipe, selected_edit):
    ingredient_edit_input_validated = False
    instructions_edit_input_validated = False
    valid_edit_inputs = [1, 2, 3]

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

            while not ingredient_edit_input_validated:
                selected_ingredient_edit = input("\nWhat would you like to do? : ")

                ingredient_edit_input_validated = input_validation.menu_input_validation(selected_ingredient_edit, valid_edit_inputs)

                if ingredient_edit_input_validated:
                    match int(selected_ingredient_edit):
                        case 1:
                            recipe_list[selected_recipe - 1].add_ingredients()
                        case 2:
                            recipe_list[selected_recipe - 1].remove_ingredients()
                        case 3:
                            recipe_list[selected_recipe - 1].change_ingredients()
                else:
                    print("\nInvalid input. Please try again.")

        # Edit recipe instructions
        case 3:
            print("\nInstruction edit options:")
            print("1. Add instructions")
            print("2. Remove instructions")
            print("3. Change instructions")

            while not instructions_edit_input_validated:
                selected_instruction_edit = input("\nWhat would you like to do? : ")

                instructions_edit_input_validated = input_validation.menu_input_validation(selected_instruction_edit, valid_edit_inputs)

                if instructions_edit_input_validated:
                    match int(selected_instruction_edit):
                        case 1:
                            recipe_list[selected_recipe - 1].add_instructions()
                        case 2:
                            recipe_list[selected_recipe - 1].remove_instructions()
                        case 3:
                            recipe_list[selected_recipe - 1].change_instructions()
                else:
                    print("\nInvalid input. Please try again.")


def recipe_delete_menu(recipe_list):
    back_to_main_menu = False
    valid_options_inputs = [1, 2]

    while not back_to_main_menu:
        recipe_input_validated = False
        options_input_validated = False

        core_functions.view_recipes(recipe_list)

        while not recipe_input_validated:
            selected_recipe_delete = input("\nWhich recipe would you like to delete? : ")

            recipe_input_validated = input_validation.recipe_input_validation(selected_recipe_delete, recipe_list)

            if recipe_input_validated:
                core_functions.delete_recipe(recipe_list, int(selected_recipe_delete) - 1)
            else:
                print("\nInvalid input. Please try again.")

        print("\nOptions: ")
        print("1. Delete more recipes")
        print("2. Back to Main Menu")

        while not options_input_validated:
            selected_option = input("\nWhat would you like to do? : ")

            options_input_validated = input_validation.menu_input_validation(selected_option, valid_options_inputs)

            if options_input_validated:
                if int(selected_option) == 2:
                    back_to_main_menu = True
            else:
                print("\nInvalid input. Please try again.")


def recipe_search_menu(recipe_list):
    back_to_main_menu = False
    valid_search_inputs = [1, 2]
    valid_options_inputs = [1, 2, 3]

    while not back_to_main_menu:
        search_input_validated = False
        options_input_validated = False
        recipe_input_validated = False

        print("\nRecipe search options: ")
        print("1. Search by Title")
        print("2. Search by Ingredients")

        while not search_input_validated:
            selected_search = input("\nWhat would you like to do? : ")

            search_input_validated = input_validation.menu_input_validation(selected_search, valid_search_inputs)

            if search_input_validated:
                if int(selected_search) == 1:
                    result_list = core_functions.search_recipe_titles(recipe_list)
                else:
                    result_list = core_functions.search_recipe_ingredients(recipe_list)
            else:
                print("\nInvalid input. Please try again.")

        core_functions.view_recipes(result_list)

        print("\nOptions: ")
        print("1. Search more recipes")
        print("2. View recipe details")
        print("3. Back to Main Menu")

        while not options_input_validated:
            selected_option = input("\nWhat would you like to do? : ")

            options_input_validated = input_validation.menu_input_validation(selected_option, valid_options_inputs)

            if options_input_validated:
                selected_option = int(selected_option)

                match selected_option:
                    case 2:
                        while not recipe_input_validated:
                            selected_recipe = input("\nWhich recipe would you like to view? : ")

                            recipe_input_validated = input_validation.recipe_input_validation(selected_recipe, result_list)

                            if recipe_input_validated:
                                result_list[int(selected_recipe) - 1].view_recipe_details()

                                recipe_title = result_list[int(selected_recipe) - 1].title
                                recipe_search_submenu(recipe_list, recipe_title)
                            else:
                                print("\nInvalid input. Please try again.")
                    case 3:
                        back_to_main_menu = True
            else:
                print("\nInvalid input. Please try again.")


def recipe_search_submenu(recipe_list, recipe_title):
    back_to_previous_menu = False
    valid_options_inputs = [1, 2, 3]

    while not back_to_previous_menu and not back_to_previous_menu:
        options_input_validated = False

        print("\nOptions: ")
        print("1. Edit recipe")
        print("2. Delete recipe")
        print("3. Back to Search Menu")

        while not options_input_validated:
            selected_option = input("\nWhat would you like to do? : ")

            options_input_validated = input_validation.menu_input_validation(selected_option, valid_options_inputs)

            if options_input_validated:
                match int(selected_option):
                    case 1:
                        recipe_index = core_functions.find_recipe_index(recipe_list, recipe_title)
                        recipe_edit_menu_direct(recipe_list, recipe_index)
                        back_to_previous_menu = True
                    case 2:
                        recipe_index = core_functions.find_recipe_index(recipe_list, recipe_title)
                        core_functions.delete_recipe(recipe_list, recipe_index)
                        back_to_previous_menu = True
                    case 3:
                        back_to_previous_menu = True
            else:
                print("\nInvalid input. Please try again.")