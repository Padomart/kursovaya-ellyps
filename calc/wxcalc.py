import wx
import re
from calc.validators import Numbers
from calc.moduls.modils import proverka, a, p, bool_proverka
from extensions.basic import equal_alph, unequal


class CalculatorFrame(wx.Frame):
    def __init__(self, parent, title):
        super(CalculatorFrame, self).__init__(parent, title=title, size=(425, 260))

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour('white'))
        self.vbox = wx.BoxSizer(wx.VERTICAL)

        # icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images', 'calculator.ico')
        # icon = wx.Icon(icon_path, wx.BITMAP_TYPE_ICO)
        # self.SetIcon(icon)

        validator = Numbers()
        #
        # self.Bind(wx.EVT_MENU, self.on_view_select, id=101)
        # self.Bind(wx.EVT_MENU, self.on_view_select, id=102)

        self.flexsize = wx.FlexGridSizer(2, 2, 1, 1)
        self.flexsize.AddGrowableCol(1, 1)

        self.label_x1 = wx.StaticText(self.panel, label="Первая координата:")
        self.entry_xy1 = wx.TextCtrl(self.panel, style=wx.TE_PROCESS_ENTER, validator=validator)
        self.entry_xy1.SetHint("x, y")
        self.flexsize.Add(self.label_x1, flag=wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, border=10)
        self.flexsize.Add(self.entry_xy1, flag=wx.EXPAND, proportion=1)

        self.label_x2 = wx.StaticText(self.panel, label="Вторая координата:")
        self.entry_xy2 = wx.TextCtrl(self.panel, style=wx.TE_PROCESS_ENTER, validator=validator)
        self.entry_xy2.SetHint("x, y")
        self.flexsize.Add(self.label_x2, flag=wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, border=10)
        self.flexsize.Add(self.entry_xy2, flag=wx.EXPAND, proportion=1)
        self.vbox.Add(self.flexsize, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        st2 = wx.StaticText(self.panel, label='Ответ')
        self.vbox.Add(st2, flag=wx.EXPAND | wx.LEFT, border=10)

        self.result_text = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.vbox.Add(self.result_text, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, border=10)

        self.result_box = wx.FlexGridSizer(1, 2, 1, 1)
        self.result_box.AddGrowableCol(0, 1)

        self.calculate_button = wx.Button(self.panel, label='Вычислить', size=(70, 30))
        self.empty_space = wx.StaticText(self.panel, label='')
        self.result_box.Add(self.empty_space, flag=wx.EXPAND | wx.ALL, proportion=1)
        self.result_box.Add(self.calculate_button, flag=wx.RIGHT | wx.DOWN)

        self.vbox.Add(self.result_box, proportion=0, flag=wx.EXPAND | wx.DOWN | wx.LEFT | wx.RIGHT, border=10)
        self.panel.SetSizer(self.vbox)

        self.entry_xy1.Bind(wx.EVT_TEXT_ENTER, self.on_enter_press_xy1)
        self.entry_xy1.Bind(wx.EVT_TEXT, self.calculate)
        self.calculate_button.Bind(wx.EVT_BUTTON, self.calculate)
        self.entry_xy2.Bind(wx.EVT_TEXT, self.calculate)
        self.entry_xy2.Bind(wx.EVT_TEXT_ENTER, self.calculate)

    def on_enter_press_xy1(self, event):
        if event.GetEventObject() == self.entry_xy1:
            self.entry_xy2.SetFocus()

    def on_enter_press_xy2(self, event):
        if event.GetEventObject() == self.entry_xy2:
            self.calculate(event)

    def calculate(self, event):
        value1 = self.entry_xy1.GetValue().strip("(){}[] ")
        value2 = self.entry_xy2.GetValue().strip("(){}[] ")

        if value1 and value2:
            match1 = re.match(r"^\s*\(*\s*\d+\s*,\s*\d+\s*\)*\s*$", value1)
            match2 = re.match(r"^\s*\(*\s*\d+\s*,\s*\d+\s*\)*\s*$", value2)
            if match1 and match2:
                x1, y1 = map(int, re.sub(r"[,?.бБ]", ",", value1).split(","))
                x2, y2 = map(int, re.sub(r"[,?.бБ]", ",", value2).split(","))

                self.result_text.Clear()
                if (x1 == x2) and (y1 == y2):
                    alpha = equal_alph(x1, y1)
                    self.result_text.AppendText(f"λ = (3 * ({x1} ^ 2) - {a})/(2 * {y1}) = {alpha}\n")
                elif (x1 == x2) or (y1 == y2):
                    alpha = unequal(x1, y1, x2, y2)
                    self.result_text.AppendText(f"λ = ({y2}-{y1})/({x2}-{x1}) = {alpha}\n")
                else:
                    alpha = unequal(x1, y1, x2, y2)
                    self.result_text.AppendText(f"λ = ({y2}-{y1})/({x2}-{x1}) = {alpha}\n")

                x3 = ((alpha ** 2) - x1 - x2) % p
                y3 = (alpha * (x1 - x3) - y1) % p

                self.result_text.AppendText(f"x3 = ({alpha}^2 - {x1} - {x2}) mod751 = {x3}\n")
                self.result_text.AppendText(f"y3 = ({alpha} * ({x1} - {x3}) - {y1}) mod751 = {y3}\n")
                self.result_text.AppendText(proverka(x3, y3))
                if bool_proverka(x3, y3) is True:
                    self.empty_space.SetLabel(f"x3, y3 = {x3}, {y3}")
        else:
            self.empty_space.SetLabel("")


if __name__ == '__main__':
    app = wx.App()
    frame = CalculatorFrame(None, title='Cложение точек на эллиптической кривой')
    frame.Show()
    app.MainLoop()
