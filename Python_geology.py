import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# خواندن فایل اکسل
df = pd.read_excel('khour-part-1-2-3-final.xls')

# تعریف متغیرهای مختلف
x = df['X']
y = df['Y']
z = df['Z']
m1 = df['1m']
m147 = df['1.47m']
m215 = df['2.15m']
m316 = df['3.16m']
m464 = df['4.64m']
m681 = df['6.81m']
m10 = df['10m']
m1470 = df['14.7m']
m2150 = df['21.5m']
m3160 = df['31.6m']
m4640 = df['46.4m']
m6810 = df['68.1m']
m100 = df['100m']
m14700 = df['147m']
m21500 = df['215m']

# رسم نمودار سه بعدی
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)

# رسم plot ها
ax.plot_trisurf(x, y, m1, cmap='viridis', edgecolor='none')
ax.plot_trisurf(x, y, m147, cmap='plasma', edgecolor='none')
ax.plot_trisurf(x, y, m215, cmap='inferno', edgecolor='none')
ax.plot_trisurf(x, y, m316, cmap='magma', edgecolor='none')
ax.plot_trisurf(x, y, m464, cmap='cividis', edgecolor='none')
ax.plot_trisurf(x, y, m681, cmap='rainbow', edgecolor='none')
ax.plot_trisurf(x, y, m10, cmap='cool', edgecolor='none')
ax.plot_trisurf(x, y, m1470, cmap='hot', edgecolor='none')
ax.plot_trisurf(x, y, m2150, cmap='winter', edgecolor='none')
ax.plot_trisurf(x, y, m3160, cmap='autumn', edgecolor='none')
ax.plot_trisurf(x, y, m4640, cmap='spring', edgecolor='none')
ax.plot_trisurf(x, y, m6810, cmap='summer', edgecolor='none')
ax.plot_trisurf(x, y, m100, cmap='gray', edgecolor='none')
ax.plot_trisurf(x, y, m14700, cmap='bone', edgecolor='none')
ax.plot_trisurf(x, y, m21500, cmap='YlGnBu', edgecolor='none')

# نمایش نمودار
plt.show()

# ذخیره نمودار
fig.savefig('plot.png')
