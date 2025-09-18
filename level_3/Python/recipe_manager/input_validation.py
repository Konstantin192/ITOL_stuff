"""
Summary:
    Validates user input when selecting options from a defined options list.
Args:
    user_input (string): The menu selected by the user.
    valid_inputs (array): The valid menu selection options.
Returns:
    input_validated (bool): Whether the user input has been validated.
"""
def menu_input_validation(user_input, valid_inputs):
    user_input_is_int = user_input.isdigit()

    if user_input_is_int:
        user_input = int(user_input)

    if user_input in valid_inputs:
        input_validated = True
    else:
        input_validated = False

    return input_validated


"""
Summary:
    Validates the user input when selecting from a variable list, e.g. the recipe list which can have an unspecified number of recipes.
Args:
    user_input (string): The recipe selected by the user
    recipe_list (list): The list containing all of the data of all recipes (title, ingredients, instructions)
Returns:
    input_validated (bool): Whether the user input has been validated.
"""
def recipe_input_validation(user_input, recipe_list):
    user_input_is_int = user_input.isdigit()

    if user_input_is_int:
        user_input = int(user_input)

        if user_input > 0 and user_input <= len(recipe_list):
            input_validated = True
        else:
            input_validated = False
    else:
        input_validated = False

    return input_validated
