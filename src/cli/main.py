# Functions imports
from cli.cli_helpers import *

# Config import
from cli.config import config

def main():
    main_menu = Menu(
        config = config,
        title = "Wayle CLI File Generator",
    )
    main_menu.run()
        

if __name__ == "__main__":
    main()