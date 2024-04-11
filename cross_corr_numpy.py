import numpy as np
import matplotlib.pyplot as plt

# 時系列データAとB（仮のデータ）
#data_A = np.array([0, 0, 1, 0, 0, 1, 0, 0, 1, 0])
#data_B = np.array([0, 0, 0, 1, 0, 0, 1, 0, 0, 1])

# 時間幅dtを設定
dt = 1  # 仮に1とします（実際のデータに合わせて変更してください）

# 相互相関を計算
cross_correlation = np.correlate(data_A, data_B, mode='full')

# 時間軸を設定
time_axis = np.arange(-len(data_A) + 1, len(data_A), 1) * dt

# 相互相関の値をプロット
fig, ax = plt.subplots()
ax.plot(time_axis, cross_correlation)
ax.set(xlabel='time (sec)', ylabel='cross_correlation', title='Cross_correlation of A and B')
ax.grid(True)

# 最大値の位置（時間ずれ (sec) ）を求める
max_index = np.argmax(cross_correlation)
time_shift = time_axis[max_index]

# プリント出力
print("最大値の位置（時間ずれ）:", time_shift)

# プロット表示
plt.show()

