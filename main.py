"""

"""

# System Imports.
import wx

# User Class Imports.
import resources.logging
from resources import gui, paralellization


# Initialize logging.
logger = resources.logging.get_logger(__name__)


if __name__ == '__main__':
    logger.info('Starting program.')

    # # Step 1.
    # interface = wx.App()
    # gui.WindowFrame(None, title='wxPython Parallelization', size=(600, 400))
    # interface.MainLoop()

    # Step 2.
    parallel_test = paralellization.Paralellization()

    # Step 3.

    logger.info('Terminating Program.')
