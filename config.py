from pathlib import Path

HOME = Path.home()

INDEX_FOLDERS = [
    HOME / "Desktop",
    HOME / "Documents",
    HOME / "Downloads",
    HOME / "Pictures",
]
# Speech Settings
SPEECH_RATE = 180
SPEECH_VOLUME = 1.0

# Supported Applications
APPLICATIONS = {
    "notepad": {
        "display": "Notepad",
        "command": "notepad.exe",
        "aliases": [
            "notepad",
            "note pad"
        ]
    },

    "calculator": {
        "display": "Calculator",
        "command": "calc.exe",
        "aliases": [
            "calculator",
            "calc"
        ]
    },

    "paint": {
        "display": "Paint",
        "command": "mspaint.exe",
        "aliases": [
            "paint",
            "mspaint"
        ]
    },

    "file explorer": {
        "display": "File Explorer",
        "command": "explorer.exe",
        "aliases": [
            "file explorer",
            "explorer",
            "files"
        ]
    },

    "vscode": {
        "display": "Visual Studio Code",
        "command": "code",
        "aliases": [
            "vscode",
            "vs code",
            "visual studio code",
            "code"
        ]
    },
    "chrome": {
        "display": "Google Chrome",
        "command": "chrome",
        "aliases": [
            "chrome",
            "google chrome"
        ]
    },

    "vscode": {
        "display": "Visual Studio Code",
        "command": "code",
        "aliases": [
            "vscode",
            "vs code",
            "visual studio code",
            "code"
        ]
    },

    "python": {
        "display": "Python",
        "command": "python",
        "aliases": [
            "python"
        ]
    },
    "chrome": {
    "display": "Google Chrome",
    "command": "chrome.exe",
    "aliases": [
        "chrome",
        "google chrome"
        ]
    },
}
