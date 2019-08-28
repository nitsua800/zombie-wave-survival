import os
from pathlib import Path

def getImage(fileName):
    root = Path(os.path.dirname(__file__)).parent
    print(root)
    return root
