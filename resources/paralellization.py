"""
Parallel process implementation.

For simplicity, we will only use standard multiprocessing.
"""

# System Imports.
import ctypes, multiprocessing

# User Class Imports.
import resources.logging


# Initialize logging.
logger = resources.logging.get_logger(__name__)


class Paralellization():
    def __init__(self):
        logger.info('Creating multiprocess pool.')

        # Initialize shared values.
        event = multiprocessing.Event()
        lock = multiprocessing.RLock()

        # Create shared array of ints and set all values to -1.
        shared_array = multiprocessing.Array(ctypes.c_int, 5)
        for index in range(len(shared_array)):
            shared_array[index] = -1

        # Initialize process thread pool.
        process_pool = multiprocessing.Pool(10, initializer=self.thread_init, initargs=(shared_array, event, lock))

        # Start up process threads from pool.
        thread_results = process_pool.map_async(self.thread_test, ['a', 'b'])

        # Display thread results.
        logger.info('Thread results: {0}'.format(thread_results.get()))

        # Clean up and close threads.
        logger.info('Closing multiprocess pool.')
        process_pool.close()
        process_pool.join()

    def thread_init(self, passed_array, passed_event, passed_lock):
        """
        Initializes shared objects between threads.
        """
        global shared_array
        shared_array = passed_array
        global event
        event = passed_event
        global lock
        lock = passed_lock

    def thread_test(self, args):
        """
        A dummy function to test that threads work.
        When all threads finish, they will create a second iterable comprised of return values.
        :param args: Value of index in the associated iterable.
        :return: True
        """
        logger.info('Thread started, yay! Passed args are "{0}".'.format(args))
        logger.info('Shared array is: {0}'.format(shared_array[:]))
        logger.info('Shared Event Handler: {0}'.format(event))
        return True

    def populate_shared_array(self, args):
        """
        Gets a random int and puts it into the shared array, if there are any free spaces.
        """
        pass

    def pull_from_shared_array(self, args):
        """
        Pulls values from shared array, if populated.
        """
        pass

    def generate_random_number(self, args):
        """
        Generates a random number.
        :return: A random number between 0 and 9.
        """
        logger.info('Random number: {0}'.format(None))
        return 'No random number yet.'
