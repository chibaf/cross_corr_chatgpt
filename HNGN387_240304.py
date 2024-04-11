""" HNGN001 Created on Tue Jun 11 08:34:11 2019
(two days before 190613) (1month before 190711)"""

s1="""HNGN1は、澄江さんが亡くなる2日前に書いたもの。輻射伝熱について勉強しようとしていた。
仏像を1000体彫るように、Pythonコードを1000作る\n """


"""
このプログラムでは、NumPyのcorrelate関数を使用してAとBの相互相関を計算し、その結果から時間ずれを求めています。

ここで、

式 np.arange(-len(data_A) + 1, len(data_A), 1) * dt は、time_axis を設定するためのものです。time_axis は相互相関の時間軸を表しており、各データポイントが何秒後かを示します。

np.arange 関数は、指定された範囲で等間隔の値の配列を生成します。この場合、開始点は -len(data_A) + 1 です。これは、data_A の長さにマイナス1を掛けているのは、data_A の左端（先頭）のデータポイントが相互相関の中心になるようにするためです。

相互相関の計算では、2つの時系列データが重なっている必要があります。そのため、相互相関の中心を正確に計算するには、2つのデータの長さを考慮する必要があります。しかし、相互相関の計算の際には片方のデータをフリップ（反転）させるため、正確には len(data_A) - 1 のようにする必要があります。しかし、相互相関の結果は対称的であるため、実際には左側のデータを中心にしても問題ありません。

最終的に、time_axis の範囲は [-len(data_A) + 1, len(data_A) - 1) となります。これは、相互相関の中心を表し、各データポイントが何秒後かを示します。
"""


import numpy as np
import matplotlib.pyplot as plt

# 時系列データAとB（仮のデータ）
data_A = np.array([0, 0, 1, 0, 0, 1, 0, 0, 1, 0])
data_B = np.array([0, 0, 0, 1, 0, 0, 1, 0, 0, 1])

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

