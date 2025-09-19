# Recipe Manager

## Summary:
The recipe manager allows the creation, editing, deletion and viewing of recipes.

Each recipe contains a title, list of ingredients and a list of instructions.

During the application sessions recipes are stored within a list.
Upon closing the application session the recipes are saved to a text file, recipe_list.txt, stored in the same folder as
the application.
Upon launching the application the stored recipes, if there are any, are loaded from the text file into the application.

Unexpected errors are logged to an error log file, error_log.txt, located in the same folder as the application.

## How to use:
To launch the application go into the "dist" folder, in there should be located the recipe_manager.exe

Follow the application prompts for the required user inputs.

When being asked to select an option from a menu or a list enter the on-screen number corresponding to the option.
