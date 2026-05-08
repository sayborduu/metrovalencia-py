from importlib.metadata import version

from metrovalencia.client import MetroValencia
from metrovalencia import exceptions

__version__ = version("metrovalencia")

__all__ = ["MetroValencia", "exceptions"]