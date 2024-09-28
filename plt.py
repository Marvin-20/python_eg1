import sys
from PyQt5.QtCore import Qt
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] =False

class MyFigureCanvas(FigureCanvas):
    """
    画布
    """
    def __init__(self):
        # 画布上初始化一个图像
        self.figure = Figure()
        super().__init__(self.figure)

class Demo(QWidget):
    def __init__(self,h):
        super(Demo, self).__init__()
        self.resize(1200, 900)
        #self.h=h
        self.h=pd.DataFrame(h)



        self.label1 = QLabel(self.h.iloc[0,5]+'学院\n\n专业数：4')

        self.label1.setStyleSheet("color:rgb(20,20,20,255);font-size:20px")
        self.label2 = QLabel('总人数：'+str(len(self.h))+'\n\n学院平均成绩：'+str(np.mean([float(i) for i in self.h.iloc[:,9]]))[0:4])

        self.label2.setStyleSheet("color:rgb(20,20,20,255);font-size:20px")

        self.figureCanvas = MyFigureCanvas()
        self.__draw_figure__()

        self.plot_btn = QPushButton('返回', self)
        self.plot_btn.clicked.connect(self.plot_slot)


        self.v_layout = QGridLayout()
        self.v_layout.addWidget(self.label1, 0, 0)
        self.v_layout.addWidget(self.label2, 0, 1)
        self.v_layout.addWidget(self.figureCanvas,1,0,4,2)
        self.v_layout.addWidget(self.plot_btn,5,1)
        self.setLayout(self.v_layout)

    def plot_slot(self):
        self.close()

    def __draw_figure__(self):
        # 下面的步骤和调用的方法和plot大致相同，这里我写一个简单的折线图
        self.axes = self.figureCanvas.figure.add_subplot(221)
        self.axes.set_title("专业设置")
        self.axes.set_xlabel("")
        self.axes.set_ylabel("人数")
        result = pd.value_counts(self.h.iloc[:,6])

        x = result.index.to_list()
        y = result.values.tolist()
        self.axes.bar(x, y, color = "m",width = 0.6 )

        self.axes2 = self.figureCanvas.figure.add_subplot(222)
        self.axes2.set_title("年级")
        result2 = pd.value_counts(self.h.iloc[:,3])
        lab = result2.index.to_list()
        num = result2.values.tolist()
        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
        self.axes2.pie(x = num, labels =lab ,autopct='%1.1f%%',colors=colors, shadow=True, startangle=90,pctdistance = 0.6)
        self.axes2.axis('equal')

        self.axes3 = self.figureCanvas.figure.add_subplot(223)
        self.axes3.set_title("")
        jidian = self.h.iloc[:,9]
        density = gaussian_kde(jidian)
        density.covariance_factor = lambda: .25
        density._compute_covariance()
        xs = np.linspace(1, 4.5, 100)
        self.axes3.set_ylabel("绩点分布")
        self.axes3.plot(xs,density(xs))

        self.axes4 = self.figureCanvas.figure.add_subplot(224)
        self.axes4.set_title("就业去向")
        self.axes4.set_xlabel("")
        self.axes4.set_ylabel("")
        result2 = pd.value_counts(self.h.iloc[:, 18])
        x2 = result2.index.to_list()
        y2 = result2.values.tolist()
        self.axes4.bar(x2, y2, color="m", width=0.6)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    t=pd.read_csv('data/data.csv')
    demo = Demo(h=t)
    demo.show()
    sys.exit(app.exec_())
    ##435135
