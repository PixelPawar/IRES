import subprocess
from speech import say

def open_application(query):
    apps = {
    "notepad": {
        "command": "notepad.exe",
        "display": "Notepad"
    },
    "paint": {
        "command": "mspaint.exe",
        "display": "Paint"
    },
    "calculator": {
        "command": "calc.exe",
        "display": "Calculator"
    },
    "file explorer": {
        "command": "explorer.exe",
        "display": "File Explorer"
    }
}

    for name, app in apps.items():
        if f"open {name}" in query:
            say(f"Opening {app['display']}")

            try:
                subprocess.Popen(app["command"])
                return True

            except Exception as e:
                say(f"Unable to open {app['display']}")
                print(e)
                return True

    return False

