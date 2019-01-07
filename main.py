"""
Project start.

Uncomment each step below to begin working on it.
"""

# System Imports.
import wx

# User Class Imports.
import resources.logging
from step_1 import gui as step_1_gui
from step_2 import parallelization as step_2_parallelization
from step_3 import parallelization as step_3_parallelization


# Initialize logging.
logger = resources.logging.get_logger(__name__)


if __name__ == '__main__':
    logger.info('Starting program.')

    # Step 1.
    logger.info('Step 1')
    interface = wx.App()
    step_1_gui.WindowFrame(None, title='wxPython Parallelization', size=(600, 400))
    interface.MainLoop()
    logger.info('')

    # Step 2.
    logger.info('Step 2')
    parallel_test = step_2_parallelization.parallelization()
    logger.info('')

    # Step 3.
    logger.info('Step 3')
    parallel_gui = step_3_parallelization.GuiThreading()
    logger.info('')

    logger.info('Terminating Program.')
