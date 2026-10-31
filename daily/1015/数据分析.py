import matplotlib.pyplot as plt

# 1. 准备数据
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# 2. 创建图形和坐标轴
fig, ax = plt.subplots()

# 3. 绘制折线图
ax.plot(x, y)

# 4. 添加标题和坐标轴标签
ax.set_title("hhh")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# 5. 显示图形
plt.show()