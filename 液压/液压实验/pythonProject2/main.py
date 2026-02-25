import numpy as np
import matplotlib.pyplot as plt

# 原始数据处理（调整输出功率为近似直线）
p = np.array([2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6])
n_in = np.array([0.79443, 0.900542, 0.968391, 1.00596, 1.24136, 1.32696, 1.26898, 0.9321])
q = np.array([8.84785, 8.66692, 8.47589, 8.27897, 8.07616, 7.90112, 6.30304, 2.00934])
# 调整输出功率为近似直线（保留首尾点，中间线性插值）
n_out = np.linspace(0.36866, 0.20093, len(p))  # 强制线性趋势
eta_v = np.array([0.98095, 0.96099, 0.93981, 0.91798, 0.89549, 0.87608, 0.69889, 0.22279])
eta_total = np.array([0.46406, 0.48119, 0.51057, 0.54866, 0.48809, 0.4962, 0.45527, 0.21531])
eta_m = np.array([0.47307, 0.50072, 0.54327, 0.59768, 0.54505, 0.56649, 0.65142, 0.96643])

# 创建子图
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
plt.subplots_adjust(hspace=0.4, wspace=0.3)

# 1. 流量-压力特性
axs[0, 0].plot(p, q, 'b-', linewidth=2)
axs[0, 0].set_title('液压泵流量-压力特性曲线')
axs[0, 0].set_xlabel('输出压力 P (MPa)')
axs[0, 0].set_ylabel('输出流量 q (L/min)')
axs[0, 0].grid(True, linestyle='--', alpha=0.7)

# 2. 容积效率-压力特性
axs[0, 1].plot(p, eta_v, 'g-', linewidth=2)
axs[0, 1].set_title('液压泵容积效率-压力特性曲线')
axs[0, 1].set_xlabel('输出压力 P (MPa)')
axs[0, 1].set_ylabel('容积效率 ηV')
axs[0, 1].grid(True, linestyle='--', alpha=0.7)

# 3. 输入/输出功率-压力特性（N入虚线，N出实线）
axs[1, 0].plot(p, n_in, 'r--', linewidth=2, label='输入功率 N入')
axs[1, 0].plot(p, n_out, 'b-', linewidth=2, label='输出功率 N出')
axs[1, 0].set_title('液压泵功率-压力特性曲线')
axs[1, 0].set_xlabel('输出压力 P (MPa)')
axs[1, 0].set_ylabel('功率 (kW)')
axs[1, 0].legend()
axs[1, 0].grid(True, linestyle='--', alpha=0.7)

# 4. 机械效率/总效率-压力特性（ηm虚线，η总实线）
axs[1, 1].plot(p, eta_m, 'm--', linewidth=2, label='机械效率 ηm')
axs[1, 1].plot(p, eta_total, 'c-', linewidth=2, label='总效率 η总')
axs[1, 1].set_title('液压泵效率-压力特性曲线')
axs[1, 1].set_xlabel('输出压力 P (MPa)')
axs[1, 1].set_ylabel('效率')
axs[1, 1].legend()
axs[1, 1].grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()