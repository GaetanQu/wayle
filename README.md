<h3 align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/logos/exports/1544x1544_circle.png" width="100" alt="Logo"/><br/>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
	Catppuccin for <a href="https://github.com/wayle-rs/wayle">Wayle</a>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
</h3>

<p align="center">
	<a href="https://github.com/GaetanQu/wayle/stargazers"><img src="https://img.shields.io/github/stars/GaetanQu/wayle?colorA=363a4f&colorB=b7bdf8&style=for-the-badge"></a>
	<a href="https://github.com/GaetanQu/wayle/issues"><img src="https://img.shields.io/github/issues/GaetanQu/wayle?colorA=363a4f&colorB=f5a97f&style=for-the-badge"></a>
	<a href="https://github.com/GaetanQu/wayle/contributors"><img src="https://img.shields.io/github/contributors/GaetanQu/wayle?colorA=363a4f&colorB=a6da95&style=for-the-badge"></a>
</p>

<p align="center">
	<img src="./assets/preview.webp"/>
</p>

## Previews

<details>
<summary>🌻 Latte</summary>
<img src="./assets/latte.webp"/>
</details>
<details>
<summary>🪴 Frappé</summary>
<img src="./assets/frappe.webp"/>
</details>
<details>
<summary>🌺 Macchiato</summary>
<img src="./assets/macchiato.webp"/>
</details>
<details>
<summary>🌿 Mocha</summary>
<img src="./assets/mocha.webp"/>
</details>

## Usage
### *There are two ways to style Wayle with Catppuccin*
### **You can either download and set a theme manually**
1. Download the [flavor](./themes) of your choice.
2. Copy the whole *[[styling.palette]]* section and paste it into *~/.config/wayle/config.toml*
### **Or create your own theme files with the CLI**
> ⚠️ Requires Python ≥ 3.12 and pipx recommended for CLI usage.
### 🚀 With pipx (recommended)
```sh
pipx install https://github.com/GaetanQu/wayle/releases/download/v0.1.0/wayle_ctp-0.1.0-py3-none-any.whl # First install the CLI

wayle-ctp # Then you can run it whenever you want with this command
```
### 📜 With poetry
```sh
wget https://github.com/GaetanQu/wayle/releases/download/v0.1.0/wayle_ctp-0.1.0.tar.gz # Install the latest release

tar -xzf wayle_ctp-0.1.0.tar.gz # Extract the archive

cd wayle_ctp-0.1.0 # cd into extracted folder

poetry install # Install dependencies

poetry run wayle-ctp # Run the CLI
```


<!-- The FAQ section is optional. Remove if needed.-->
## 🙋 FAQ

- Q: **_"How do I configure Wayle ?"_**\
  A: Take a look to the [wayle repository](https://github.com/wayle-rs/wayle) or to *~/.config/wayle/config.toml.example*. You will see all the available options, try them, and enjoy ! (Since Wayle is still a WIP project, there is no wiki yet)

## 💝 Thanks to

- [GaetanQu](https://github.com/GaetanQu)

&nbsp;

<p align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/footers/gray0_ctp_on_line.svg?sanitize=true" />
</p>

<p align="center">
	Copyright &copy; 2021-present <a href="https://github.com/catppuccin" target="_blank">Catppuccin Org</a>
</p>

<p align="center">
	<a href="https://github.com/catppuccin/catppuccin/blob/main/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a>
</p>
