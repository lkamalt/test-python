from PyQt5 import QtWidgets, QtGui
import pyqtgraph as pg


class ProjType(object):
    MD_INCL, MD_AZIM, AZIM_INCL = range(3)


table_params_header = ['Среднее', 'СКО', 'Медиана']


class MyAppUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.showMaximized()
        self.setWindowTitle('Траектория')

        self.setWindowIcon(QtGui.QIcon('icon.svg'))

        # Минимальный размер для виджета
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        # Виджеты для загружаемого las-файла ------------------------------------------------------
        # Поле для вывода названия las-файла, оно недоступно для редактирования
        self.label_file_path = QtWidgets.QLabel('Название файла')
        self.edit_file_path = QtWidgets.QLineEdit()
        self.edit_file_path.setReadOnly(True)
        
        # Кнопка Browse для выбора las-файла
        self.button_browse = QtWidgets.QPushButton('Обзор...')
        self.button_browse.setSizePolicy(size_policy)
        
        # Горизонтальная сетка для элементов отображения и выбора файла
        hgrid_file = QtWidgets.QHBoxLayout()
        # Добавляем виджеты в горизонтальную сетку для элементов загружаемого файла
        hgrid_file.addWidget(self.label_file_path)
        hgrid_file.addWidget(self.edit_file_path)
        hgrid_file.addWidget(self.button_browse)

        # Таблицы для отображения параметров траектории -------------------------------------------
        self.tab_params = QtWidgets.QTabWidget()
        self.tab_params.setTabPosition(QtWidgets.QTabWidget.South)

        # Таблица, вычисленная кастомными функциями
        self.table_params_c = self._get_table_params()
        # Таблица, вычисленная функциями numpy
        self.table_params_np = self._get_table_params()

        self.tab_params.addTab(self.table_params_c, 'Пользовательские функции')
        self.tab_params.addTab(self.table_params_np, 'Numpy')

        self.tab_params.setFixedHeight(self.table_params_c.height())

        # Виджеты для графиков --------------------------------------------------------------------
        self.chart_md_incl = self._get_chart(ProjType.MD_INCL)
        self.chart_md_azim = self._get_chart(ProjType.MD_AZIM)
        self.chart_azim_incl = self._get_chart(ProjType.AZIM_INCL)

        # Вертикальная сетка для графиков
        vgrid_charts = QtWidgets.QVBoxLayout()
        vgrid_charts.addWidget(self.chart_md_incl, 1)
        vgrid_charts.addWidget(self.chart_md_azim, 1)
        vgrid_charts.addWidget(self.chart_azim_incl, 1)

        # Виджет, содержащий графики
        self.widget_charts = QtWidgets.QWidget()
        self.widget_charts.setLayout(vgrid_charts)

        # Кнопки для переключения проекций --------------------------------------------------------
        self.tbutton_md_incl = self._get_tool_button('MD-INCL')
        self.tbutton_md_azim = self._get_tool_button('MD-AZIM')
        self.tbutton_azim_incl = self._get_tool_button('AZIM-INCL')

        # Горизонтальная сетка для кнопок управления видимостью проекций
        hgrid_tbuttons = QtWidgets.QHBoxLayout()
        hgrid_tbuttons.addWidget(self.tbutton_md_incl)
        hgrid_tbuttons.addWidget(self.tbutton_md_azim)
        hgrid_tbuttons.addWidget(self.tbutton_azim_incl)
        hgrid_tbuttons.addStretch()

        # Вертикальная сетка для таблицы с параметрами и виджета с графиком
        vgrid_table_params_and_graph = QtWidgets.QVBoxLayout()
        # Добавление табвиджета с таблицами параметров траектории
        vgrid_table_params_and_graph.addWidget(self.tab_params)
        # Добавление виджета с графиками
        vgrid_table_params_and_graph.addWidget(self.widget_charts)
        # Добавление кнопок для управления видимостью проекций
        vgrid_table_params_and_graph.addLayout(hgrid_tbuttons)

        # Таблица для отображения загруженных из las-файла данных ----------------------------------
        self.table_trj = QtWidgets.QTableWidget()
        self.table_trj.horizontalHeader().setResizeMode(QtWidgets.QHeaderView.Stretch)

        # Горизонтальная сетка для сетки с табвиджетом и графиком и таблицы с таректорией
        hgrid_trj = QtWidgets.QHBoxLayout()
        hgrid_trj.addLayout(vgrid_table_params_and_graph)
        hgrid_trj.addWidget(self.table_trj)

        # Вертикальная сетка - основная -----------------------------------------------------------
        vgrid = QtWidgets.QVBoxLayout()
        vgrid.addLayout(hgrid_file)
        vgrid.addLayout(hgrid_trj)

        self.setLayout(vgrid)

    def _get_chart(self, proj_type):
        """
        Возвращает чарт - объект класса pg.PlotItem для отрисовки данных в зависимости от типа проекции
        :param proj_type: тип проекции, ProjType
        :return: объект класса pg.PlotItem
        """
        chart = pg.PlotWidget()
        chart.setBackground(pg.mkColor(255, 255, 255))
        plot_item = chart.getPlotItem()
        plot_item.showGrid(True, True, 0.5)

        label_color = {'color': (0, 0, 0)}
        bottom_units = 'м'
        left_units = u'\N{DEGREE SIGN}'

        if proj_type == ProjType.MD_INCL:
            plot_item.setTitle('Проекция MD-INCL', **label_color)
            bottom_axis_name = 'MD'
            left_axis_name = 'INCL'
        elif proj_type == ProjType.MD_AZIM:
            plot_item.setTitle('Проекция MD-AZIM', **label_color)
            bottom_axis_name = 'MD'
            left_axis_name = 'AZIM'
        else:
            plot_item.setTitle('Проекция AZIM-INCL', **label_color)
            bottom_axis_name = 'AZIM'
            left_axis_name = 'INCL'
            bottom_units = u'\N{DEGREE SIGN}'

        # Нижняя и левая оси
        bottom_axis = plot_item.getAxis('bottom')
        left_axis = plot_item.getAxis('left')

        # Задаем осям названия
        bottom_axis.setLabel(bottom_axis_name, bottom_units, **label_color)
        left_axis.setLabel(left_axis_name, left_units, **label_color)

        # Задаем осям стиль
        axis_pen = pg.mkPen(color=(0, 0, 0), width=1)
        bottom_axis.setPen(axis_pen)
        left_axis.setPen(axis_pen)

        return chart

    def _get_table_params(self):
        """
        Создание таблицы для отображения параметров траектории (mean, std, median)
        :return: таблица - объект класса QTableWidget
        """
        table_params = QtWidgets.QTableWidget()
        # Устанавливаем количество столбцов и подписи вертикальной шапки таблицы
        table_params.setRowCount(3)
        table_params.setColumnCount(3)
        table_params.setVerticalHeaderLabels(table_params_header)
        table_params.horizontalHeader().setResizeMode(QtWidgets.QHeaderView.Stretch)
        table_params.setFixedHeight(150)

        return table_params

    def _get_tool_button(self, name):
        """
        Создание кнопки для управления видимостью графиков
        :param name: название кнопки, str
        :return: кнопка - объект класса QToolButton
        """
        tbutton = QtWidgets.QToolButton()
        tbutton.setCheckable(True)
        tbutton.setChecked(True)
        tbutton.setText(name)
        return tbutton
