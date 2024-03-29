import wx

ID_CALCULATOR = 777
ID_ISH = 778
ID_DEV = 779


class MyMenu(wx.MenuBar):
    def __init__(self):
        super(MyMenu, self).__init__()

        tools_menu = wx.Menu()
        tools_menu.Append(ID_CALCULATOR, "Калькулятор")
        tools_menu.Append(ID_ISH, "Исходные данные")

        info_menu = wx.Menu()
        info_menu.Append(wx.ID_INFO, "Инфо")
        info_menu.Append(ID_DEV, "Разработчик")

        self.Append(tools_menu, "Инструменты")
        self.Append(info_menu, "О программе")


class InfoIshodData(wx.Dialog):
    def __init__(self, parent, data, *args, **kwargs):
        super().__init__(parent, *args, **kwargs, size=(350, 300))

        self.text = wx.TextCtrl(self, style=wx.ALIGN_CENTER_HORIZONTAL | wx.TE_READONLY | wx.TE_MULTILINE)
        formatted_data = '\n'.join([f"{key} = {value}" for key, value in data.items()])
        self.text.SetValue(formatted_data)

        self.Bind(wx.EVT_CLOSE, self.onClose)
        self.parent = parent

    def onClose(self, event):
        self.Destroy()
        self.parent.dlg = None


class InfoDeveloper(wx.Dialog):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs, size=(200, 100))

        wx.StaticText(self, label="Разработчик: \nАртур Джанкуланов ДЗ-41\n\n© 2023", style=wx.ALIGN_CENTER_HORIZONTAL)
        self.parent = parent
        self.Bind(wx.EVT_CLOSE, self.onClose)

    def onClose(self, event):
        self.Destroy()
        self.parent.dlg = None


class InfoApp(wx.Dialog):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs, size=(350, 240))

        wx.StaticText(self, label="Программа с графическим интерфейсом по курсовой:\n\n"
                                  "Криптографические методы защиты информации на основе эллиптических кривых\n\n"
                                  "В интерфейсе представлены:\n"
                                  "1. Выпадающий список с выбором варианта\n"
                                  "2. Выбор таблицы для задач 1, 2\n"
                                  "3. Кнопка выполнить\n"
                                  "4. Окно вывода с выбором задачи\n\n"
                                  "В вкладки-инструменты присутствует\n"
                                  "калькулятор для сложения точек на кривой\n\n", style=wx.ALIGN_CENTER_HORIZONTAL)
        self.parent = parent
        self.Bind(wx.EVT_CLOSE, self.onClose)

    def onClose(self, event):
        self.Destroy()
        self.parent.dlg = None
