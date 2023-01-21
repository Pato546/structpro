import wx.lib.mixins.inspection as wit

from frontend import gui


def main():
    app = wit.InspectableApp()

    window = gui.MainFrame(None, title="StructPro")
    app.SetTopWindow(window)
    window.Show()

    app.MainLoop()


if __name__ == "__main__":
    main()
