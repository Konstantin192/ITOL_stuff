class Recipe:
    def __init__(self, title, ingredients_list, instructions):
        self.title = title
        self.ingredients_list = ingredients_list
        self.instructions = instructions


    def change_title(self):
        old_title = self.title

        print("Current title: " + self.title)
        new_title = input("Enter new title: ")
        self.title = new_title

        print(f"Title changed FROM {old_title} TO {new_title}")


    def view_ingredients(self):
        for ingredient in self.ingredients_list:
            print(f"{self.ingredients_list.index(ingredient) + 1}. {ingredient}")


    def add_ingredients(self):
        print("Current ingredient list: ")
        self.view_ingredients()
        add_more_ingredients = 1

        while add_more_ingredients == 1:
            new_ingredient = input("Enter new ingredient: ")
            self.ingredients_list.append(new_ingredient)

            print("New ingredient list: ")
            self.view_ingredients()

            add_more_ingredients = int(input("Would you like to add another ingredient?: \n1. Yes \n2. No \n"))


    def remove_ingredients(self):
        print("Current ingredient list: ")
        self.view_ingredients()
        remove_more_ingredients = 1

        while remove_more_ingredients == 1:
            ingredient_to_remove = int(input("Enter index of ingredient to remove: "))
            self.ingredients_list.pop(ingredient_to_remove - 1)

            print("New ingredient list: ")
            self.view_ingredients()

            remove_more_ingredients = int(input("Would you like to remove another ingredient?: \n1. Yes \n2. No \n"))


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