"""Exceptions."""


class NotGolombRuler(Exception):
    """Indicates that the passed sequence does not satisfy the conditions of a Golomb Ruler."""


class AMPLNotFound(Exception):
    """Indicates that the ampl executable is not found on this system."""

class FormulationNotImplemented(Exception):
    """Used to indicate that the formulation has not yet been implemented in AMPL."""