"""Module that facilities the automatic generation and execution of OGR models using ampl."""


from shutil import which
from .exceptions import AMPLNotFound
from .exploration import GolombRuler
from .ampl import ogr_integer_lp
from .solvers import AMPLSolver
from enum import Enum
from collections.abc import Callable

# First check if ampl exists on this machine
_AMPL_PATH = which("ampl")
if _AMPL_PATH is None:
    raise AMPLNotFound

if __name__ == '__main__':
    full_path = which("ampl")
    full_path_fail = which("fake_executable")

class Formulations(Enum):
    """Class to represent the different formulations presented in our paper."""
    IntegerLinearProgram = 1
    IntegerLinearProgramRelaxation = 2
    ConstraintProgram = 3
    QuadraticProgram = 4

    def callback(self) -> Callable[[int, int, AMPLSolver], str]:
        """Return the function that generates the AMPL source code implementing this formulation."""
        if self == Formulations.IntegerLinearProgram:
            return ogr_integer_lp




def solve(order: int, upper_bound: int = None, formulation = Formulations.IntegerLinearProgram, solver: AMPLSolver = AMPLSolver.CPLEX) -> GolombRuler:
    """Attempt to solve an instance of the OGR with `order` marks and """
    if upper_bound is None:
        upper_bound = 2 ** (order - 1) - 1

    ampl_source_code_callback = formulation.callback()

    source_code = ampl_source_code_callback(order, upper_bound, solver)

    print(source_code)






