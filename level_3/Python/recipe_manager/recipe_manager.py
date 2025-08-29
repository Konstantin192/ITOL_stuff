import core_functions


def main():
    recipe_list = list()

    core_functions.add_recipe(recipe_list,
                              "Salad",
                              ["cucumbers", "tomatoes", "cow cheese"],
                              ["cut ingredients", "mix ingredients"])
    core_functions.add_recipe(recipe_list,
                              "Salmon with potatoes and carrots",
                              ["salmon fillet", "carrots, potatoes"],
                              ["cut ingredients", "season ingredients", "put into air fryer"])
    core_functions.add_recipe(recipe_list,
                              "Vegetable fried rice",
                              ["rice", "red onions", "bell peper", "spring onion", "frozen peas", "eggs", "soy sauce", "sesame seed oil"],
                              ["boil rice", "mix rice with vegetables and sauces", "put in air fryer"])

    # core_functions.view_recipes(recipe_list)
    # core_functions.search_recipe_titles(recipe_list, "Salmon")
    # core_functions.search_recipe_ingredients(recipe_list, "rice")
    # core_functions.delete_recipe(recipe_list, 0)

if __name__ == "__main__":
    main()

