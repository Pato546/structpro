import wx
import wx.lib.agw.flatmenu as fm

from . import controls
from .controls import IconProvider


class MainFrame(wx.Frame):
    """Top Level Window"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.menuBar = fm.FlatMenuBar(
            parent=self, iconSize=16, spacer=7, options=fm.FM_OPT_IS_LCD
        )
        self.CreateMenus()

        self.toolbar = wx.ToolBar(
            self, style=wx.TB_HORIZONTAL | wx.TB_FLAT | wx.NO_BORDER
        )
        self.toolbar.AddTool(wx.ID_NEW, "new", IconProvider.get("new"))
        self.toolbar.AddTool(wx.ID_OPEN, "open", IconProvider.get("open"))
        self.toolbar.AddTool(wx.ID_SAVE, "save", IconProvider.get("save"))
        self.toolbar.AddSeparator()
        self.toolbar.AddTool(wx.ID_PRINT, "print", IconProvider.get("printer-custom"))
        self.toolbar.AddSeparator()
        self.toolbar.AddTool(wx.ID_UNDO, "undo", IconProvider.get("undo"))
        self.toolbar.AddTool(wx.ID_REDO, "redo", IconProvider.get("redo"))
        self.toolbar.AddTool(wx.ID_ZOOM_IN, "zoom_in", IconProvider.get("zoom_in"))
        self.toolbar.AddTool(wx.ID_ZOOM_OUT, "zoom_out", IconProvider.get("zoom_out"))
        self.toolbar.AddSeparator()
        # Add toolbars here
        self.toolbar.AddSeparator()
        self.toolbar.AddTool(wx.ID_ANY, "run", IconProvider.get("run"))
        self.toolbar.AddSeparator()
        self.toolbar.Realize()

        self.mainWindow = MainWindow(self)

        self.statusBar = self.CreateStatusBar()

        mainSizer = wx.BoxSizer(orient=wx.VERTICAL)
        mainSizer.Add(self.menuBar, flag=wx.EXPAND)
        mainSizer.Add(self.toolbar, flag=wx.EXPAND)
        mainSizer.Add(self.mainWindow, proportion=1, flag=wx.EXPAND)

        self.SetSizer(mainSizer)

        mainSizer.Layout()

    def CreateMenus(self):
        fileMenu = fm.FlatMenu()
        newModel = fm.FlatMenuItem(
            fileMenu,
            id=wx.ID_NEW,
            label="New",
            helpString="Create a New Model",
            normalBmp=IconProvider.get("new"),
        )
        openModel = fm.FlatMenuItem(
            fileMenu,
            id=wx.ID_OPEN,
            label="Open",
            helpString="Open an existing model",
            normalBmp=IconProvider.get("open"),
        )
        saveModel = fm.FlatMenuItem(
            fileMenu,
            id=wx.ID_SAVE,
            label="Save",
            helpString="Saves a model",
            normalBmp=IconProvider.get("save"),
        )
        saveAs = fm.FlatMenuItem(
            fileMenu,
            id=wx.ID_SAVEAS,
            label="Save As",
            helpString="",
            normalBmp=IconProvider.get("save_as"),
        )
        exitProgram = fm.FlatMenuItem(
            fileMenu,
            id=wx.ID_EXIT,
            label="Exit",
            helpString="Closes the program",
            normalBmp=IconProvider.get("close"),
        )
        fileMenu.AppendItem(newModel)
        fileMenu.AppendSeparator()
        fileMenu.AppendItem(openModel)
        fileMenu.AppendItem(saveModel)
        fileMenu.AppendItem(saveAs)
        fileMenu.AppendSeparator()
        fileMenu.AppendItem(exitProgram)

        editMenu = fm.FlatMenu()
        undo = fm.FlatMenuItem(
            editMenu,
            id=wx.ID_UNDO,
            label="Undo\tCtrl+Z",
            helpString="",
            normalBmp=IconProvider.get("undo"),
        )
        redo = fm.FlatMenuItem(
            editMenu,
            id=wx.ID_REDO,
            label="Redo\tCtrl+Y",
            helpString="",
            normalBmp=IconProvider.get("redo"),
        )
        zoomIn = fm.FlatMenuItem(
            editMenu,
            id=wx.ID_ZOOM_IN,
            label="Zoom In",
            helpString="",
            normalBmp=IconProvider.get("zoom_in"),
        )
        zoomOut = fm.FlatMenuItem(
            editMenu,
            id=wx.ID_ZOOM_OUT,
            label="Zoom Out",
            helpString="",
            normalBmp=IconProvider.get("zoom_out"),
        )
        defineGrid = fm.FlatMenuItem(
            editMenu,
            id=wx.ID_ANY,
            label="Define Grid",
            helpString="",
            normalBmp=IconProvider.get("grid"),
        )
        showGrid = fm.FlatMenuItem(
            editMenu,
            id=wx.ID_ANY,
            label="Show Grid",
            helpString="",
            normalBmp=IconProvider.get("show_grid"),
        )
        showAxes = fm.FlatMenuItem(
            editMenu,
            id=wx.ID_ANY,
            label="Show Axes",
            helpString="",
            normalBmp=IconProvider.get("show_axes"),
        )
        editMenu.AppendItem(undo)
        editMenu.AppendItem(redo)
        editMenu.AppendSeparator()
        editMenu.AppendItem(zoomIn)
        editMenu.AppendItem(zoomOut)
        editMenu.AppendSeparator()
        editMenu.AppendItem(defineGrid)
        editMenu.AppendItem(showGrid)
        editMenu.AppendItem(showAxes)

        defineMenu = fm.FlatMenu()
        load = fm.FlatMenuItem(defineMenu, id=wx.ID_ANY, label="Load", helpString="")
        frameSection = fm.FlatMenuItem(
            defineMenu, id=wx.ID_ANY, label="Frame Section", helpString=""
        )
        material = fm.FlatMenuItem(
            defineMenu, id=wx.ID_ANY, label="Material", helpString=""
        )
        defineMenu.AppendItem(load)
        defineMenu.AppendItem(frameSection)
        defineMenu.AppendItem(material)

        analyzeMenu = fm.FlatMenu()
        staticAnalysis = fm.FlatMenuItem(
            analyzeMenu, id=wx.ID_ANY, label="Run Static Analysis", helpString=""
        )
        staticAnalysisResults = fm.FlatMenuItem(
            analyzeMenu, id=wx.ID_ANY, label="Tabulate Static Analysis Results"
        )
        staticAnalysisResults.Enable(enable=False)
        dynamicAnalysis = fm.FlatMenuItem(
            analyzeMenu, id=wx.ID_ANY, label="Run Dynamic Analysis", helpString=""
        )
        dynamicAnalysisResults = fm.FlatMenuItem(
            analyzeMenu, id=wx.ID_ANY, label="Tabulate Dynamic Analysis Results"
        )
        dynamicAnalysisResults.Enable(enable=False)
        analyzeMenu.AppendItem(staticAnalysis)
        analyzeMenu.AppendItem(staticAnalysisResults)
        analyzeMenu.AppendItem(dynamicAnalysis)
        analyzeMenu.AppendItem(dynamicAnalysisResults)

        displayMenu = fm.FlatMenu()
        bendingMoment = fm.FlatMenuItem(
            displayMenu, id=wx.ID_ANY, label="Bending Moment", helpString=""
        )
        shearForce = fm.FlatMenuItem(
            displayMenu, id=wx.ID_ANY, label="Shear Force", helpString=""
        )
        reaction = fm.FlatMenuItem(
            displayMenu, id=wx.ID_ANY, label="Reactions", helpString=""
        )
        deflection = fm.FlatMenuItem(
            displayMenu, id=wx.ID_ANY, label="Deflection", helpString=""
        )
        displayMenu.AppendItem(bendingMoment)
        displayMenu.AppendItem(shearForce)
        displayMenu.AppendItem(reaction)
        displayMenu.AppendItem(deflection)

        pluginsMenu = fm.FlatMenu()
        addPlugin = fm.FlatMenuItem(
            pluginsMenu, id=wx.ID_UNDO, label="Add/Show Plugin", helpString=""
        )
        pluginsMenu.AppendItem(addPlugin)

        helpMenu = fm.FlatMenu()
        quickIntro = fm.FlatMenuItem(
            helpMenu, id=wx.ID_ANY, label="Quick Introduction", helpString=""
        )
        about = fm.FlatMenuItem(helpMenu, id=wx.ID_ANY, label="About", helpString="")
        checkUpdate = fm.FlatMenuItem(
            helpMenu, id=wx.ID_ANY, label="Check for Updates", helpString=""
        )
        helpMenu.AppendItem(quickIntro)
        helpMenu.AppendItem(about)
        helpMenu.AppendItem(checkUpdate)

        self.menuBar.Append(fileMenu, title="&File")
        self.menuBar.Append(editMenu, title="&Edit")
        self.menuBar.Append(defineMenu, title="&Define")
        self.menuBar.Append(analyzeMenu, title="Analyze")
        self.menuBar.Append(displayMenu, title="Display")
        self.menuBar.Append(pluginsMenu, title="&Plugins")
        self.menuBar.Append(helpMenu, title="&Help")

        self.Bind(event=wx.EVT_MENU, handler=self.ExitApp, source=exitProgram)

    def ExitApp(self, event):
        self.Close()


class ModelViewWindow(wx.Panel):
    """Manages the 2D and 3D Canvas"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.parent = parent

        self.splitter = wx.SplitterWindow(self, style=wx.SP_LIVE_UPDATE)
        self.window2D = controls.Window2D(self.splitter)
        self.window3D = controls.Window3D(self.splitter)
        self.splitter.SplitVertically(self.window2D, self.window3D)
        self.splitter.SetSashPosition(650)

        hbox = wx.BoxSizer(orient=wx.HORIZONTAL)
        hbox.Add(self.splitter, proportion=1, flag=wx.EXPAND)

        self.SetSizer(hbox)


