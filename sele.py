import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRegExp
from plt import Demo
from plt2 import Demo2
import time
from PyQt5.QtSql import QSqlDatabase,QSqlQuery

class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('查询')
        self.resize(600,400)

        layout = QGridLayout()

        self.edit1 = QLineEdit()
        # 使用int校验器
        self.edit1.setMaxLength(12)  # 不超过9999
        reg = QRegExp('[0-9]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)
        self.edit1.setValidator(validator)

        self.label1 = QLabel('请输入学号进行查询')
        self.label1.setStyleSheet("color:rgb(20,20,20,255);font-size:20px")

        self.cb = QComboBox()
        self.cb.addItem('数理学院')

        self.button1 = QPushButton()
        self.button1.setText('学院视角')
        self.button1.clicked.connect(self.state1)

        self.button2 = QPushButton()
        self.button2.setText('学生画像')
        self.button2.clicked.connect(self.state2)

        layout.addWidget(self.label1,0,1)
        layout.addWidget(self.edit1,1,1,2,1)
        layout.addWidget(self.button2,1,2,2,1)
        layout.addWidget(self.cb, 3, 1,2,1)
        layout.addWidget(self.button1 , 3, 2,2,1)

        self.setLayout(layout)

    def state1(self):
        h=self.sele_data("select * from stu_data where `学院` == '数理'")
        self.win1=Demo(h)
        self.win1.show()

    def state2(self):
        txt=self.edit1.text()
        if len(txt) !=12:
            self.messageDialog('请输入12位数字学号')
        else:
            h = self.sele_data("select * from stu_data where `学号` == "+txt)
            if len(h)>0:
                self.win2=Demo2(h[0])
                self.win2.show()
            else:
                self.messageDialog('查无此人')

    # 警告框
    def messageDialog(self,str):
        msg_box = QMessageBox(QMessageBox.Warning, 'Warning', str)
        msg_box.exec_()

    def sele_data(self,sql):

        db = QSqlDatabase.addDatabase('QSQLITE')
        # 指定SQLite数据库的文件名
        db.setDatabaseName('./data/stu_data.db')
        db.open()
        query = QSqlQuery()
        query.prepare(sql)
        ls=[]
        if not query.exec_():
            query.lastError()
        else:
            while query.next():
                a = [query.value(i) for i in range(20)]
                ls.append(a)
        db.close()
        return ls


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComboBoxDemo()
    main.show()
    sys.exit(app.exec_())