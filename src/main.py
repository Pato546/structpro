import wx.lib.mixins.inspection as wit
import wx

from frontend import gui


def main():
    app = wit.InspectableApp()

    display_width, display_height = wx.DisplaySize()

    window = gui.MainFrame(
        None, title="StructPro", size=(display_width, display_height)
    )
    app.SetTopWindow(window)
    window.Show()

    app.MainLoop()


if __name__ == "__main__":
    main()
