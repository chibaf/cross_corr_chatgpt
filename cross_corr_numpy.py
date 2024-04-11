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

# 相互相関を計算
cross_correlation = np.correlate(a[0], a[4], mode='full')  # ０番と４番の相互相関

# 時間軸を設定
#time_axis = np.arange(-len(data_A) + 1, len(data_A), 1) * dt


# 最大値の位置（時間ずれ (sec) ）を求める
max_index = np.argmax(cross_correlation)
#time_shift = time_axis[max_index]

# プリント出力
print("最大値の位置（時間ずれ）:", max_index)

# プロット表示
x=range(0,len(cross_correlation))
plt.plot(x, cross_correlation)
plt.show()

