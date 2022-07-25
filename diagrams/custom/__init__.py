"""
Custom provides the possibility of load an image to be presented as a node.
"""

from diagrams import Node
from urllib.request import urlopen
from typing import Dict
import hashlib

class Custom(Node):
    _provider = "custom"
    _type = "custom"
    _icon_dir = None

    fontcolor = "#ffffff"

    def _load_icon(self):
        return self._icon

    def __init__(self, label, icon_path, **attrs: Dict):
        if icon_path.startswith('data:image/'):
            with urlopen(icon_path) as response:
                data = response.read()
                icon_path = "/tmp/" + hashlib.md5(data).hexdigest()
                with open(icon_path, "wb") as f:
                    f.write(data)
                    f.close()
        self._icon = icon_path
        super().__init__(label, **attrs)
