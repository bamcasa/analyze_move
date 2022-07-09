from matplotlib import animation
import matplotlib.pyplot as plt
# 기본 라이브러리
import numpy as np

# 물체
mass = 0.211                     # 질량 [kg]
position = np.array([0, 0.67]) # x, y 위치 [m]
v = np.array([0, 0])         # x, y 방향 초기 속도 [m/s]
t = 0                        # 초기 시간 [s]
dt = 0.01                    # 시간 단위 [s]
g = np.array([0, -9.8])      # 중력 가속도 [m/s]

# 시뮬레이션
ts = []
positions = []
while position[1] >= 0:
    ts.append(t)
    positions.append(position)

    position = position + v * t + 0.5 * g * t ** 2
    t += dt

fig, ax = plt.subplots(figsize=(4, 4), constrained_layout=True)
scatter, = ax.plot([], [], marker="o", mfc="b", mec="w")
time_text = ax.text(0.5, 0.9, f"", transform=ax.transAxes, ha="center")

ax.set_ylim(0, 1)

def updatefig(i):
    scatter.set_data(positions[i][0], positions[i][1])
    time_text.set_text(f"t = {ts[i]:.03f} sec.")
    return fig,


ani = animation.FuncAnimation(fig, updatefig, interval=100, blit=True, repeat=False, frames=len(ts))
ani.save("1_gravity_02.gif")