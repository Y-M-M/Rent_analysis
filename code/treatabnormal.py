import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv('../totaldata/combined_data.csv')

# 打印基本信息摘要
data.info()
print('----------')

# 打印数据的统计摘要
print(data.describe())

# 获取城市列表
cities = data['city'].unique()

# 绘制原始数据的箱型图
plt.figure(figsize=(12, 6))
for i, city in enumerate(cities):
    plt.subplot(1, len(cities), i + 1)
    city_data = data[data['city'] == city]
    plt.boxplot(city_data['price'])
    plt.title(city)
    plt.xlabel('Price')

# 剔除超出均值3倍标准差的异常值
for city in cities:
    city_data = data[data['city'] == city]
    mean = city_data['price'].mean()
    std_dev = city_data['price'].std()
    low_limit = mean - 3 * std_dev
    high_limit = mean + 3 * std_dev

    # 直接在原 DataFrame 上进行操作
    data = data[~((data['city'] == city) & 
                   ((data['price'] > high_limit) | (data['price'] < low_limit)))]

# 将修改后的数据保存到原 CSV 文件
data.to_csv('../totaldata/combined_data.csv', index=False)

# 绘制过滤后的数据的箱型图
plt.figure(figsize=(12, 6))
for i, city in enumerate(cities):
    plt.subplot(1, len(cities), i + 1)
    city_data = data[data['city'] == city]
    plt.boxplot(city_data['price'])
    plt.title(city)
    plt.xlabel('Price')

plt.tight_layout()
plt.suptitle('Price Distribution by City (Filtered)', y=1.05)
plt.show()