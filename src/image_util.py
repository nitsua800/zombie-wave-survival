from pathlib import Path
from os import path

def getImage(fileName):
    root = Path(path.dirname(__file__)).parent / "assets" / fileName
    if root.exists():
        return str(root)
    else:
        return "No image"
