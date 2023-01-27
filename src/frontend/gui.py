import pathlib

import wx
import wx.lib.agw.flatmenu as fm

from . import controls


IMG_PATH = str((pathlib.Path(__file__).parent / "imgs/").absolute())


class IconPath:
    new = IMG_PATH + r"\new.png"
    open = IMG_PATH + r"\open.gif"
    save = IMG_PATH + r"\save.png"
    save_as = IMG_PATH + r"\save_as.png"
    exit = IMG_PATH + r"\close.png"
    pointer = IMG_PATH + r"\pointer.gif"
    node = IMG_PATH + r"\node.gif"
    member = IMG_PATH + r"\member.gif"
    grid = IMG_PATH + r"\grid.png"
    show_grid16 = IMG_PATH + r"\show_grid16.png"


class MainFrame(wx.Frame):
    """Top Level Window"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.newIcon = wx.Bitmap(IconPath.new)
        self.openIcon = wx.Bitmap(IconPath.open)
        self.saveIcon = wx.Bitmap(IconPath.save)
        self.saveAsIcon = wx.Bitmap(IconPath.save_as)
        self.exitIcon = wx.Bitmap(IconPath.exit)
        self.pointerIcon = wx.Bitmap(IconPath.pointer)
        self.nodeIcon = wx.Bitmap(IconPath.node)
        self.memberIcon = wx.Bitmap(IconPath.member)
        self.gridIcon = wx.Bitmap(IconPath.grid)
        self.showGridIcon = wx.Bitmap(IconPath.show_grid16)

        self.menuBar = fm.FlatMenuBar(parent=self, iconSize=16, spacer=10, options=fm.FM_OPT_IS_LCD)
        self.CreateMenus()

        self.toolbar = wx.ToolBar(self, style=wx.TB_HORIZONTAL | wx.TB_FLAT | wx.NO_BORDER)
        self.toolbar.AddTool(wx.ID_NEW, "new", self.newIcon)
        self.toolbar.AddTool(wx.ID_OPEN, "open", self.openIcon)
        self.toolbar.AddTool(wx.ID_SAVE, "save", self.saveIcon)
        self.toolbar.AddSeparator()
        self.toolbar.Realize()

        self.mainWindow = MainWindow(self)

        self.CreateStatusBar()

        mainSizer = wx.BoxSizer(orient=wx.VERTICAL)
        mainSizer.Add(self.menuBar, flag=wx.EXPAND)
        mainSizer.Add(self.toolbar, flag=wx.EXPAND)
        mainSizer.Add(self.mainWindow, proportion=1, flag=wx.EXPAND)

        self.SetSizer(mainSizer)

        mainSizer.Layout()

    def CreateMenus(self):
        fileMenu = fm.FlatMenu()
        newModel = fm.FlatMenuItem(fileMenu, id=wx.ID_NEW, label="New", helpString="Create a New Model",
                                   normalBmp=self.newIcon)
        openModel = fm.FlatMenuItem(fileMenu, id=wx.ID_OPEN, label="Open", helpString="Open an existing model",
                                    normalBmp=self.openIcon)
        saveModel = fm.FlatMenuItem(fileMenu, id=wx.ID_SAVE, label="Save", helpString="Saves a model",
                                    normalBmp=self.saveIcon)
        saveAs = fm.FlatMenuItem(fileMenu, id=wx.ID_SAVEAS, label="Save As", helpString="",
                                 normalBmp=self.saveAsIcon)
        exitProgram = fm.FlatMenuItem(fileMenu, id=wx.ID_EXIT, label="Exit", helpString="Closes the program",
                                      normalBmp=self.exitIcon)
        fileMenu.AppendItem(newModel)
        fileMenu.AppendSeparator()
        fileMenu.AppendItem(openModel)
        fileMenu.AppendItem(saveModel)
        fileMenu.AppendItem(saveAs)
        fileMenu.AppendSeparator()
        fileMenu.AppendItem(exitProgram)

        editMenu = fm.FlatMenu()
        undo = fm.FlatMenuItem(editMenu, id=wx.ID_UNDO, label="Undo\tCtrl+Z", helpString="")
        redo = fm.FlatMenuItem(editMenu, id=wx.ID_REDO, label="Redo\tCtrl+Y", helpString="")
        zoomIn = fm.FlatMenuItem(editMenu, id=wx.ID_ZOOM_IN, label="Zoom In", helpString="")
        zoomOut = fm.FlatMenuItem(editMenu, id=wx.ID_ZOOM_OUT, label="Zoom Out", helpString="")
        defineGrid = fm.FlatMenuItem(editMenu, id=wx.ID_ANY, label="Define Grid", helpString="",
                                     normalBmp=self.gridIcon)
        showGrid = fm.FlatMenuItem(editMenu, id=wx.ID_ANY, label="Show Grid", helpString="",
                                   normalBmp=self.showGridIcon)
        showAxes = fm.FlatMenuItem(editMenu, id=wx.ID_ANY, label="Show Axes", helpString="")
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
        frameSection = fm.FlatMenuItem(defineMenu, id=wx.ID_ANY, label="Frame Section", helpString="")
        material = fm.FlatMenuItem(defineMenu, id=wx.ID_ANY, label="Material", helpString="")
        defineMenu.AppendItem(load)
        defineMenu.AppendItem(frameSection)
        defineMenu.AppendItem(material)

        analyzeMenu = fm.FlatMenu()
        staticAnalysis = fm.FlatMenuItem(analyzeMenu, id=wx.ID_ANY, label="Run Static Analysis", helpString="")
        staticAnalysisResults = fm.FlatMenuItem(analyzeMenu, id=wx.ID_ANY, label="Tabulate Static Analysis Results")
        staticAnalysisResults.Enable(enable=False)
        dynamicAnalysis = fm.FlatMenuItem(analyzeMenu, id=wx.ID_ANY, label="Run Dynamic Analysis", helpString="")
        dynamicAnalysisResults = fm.FlatMenuItem(analyzeMenu, id=wx.ID_ANY, label="Tabulate Dynamic Analysis Results")
        dynamicAnalysisResults.Enable(enable=False)
        analyzeMenu.AppendItem(staticAnalysis)
        analyzeMenu.AppendItem(staticAnalysisResults)
        analyzeMenu.AppendItem(dynamicAnalysis)
        analyzeMenu.AppendItem(dynamicAnalysisResults)

        displayMenu = fm.FlatMenu()
        bendingMoment = fm.FlatMenuItem(displayMenu, id=wx.ID_ANY, label="Bending Moment", helpString="")
        shearForce = fm.FlatMenuItem(displayMenu, id=wx.ID_ANY, label="Shear Force", helpString="")
        reaction = fm.FlatMenuItem(displayMenu, id=wx.ID_ANY, label="Reactions", helpString="")
        deflection = fm.FlatMenuItem(displayMenu, id=wx.ID_ANY, label="Deflection", helpString="")
        displayMenu.AppendItem(bendingMoment)
        displayMenu.AppendItem(shearForce)
        displayMenu.AppendItem(reaction)
        displayMenu.AppendItem(deflection)

        pluginsMenu = fm.FlatMenu()
        addPlugin = fm.FlatMenuItem(pluginsMenu, id=wx.ID_UNDO, label="Add/Show Plugin", helpString="")
        pluginsMenu.AppendItem(addPlugin)

        helpMenu = fm.FlatMenu()
        quickIntro = fm.FlatMenuItem(helpMenu, id=wx.ID_ANY, label="Quick Introduction", helpString="")
        about = fm.FlatMenuItem(helpMenu, id=wx.ID_ANY, label="About", helpString="")
        checkUpdate = fm.FlatMenuItem(helpMenu, id=wx.ID_ANY, label="Check for Updates", helpString="")
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


class MainWindow(wx.Panel):
    """Main Panel on which all other panels are laid on"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.SetBackgroundColour("red")
        self.toolBar = wx.ToolBar(self, style=wx.TB_VERTICAL | wx.TB_FLAT | wx.NO_BORDER)
        self.toolBar.AddTool(wx.ID_ANY, "pointer", parent.pointerIcon)
        self.toolBar.AddSeparator()
        self.toolBar.AddTool(wx.ID_ANY, "node", parent.nodeIcon)
        self.toolBar.AddSeparator()
        self.toolBar.AddTool(wx.ID_ANY, "member", parent.memberIcon)
        self.toolBar.AddSeparator()
        self.toolBar.AddTool(wx.ID_ANY, "grid", parent.gridIcon)
        self.toolBar.AddSeparator()
        self.toolBar.AddTool(wx.ID_ANY, "show_grid", parent.showGridIcon)
        self.toolBar.AddSeparator()
        self.toolBar.Realize()

        self.splitter = wx.SplitterWindow(self)
        p1 = wx.Panel(self.splitter)
        p1.SetBackgroundColour("blue")
        p2 = wx.Panel(self.splitter)
        p2.SetBackgroundColour("green")
        self.splitter.SplitVertically(p1, p2)
        self.splitter.SetSashPosition(500)

        hbox = wx.BoxSizer(orient=wx.HORIZONTAL)
        hbox.Add(self.toolBar, flag=wx.EXPAND)
        hbox.Add(self.splitter, proportion=1, flag=wx.EXPAND)

        self.SetSizer(hbox)

        self.Bind(event=wx.EVT_LEFT_DOWN, handler=self.OnMouseDown)

    def OnMouseDown(self, event):
        dc = wx.ClientDC(self)
        pen = wx.Pen("red")
        pen.SetWidth(20)
        dc.SetPen(pen)
        dc.DrawPoint(event.GetPosition())
