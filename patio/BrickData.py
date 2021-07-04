from typing import Tuple
from dataclasses import dataclass


@dataclass
class BrickCircle:
    radius: float
    sector: float
    sides: int
    brick: Tuple[float, float]
