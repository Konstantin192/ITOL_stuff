def menu_input_validation(user_input, valid_inputs):
    user_input_is_int = user_input.isdigit()

    if user_input_is_int:
        user_input = int(user_input)

    if user_input in valid_inputs:
        input_validated = True
    else:
        input_validated = False

    return input_validated