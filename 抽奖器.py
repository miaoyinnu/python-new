__author__ = 'glcsnz123'
import wx;
import random;


class Random(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, id=-1, title="Numerical Selection Machine", size=(300, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP)
        self.matp = [0] * 300;
        self.panel = wx.Panel(self, id=-1);
        self.panel.SetBackgroundColour("white")
        self.limit = int(50);
        self.sizee = 30;
        # create the label
        self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, 'Courier New')
        self.font.SetPointSize(self.sizee)
        self.st = wx.StaticText(self.panel, -1, label="select:", pos=(30, 30));
        self.st.SetFont(self.font)
        self.st.SetForegroundColour("red")

        # create the label2
        self.st2 = wx.StaticText(self.panel, -1, label="press", pos=(60, 100))
        self.st2.SetFont(self.font);

        # create the button
        self.but = wx.Button(self.panel, -1, "Random Click", pos=(80, 180))

        # create the menu
        self.CreateTheMenuBar()
        # create the bind
        self.Bind(wx.EVT_BUTTON, self.RandomBut, self.but)

    def RandomBut(self, event):
        while True:
            t = random.randrange(1, self.limit)
            if self.matp[t] == 1:
                continue;
            else:
                self.matp[t] = 1;
                self.st2.SetLabel("d" % t)
                break;

    def CreateTheMenuBar(self):
        menuBar = wx.MenuBar();

        # create menu
        menu1 = wx.Menu()

        # create menuItem
        mIU = menu1.Append(-1, "Set Range")
        mIS = menu1.Append(-1, "Set Size")
        # Append
        menuBar.Append(menu1, "&File")
        self.SetMenuBar(menuBar)

        # create the bind
        self.Bind(wx.EVT_MENU, self.GetRangE, mIU)
        self.Bind(wx.EVT_MENU, self.GetSIZE, mIS)

    def GetRangE(self, event):
        ted = wx.TextEntryDialog(self, message="press the Range(integer):", style=wx.OK | wx.CANCEL)
        if ted.ShowModal() == wx.ID_OK:
            self.limit = int(ted.GetValue());

    def GetSIZE(self, event):
        ted = wx.TextEntryDialog(self, message="press the size(integer):", style=wx.OK | wx.CANCEL)
        if ted.ShowModal() == wx.ID_OK:
            self.sizee = int(ted.GetValue());
            self.font.SetPointSize(self.sizee)
            self.st.SetFont(self.font)
            self.font.SetPointSize(self.sizee + 10)
            self.st2.SetFont(self.font)


if __name__ == '__main__':
    app = wx.PySimpleApp();
    frame = Random();
    frame.Show(True);
    app.MainLoop()
