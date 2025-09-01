class Recipe:
    def __init__(self, title, ingredients_list, instructions):
        self.title = title
        self.ingredients_list = ingredients_list
        self.instructions = instructions

    def change_title(self, title):
        self.title = title

    def view_ingredients(self):
        for ingredient in self.ingredients_list:
            print(f"{self.ingredients_list.index(ingredient) + 1}. {ingredient}")

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