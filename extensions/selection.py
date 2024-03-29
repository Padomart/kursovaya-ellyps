import wx


class Choices(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        choices = [f"Вариант: {i}" for i in range(1, 28)]  # Создаем 27 вариантов

        self.combo = wx.ComboBox(self, choices=choices, style=wx.CB_DROPDOWN | wx.TE_READONLY)
        self.combo.Bind(wx.EVT_COMBOBOX, self.on_combobox)  # Привязываем событие выбора
        self.combo.SetSelection(0)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.combo, 0, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(sizer)

        self.selected_value = 1

    def on_combobox(self, event):
        self.selected_value = self.combo.GetValue().split(" ")[-1]

    def get_selected_value(self):
        return self.selected_value


class Radio(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        # Создаем Radiobuttons
        self.rb_option1 = wx.RadioButton(self, label='Таблица 1')
        self.rb_option2 = wx.RadioButton(self, label='Таблица 2')

        self.rb_option1.Bind(wx.EVT_RADIOBUTTON, self.on_radio_select)
        self.rb_option1.SetFocus()
        self.rb_option2.Bind(wx.EVT_RADIOBUTTON, self.on_radio_select)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.rb_option1, flag=wx.EXPAND | wx.ALL, border=10)
        sizer.Add(self.rb_option2, flag=wx.EXPAND | wx.ALL, border=10)

        self.SetSizer(sizer)

    def on_radio_select(self, event):
        selected_option = self.rb_option1.GetValue()
        return selected_option
