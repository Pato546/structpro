import wx
import wx.lib.agw.flatnotebook as fnb

FLAT_NOTEBOOK_STYLES = (
    fnb.FNB_DROPDOWN_TABS_LIST
    | fnb.FNB_RIBBON_TABS
    | fnb.FNB_SMART_TABS
    | fnb.FNB_X_ON_TAB
    | fnb.FNB_TABS_BORDER_SIMPLE
    | fnb.FNB_ALLOW_FOREIGN_DND
    | fnb.FNB_NAV_BUTTONS_WHEN_NEEDED
)


class CDI(wx.ToolBar):
    """Command Line Interface"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(
            parent, *args, size=(200, 35), style=wx.TB_HORIZONTAL | wx.TB_FLAT, **kwargs
        )
        self.SetBackgroundColour("#000000")


class Canvas2D(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.parent = parent
        self.name = "2-D View"

        self.SetBackgroundColour("blue")


class Window2D(fnb.FlatNotebook):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, agwStyle=FLAT_NOTEBOOK_STYLES, **kwargs)

        self.parent = parent
        self.canvas = Canvas2D(self)
        self.AddPage(self.canvas, self.canvas.name)


class Canvas3D(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.parent = parent
        self.name = "3-D View"


class Window3D(fnb.FlatNotebook):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, agwStyle=FLAT_NOTEBOOK_STYLES, **kwargs)
        self.parent = parent

        self.canvas = Canvas3D(self)
        self.AddPage(self.canvas, self.canvas.name)
