from PyQt5 import QtWidgets, QtGui


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
        # self.edit_file_path.setSizePolicy(size_policy)
        self.edit_file_path.setReadOnly(True)
        
        # Кнопка Browse для выбора las-файла
        self.button_browse = QtWidgets.QPushButton('Обзор...')
        self.button_browse.setSizePolicy(size_policy)
        
        # Горизонтальная сетка для элементов отображения и выбора файла
        self.hgrid_file = QtWidgets.QHBoxLayout()
        # Добавляем виджеты в горизонтальную сетку для элементов загружаемого файла
        self.hgrid_file.addWidget(self.label_file_path)
        self.hgrid_file.addWidget(self.edit_file_path)
        self.hgrid_file.addWidget(self.button_browse)

        # Таблица для отображения параметров траектории -------------------------------------------
        self.table_params = QtWidgets.QTableWidget()
        # Устанавливаем количество столбцов и подписи вертикальной шапки таблицы
        self.table_params.setRowCount(3)
        self.table_params.setVerticalHeaderLabels(['mean', 'std', 'median'])
        # self.table_params.resizeColumnsToContents()
        # self.table_params.resizeRowsToContents()
        self.table_params.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)

        # Вертикальная сетка - основная -----------------------------------------------------------
        self.vgrid = QtWidgets.QVBoxLayout()
        self.vgrid.addLayout(self.hgrid_file)
        self.vgrid.addWidget(self.table_params)

        self.setLayout(self.vgrid)
