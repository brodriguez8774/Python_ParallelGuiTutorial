"""

"""

# System Imports.
import wx

# User Class Imports.
import resources.logging
from step_1 import gui
from step_2 import paralellization
from step_3 import gui, parallelization


# Initialize logging.
logger = resources.logging.get_logger(__name__)


if __name__ == '__main__':
    logger.info('Starting program.')

    # # Step 1.
    # interface = wx.App()
    # gui.WindowFrame(None, title='wxPython Parallelization', size=(600, 400))
    # interface.MainLoop()

    # # Step 2.
    # parallel_test = paralellization.Paralellization()

    # # Step 3.
    # parallel_gui = parallelization.GuiThreading()

    logger.info('Terminating Program.')
