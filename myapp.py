from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import numpy as np
import lasio

from myapp_ui import MyAppUI
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
                    self.data[curve.mnemonic] = curve.data
                    self.data_params[curve.mnemonic] = [get_mean_custom(curve.data),
                                                        get_std_custom(curve.data),
                                                        get_median_custom(curve.data)]

                # Заполняем таблицу с параметрами кривых (mean, std, median)
                self.fill_table_params()

    def fill_table_params(self):
        """ Заполнение таблицы с параметрами траектории скважины """
        def get_table_item(value):
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

        # Устанавливаем количество строк и задаем подписи горизонтальной шапки таблицы названиями колонок из las-файла
        self.table_params.setColumnCount(len(self.data))
        self.table_params.setHorizontalHeaderLabels(self.data.keys())

        for row in range(0, 3):
            for col, name in enumerate(self.data.keys()):
                value = np.around(self.data_params[name][row], 2)
                item = get_table_item(value)
                self.table_params.setItem(row, col, item)
