"""
Parallel implementation of a GUI..

For simplicity, we will only use standard multiprocessing.
"""

# System Imports.
import ctypes, multiprocessing, wx
from random import randint

# User Class Imports.
import resources.logging
from step_3 import gui


# Initialize logging.
logger = resources.logging.get_logger(__name__)


class GuiThreading():
    def __init__(self):
        logger.info('Creating multiprocess pool.')

        # Initialize shared values.
        run_bool = multiprocessing.Value(ctypes.c_bool, True)
        shared_int = multiprocessing.Value(ctypes.c_int, -1)
        shared_event = multiprocessing.Event()

        # Initialize process thread pool.
        process_pool = multiprocessing.Pool(
            2,
            initializer=self.thread_init,
            initargs=(run_bool, shared_int, shared_event)
        )

        # Start up process threads from pool.

        # Display thread results.
        logger.info('GUI Thread results: {0}'.format(None))
        logger.info('Rand Thread results: {0}'.format(None))

        # Clean up and close threads.
        logger.info('Closing multiprocess pool.')
        process_pool.close()
        process_pool.join()

    def thread_init(self, passed_bool, passed_int, passed_event):
        """
        Initializes shared objects between threads.
        """
        global run_bool
        run_bool = passed_bool
        global shared_int
        shared_int = passed_int
        global thread_event
        thread_event = passed_event

    def thread_gui(self, args):
        """
        A dummy function to test that threads work.
        When all threads finish, they will create a second iterable comprised of return values.
        :param args: Value of index in the associated iterable.
        :return: True
        """
        # Run GUI.

        # GUI has exited.
        return True

    def generate_random_number(self, args):
        """
        Generates a random number between 0 and 9.
        :return: Array of all generated values while thread was alive.
        """

        # Loop thread as long as boolean is True.
        while run_bool.value:

            if run_bool.value:
                # Get random number.
                a_number = randint(0, 9)
                logger.info('Rand Gen Thread: New random int is {0}'.format(a_number))

                # Set thread values here.

            else:
                logger.info('Exiting random number generation thread.')
        return None
