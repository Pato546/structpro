import functools

import wx
import wx.lib.agw.flatnotebook as fnb

from . import IMG_PATH


FLAT_NOTEBOOK_STYLES = (
    fnb.FNB_DROPDOWN_TABS_LIST
    | fnb.FNB_RIBBON_TABS
    | fnb.FNB_SMART_TABS
    | fnb.FNB_X_ON_TAB
    | fnb.FNB_TABS_BORDER_SIMPLE
    | fnb.FNB_ALLOW_FOREIGN_DND
    | fnb.FNB_NAV_BUTTONS_WHEN_NEEDED
)


class IconProvider:
    """Provides and caches bitmap icons"""

    @classmethod
    @functools.cache
    def get(cls, icon: str):
        return wx.Bitmap(IMG_PATH + f"\\{icon}.gif")


class CDI(wx.ToolBar):
    """Command Line Interface"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(
            parent, *args, size=(200, 35), style=wx.TB_HORIZONTAL | wx.TB_FLAT, **kwargs
        )
        self.SetBackgroundColour("#000000")


class Canvas(wx.Panel):
    def __init__(self, parent, canvas_name, imgCoordinate, *args, **kwargs):
        super().__init__(parent, *args, style=wx.SIMPLE_BORDER, **kwargs)

        self.canvasName = canvas_name
        self.showCoordinateSystem(imgCoordinate)

    def showCoordinateSystem(self, imgCoordinate: str):
        img_2d_coordinate_ctrl = wx.StaticBitmap(
            self, wx.ID_ANY, IconProvider.get(imgCoordinate)
        )

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(img_2d_coordinate_ctrl, 0, wx.ALIGN_LEFT | wx.ALIGN_BOTTOM)
        self.SetSizer(sizer)


class Canvas2D(Canvas):
    pass


class Window2D(fnb.FlatNotebook):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, agwStyle=FLAT_NOTEBOOK_STYLES, **kwargs)

        self.parent = parent
        self.canvas = Canvas2D(self, "2D-View", "coordinates_2d_xy")
        self.AddPage(self.canvas, self.canvas.canvasName)


class Canvas3D(Canvas):
    pass


class Window3D(fnb.FlatNotebook):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, agwStyle=FLAT_NOTEBOOK_STYLES, **kwargs)
        self.parent = parent

        self.canvas = Canvas3D(self, "3D-View", "coordinates_3d_xyz")
        self.AddPage(self.canvas, self.canvas.canvasName)
