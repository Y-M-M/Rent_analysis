import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取 combined_data.csv 文件
data = pd.read_csv('../totaldata/combined_data.csv')

# 计算均价
average_price = data.groupby(['city', 'section'])['price'].mean().reset_index()

print(average_price)

# 显示中文
plt.rcParams['font.sans-serif'] = ['Songti SC']

# 可视化
plt.figure(figsize=(12, 6))
sns.scatterplot(data=average_price, x='section', y='price', hue='city', style='city', s=100)

# 添加标题和标签
plt.title('Average Price by Section for Each City')
plt.xlabel('Section')
plt.ylabel('Average Price')
plt.xticks([])  # 隐藏 x 轴的刻度标签
plt.legend(title='City')
plt.tight_layout()
plt.show()

