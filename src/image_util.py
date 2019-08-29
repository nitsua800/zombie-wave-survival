from pathlib import Path
from os import path

def getImage(fileName):
    root = Path(path.dirname(__file__)).parent / "assets" / fileName
    print(root)
    if root.exists():
        return str(root)
    else:
        return "No image"
