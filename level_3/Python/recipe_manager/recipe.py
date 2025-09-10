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

        print("Current ingredient list: ")
        self.view_ingredients()
        add_more_ingredients = True

        while add_more_ingredients:
            new_ingredient = input("Enter new ingredient: ")
            self.ingredients_list.append(new_ingredient)

            print("New ingredient list: ")
            self.view_ingredients()

            input_validated = False

            while not input_validated:
                user_input = input("\nWould you like to add another ingredient ? : \n1. Yes \n2. No \n")
                user_input_is_int = user_input.isdigit()

                if user_input_is_int:
                    user_input = int(user_input)

                if user_input in valid_inputs:
                    input_validated = True

                    if user_input == 2:
                        add_more_ingredients = False
                else:
                    print("\nInvalid input. Please try again.")


    def remove_ingredients(self):
        valid_inputs = [1, 2]

        print("Current ingredient list: ")
        self.view_ingredients()
        remove_more_ingredients = True

        while remove_more_ingredients == 1:
            ingredient_to_remove = int(input("Enter index of ingredient to remove: "))
            self.ingredients_list.pop(ingredient_to_remove - 1)

            print("New ingredient list: ")
            self.view_ingredients()

            input_validated = False

            while not input_validated:
                user_input = input("Would you like to remove another ingredient?: \n1. Yes \n2. No \n")
                user_input_is_int = user_input.isdigit()

                if user_input_is_int:
                    user_input = int(user_input)

                if user_input in valid_inputs:
                    input_validated = True

                    if user_input == 2:
                        remove_more_ingredients = False
                else:
                    print("\nInvalid input. Please try again.")


    def change_ingredients(self):
        print("Current ingredient list: ")
        self.view_ingredients()
        change_more_ingredients = 1

        while change_more_ingredients == 1:
            selected_ingredient = input("Select index of ingredient to change: ")
            new_ingredient = input("Enter new ingredient: ")

            self.ingredients_list[int(selected_ingredient) - 1] = new_ingredient

            print("New ingredient list:")
            self.view_ingredients()

            change_more_ingredients = int(input("Would you like to change another ingredient?: \n1. Yes \n2. No \n"))


    def view_instructions(self):
        if len(self.instructions) == 0:
            print("No instructions")

        else:
            for instruction in self.instructions:
                print(f"{self.instructions.index(instruction) + 1}. {instruction}")


    def add_instructions(self):
        print("Current instruction list: ")
        self.view_instructions()
        add_more_instructions = 1

        while add_more_instructions == 1:
            new_instruction = input("Enter new instruction: ")
            self.instructions.append(new_instruction)

            print("New instruction list: ")
            self.view_instructions()

            add_more_instructions = int(input("Would you like to add another instruction?: \n1. Yes \n2. No \n"))


    def remove_instructions(self):
        print("Current instruction list: ")
        self.view_instructions()
        remove_more_instructions = 1

        while remove_more_instructions == 1:
            instruction_to_remove = int(input("Enter index of instruction to remove: "))
            self.instructions.pop(instruction_to_remove - 1
                                  )
            print("New instruction list: ")
            self.view_instructions()

            remove_more_instructions = int(input("Would you like to remove another instruction?: \n1. Yes \n2. No \n"))


    def change_instructions(self):
        print("Current instruction list: ")
        self.view_instructions()
        change_more_instructions = 1

        while change_more_instructions == 1:
            selected_instruction = input("Select index of instruction to change: ")
            new_instruction = input("Enter new instruction: ")

            self.instructions[int(selected_instruction) - 1] = new_instruction

            print("New instruction list:")
            self.view_instructions()

            change_more_instructions = int(input("Would you like to change another instruction?: \n1. Yes \n2. No \n"))