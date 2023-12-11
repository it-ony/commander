import adsk.core
import adsk.fusion

from .base import RunningCommandBase, Action


def toggleVisibility(occurrence: adsk.fusion.Occurrence, visibility: bool):
    occurrence.isLightBulbOn = visibility

    for occurrence in occurrence.childOccurrences:
        occurrence.isLightBulbOn = visibility

    for body in occurrence.component.bRepBodies:
        body.isVisible = visibility


class VisibilityAll(RunningCommandBase):
    def onExecute(self, args: adsk.core.CommandEventArgs):
        # noinspection PyUnresolvedReferences
        app = adsk.core.Application.get()

        design: adsk.fusion.Design = app.activeProduct

        for component in design.allComponents:
            for occurrence in component.allOccurrences:
                # noinspection PyUnresolvedReferences
                toggleVisibility(occurrence, self.Visibility)


class Visibility(RunningCommandBase):
    def onExecute(self, args: adsk.core.CommandEventArgs):
        # noinspection PyUnresolvedReferences
        app = adsk.core.Application.get()

        design: adsk.fusion.Design = app.activeProduct

        # noinspection PyUnresolvedReferences
        toggleVisibility(design.activeOccurrence, self.Visibility)


def visibility(visible: bool):
    return type(f"Visibility{visible}", (Visibility,), {"Visibility": visible})


def visibilityAll(visible: bool):
    return type(f"VisibilityAll{visible}", (VisibilityAll,), {"Visibility": visible})


viewActions = [
    Action("Show", "Show", "Show children", visibility(True)),
    Action("Hide", "Hide", "Hide children", visibility(False)),

    Action("ShowAll", "Show all", "Show all children", visibilityAll(True)),
    Action("HideAll", "Hide all", "Hide all children", visibilityAll(False))
]
