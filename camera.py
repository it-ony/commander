import adsk.core
import adsk.fusion

from .base import RunningCommandBase, Action

cameraPositions: dict[str, adsk.core.ViewOrientations] = {
    "Front": adsk.core.ViewOrientations.FrontViewOrientation,
    "Top": adsk.core.ViewOrientations.TopViewOrientation,
    "Right": adsk.core.ViewOrientations.RightViewOrientation,
    "Left": adsk.core.ViewOrientations.LeftViewOrientation,
    "Bottom": adsk.core.ViewOrientations.BottomViewOrientation
}


class CameraCommand(RunningCommandBase):
    def onExecute(self, args: adsk.core.CommandEventArgs):
        # noinspection PyUnresolvedReferences
        app = adsk.core.Application.get()

        cam = app.activeViewport.camera
        cam.isSmoothTransition = True

        # noinspection PyUnresolvedReferences
        cam.viewOrientation = self.position

        app.activeViewport.camera = cam


class CameraHome(RunningCommandBase):
    def onExecute(self, args: adsk.core.CommandEventArgs):
        app = adsk.core.Application.get()
        app.activeViewport.goHome()


def camera(name: str, position: adsk.core.ViewOrientations):
    return type(f"CameraCommand{name}", (CameraCommand,), {"position": position, "name": name})


home = Action("CameraHome", "Camera: Home", "Set the camera perspective to home", CameraHome)
cameraActions = [home] + [
    Action(f"Camera{key}", f"Camera: {key}", f"Set the camera perspective to {key}", camera(key, value))
    for key, value in cameraPositions.items()]
