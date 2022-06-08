import sys
import numpy as np
from PyQt5.QtWidgets import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import  QApplication, QWidget, QGridLayout
import matplotlib.pyplot as plt
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

class Demo2(QWidget):
    def __init__(self,h):
        super(Demo2, self).__init__()
        self.resize(1400, 900)
        self.h=h

        self.label1 = QLabel('姓名：'+self.h[1]+'\n\n学院：'+self.h[5]+'\n\n民族：'+str(self.h[2])+'\n\n应修学分：'+self.h[10])
        self.label1.setStyleSheet("color:rgb(20,20,20,255);font-size:20px")
        self.label2 = QLabel('学号：'+str(self.h[4])+'\n\n年级：'+self.h[3]+'\n\n排名：'+self.h[8]+'\n\n已修学分：'+self.h[11])
        self.label2.setStyleSheet("color:rgb(20,20,20,255);font-size:20px")
        self.label3 = QLabel('身份：'+str(self.h[7])+'\n\n专业：'+self.h[6]+'\n\n绩点：'+str(self.h[9])+'\n\n挂科学分：'+self.h[12])
        self.label3.setStyleSheet("color:rgb(20,20,20,255);font-size:20px")

        self.figureCanvas = MyFigureCanvas()
        self.__draw_figure__()

        self.plot_btn = QPushButton('返回', self)
        self.plot_btn.clicked.connect(self.plot_slot)


        self.v_layout = QGridLayout()
        self.v_layout.addWidget(self.label1, 0, 0)
        self.v_layout.addWidget(self.label2, 0, 1)
        self.v_layout.addWidget(self.label3, 0, 2)
        self.v_layout.addWidget(self.figureCanvas,1,0,2,3)
        self.v_layout.addWidget(self.plot_btn,3,1)
        self.setLayout(self.v_layout)

    def plot_slot(self):
        self.close()

    def __draw_figure__(self):
        # 下面的步骤和调用的方法和plot大致相同，这里我写一个简单的折线图
        self.axes = self.figureCanvas.figure.add_subplot(121,polar=True)
        self.axes.set_title("个人画像")
        ls=[]
        ls.append(self.h[9]-int(self.h[12])/5)
        tinydict = {'党员': 4.5, '预备党员': 4, '入党积极分子': 3.5,'团员':3,'群众':2.5}
        num = 0.3 if self.h[2]=='汉' else 0.5
        ls.append(tinydict[self.h[7]]+num)
        ls.append(4-1*int(self.h[13]))
        ls.append(4.5-abs(int(self.h[16])-1900)/400)
        ls.append(4.5-0.5*self.h[14])
        values = np.array(ls)
        feature = np.array(['学习', '身份', '奖励', '生活', '信用'])

        N = len(values)
        # 设置雷达图的角度，用于平分切开一个圆面
        angles = np.linspace(0, 2 * np.pi, N, endpoint=False)

        # 将折线图形进行封闭操作
        values = np.concatenate((values, [values[0]]))
        angles = np.concatenate((angles, [angles[0]]))
        feature = np.concatenate((feature, [feature[0]]))
        # 绘制折线图
        self.axes.plot(angles, values, 'o-', linewidth=2)
        # 填充颜色
        self.axes.fill(angles, values, alpha=0.25)
        # 添加每个特征的标签
        self.axes.set_thetagrids(angles*180/np.pi, feature)
        # 设置雷达图的范围
        self.axes.set_ylim(0,5)
        self.axes.grid(True)

        self.axes2 = self.figureCanvas.figure.add_subplot(122)
        self.axes2.set_title("月消费总额")
        self.axes2.set_ylabel("元")
        ls=[1600,1850,1900]
        ls.append(int(self.h[16]))
        self.axes2.set_ylim(0,2500)
        self.axes2.plot([1,2,3,4],ls)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    t=['4', '林丹', '汉', '2015', 161203105317, '数理', '应统', '党员', '4', 3.88, '120', '120', '0', '0', 0, '1', '1906', '1', '珠海', '0']
    demo = Demo2(h=t)
    demo.show()
    sys.exit(app.exec_())