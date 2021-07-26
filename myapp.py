from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import numpy as np
import pyqtgraph as pg
import lasio

from myapp_ui import MyAppUI, ProjType
from funcs import get_mean_custom, get_std_custom, get_median_custom


class MyApp(MyAppUI):
    def __init__(self):
        super().__init__()

        # Название las-файла
        self.file_name = None
        # Словарь, который хранит загруженные из las-файла данные
        self.data = {}
        # Словарь, который хранит параметры (mean, std, median) каждой кривой из las-файла
        self.data_params = {}

        # Количество строк и столбцов в таблице из данных las-файла
        self.ncols = 0
        self.nrows = 0

        self.connect_signals()

    def connect_signals(self):
        self.button_browse.clicked.connect(self.browse_to_open)

    def browse_to_open(self):
        """ Слот, срабатывающий при нажатии на кнопку 'Обзор...' """
        # Маска, чтобы пользователь мог выбирать только las-файлы
        filters = "Las files (*.las)"
        # Возаращает список: [название_файла, фильтры]
        file_names = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбрать файл', None, filters)

        # Записываем путь в текстбокс и считываем файл, только если выбрали файл
        if file_names:
            # Если файл не был выбран, то возвращается список из двух пустых строк, поэтому нужно проверить
            # что первый элемент - название файла не является пустой строкой
            if file_names[0] != '':
                self.file_name = file_names[0]
                self.edit_file_path.setText(self.file_name)

                # Считывание из las-файла
                las = lasio.read(self.file_name)

                # Заносим загруженные из файла данные в словарь
                for curve in las.curves:
                    self.ncols += 1
                    self.nrows = len(curve.data)

                    self.data[curve.mnemonic] = curve.data
                    self.data_params[curve.mnemonic] = [get_mean_custom(curve.data),
                                                        get_std_custom(curve.data),
                                                        get_median_custom(curve.data)]

                # Заполняем таблицу с параметрами кривых (mean, std, median)
                self.fill_table_params()

                # Заполняем таблицу с загруженной траекторией
                self.fill_table_trj()

                # Отрисовка линий
                self.draw_curves()

    def _get_table_item(self, value):
        """
        Создает ячейку таблицы и заполняет её значением value
        :param value: число, которое должно быть записано в текущей ячейке, float
        :return: объект ячейки таблицы, QTableWidgetItem
        """
        item = QtWidgets.QTableWidgetItem()
        item.setText(str(value))
        # Включаем в ячейке выравнивание текста по центру
        item.setTextAlignment(Qt.AlignCenter)
        # Ячейки таблицы делаем нередактируемыми
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        return item

    def fill_table_params(self):
        """ Заполнение таблицы с параметрами траектории скважины """
        # Устанавливаем количество строк и задаем подписи горизонтальной шапки таблицы названиями колонок из las-файла
        self.table_params.setColumnCount(len(self.data))
        self.table_params.setHorizontalHeaderLabels(self.data.keys())

        for row in range(0, 3):
            for col, name in enumerate(self.data.keys()):
                value = np.around(self.data_params[name][row], 2)
                item = self._get_table_item(value)
                self.table_params.setItem(row, col, item)

    def fill_table_trj(self):
        """ Заполнение таблицы траекторией скважины """
        # Устанавливаем число столбцов и строк
        self.table_trj.setColumnCount(self.ncols)
        self.table_trj.setRowCount(self.nrows)

        # Задаем названия столбцов в шапке таблицы названиями из las-файла
        self.table_trj.setHorizontalHeaderLabels(self.data.keys())

        # Заполнение таблицы
        for row in range(0, self.nrows):
            for col, name in enumerate(self.data.keys()):
                value = np.around(self.data[name][row], 2)
                item = self._get_table_item(value)
                self.table_trj.setItem(row, col, item)

    def draw_curves(self):
        """ Отрисовка кривых """
        def get_curve(proj_type):
            """
            Возаращает данные по типу проекции
            :param proj_type: тип проекции, ProjType
            :return: кортеж из двух списков, tupe(np.array, np.array)
            """
            if proj_type == ProjType.MD_INCL:
                data = (self.data['MD'], self.data['INCL'])
            elif proj_type == ProjType.MD_AZIM:
                data = (self.data['MD'], self.data['AZIM'])
            else:
                data = (self.data['AZIM'], self.data['INCL'])

            plot_curve_item = pg.PlotCurveItem(*data)
            plot_curve_item.setPen(pg.mkPen(color=(0, 0, 0), width=2))
            return plot_curve_item

        self.chart1.addItem(get_curve(ProjType.MD_INCL))
        self.chart2.addItem(get_curve(ProjType.MD_AZIM))
        self.chart3.addItem(get_curve(ProjType.AZIM_INCL))
