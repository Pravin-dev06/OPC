from pathlib import Path
import os

name = Path.home()

path = f"{Path.home()}/opc/.config"

print("path exists" if os.path.exists(path) else "no create it please")
