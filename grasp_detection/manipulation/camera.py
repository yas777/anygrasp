from dataclasses import dataclass
from typing import Type

import numpy as np
from PIL import Image

@dataclass
class CameraParmaters:
    fx: float
    fy: float
    cx: float
    cy: float
    image: Type[Image.Image]
    colors: np.ndarray
    depths: np.ndarray
    headtilt: float
