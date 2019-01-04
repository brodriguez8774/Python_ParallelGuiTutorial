"""

"""

# System Imports.
import wx

# User Class Imports.
import resources.logging
from resources import gui


# Initialize logging.
logger = resources.logging.get_logger(__name__)


if __name__ == '__main__':
    logger.info('Starting program.')

    interface = wx.App()
    gui.WindowFrame(None, title='wxPython Parallelization', size=(600, 400))
    interface.MainLoop()

    logger.info('Terminating Program.')
