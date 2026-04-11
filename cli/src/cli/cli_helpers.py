from InquirerPy import inquirer
from InquirerPy.separator import Separator
import palette_utils
from config_manager import ConfigManager

class MenuOption():
    def __init__(self, label:str, action:callable = None, value:str = None):
        self.label:str = label
        self.action:callable = action
        self.value:str = value

class Menu:
    def __init__(self, config:dict, title:str, default:int = 0, node:dict = None, parent:Menu = None):
        self.config:dict = config
        self.title:str = title
        self.default:int = default
        self.node:dict = node
        self.options:list[MenuOption] = self._build_options(node)
        self.parent:Menu = parent
        self.configManager = ConfigManager(self.config)

    @property
    def ui_state(self):
        return {
            "palette_label": f"Palette : {self.config['palette']['value']}",
            "exit_label": "Exit"
        }

    def _select(self):
        choices = []
        for opt in self.options:
            if isinstance(opt, Separator):
                choices.append(Separator())
            else:
                label = opt.label
                if opt.label.lower() == "palette":
                    label = self.ui_state["palette_label"]

                if opt.label == "Back" and not self.parent:
                    label = self.ui_state["exit_label"]
                
                choices.append({
                    "name": label,
                    "value": opt
                })
        print("\033[2J\033[H", end="")
        try :
            return inquirer.select(
                message=self.title,
                choices=choices,
                default= self.default,
                qmark="ᓚᘏᗢ",
                amark="ᓚᘏᗢ",
                show_cursor=False,
                height=100,
            ).execute()
        except KeyboardInterrupt:
            return "__exit__"

    def run(self):
        while True:
            self.options = self._build_options(self.node)
            choice:MenuOption = self._select()

            result = choice.action()

            if result == "__back__":
                if self.parent:
                    return
                return self._exit()
            
            if result == "__exit__":
                return self._exit()

    def _set_value(self, value):
        self.node["value"] = value
        return "__back__"

    def _build_options(self, node:dict = None):
        options:list[MenuOption] = []

        if not node:
            for key in self.config:
                options.append(MenuOption(
                    label = key.capitalize(),
                    action = lambda k=key: self._open_child(k),
                ))
        else:
            # Container
            if isinstance(node, dict) and "value" not in node and "options" not in node:
                for key, value in node.items():
                    options.append(MenuOption(
                        label = f"{key} : {value['value']}",
                        action=lambda k=key: self._open_child(k),
                    ))
            # Leaf
            elif isinstance(node, dict) and "value" in node and "options" in node:
                for option in node["options"]:
                    options.append(MenuOption(
                        label = f"{option}",
                        action=lambda v=option: self._set_value(v)
                    ))
                if not node.get("disable_more"):
                    options.append(MenuOption(
                        label="More Colors",
                        action=lambda: self._fuzzy_all_values()
                    ))

        options.append(Separator())
        if not node:
            options.append(MenuOption(
                label = "Generate File !",
                action = lambda: self._generate_file()
            ))
        options.append(MenuOption(
            label = "Back",
            action = lambda: "__back__"
        ))

        return options

    def _generate_file(self):
        continue_file_generation = self.configManager.create_file()
        if continue_file_generation == 1:
            self._exit()

    def _fuzzy_all_values(self):
        return self._set_value(palette_utils.fuzzy_all_colors())

    def _open_child(self, key) -> None:
        source = self.node if self.node is not None else self.config
        child_node = source[key]
        child_menu = Menu(title = "Pick one", config = self.config, node = child_node, parent = self)

        child_menu.run()

    def _exit(self):
        print("Bye ! 👋")
        raise SystemExit