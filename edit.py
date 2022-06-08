
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

def initializeModel(model):
    model.setTable('stu_data')
    model.setEditStrategy(QSqlTableModel.OnFieldChange)
    model.select()


def createView(title,model):
    view = QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view
def findrow(i):
    delrow = i.row()

def addrow():
    ret = model.insertRows(model.rowCount(),1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('./data/stu_data.db')
    model = QSqlTableModel()
    delrow = -1
    initializeModel(model)
    view = createView("展示数据",model)
    view.clicked.connect(findrow)

    dlg = QDialog()
    layout = QVBoxLayout()
    layout.setSpacing(40)
    layout.addWidget(view)
    addBtn = QPushButton('添加一行')
    addBtn.clicked.connect(addrow)

    delBtn = QPushButton('删除一行')
    delBtn.clicked.connect(lambda :model.removeRow(view.currentIndex().row()))
    layout.addWidget(addBtn)
    layout.addWidget(delBtn)

    dlg.setLayout(layout)
    dlg.setWindowTitle("Edit")
    dlg.resize(1200,600)

    dlg.show()

    sys.exit(app.exec())