import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from sele import QComboBoxDemo
from edit import *
from PyQt5.QtSql import QSqlDatabase,QSqlQuery

class mainwin(QWidget):
    def __init__(self):
        super(mainwin,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('bitzh')
        self.resize(600,300)

        layout = QGridLayout()
        self.label1 = QLabel('学生信息管理系统')
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setStyleSheet("color:rgb(200,20,20,255);font-size:30px")

        self.button1 = QPushButton()
        self.button1.setText('数据编辑')
        self.button1.clicked.connect(self.zh1)

        self.button2 = QPushButton()
        self.button2.setText('数据查询')
        self.button2.clicked.connect(self.zh2)

        layout.addWidget(self.label1,0,0)
        layout.addWidget(self.button1,1,0)
        layout.addWidget(self.button2,2,0)

        self.setLayout(layout)

    def zh1(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('./data/stu_data.db')
        model = QSqlTableModel()
        initializeModel(model)
        view = createView("展示数据", model)
        view.clicked.connect(findrow)

        self.dlg = QDialog()
        layout = QVBoxLayout()
        layout.setSpacing(40)
        layout.addWidget(view)
        addBtn = QPushButton('添加一行')
        addBtn.clicked.connect(addrow)

        delBtn = QPushButton('删除一行')
        delBtn.clicked.connect(lambda: model.removeRow(view.currentIndex().row()))
        layout.addWidget(addBtn)
        layout.addWidget(delBtn)

        self.dlg.setLayout(layout)
        self.dlg.setWindowTitle("Edit")
        self.dlg.resize(1200, 600)

        self.dlg.show()

    def zh2(self):
        self.win2=QComboBoxDemo()
        self.win2.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = mainwin()
    main.show()
    sys.exit(app.exec_())
