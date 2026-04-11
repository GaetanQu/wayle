from catppuccin import PALETTE
from recommended import Recommended

Recommended = Recommended()

config = {
    "palette": {
        "value": "Mocha",
        "options": [flavor.name for flavor in PALETTE],
        "disable_more": True
    },

    "background": {
        "bg": {
            "value": "base",
            "options": Recommended.bg
        },
        "surface": {
            "value": "mantle",
            "options": Recommended.surface
        },
        "elevated": {
            "value": "surface0",
            "options": Recommended.elevated
        }
    },

    "foreground": {
        "primary": {
            "value": "text",
            "options": Recommended.primary
        },
        "fg": {
            "value": "text",
            "options": Recommended.fg
        },
        "fg_muted": {
            "value": "subtext0",
            "options": Recommended.fg_muted
        }
    },

    "accent": {
        "blue": {
            "value": "blue",
            "options": Recommended.blue
        },
        "green": {
            "value": "green",
            "options": Recommended.green
        },
        "red": {
            "value": "red",
            "options": Recommended.red
        },
        "yellow": {
            "value": "yellow",
            "options": Recommended.yellow
        }
    }
}