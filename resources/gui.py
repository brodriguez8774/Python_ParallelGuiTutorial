"""
Basic Gui.
"""

# System Imports.
import wx

# User Class Imports.
import resources.logging


# Initialize logging.
logger = resources.logging.get_logger(__name__)


class WindowFrame(wx.Frame):
    """
    Window frame object. Contains general layout.
    """
    def __init__(self, *args, **kwargs):
        """
        Object initialization.
        """
        super(WindowFrame, self).__init__(*args, **kwargs)

        self.window_title = None

        self.initialize_layout()
        self.SetMinSize((300, 200)) # Set minimum window size.
        self.Center()               # Center window on screen.
        self.Show()                 # Display window.

    def initialize_layout(self):
        """
        Initializes overall layout of program.
        """
        # Create row groups. Essentially establishes rows of content to display to user.
        top_row_sizer = self.create_gui_top_row()
        # bot_row_sizer = self.create_gui_bottom_row()

        # Create window sizer. Essentially takes the above groups and automatically sizes them based on window size.
        form_sizer = wx.BoxSizer(wx.VERTICAL)
        form_sizer.Add(top_row_sizer, 1, wx.EXPAND | wx.TOP | wx.RIGHT | wx.LEFT, 20)
        # form_sizer.Add(bot_row_sizer, 1, wx.EXPAND | wx.RIGHT | wx.BOTTOM | wx.LEFT, 20)

        # Initialize form settings.
        self.SetAutoLayout(True)
        self.SetSizer(form_sizer)
        self.Layout()

    def create_gui_top_row(self):
        """
        Top row of GUI.
        """
        # Create group panel.
        panel = wx.Panel(self)

        # Create group sizer.
        col_sizer = wx.BoxSizer(wx.HORIZONTAL)
        col_sizer.AddStretchSpacer(1)

        # Create Title fields.
        title = wx.StaticText(panel, label='wxPython Parallelization', style=wx.ALIGN_CENTER)
        title.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.NORMAL))
        col_sizer.Add(title, 1, wx.ALIGN_CENTER)
        col_sizer.AddStretchSpacer(1)

        panel.SetSizer(col_sizer)
        self.window_title = title
        return panel

    def create_gui_bottom_row(self):
        """
        Bottom row of GUI.
        """
        # Create group panel.

        # Create group sizer.

        # Panel content.

        # Return panel for parent to manipulate.


class GuiButton(wx.Button):
    """
    Sign In button object.
    """
    def __init__(self, widget_dict, *args, **kwargs):
        super(GuiButton, self).__init__(*args, **kwargs)

        # Useful groups for later manipulation.
        self.window = widget_dict['window']

        # Set button properties.
        self.SetLabelText('Button Text Here')
        self.Bind(wx.EVT_BUTTON, self.on_click)

    def on_click(self, event):
        """
        Base handling for button click.
        """
        logger.info('Button Clicked')
