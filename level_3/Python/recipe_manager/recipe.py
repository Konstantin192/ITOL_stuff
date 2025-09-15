import input_validation

class Recipe:
    def __init__(self, title, ingredients_list, instructions):
        self.title = title
        self.ingredients_list = ingredients_list
        self.instructions = instructions

    def view_recipe_details(self):
        print("\nTitle:")
        print(f"{self.title} \n")

        print("Ingredients:")
        self.view_ingredients()
        print("")

        print("Instructions:")
        self.view_instructions()
        print("")


    def change_title(self):
        old_title = self.title

        print("Current title: " + self.title)
        new_title = input("Enter new title: ")
        self.title = new_title

        print(f"Title changed FROM {old_title} TO {new_title}")


    def view_ingredients(self):
        if len(self.ingredients_list) == 0:
            print("No ingredients")

        else:
            for ingredient in self.ingredients_list:
                print(f"{self.ingredients_list.index(ingredient) + 1}. {ingredient}")


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


    def remove_ingredients(self):
        valid_inputs = [1, 2]

        print("\nCurrent ingredient list: ")
        self.view_ingredients()
        remove_more_ingredients = True

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

            while not input_validated:
                user_input = input("\nWould you like to remove another ingredient?: \n1. Yes \n2. No \n")

                input_validated = input_validation.menu_input_validation(user_input, valid_inputs)

                if input_validated:
                    if int(user_input) == 2:
                        remove_more_ingredients = False
                else:
                    print("\nInvalid input. Please try again.")


    def change_ingredients(self):
        valid_inputs = [1, 2]

        print("\nCurrent ingredient list: ")
        self.view_ingredients()
        change_more_ingredients = True

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


    def view_instructions(self):
        if len(self.instructions) == 0:
            print("No instructions")

        else:
            for instruction in self.instructions:
                print(f"{self.instructions.index(instruction) + 1}. {instruction}")


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


    def remove_instructions(self):
        valid_inputs = [1, 2]

        print("Current instruction list: ")
        self.view_instructions()
        remove_more_instructions = True

        while remove_more_instructions:
            instruction_input_validated = False
            input_validated = False

            while not instruction_input_validated:
                instruction_to_remove = input("Enter index of instruction to remove: ")
                instruction_to_remove_is_int = instruction_to_remove.isdigit()

                if instruction_to_remove_is_int:
                    instruction_to_remove = int(instruction_to_remove)

                    if instruction_to_remove > 0 and instruction_to_remove <= len(self.instructions):
                        instruction_input_validated = True
                        self.instructions.pop(instruction_to_remove - 1)
                        print("New instruction list: ")
                        self.view_instructions()
                    else:
                        print("\nInvalid input. Please try again.")
                else:
                    print("\nInvalid input. Please try again.")

            while not input_validated:
                user_input = input("Would you like to remove another instruction?: \n1. Yes \n2. No \n")
                user_input_is_int = user_input.isdigit()

                if user_input_is_int:
                    user_input = int(user_input)

                if user_input in valid_inputs:
                    input_validated = True

                    if user_input == 2:
                        remove_more_instructions = False
                else:
                    print("\nInvalid input. Please try again.")


    def change_instructions(self):
        valid_inputs = [1, 2]

        print("\nCurrent instruction list: ")
        self.view_instructions()
        change_more_instructions = True

        while change_more_instructions:
            instruction_input_validated = False
            user_input_validated = False

            while not instruction_input_validated:
                selected_instruction = input("\nSelect index of instruction to change: ")
                selected_instruction_is_int = selected_instruction.isdigit()

                if selected_instruction_is_int:
                    selected_instruction = int(selected_instruction)

                    if selected_instruction > 0 and selected_instruction <= len(self.instructions):
                        instruction_input_validated = True

                        new_instruction = input("\nEnter new instruction: ")
                        self.instructions[int(selected_instruction) - 1] = new_instruction
                        print("\nNew instruction list:")
                        self.view_instructions()
                    else:
                        print("\nInvalid input. Please try again.")
                else:
                    print("\nInvalid input. Please try again.")

            while not user_input_validated:
                user_input = input("\nWould you like to change another instruction?: \n1. Yes \n2. No \n")
                user_input_is_int = user_input.isdigit()

                if user_input_is_int:
                    user_input = int(user_input)

                if user_input in valid_inputs:
                    user_input_validated = True

                    if user_input == 2:
                        change_more_instructions = False
                else:
                    print("\nInvalid input. Please try again.")