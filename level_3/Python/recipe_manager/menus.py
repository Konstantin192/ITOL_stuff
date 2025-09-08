import core_functions

def main_menu(recipe_list):
    application_exit = False
    valid_inputs = [1, 2, 3, 4, 5, 0]
    input_validated = False

    while not application_exit:
        print("\nWelcome to Recipe Manager")
        print("1. View Recipes")
        print("2. Add Recipes")
        print("3. Edit Recipes")
        print("4. Delete Recipes")
        print("5. Search Recipes")
        print("0. Exit")

        while not input_validated:
            option_selected = input("\nWhat would you like to do? : ")
            input_is_int = option_selected.isdigit()

            if input_is_int:
                option_selected = int(option_selected)

            if option_selected in valid_inputs:
                input_validated = True
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
            selected_recipe_is_int = selected_recipe.isdigit()

            if selected_recipe_is_int:
                selected_recipe = int(selected_recipe)
                if selected_recipe > 0 and selected_recipe <= len(recipe_list):
                    recipe_input_validated = True
                    recipe_list[selected_recipe - 1].view_recipe_details()
                else:
                    print("\nInvalid input. Please try again.")
            else:
                print("\nInvalid input. Please try again.")

        while not menu_input_validated:
            print("\nOptions: ")
            print("1. View more Recipes")
            print("2. Back to Main Menu")
            option_select = input("\nWhat would you like to do? : ")
            option_select_is_int = option_select.isdigit()

            if option_select_is_int:
                option_select = int(option_select)

            if option_select in valid_menu_inputs:
                menu_input_validated = True

                if option_select == 2:
                    back_to_main_menu = True
                    main_menu(recipe_list)
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
            selected_option_is_int = selected_option.isdigit()

            if selected_option_is_int:
                selected_option = int(selected_option)

            if selected_option in valid_inputs:
                input_validated = True

                if selected_option == 2:
                    back_to_main_menu = True
                    main_menu(recipe_list)
            else:
                print("\nInvalid input. Please try again.")


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


def recipe_edit_menu(recipe_list, recipe_index):
    back_to_previous_menu = False

    while not back_to_previous_menu:
        # core_functions.view_recipes(recipe_list)
        # selected_recipe = int(input("\nSelect recipe to edit: "))
        # recipe_list[recipe_index].view_recipe_details()

        print("Recipe edit options: ")
        print("1. Change title")
        print("2. Edit ingredients")
        print("3. Edit instructions")
        selected_edit = int(input("\nWhat would you like to do? : "))

        # Why is index +1 here instead of -1 ? - In all other places where an index is used to get a specific recipe
        # from a list they are  -1 because user selection is being translated to the corresponding list index. In this
        # instance however the previously called "find_recipe_index" function has already gotten the translated index.
        # As the below called function is also called by the original recipe_edit_menu function , which passes user
        # inputs, it has to translate them to the corresponding list index which if done to the index being passed by
        # the current function would mean that the list index would be 1 lower than it should be thus targeting a wrong
        # recipe. Hence the +1 to counteract that.
        recipe_edit_submenu(recipe_list, recipe_index + 1, selected_edit)

        print("\nOptions: ")
        print("1. Edit recipe further")
        # print("2. Back to previous menu")
        print("2. Back to Main Menu")
        selected_option = int(input("\nWhat would you like to do? : "))

        match selected_option:
            case 1:
                recipe_edit_menu(recipe_list, recipe_index)
            # case 2:
            #     back_to_previous_menu = True
            case 2:
                main_menu(recipe_list)

        # if selected_option == 2:
        #     back_to_previous_menu = True


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
            result_list = core_functions.search_recipe_titles(recipe_list)
        else:
            result_list = core_functions.search_recipe_ingredients(recipe_list)

        core_functions.view_recipes(result_list)

        print("\nOptions: ")
        print("1. Search more recipes")
        print("2. View recipe details")
        print("3. Back to Main Menu")
        selected_option = int(input("\nWhat would you like to do? : "))

        match selected_option:
            case 1:
                recipe_search_menu(result_list)
            case 2:
                selected_recipe = int(input("\nWhich recipe would you like to view? : "))
                result_list[selected_recipe - 1].view_recipe_details()

                recipe_title = result_list[selected_recipe - 1].title
                recipe_search_submenu(recipe_list, recipe_title)
            case 3:
                back_to_main_menu = True


def recipe_search_submenu(recipe_list, recipe_title):
    back_to_previous_menu = False

    while not back_to_previous_menu:
        print("\nOptions: ")
        print("1. Edit recipe")
        print("2. Delete recipe")
        print("3. Back to Previous Menu")
        print("4. Back to Main Menu")
        selected_option = int(input("\nWhat would you like to do? : "))

        match selected_option:
            case 1:
                # selected_option = int(input("\nWhich recipe would you like to edit? : "))
                # recipe_title = result_list[selected_option - 1].title()
                recipe_index = core_functions.find_recipe_index(recipe_list, recipe_title)
                recipe_edit_menu(recipe_list, recipe_index)
            case 2:
                # selected_option = int(input("\nWhich recipe would you like to delete? : "))
                # recipe_title = result_list[selected_option - 1].title()
                recipe_index = core_functions.find_recipe_index(recipe_list, recipe_title)
                core_functions.delete_recipe(recipe_list, recipe_index)
                back_to_previous_menu = True
            case 3:
                back_to_previous_menu = True
            case 4:
                main_menu(recipe_list)

