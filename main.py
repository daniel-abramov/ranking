import sys
import math
import numpy as np

from PySide.QtGui import QMainWindow
from PySide.QtGui import QApplication, QTableWidgetItem
from mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.prioritiesEdit.setText("1.0 1.0 1.0")

        self.priorities = np.array([1.0, 1.0, 1.0])
        self.alternatives = np.array([
            [0.1, 10, 350],
            [1.3, 15, 250],
            [0.8, 10, 300],
            [3.2, 50, 150],
            [0.5, 30, 750],
            [2.5, 23, 400]
        ])
        self.update_table()

        self.normalizeButton.clicked.connect(self.normalize)
        self.actionAdditive.triggered.connect(self.additive)
        self.actionMultiplicative.triggered.connect(self.multiplicative)
        self.actionKobbDouglas.triggered.connect(self.kobb_douglas)
        self.actionMainIndividual.triggered.connect(self.individual)
        self.actionPareto.triggered.connect(self.pareto)
        self.actionIdealPoint.triggered.connect(self.idealPoint)

    def prepare_calculations(self):
        self.parse_priorities()
        self.normalize_priorities()
        self.f0 = []

    def idealPoint(self):
        self.prepare_calculations()
        ideal_point = np.max(self.alternatives, axis = 0)
        for row in self.alternatives:
            distance = np.sum(self.priorities * ((ideal_point - row)) ** 2.0) ** 0.5
            self.f0.append(distance)
        self.display_f0()

    def pareto(self):
        dimensions = ( len(self.alternatives), len(self.alternatives) )
        pareto_matrix = np.zeros(shape=dimensions)
        final_str = ""
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                if i != j:
                    pareto_matrix[i][j] = np.all(self.alternatives[i] > self.alternatives[j])
                final_str += "%5d " % pareto_matrix[i][j]
            final_str += "\n"
        self.textEdit.setText(final_str)

        elites = dict()
        for column_index in range(dimensions[1]):
            ones_count = np.count_nonzero(pareto_matrix[:, column_index])
            if ones_count in elites:
                elites[ones_count].append(column_index+1)
            else:
                elites[ones_count] = [column_index+1]

        for key in elites.keys():
            self.textEdit.append("\n%d elite: %s" % (key + 1, elites[key]))

    def individual(self):
        self.prepare_calculations()
        for row in self.alternatives:
            params_ok = True
            for i in range(len(self.priorities)):
                if row[i] < self.priorities[i]:
                    params_ok = False
                    break
            if params_ok:
                self.f0.append(row[0])
            else:
                self.f0.append(0)
        self.display_f0()

    def kobb_douglas(self):
        self.prepare_calculations()
        for row in self.alternatives:
            mul = 1.0
            for i in range(len(self.priorities)):
                mul *= math.pow(self.priorities[i] * row[i], 1.0 / len(self.priorities))
            self.f0.append(mul)
        self.display_f0()

    def multiplicative(self):
        self.prepare_calculations()
        for row in self.alternatives:
            mul = np.product(self.priorities * row)
            self.f0.append(mul)
        self.display_f0()

    def additive(self):
        self.prepare_calculations()
        for row in self.alternatives:
            f0 = sum([x * y for (x, y) in zip(row, self.priorities)])
            self.f0.append(f0)
        self.display_f0()

    def normalize_priorities(self):
        priorities_sum = np.sum(self.priorities)
        if priorities_sum != 0:
            self.priorities /= np.sum(self.priorities)

    def display_f0(self):
        last_column = self.tableWidget.columnCount() - 1
        for i, value in enumerate(self.f0):
            self.tableWidget.setItem(i, last_column, QTableWidgetItem(str(value)))
        self.tableWidget.setHorizontalHeaderItem(last_column, QTableWidgetItem("f0"))
        # self.tableWidget.sortItems(last_column)

    def normalize(self):
        self.alternatives = ((self.alternatives - self.alternatives.min(axis=1)) /
                (self.alternatives.max(axis=1) - self.alternatives.min(axis=1)))
        self.update_table()

    def update_table(self):
        self.tableWidget.clear()
        (rows, columns) = self.alternatives.shape
        self.tableWidget.setRowCount(rows)
        self.tableWidget.setColumnCount(columns + 1)

        for i, row in enumerate(self.alternatives):
            self.tableWidget.setVerticalHeaderItem(i, QTableWidgetItem("A" + str(i)))
            for j, value in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))

    def parse_priorities(self):
        text = self.prioritiesEdit.text()
        values = text.split(' ')
        if len(values) != 3:
            raise IOError()
        self.priorities = np.array([float(x) for x in values])


app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()
