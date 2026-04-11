from catppuccin import PALETTE
import unicodedata
from pathlib import Path
import tomlkit


class ConfigManager():
    def __init__(self, config):
        self.config = config
        self.BASE_DIR = Path.home() / ".config" / "wayle"

    @property
    def palette(self):
        return self._normalize(self.config["palette"]["value"])

    @property
    def palette_obj(self):
        return getattr(PALETTE, self.palette)

    @property
    def all_colors(self):
        return self.palette_obj.colors

    @property
    def path(self):
        return (
            self.BASE_DIR
            / "themes"
            / "catppuccin"
            / f"catppuccin-{self.palette}.toml"
        )

    def _normalize(self, name: str) -> str:
        return "".join(
            c for c in unicodedata.normalize("NFKD", name)
            if not unicodedata.combining(c)
        ).lower()

    def _get_color_from_key(self, color: str):
        try:
            return getattr(self.all_colors, self._normalize(color)).hex
        except AttributeError:
            print(f"Unknown color: {color}")
            return "#000000"

    def generate_toml(self) -> list[str]:
        output = []
        output.append("[styling.palette]")

        for key, value in self.config.items():
            if key.lower() != "palette":
                output.append("")
                output.append(f"# {key.capitalize()}")

                for subkey, subvalue in value.items():
                    color = self._get_color_from_key(subvalue["value"])
                    output.append(
                        f"{subkey.replace('_', '-')} = \"{color}\" # {subvalue['value']}"
                    )

        return output

    def create_file(self):
        file = self.generate_toml()
        path = self.path  # ✅ local

        while True:
            answer = input(f"Generate file at {path} ? (Y/n/<e>dit path) ").lower()

            match answer:
                case "y" | "yes" | "":
                    if path.exists():
                        path = self._already_exists(path)

                    self._write_file(file, path)
                    print(f"File generated at {path} !")

                    self._apply_theme_prompt(path)
                    return self._continue_file_creation()

                case "n" | "no":
                    return

                case "e":
                    raw = input("New path: ").strip()

                    if raw:
                        if not raw.startswith("/"):
                            print("Path must be absolute")
                            continue
                        path = Path(raw)
                    else:
                        path = self.path

                case _:
                    print("Invalid choice")

    def _already_exists(self, path: Path) -> Path:
        while True:
            answer = input(
                f"{path} already exists. (O)verwrite / (r)ename / (c)ancel ? "
            ).lower()

            match answer:
                case "o" | "overwrite" | "":
                    return path

                case "r" | "rename":
                    new_name = input("New file name: ").strip()

                    if not new_name:
                        print("Invalid name")
                        continue

                    if not new_name.endswith(".toml"):
                        new_name += ".toml"

                    new_path = path.parent / new_name

                    if new_path.exists():
                        print("File already exists")
                        continue

                    return new_path

                case "c" | "cancel":
                    print("Canceled")
                    return path

                case _:
                    print("Invalid choice")

    def _write_file(self, content: list[str], path: Path):
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(content))

    def _apply_theme_prompt(self, path: Path):
        answer = input("Apply theme now ? (Y/n) ").strip().lower()

        if answer in ("y", "", "yes"):
            self.apply_theme(path)
            print("Theme applied !")

    def apply_theme(self, path: Path):
        wayle_config_path = self.BASE_DIR / "config.toml"
        themes_dir = self.BASE_DIR / "themes"
        theme_path = str(path)

        # Create config if missing
        if not wayle_config_path.exists():
            wayle_config_path.parent.mkdir(parents=True, exist_ok=True)
            wayle_config_path.write_text(
                f'imports = ["{theme_path}"]\n',
                encoding="utf-8"
            )
            return

        # Parse TOML
        try:
            doc = tomlkit.parse(
                wayle_config_path.read_text(encoding="utf-8")
            )
        except Exception:
            print("Warning: config.toml is invalit, resetting imports")
            dec = tomlkit.document()

        imports = list(doc.get("imports", []))

        # Remove old themes
        cleaned = []
        for imp in imports:
            try:
                p = Path(imp).expanduser()
                if not p.resolve().is_relative_to(themes_dir.resolve()):
                    cleaned.append(imp)
            except Exception:
                cleaned.append(imp)

        # Add new theme
        if theme_path not in cleaned:
            cleaned.append(theme_path)

        doc["imports"] = cleaned

        wayle_config_path.write_text(
            tomlkit.dumps(doc),
            encoding="utf-8"
        )

    def _continue_file_creation(self):
        answer = input("Continue creating files ? (y/N) ").lower()

        match answer:
            case "y":
                return
            case "n" | "":
                return 1