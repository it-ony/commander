from typing import Optional, List

from . import base
from . import util
from .camera import cameraActions
from .view import viewActions
from .log import logger

# Global variable to hold the add-in (created in run(), destroyed in stop())
addIn: Optional[base.AddIn] = None


class CommanderAddIn(base.AddIn):
    def _prefix(self) -> str:
        return 'tfDoge'

    def actions(self) -> List[base.Action]:
        return viewActions + cameraActions


def run(_context):
    global addIn
    try:
        if addIn is not None:
            stop({'IsApplicationClosing': False})
        addIn = CommanderAddIn()
        addIn.addToUi()
    except Exception as e:
        logger.exception(e)
        util.reportError('Uncaught exception', True)


def stop(_context):
    global addIn

    if addIn:
        addIn.removeFromUI()

    addIn = None
