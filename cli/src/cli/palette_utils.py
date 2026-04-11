from catppuccin import PALETTE
import unicodedata
from InquirerPy import inquirer

# Change "Frappé" to Frappe
def _remove_accents(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    return "".join(c for c in normalized if not unicodedata.combining(c))

# Get the names of all the colors of the palette
def _get_all_colors():
    return [color.name for color in PALETTE.mocha.colors]

# Allow the user to select from every colors of the palette
def fuzzy_all_colors():
    try:
        choice = inquirer.fuzzy(
            message="Here are all the available colors! Have fun!",
            choices= _get_all_colors() + ["Back"]
        ).execute()

        if choice == "Back":
            return "__back__"
    
        return choice
    except KeyboardInterrupt:
        return 0