import numpy as np
import matplotlib.pyplot as plt
import sys
from numpy import genfromtxt

# 時系列データAとB（仮のデータ）
#data_A = np.array([0, 0, 1, 0, 0, 1, 0, 0, 1, 0])
#data_B = np.array([0, 0, 0, 1, 0, 0, 1, 0, 0, 1])
# read csv with numpy
a=genfromtxt(sys.argv[1], delimiter=',')
#print(a[0])
at=np.transpose(a)

# 時間幅dtを設定
dt = 1  # 仮に1とします（実際のデータに合わせて変更してください）

# 時間軸を設定
x=range(0,10)
for i in range(0,10):
  plt.plot(x, at[i])
plt.show()
