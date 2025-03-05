import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取 combined_data.csv 文件
data = pd.read_csv('../totaldata/combined_data.csv')

# 提取居室类型
data['bedrooms'] = data['category'].astype(str).str.extract(r'(\d)')[0]

# 只统计一居、二居、三居
filtered_data = data[data['bedrooms'].isin(['1', '2', '3'])]

# 转换价格列为数值型
filtered_data['price'] = pd.to_numeric(filtered_data['price'], errors='coerce')

# 计算统计信息
stats = filtered_data.groupby(['city', 'bedrooms'])['price'].agg(['mean', 'max', 'min', 'median']).reset_index()

# 重命名列
stats.columns = ['city', 'bedrooms', 'average_price', 'max_price', 'min_price', 'median_price']

print(stats)

# 显示中文
plt.rcParams['font.sans-serif'] = ['Songti SC']

# 可视化展示
def plot_stats(statistics, stat_name):
    plt.figure(figsize=(8, 6))
    sns.barplot(data=statistics, x='city', y=stat_name, hue='bedrooms', errorbar=None)
    plt.title(f'{stat_name.capitalize()} by City and Bedrooms')
    plt.ylabel(stat_name.capitalize())
    plt.xlabel('City')
    plt.xticks(rotation=45)
    plt.legend(title='Bedrooms')
    plt.tight_layout()
    plt.show()

# 绘制均价、最高价、最低价、中位数的柱状图
plot_stats(stats, 'average_price')
plot_stats(stats, 'max_price')
plot_stats(stats, 'min_price')
plot_stats(stats, 'median_price')