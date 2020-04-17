# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 16:12:57 2019

@author: Jeremy La Porte
Release V1.0
Premiere version.
Plot avec plt des ensembles de Julia
"""
import numpy as np
import matplotlib.pyplot as plt
import time
start_time = time.time()



# color = ['w', 'c', 'b', 'm', 'g', 'y', 'r']
# color2 = ['k','k','b', 'tab:blue', 'tab:cyan', 'tab:green', 'tab:olive', 'tab:orange', 'tab:red','r','r']
# color3 = ['k','k','yellow','gold','orange','darkorange','tomato','orangered','red','r','r','r','r']


"precision de la figure"
k = 1/250


area = 1
p = 0.285 + 0.01j

a = np.arange(-2,2,k)
b = np.arange(-2,2,k)
t = np.pi
C = 1/2*np.exp(1j*t)-1/4*np.exp(2j*t)

listX = []
listY = []
listX_2 = []
listY_2 = []
Color = []

for x1 in b:
    if int(x1*1000%(100)) == 0:
        print(int(100*(x1+2)/4),'%')
    for y1 in a:
        z = x1+ 1j*y1
        count = 0
        for i in range(100):
            if np.absolute(z) <= 2: 
                z = z**2+p
                count += count
            else:
                break
                
        if  i == 99:
            listX_2.append(x1)
            listY_2.append(y1)
        else:
            Color.append(count)
            listX.append(x1)
            listY.append(y1)        
        
            
print('nb de points:',len(listX))
plt.scatter(listX, listY, s=area, c= Color, alpha= 1)
plt.scatter(listX_2, listY_2, s=area/2, c='r', alpha= 1)
                
               
# fig = plt.figure()
# ax = plt.axes(projection='3d')




# X, Y = np.meshgrid(x, y)
# Z = f(X, Y)

# ax = plt.axes(projection='3d')
# ax.contour3D(X, Y, Z, 50, cmap=cm.plasma, shade = True)

# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z');

# fig
# ax = plt.axes(projection='3d')
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
#                 cmap='plasma', edgecolor='none')
# ax.set_title('surface');
# ax.view_init(60, 35)
print("--- %s seconds ---" % (time.time() - start_time))