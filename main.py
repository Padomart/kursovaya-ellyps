from initial_data import ishodn
from extensions.basic import calculation, cipher, transcript, zadacha4, zadacha3
import wx
from extensions.selection import Choices, Radio
from calc.wxcalc import CalculatorFrame
from extensions.menubar import MyMenu, ID_CALCULATOR, ID_ISH, InfoIshodData, InfoDeveloper, ID_DEV, InfoApp


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, pos=(100, 100), size=(700, 350))

        # Создаем основную панель
        panel = wx.Panel(self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        panel.SetSizer(hbox)
        menu = MyMenu()

        # Создаем левую панель для текста
        self.left_panel = wx.Panel(panel)
        self.left_vbox = wx.BoxSizer(wx.VERTICAL)
        self.left_panel.SetSizer(self.left_vbox)

        # Создаем кнопки
        self.choices = Choices(self.left_panel)
        self.calculate = wx.Button(self.left_panel, label="Расчет")
        self.radio = Radio(self.left_panel)

        self.left_vbox.Add(wx.StaticText(self.left_panel, label="Выбор варианта"), flag=wx.LEFT, border=20)
        self.left_vbox.Add(self.choices, flag=wx.EXPAND | wx.ALL, border=0)
        self.left_vbox.Add(self.radio, flag=wx.EXPAND | wx.ALL, border=0)
        self.left_vbox.Add(self.calculate, flag=wx.ALIGN_RIGHT)

        # Создаем вкладки
        self.tabs = Tasks(panel)

        hbox.Add(self.left_panel, 3, wx.EXPAND | wx.ALL, 5)
        hbox.Add(self.tabs, 7, wx.EXPAND | wx.ALL, 5)
        panel.SetSizer(hbox)

        self.SetMenuBar(menu)
        self.dlg = None

        self.calculate.Bind(wx.EVT_BUTTON, self.on_calculate)
        self.Bind(wx.EVT_MENU, self.info_show_dev, id=ID_DEV)
        self.Bind(wx.EVT_MENU, self.info_show_app, id=wx.ID_INFO)
        self.Bind(wx.EVT_MENU, self.tool_calculator, id=ID_CALCULATOR)
        self.Bind(wx.EVT_MENU, self.tool_show_ish, id=ID_ISH)
        self.Bind(wx.EVT_CLOSE, self.on_close)

    def on_close(self, event):
        choices_panel = Choices(self)  # Создание экземпляра класса Choices
        selected_variant = choices_panel.get_selected_value()
        ishodn.selected_variant = selected_variant
        event.Skip()

    def on_calculate(self, event):
        self.tabs.task1(self.choices, self.radio.on_radio_select(self.radio))
        self.tabs.task2(self.choices, self.radio.on_radio_select(self.radio))
        self.tabs.task3()
        self.tabs.task4()

    def tool_calculator(self, event):
        calculator = CalculatorFrame(self, title='Калькулятор')
        calculator.Show()

    def tool_show_ish(self, event):
        variant = self.choices.get_selected_value()
        data = ishodn.vaar(variant)
        if self.dlg is None:
            self.dlg = InfoIshodData(self, title='Исходные данные для выбр. варианта', data=data)
            self.dlg.Show()

    def info_show_dev(self, event):
        if self.dlg is None:
            self.dlg = InfoDeveloper(self, title='')
            self.dlg.Show()

    def info_show_app(self, event):
        if self.dlg is None:
            self.dlg = InfoApp(self, title='О программе')
            self.dlg.Show()


class Tasks(wx.Notebook):
    def __init__(self, parent):
        super().__init__(parent)

        self.page1 = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT)
        self.page1.SetFont(wx.Font(wx.FontInfo(12)))
        self.page1.SetBackgroundColour(wx.Colour('white'))
        self.page3 = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.page4 = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.page2 = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT)
        self.page2.SetFont(wx.Font(wx.FontInfo(12)))
        self.page2.SetBackgroundColour(wx.Colour('white'))

        self.z1 = wx.StaticText(self, label="")
        self.InsertPage(0, self.page1, "Задача 1", select=True)
        self.InsertPage(1, self.page2, "Задача 2")
        self.InsertPage(2, self.page3, "Задача 3")
        self.InsertPage(3, self.page4, "Задача 4")

    def task1(self, choices, selected_option):
        self.page1.ClearAll()
        ishodn.change_variable(choices.get_selected_value())

        ishodn.kpb['pb1'] = ishodn.b
        gk = calculation(0, 1, 0, 1, ishodn.gk, "g", ishodn.K)
        kpb = calculation(ishodn.b[0], ishodn.b[1], ishodn.b[0], ishodn.b[1], ishodn.kpb, "pb", ishodn.K)
        ciphr = cipher(ishodn.K)

        if selected_option:
            self.page1.InsertColumn(1, 'Нумерация', width=95)
            self.page1.InsertColumn(2, 'Kg', width=90)
            self.page1.InsertColumn(3, 'Pb', width=90)
            self.page1.InsertColumn(4, '', width=30)
            for k in range(1, max(ishodn.K) + 1):
                if k in ishodn.K:
                    self.page1.Append((k, gk[f"g{k}"], kpb[f"pb{k}"], "✓"))
                else:
                    self.page1.Append((k, gk[f"g{k}"], kpb[f"pb{k}"]))
        else:
            self.page1.InsertColumn(1, 'x', width=60)
            self.page1.InsertColumn(2, 'y', width=60)
            self.page1.InsertColumn(3, 'Шифртекст', width=200)
            for cifr in ciphr:
                self.page1.Append(cifr)

    def task2(self, choices, selected_option):
        self.page2.ClearAll()
        ishodn.change_variable(choices.get_selected_value())
        if selected_option:
            self.page2.InsertColumn(0, 'i-й символ', width=160)
            self.page2.InsertColumn(1, 'Координаты', width=105)
            trans = transcript()[1]
        else:
            self.page2.InsertColumn(1, 'λ', width=60)
            self.page2.InsertColumn(2, 'Координаты', width=105)
            self.page2.InsertColumn(3, 'Буква', width=80)
            trans = transcript()[0]

        for symbol in trans:
            self.page2.Append(symbol)

    def task3(self):
        self.page3.Clear()
        for elemeint in zadacha3():
            self.page3.AppendText(elemeint + '\n')

    def task4(self):
        self.page4.Clear()
        self.page4.AppendText(str(zadacha4()))


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, 'wxPython')
    frame.Show()
    app.MainLoop()
