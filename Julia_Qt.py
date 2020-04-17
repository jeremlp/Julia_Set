# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 02:21:51 2020

@author: Jeremy La Porte
Release V1.0
Premiere version.
Plot avec pyQt des ensembles de Julia
"""
import numpy as np
import PyQt5.QtGui as QtGui
import PyQt5.QtCore  as QtCore
import matplotlib.pyplot as plt

import pyqtgraph.opengl as gl
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QSlider
from PyQt5.QtCore import Qt
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(300,50,1500,900)#xw, yw, x size, y size
        
        self.home()
        
    def home(self):
        # self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.dynamicPlt = pg.PlotWidget(self)
        self.dynamicPlt.setBackground('#D3D3D3')
        self.dynamicPlt.move(20,20)
        self.dynamicPlt.resize(1450,800)
        
        self.horizontalSlider_1 = QSlider(Qt.Horizontal,self)
        # self.horizontalSlider_1 = QtWidgets.QSlider()
        self.horizontalSlider_1.setGeometry(QtCore.QRect(725, 850, 160, 22))
        self.horizontalSlider_1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_1.setMaximum(0)
        self.horizontalSlider_1.setMinimum(-20)
        self.horizontalSlider_1.setObjectName("horizontalSlider_1")
        self.horizontalSlider_1.valueChanged.connect(self.plotgraph)
        self.horizontalSlider_1.valueChanged.connect(self.rename)
        self.label = QtGui.QLabel(str(self.horizontalSlider_1.value()/10),self)
        self.label.move(725,825)
        
        self.horizontalSlider_2 = QSlider(Qt.Horizontal,self)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(550, 850, 160, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setMaximum(50)
        self.horizontalSlider_2.setMinimum(-50)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.valueChanged.connect(self.plotgraph)
        self.horizontalSlider_2.valueChanged.connect(self.rename)
        self.label_2 = QtGui.QLabel(str(self.horizontalSlider_2.value()/10),self)
        self.label_2.move(525,825)
        
        self.horizontalSlider_3 = QSlider(Qt.Horizontal,self)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(200, 850, 160, 22))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setMaximum(1000)
        self.horizontalSlider_3.setMinimum(0)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalSlider_3.valueChanged.connect(self.plotgraph)
        self.horizontalSlider_3.valueChanged.connect(self.rename)
        self.label_3 = QtGui.QLabel(str(self.horizontalSlider_3.value()),self)
        self.label_3.move(175,825)
        
        self.horizontalSlider_4 = QSlider(Qt.Horizontal,self)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(900, 850, 160, 22))
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setMaximum(50)
        self.horizontalSlider_4.setMinimum(5)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.horizontalSlider_4.valueChanged.connect(self.plotgraph)
        self.horizontalSlider_4.valueChanged.connect(self.rename)
        self.label_4 = QtGui.QLabel(str(self.horizontalSlider_4.value()/10),self)
        self.label_4.move(900,825)
        self.plotgraph()
        # super(MainWindow, self).__init__(*args, **kwargs)

        # self.graphWidget = pg.PlotWidget()
        # self.setCentralWidget(self.graphWidget)

        # self.graphWidget.setBackground('k')
    def rename(self):
        self.label.setText(str(self.horizontalSlider_1.value()/10))
        self.label_2.setText(str(self.horizontalSlider_2.value()/10))
        self.label_3.setText(str(self.horizontalSlider_3.value()))
        self.label_4.setText(str(self.horizontalSlider_4.value()/10))
    def plotgraph(self):
        import time
        start_time = time.time()

        self.dynamicPlt.clear()
        force = True
        
        if force == False:
            p = self.horizontalSlider_1.value()/10
            k = 1/self.horizontalSlider_3.value()
            exp = self.horizontalSlider_2.value()/10
            area = self.horizontalSlider_4.value()/10
        else:
            p = -0.7269 + 0.1889j
            k = 1000
            domaine = 200
            exp = 2
            area = 0.1
            t = np.pi
            C = 1/2*np.exp(1j*t)-1/4*np.exp(2j*t)
       
        A = 0.9
        B = 1.6
        a = np.linspace(-A,A,k)
        b = np.linspace(-B,B,k)
        listX = []
        listY = []
        listX_2 = []
        listY_2 = []
        ColorList = []
        cmap = plt.get_cmap('plasma')
        Color = []
        for i in range(domaine):
            Tup = []
            for j in cmap(i*17):
                Tup.append(j*255)
            Color.append(tuple(Tup))
        for x1 in b:
            if int(x1*1000%(100)) == 0:
                print(int(100*(x1+1.6)/3.2),'%')
            for y1 in a:
                z = x1+ 1j*y1
                count = 0
                
                for i in range(domaine):
                    if np.absolute(z) <= 2:
                        z = z**exp+C
                        count += 1
                    else:
                        break

                if i == domaine-1:
                    listX_2.append(x1)
                    listY_2.append(y1)
                else:
                    ColorList.append(Color[count])
                    listX.append(x1)
                    listY.append(y1)

                
        # brush_list = [pg.mkColor(c) for c in "rgbcmykwrg"]
        print('nb points :',len(listY))
        
        brush_list = [pg.mkColor(c) for c in ColorList]
        
        #s1 = self.dynamicPlt.setData(x=x, y=listY, size=10, pen=pg.mkPen(None), brush='g', symbol='o', symbolBrush=pg.mkColor((0.0, 0.5666666666666667, 1.0, 1.0)), symbolPen='r')
        self.scatter_1 = pg.ScatterPlotItem(listX, listY,pen = None,symbol='o', symbolSize=0.1 ,brush=brush_list,pxMode = True,antialias = True)
        self.scatter_2 = pg.ScatterPlotItem(listX_2, listY_2,pen = None,symbol='o', symbolSize=0.1 , brush= 'r',pxMode = True,antialias = True) #forme
        self.dynamicPlt.addItem(self.scatter_1)
        self.dynamicPlt.addItem(self.scatter_2)
        print("--- %s seconds ---" % (time.time() - start_time))



def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


