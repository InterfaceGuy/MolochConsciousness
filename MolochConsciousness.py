import importlib
import pydeation.imports
importlib.reload(pydeation.imports)
from pydeation.imports import *
from DomesticatedMind.DomesticatedMind import DomesticatedMind3D


class MolochConsciousness(CustomObject):

    def specify_parts(self):
        self.domesticated_mind = DomesticatedMind3D()
        self.triangle = Triangle(plane="xy", radius=125, y=-5, color=BLUE)

        self.parts += [self.domesticated_mind, self.triangle]

    def specify_creation(self):
        creation_action = XAction(
            Movement(self.domesticated_mind.creation_parameter, (0, 1), part=self.domesticated_mind),
            Movement(self.triangle.creation_parameter, (1/3, 1), part=self.triangle),
            target=self, completion_parameter=self.creation_parameter, name="Creation")

    def specify_parameters(self):
        self.tilt_triangle_parameter = UCompletion(name="TiltTriangle", default_value=0)
        self.parameters += [self.tilt_triangle_parameter]

    def specify_relations(self):
        self.tilt_triangle_relation = XRelation(
            part=self.triangle,
            whole=self,
            desc_ids=[ROT_P],
            parameters=[self.tilt_triangle_parameter],
            formula=f"PI/2 * {self.tilt_triangle_parameter.name}"
            )
        self.lower_triangle_relation = XRelation(
            part=self.triangle,
            whole=self,
            desc_ids=[POS_Y],
            parameters=[self.tilt_triangle_parameter],
            formula=f"-50 * {self.tilt_triangle_parameter.name}"
            )

    def specify_action_parameters(self):
        self.tilt_triangle_action_parameter = UCompletion(name="TiltTriangleAction", default_value=0)
        self.action_parameters += [self.tilt_triangle_action_parameter]

    def specify_actions(self):
        tilt_triangle_action = XAction(
            Movement(self.tilt_triangle_parameter, (0, 1), part=self),
            target=self, completion_parameter=self.tilt_triangle_action_parameter, name="Tilt Triangle")


if __name__ == "__main__":
    moloch_consciousness = MolochConsciousness()