import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取合并后的数据
combined_data = pd.read_csv('../totaldata/combined_data.csv')

# 计算租金的统计信息
rent_stats = combined_data.groupby('city')['price'].agg(
    mean_price='mean',
    max_price='max',
    min_price='min',
    median_price='median'
).reset_index()

# 计算单位面积租金（元/平米）的统计信息
combined_data['rent_per_sqm'] = combined_data['price'] / combined_data['area']
area_rent_stats = combined_data.groupby('city')['rent_per_sqm'].agg(
    mean_rent='mean',
    max_rent='max',
    min_rent='min',
    median_rent='median'
).reset_index()

# 显示统计结果
print("房租统计信息：")
print(rent_stats)
print("\n单位面积租金统计信息：")
print(area_rent_stats)

# 显示中文
plt.rcParams['font.sans-serif'] = ['Songti SC']

# 可视化租金统计信息
plt.figure(figsize=(8, 6))

# 租金统计图
plt.subplot(2, 1, 1)
sns.barplot(data=rent_stats, x='city', y='mean_price', color='slateblue')
plt.title('各城市租金均价')
plt.ylabel('租金均价（元）')

# 单位面积租金统计图
plt.subplot(2, 1, 2)
sns.barplot(data=area_rent_stats, x='city', y='mean_rent', color='lightgreen')
plt.title('各城市单位面积租金均价')
plt.ylabel('单位面积租金均价（元/平米）')

plt.tight_layout()
plt.show()