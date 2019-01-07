
# Python - Parallel wxPython Gui Tutorial

## Author
Brandon Rodriguez

## About This Program
A tutorial to help understanding of Parallelization and wxPython GUI's. Written and tested in Python Version 3.5.

This program has 3 major steps:
1) Creating a GUI that updates on button press.
2) Creating a multiprocessing pool which essentially creates and reads randomly generated ints through separate process
threads.
3) Combine the above two. Results in a threaded GUI that calls a separate thread to create a random int. GUI updates
self afterwards.

### Hints and Solution
If you get stuck, need hints, or simply want to see a solution, check out the ``solution`` branch of this project.

## Steps

### Step 1 - Setting up a wxPython Gui

#### Before we Start
Before we start, there are some important things to note about wxPython:
* The GUI is always built from the topmost parent, inward. So you always start by creating the outer frame window. Then
you populate the smaller children, going either by row or column (your choice).
* Nearly every row/column element is a "panel". Panels are can be used to hold smaller elements (including other
panels). Panels can also resize automatically as the window frame resizes.
    * This means, a standard wxPython GUI will often be comprised of multiple, nested panels to establish interface
    layout. The more complex the layout, the more panels are generally required.

#### Creating the GUI
In ``step_1/gui.py`` there is a partially established wxPython gui.
1) Try creating a second "bottom row" for the GUI. Use the already present "top row" as a reference if needed.
    * In this row, add a button for the user to click.
    * On creation, the button should be passed a dictionary object, which will be used to allow the button to reference
    the window frame. At minimum, this dictionary should contain ``"window": self``.
2) For extra practice, optionally create a third "middle row" that exists between the other two rows.
    * At minimum, add a staticText element to this row.
3) Note that, because of the passed dictionary, our button can reference any variables contained in the window frame
object.
    * Make sure the window frame has class variable references to any staticText elements.
    * On button click, use the ``.SetLabelText()`` function to change the text of any staticText element.
4) If done correctly, you should be able to start the program.
    * A Gui should show up containing at least two rows, a text
    element, and a button.
    * The Gui should be able to resize, with all elements automataically adjusting.
    * Clicking the button should change the text of at least one text element.

### Step 2 - Threading and Parallelization

#### Before we Start
Before we start, there are some important things to note about parallelization in Python:
* There are a few ways to implement parallelization, but the easiest is probably through the ``multiprocessing`` system
library.
* The ``multiprocessing`` library can implement either multiprocessing or multithreading.
    * Standard ``multiprocessing`` is used to implement multiprocessing.
    * Otherwise, use ``multiprocessing.dummy`` to implement multithreading.
    * Outside of the above differences, these two implementations should otherwise handle identically.
* Once you create a thread pool, there are two ways to actually start/run threads:
    * Use ``thread_pool.map()`` to run the same function on all threads.
    * Use ``thread_poo.async_map()`` to run different functions on each thread.
        * Note that for ``async_map()``, the second arg is an iterable with length equal to the number of threads being
        started. Each value in this iterable is treated as args for the given thread.

#### Implementing Multi-processing
In ``step_2/parallelization.py`` there is a partially established multiprocess class. All the shared variables you need
should already be provided.
1) Flesh out the ``generate_random_number`` function to generate a random int from 0 through 9.
    * Hint: Use ``random.randint``
2) Update thread calling so that half of the 10 threads call one function, the other half call a different one.
    * We will want the threads to call ``populate_shared_array()`` and ``pull_from_shared_array()``.
    * Make sure to add logging statements to ensure threads are being called as expected.
3) Add logic to ``populate_shared_array()`` so that it grabs a random number from the ``generate_random_number()``
function and inserts it into the first "empty" shared array index (aka first index with a value of -1).
4) Add logic to ``pull_from_shared_array()`` so that it pulls the first "non-empty" shared array index (aka fist value
that is not -1).
5) If threads try to pull from the array before values are inserted, then they will fail. Use the "event.wait()" and
"event.set()" threading functions to delay pulling values until explicitly called.
6) Finally, when each thread exits, it should return the value inserted or removed from the shared array.

### Step 3 - Combining Parallelization into the Gui
Now copy your GUI file from step one into the ``step_3`` folder. As in step 2, there is a partially established
multiprocess class. All shared variables you need should be already provided.
1) This time, we want exactly two threads. In the multiprocessing class, update the ``thread_gui()`` function to call
your newly copied GUI.
2) You'll want to modify your GUI kwargs to accept the "run_bool", "shared_int", "shared_event" thread variables. Also
modify the GUI button to accept these as well. These variables are how your threads will communicate.
3) Update the ``generate_random_number()`` function:
    * Use "event.clear()" and "event.wait()" so it only generates a number when told to by the gui.
    * Set the shared_int value to this newly generated value.
    * Use "event.set()" to let the GUI thread know a random value has been generated.
    * Use the run_bool value to keep this thread alive until GUI exits.
    * When this function exits, it should return an array of all random values generated during life of thread.
4) Update the button in the GUI. On click, the button should:
    * Use "event.set()" to tell the random generator a new value is needed.
    * Use "event.clear()" and "event.wait()" to wait until the generator has a new value.
        * NOTE: Normally in a GUI thread, you wouldn't want to block logic like this. However, in this example, the
        logic is simple enough that the block is trivial, and more importantly, it shows having two threads wait for
        each other at different steps of communication.
    * Finally, update the actual text on the GUI to display the newly generated random value from the other thread.
5) For added clarity and/or debugging purposes, don't forget to add proper logging statements.
