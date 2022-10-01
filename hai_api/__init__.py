
import os, sys
from pathlib import Path
pydir = Path(os.path.abspath(__file__)).parent

try:
    import hai
except ImportError:
    sys.path.insert(0, f'{pydir.parent.parent}/hai')
    import hai


from .finet_api import *
