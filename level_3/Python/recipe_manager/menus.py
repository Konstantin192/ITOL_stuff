import core_functions

def main_menu(recipe_list):
    print("\nWelcome to Recipe Manager")
    print("1. View Recipes")
    print("2. Add Recipes")
    print("3. Edit Recipes")
    print("4. Delete Recipes")
    print("5. Search Recipes")
    print("6. Exit")

    option_selected = int(input("\nWhat would you like to do? : "))

    match option_selected:
        case 1:
            core_functions.view_recipes(recipe_list)
            selected_recipe = int(input("\nSelect recipe to view: "))
            recipe_list[selected_recipe - 1].view_recipe_details()
        case 2:
            core_functions.add_recipe(recipe_list)
        # ToDo split into smaller functions
        case 3:
            core_functions.view_recipes(recipe_list)
            selected_recipe = int(input("\nSelect recipe to edit: "))
            recipe_list[selected_recipe - 1].view_recipe_details()

            print("Recipe edit options: ")
            print("1. Change title")
            print("2. Edit ingredients")
            print("3. Edit instructions")
            selected_edit = int(input("\nWhat would you like to do? : "))

            match selected_edit:
                case 1:
                    recipe_list[selected_recipe - 1].change_title()
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
        case 4:
            print("\nCurrent recipes")
            core_functions.view_recipes(recipe_list)
            selected_recipe_delete = int(input("\nWhich would you like to delete? : "))

            core_functions.delete_recipe(recipe_list, selected_recipe_delete - 1)

