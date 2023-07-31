import psutil
import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(800, 500, 800, 500)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(800, 800)
        self.tableWidget.setColumnCount(len(psutil.users()[0]))
        self.tableWidget.setRowCount(len(psutil.users()))
        for i1, v1 in enumerate(psutil.users()):
            for i2,v2 in enumerate(v1):
                self.tableWidget.setItem(int(i1), int(i2), QTableWidgetItem(str(v2)))
                


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()