class MainWindow(wx.Panel):
    """Main Panel on which all other panels are laid on"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        # self.SetBackgroundColour("red")
        self.leftToolBar = wx.ToolBar(
            self, style=wx.TB_VERTICAL | wx.TB_FLAT | wx.NO_BORDER
        )
        self.leftToolBar.AddTool(wx.ID_ANY, "pointer", IconProvider.get("pointer"))
        self.leftToolBar.AddSeparator()
        self.leftToolBar.AddTool(wx.ID_ANY, "node", IconProvider.get("node"))
        self.leftToolBar.AddSeparator()
        self.leftToolBar.AddTool(wx.ID_ANY, "member", IconProvider.get("member"))
        self.leftToolBar.AddSeparator()
        self.leftToolBar.AddTool(wx.ID_ANY, "grid", IconProvider.get("grid"))
        self.leftToolBar.AddSeparator()
        self.leftToolBar.AddTool(wx.ID_ANY, "show_grid", IconProvider.get("show_grid"))
        self.leftToolBar.AddSeparator()
        self.leftToolBar.AddTool(wx.ID_ANY, "show_axes", IconProvider.get("show_axes"))
        self.leftToolBar.AddSeparator()
        self.leftToolBar.Realize()

        # self.rightToolBar = wx.ToolBar(
        #     self, style=wx.TB_VERTICAL | wx.TB_FLAT | wx.NO_BORDER
        # )
        # self.rightToolBar.Realize()

        self.modelViewWindow = ModelViewWindow(self)
        self.modelViewWindow.SetBackgroundColour("cyan")

        hbox = wx.BoxSizer(orient=wx.HORIZONTAL)
        hbox.Add(self.leftToolBar, flag=wx.EXPAND)
        hbox.Add(self.modelViewWindow, proportion=1, flag=wx.EXPAND)
        # hbox.Add(self.rightToolBar, flag=wx.EXPAND)

        self.SetSizer(hbox)

        self.Refresh()

        self.Bind(event=wx.EVT_LEFT_DOWN, handler=self.OnMouseDown)

    def OnMouseDown(self, event):
        dc = wx.ClientDC(self)
        pen = wx.Pen("red")
        pen.SetWidth(20)
        dc.SetPen(pen)
        dc.DrawPoint(event.GetPosition())
