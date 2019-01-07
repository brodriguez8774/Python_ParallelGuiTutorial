"""
Project start.

Uncomment each step below to begin working on it.
"""

# System Imports.
import wx

# User Class Imports.
import resources.logging
from step_1 import gui as step_1_gui
from step_2 import paralellization as step_2_paralellization
from step_3 import parallelization as step_3_paralellization


# Initialize logging.
logger = resources.logging.get_logger(__name__)


if __name__ == '__main__':
    logger.info('Starting program.')

    # # Step 1.
    # interface = wx.App()
    # step_1_gui.WindowFrame(None, title='wxPython Parallelization', size=(600, 400))
    # interface.MainLoop()
    #
    # # Step 2.
    # parallel_test = step_2_paralellization.Paralellization()
    #
    # # Step 3.
    # parallel_gui = step_3_paralellization.GuiThreading()

    logger.info('Terminating Program.')
