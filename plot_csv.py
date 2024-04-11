import numpy as np
import matplotlib.pyplot as plt
import sys
from numpy import genfromtxt # csv reading

# 時系列データAとB（仮のデータ）
#data_A = np.array([0, 0, 1, 0, 0, 1, 0, 0, 1, 0])
#data_B = np.array([0, 0, 0, 1, 0, 0, 1, 0, 0, 1])
# read csv with numpy
a=genfromtxt(sys.argv[1], delimiter=',') # CSVデータの読み込み 1レコード＝Tc x 10 , 10レコード
at=np.transpose(a) # 信号の分離

# 時間幅dtを設定
dt = 1  # 仮に1とします（実際のデータに合わせて変更してください）

# 時間軸を設定
x=range(0,10)

# １０個の信号のプロット：山が０から１０まで順番に並ぶ
for i in range(0,10):
  plt.plot(x, at[i])
plt.show()
