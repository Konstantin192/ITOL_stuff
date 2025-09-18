import input_validation

"""
Summary:
    A recipe
Attributes:
    title (str): The title of the recipe
    ingredients_list (list): The ingredients of the recipe
    instructions (list): The instructions for the recipe
"""
class Recipe:
    def __init__(self, title, ingredients_list, instructions):
        self.title = title
        self.ingredients_list = ingredients_list
        self.instructions = instructions

    """
    Summary:
        Provides the user with the full details of the recipe
    Args:
        self (Recipe): The Recipe for which to view the details
    """
    def view_recipe_details(self):
        print("\nTitle:")
        print(f"{self.title} \n")

        print("Ingredients:")
        self.view_ingredients()
        print("")

        print("Instructions:")
        self.view_instructions()
        print("")


    """
    Summary:
        Allows the user to change the title of the recipe
    Args:
        self (Recipe): The Recipe of which to change the title
    """
    def change_title(self):
        old_title = self.title

        print("Current title: " + self.title)
        new_title = input("Enter new title: ")
        self.title = new_title

        print(f"Title changed FROM {old_title} TO {new_title}")


    """
    Summary:
        Provides the list of ingredients of the recipe to the user
    Args:
        self (Recipe): The Recipe for which to view the ingredients
    """
    def view_ingredients(self):
        if len(self.ingredients_list) == 0:
            print("No ingredients")

        else:
            for ingredient in self.ingredients_list:
                print(f"{self.ingredients_list.index(ingredient) + 1}. {ingredient}")


    """
    Summary:
        Allows the user to add ingredients to the recipe
    Args:
        self (Recipe): The Recipe of which to change the title
    """
    def add_ingredients(self):
        valid_inputs = [1, 2]

        print("\nCurrent ingredient list: ")
        self.view_ingredients()
        add_more_ingredients = True

        while add_more_ingredients:
            new_ingredient = input("\nEnter new ingredient: ")
            self.ingredients_list.append(new_ingredient)

            print("\nNew ingredient list: ")
            self.view_ingredients()

            input_validated = False

            while not input_validated:
                user_input = input("\nWould you like to add another ingredient ? : \n1. Yes \n2. No \n")

                input_validated = input_validation.menu_input_validation(user_input, valid_inputs)

                if input_validated:
                    if int(user_input) == 2:
                        add_more_ingredients = False
                else:
                    print("\nInvalid input. Please try again.")


    """
    Summary:
        Allows the user to remove ingredients from the recipe
    Args:
        self (Recipe): The Recipe from which to remove ingredients
    """
    def remove_ingredients(self):
        valid_inputs = [1, 2]

        print("\nCurrent ingredient list: ")
        self.view_ingredients()
        remove_more_ingredients = True

        if len(self.ingredients_list) == 0:
            remove_more_ingredients = False

        while remove_more_ingredients:
            ingredient_input_validated = False
            input_validated = False

            while not ingredient_input_validated:
                ingredient_to_remove = input("\nEnter index of ingredient to remove: ")

                ingredient_input_validated = input_validation.recipe_input_validation(ingredient_to_remove, self.ingredients_list)

                if ingredient_input_validated:
                    self.ingredients_list.pop(int(ingredient_to_remove) - 1)
                    print("\nNew ingredient list: ")
                    self.view_ingredients()
                else:
                    print("\nInvalid input. Please try again.")

            if len(self.ingredients_list) == 0:
                remove_more_ingredients = False
                break

            while not input_validated:
                user_input = input("\nWould you like to remove another ingredient?: \n1. Yes \n2. No \n")

                input_validated = input_validation.menu_input_validation(user_input, valid_inputs)

                if input_validated:
                    if int(user_input) == 2:
                        remove_more_ingredients = False
                else:
                    print("\nInvalid input. Please try again.")


    """
    Summary:
        Allows the user to change existing ingredients from the recipe
    Args:
        self (Recipe): The Recipe of which to change ingredients
    """
    def change_ingredients(self):
        valid_inputs = [1, 2]

        print("\nCurrent ingredient list: ")
        self.view_ingredients()
        change_more_ingredients = True

        if len(self.ingredients_list) == 0:
            change_more_ingredients = False

        while change_more_ingredients:
            ingredient_input_validated = False
            user_input_validated = False

            while not ingredient_input_validated:
                selected_ingredient = input("\nSelect ingredient to change: ")

                ingredient_input_validated = input_validation.recipe_input_validation(selected_ingredient, self.ingredients_list)

                if ingredient_input_validated:
                    new_ingredient = input("\nEnter new ingredient: ")
                    self.ingredients_list[int(selected_ingredient) - 1] = new_ingredient

                    print("\nNew ingredient list:")
                    self.view_ingredients()
                else:
                    print("\nInvalid input. Please try again.")

            while not user_input_validated:
                user_input = input("\nWould you like to change another ingredient?: \n1. Yes \n2. No \n")

                user_input_validated = input_validation.menu_input_validation(user_input, valid_inputs)

                if user_input_validated:
                    if int(user_input) == 2:
                        change_more_ingredients = False
                else:
                    print("\nInvalid input. Please try again.")


    """
    Summary:
        Allows the user to view the instructions of the recipe
    Args:
        self (Recipe): The Recipe of which to view the instructions
    """
    def view_instructions(self):
        if len(self.instructions) == 0:
            print("No instructions")

        else:
            for instruction in self.instructions:
                print(f"{self.instructions.index(instruction) + 1}. {instruction}")


    """
    Summary:
        Allows the user to add instructions to the recipe
    Args:
        self (Recipe): The Recipe for which to add instructions
    """
    def add_instructions(self):
        valid_inputs = [1, 2]

        print("\nCurrent instruction list: ")
        self.view_instructions()
        add_more_instructions = True

        while add_more_instructions:
            new_instruction = input("\nEnter new instruction: ")
            self.instructions.append(new_instruction)

            print("\nNew instruction list: ")
            self.view_instructions()

            input_validated = False

            while not input_validated:
                user_input = input("\nWould you like to add another instruction?: \n1. Yes \n2. No \n")

                input_validated = input_validation.menu_input_validation(user_input, valid_inputs)

                if input_validated:
                    if int(user_input) == 2:
                        add_more_instructions = False
                else:
                    print("\nInvalid input. Please try again.")


    """
    Summary:
        Allows the user to remove instructions from the recipe
    Args:
        self (Recipe): The Recipe from which to remove instructions
    """
    def remove_instructions(self):
        valid_inputs = [1, 2]

        print("\nCurrent instruction list: ")
        self.view_instructions()
        remove_more_instructions = True

        if len(self.instructions) == 0:
            remove_more_instructions = False

        while remove_more_instructions:
            instruction_input_validated = False
            input_validated = False

            while not instruction_input_validated:
                instruction_to_remove = input("\nEnter index of instruction to remove: ")

                instruction_input_validated = input_validation.recipe_input_validation(instruction_to_remove, self.instructions)

                if instruction_input_validated:
                    self.instructions.pop(int(instruction_to_remove) - 1)
                    print("\nNew instruction list: ")
                    self.view_instructions()
                else:
                    print("\nInvalid input. Please try again.")

            if len(self.instructions) == 0:
                remove_more_instructions = False
                break

            while not input_validated:
                user_input = input("\nWould you like to remove another instruction?: \n1. Yes \n2. No \n")

                input_validated = input_validation.menu_input_validation(user_input, valid_inputs)

                if input_validated:
                    if int(user_input) == 2:
                        remove_more_instructions = False
                else:
                    print("\nInvalid input. Please try again.")


    """
    Summary:
        Allows the user to change existing instructions of the recipe
    Args:
        self (Recipe): The Recipe of which to change the instructions
    """
    def change_instructions(self):
        valid_inputs = [1, 2]

        print("\nCurrent instruction list: ")
        self.view_instructions()
        change_more_instructions = True

        if len(self.instructions) == 0:
            change_more_instructions = False

        while change_more_instructions:
            instruction_input_validated = False
            user_input_validated = False

            while not instruction_input_validated:
                selected_instruction = input("\nSelect instruction to change: ")

                instruction_input_validated = input_validation.recipe_input_validation(selected_instruction, self.instructions)

                if instruction_input_validated:
                    new_instruction = input("\nEnter new instruction: ")
                    self.instructions[int(selected_instruction) - 1] = new_instruction
                    print("\nNew instruction list:")
                    self.view_instructions()
                else:
                    print("\nInvalid input. Please try again.")

            while not user_input_validated:
                user_input = input("\nWould you like to change another instruction?: \n1. Yes \n2. No \n")

                user_input_validated = input_validation.menu_input_validation(user_input, valid_inputs)

                if user_input_validated:
                    if int(user_input) == 2:
                        change_more_instructions = False
                else:
                    print("\nInvalid input. Please try again.")