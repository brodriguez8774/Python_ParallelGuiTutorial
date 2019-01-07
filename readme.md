
# Python - Parallel wxPython Gui Tutorial

## Author
Brandon Rodriguez

## About This Program
A tutorial to help understanding of Parallelization and wxPython GUI's.

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
In ``resources/gui.py`` there is a partially established wxPython gui.
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
* There are a few ways to implement paralellization, but the easiest is probably through the ``multiprocessing`` system
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
In ``resources/paralellization.py`` there is a partially established multiprocess class.
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

