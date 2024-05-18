import importlib
import pydeation.imports
importlib.reload(pydeation.imports)
from pydeation.imports import *
from DomesticatedMind.DomesticatedMind import DomesticatedMind


class MolochConsciousness(CustomObject):

    def specify_parts(self):
        self.domesticated_mind = DomesticatedMind()
        self.triangle = Triangle(plane="xy", radius=125, y=-5, color=BLUE)

        self.parts += [self.domesticated_mind, self.triangle]

    def specify_creation(self):
        creation_action = XAction(
            Movement(self.domesticated_mind.creation_parameter, (1/3, 1), part=self.domesticated_mind),
            Movement(self.triangle.creation_parameter, (0, 2/3), part=self.triangle),
            target=self, completion_parameter=self.creation_parameter, name="Creation")