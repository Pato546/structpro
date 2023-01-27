import wx
import wx.lib.agw.flatnotebook as fnb


class CDI(wx.ToolBar):
    """Command Line Interface"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, size=(400, 35), **kwargs)
        self.SetBackgroundColour("#00ff00")

        self.closeBtn = wx.Button(self, label="1", size=(20, 20))
        self.settingsBtn = wx.Button(self, label="2", size=(20, 20))
        self.searchCommand = wx.SearchCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.searchCommand.ShowCancelButton(show=True)
        self.searchCommand.SetHint("Type a command")

        hbox = wx.BoxSizer(orient=wx.HORIZONTAL)
        hbox.Add(self.closeBtn, flag=wx.ALIGN_CENTER_VERTICAL)
        hbox.Add(self.settingsBtn, flag=wx.ALIGN_CENTER_VERTICAL)
        hbox.Add(self.searchCommand, proportion=1, flag=wx.ALIGN_CENTER_VERTICAL)

        self.SetSizer(hbox)


class Window2D(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.SetBackgroundColour("green")


class Window3D(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.SetBackgroundColour("blue")


class RandomPanel(wx.Panel):
    """"""
    def __init__(self, parent, color):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour(color)





