import wx
import wx.lib.agw.flatmenu as FM

# from . import controls


class MainFrame(wx.Frame):
    """Top Level Window"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.menuBar = FM.FlatMenuBar(parent=self, iconSize=16, spacer=10, options=FM.FM_OPT_IS_LCD)
        self.createMenus()

        self.mainWindow = MainWindow(self)

        self.CreateStatusBar()

        mainSizer = wx.BoxSizer(orient=wx.VERTICAL)
        mainSizer.Add(self.menuBar, flag=wx.EXPAND)
        mainSizer.Add(self.mainWindow, proportion=1, flag=wx.EXPAND)

        self.SetSizer(mainSizer)

        mainSizer.Layout()

    def createMenus(self):
        fileMenu = FM.FlatMenu()
        newModel = FM.FlatMenuItem(fileMenu, id=wx.ID_NEW, label="New", helpString="Create a New Model")
        openModel = FM.FlatMenuItem(fileMenu, id=wx.ID_OPEN, label="Open", helpString="Open an existing model")
        saveModel = FM.FlatMenuItem(fileMenu, id=wx.ID_SAVE, label="Save", helpString="Saves a model")
        saveAs = FM.FlatMenuItem(fileMenu, id=wx.ID_SAVEAS, label="Save As", helpString="")
        exitProgram = FM.FlatMenuItem(fileMenu, id=wx.ID_EXIT, label="Exit", helpString="Closes the program")
        fileMenu.AppendItem(newModel)
        fileMenu.AppendSeparator()
        fileMenu.AppendItem(openModel)
        fileMenu.AppendItem(saveModel)
        fileMenu.AppendItem(saveAs)
        fileMenu.AppendSeparator()
        fileMenu.AppendItem(exitProgram)

        editMenu = FM.FlatMenu()
        undo = FM.FlatMenuItem(editMenu, id=wx.ID_UNDO, label="Undo\tCtrl+Z", helpString="")
        redo = FM.FlatMenuItem(editMenu, id=wx.ID_REDO, label="Redo\tCtrl+Y", helpString="")
        zoomIn = FM.FlatMenuItem(editMenu, id=wx.ID_ZOOM_IN, label="Zoom In", helpString="")
        zoomOut = FM.FlatMenuItem(editMenu, id=wx.ID_ZOOM_OUT, label="Zoom Out", helpString="")
        defineGrid = FM.FlatMenuItem(editMenu, id=wx.ID_ANY, label="Define Grid", helpString="")
        showGrid = FM.FlatMenuItem(editMenu, id=wx.ID_ANY, label="Show Grid", helpString="")
        showAxes = FM.FlatMenuItem(editMenu, id=wx.ID_ANY, label="Show Axes", helpString="")
        editMenu.AppendItem(undo)
        editMenu.AppendItem(redo)
        editMenu.AppendSeparator()
        editMenu.AppendItem(zoomIn)
        editMenu.AppendItem(zoomOut)
        editMenu.AppendSeparator()
        editMenu.AppendItem(defineGrid)
        editMenu.AppendItem(showGrid)
        editMenu.AppendItem(showAxes)

        defineMenu = FM.FlatMenu()
        load = FM.FlatMenuItem(defineMenu, id=wx.ID_ANY, label="Load", helpString="")
        frameSection = FM.FlatMenuItem(defineMenu, id=wx.ID_ANY, label="Frame Section", helpString="")
        material = FM.FlatMenuItem(defineMenu, id=wx.ID_ANY, label="Material", helpString="")
        defineMenu.AppendItem(load)
        defineMenu.AppendItem(frameSection)
        defineMenu.AppendItem(material)

        analyzeMenu = FM.FlatMenu()
        staticAnalysis = FM.FlatMenuItem(analyzeMenu, id=wx.ID_ANY, label="Run Static Analysis", helpString="")
        staticAnalysisResults = FM.FlatMenuItem(analyzeMenu, id=wx.ID_ANY, label="Tabulate Static Analysis Results")
        staticAnalysisResults.Enable(enable=False)
        dynamicAnalysis = FM.FlatMenuItem(analyzeMenu, id=wx.ID_ANY, label="Run Dynamic Analysis", helpString="")
        dynamicAnalysisResults = FM.FlatMenuItem(analyzeMenu, id=wx.ID_ANY, label="Tabulate Dynamic Analysis Results")
        dynamicAnalysisResults.Enable(enable=False)
        analyzeMenu.AppendItem(staticAnalysis)
        analyzeMenu.AppendItem(staticAnalysisResults)
        analyzeMenu.AppendItem(dynamicAnalysis)
        analyzeMenu.AppendItem(dynamicAnalysisResults)

        displayMenu = FM.FlatMenu()
        bendingMoment = FM.FlatMenuItem(displayMenu, id=wx.ID_ANY, label="Bending Moment", helpString="")
        shearForce = FM.FlatMenuItem(displayMenu, id=wx.ID_ANY, label="Shear Force", helpString="")
        reaction = FM.FlatMenuItem(displayMenu, id=wx.ID_ANY, label="Reactions", helpString="")
        deflection = FM.FlatMenuItem(displayMenu, id=wx.ID_ANY, label="Deflection", helpString="")
        displayMenu.AppendItem(bendingMoment)
        displayMenu.AppendItem(shearForce)
        displayMenu.AppendItem(reaction)
        displayMenu.AppendItem(deflection)

        pluginsMenu = FM.FlatMenu()
        addPlugin = FM.FlatMenuItem(pluginsMenu, id=wx.ID_UNDO, label="Add/Show Plugin", helpString="")
        pluginsMenu.AppendItem(addPlugin)

        helpMenu = FM.FlatMenu()
        quickIntro = FM.FlatMenuItem(helpMenu, id=wx.ID_ANY, label="Quick Introduction", helpString="")
        about = FM.FlatMenuItem(helpMenu, id=wx.ID_ANY, label="About", helpString="")
        checkUpdate = FM.FlatMenuItem(helpMenu, id=wx.ID_ANY, label="Check for Updates", helpString="")
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

        self.Bind(event=wx.EVT_MENU, handler=self.exitApp, source=exitProgram)

    def exitApp(self, event):
        self.Close()


class MainWindow(wx.Panel):
    """Main Panel on which all other panels are laid on"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.SetBackgroundColour("#0000ff")

        self.toolBar1 = wx.ToolBar(self, style=wx.TB_VERTICAL)
        self.toolBar1.SetBackgroundColour("#ff0000")
        self.toolBar1.Realize()

        self.toolBar2 = wx.ToolBar(self, style=wx.TB_HORIZONTAL)
        self.toolBar2.Realize()

        hbox = wx.BoxSizer(orient=wx.HORIZONTAL)
        hbox.Add(self.toolBar1)

        vbox = wx.BoxSizer(orient=wx.VERTICAL)
        vbox.Add(self.toolBar2)
        vbox.Add(hbox)

        self.SetSizer(vbox)
