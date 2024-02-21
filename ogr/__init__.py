"""Module that facilitates the solving of OGR instances using AMPL."""

from .generation import generate_golomb_ruler_improved, generate_golomb_ruler_naive
from .models import solve
from .ruler import GolombRuler

__all__ = [
    "solve",
    "generate_golomb_ruler_improved",
    "generate_golomb_ruler_naive",
    "GolombRuler",
]
