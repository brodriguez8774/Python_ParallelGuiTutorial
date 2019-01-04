
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


### Step 3 - Combining Parallelization into the Gui

