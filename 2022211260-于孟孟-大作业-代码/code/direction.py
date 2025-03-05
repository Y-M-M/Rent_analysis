import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取数据
data = pd.read_csv('../totaldata/combined_data.csv')

# 计算单位面积租金
data['unit_price'] = data['price'] / data['area']

# 计算不同城市不同方向单位面积租金的平均值
directions = ['East', 'Southeast', 'South', 'Southwest', 'West', 'Northwest', 'North', 'Northeast']
average_rent = {}

for direction in directions:
    avg_rent = data[data[direction] == 1].groupby('city')['unit_price'].mean()
    average_rent[direction] = avg_rent

# 转换为 DataFrame
average_rent_df = pd.DataFrame(average_rent)

# 找出每个城市单位面积租金最高和最低的方向
highest_direction = average_rent_df.idxmax(axis=1)  # 每个城市最高的方向
highest_value = average_rent_df.max(axis=1)  # 每个城市最高的租金

lowest_direction = average_rent_df.idxmin(axis=1)  # 每个城市最低的方向
lowest_value = average_rent_df.min(axis=1)  # 每个城市最低的租金

# 创建新的 DataFrame 存储结果
result_df = pd.DataFrame({
    'City': average_rent_df.index,
    'Highest Direction': highest_direction,
    'Highest Value': highest_value,
    'Lowest Direction': lowest_direction,
    'Lowest Value': lowest_value
})

# 打印结果
print(result_df)

# 可视化
average_rent_df.plot(kind='bar', figsize=(14, 8)) 
plt.title('Average Unit Rent by Direction in Different Cities')
plt.ylabel('Average Unit Rent')
plt.xlabel('City')
plt.xticks(rotation=45)
plt.legend(title='Direction')
plt.tight_layout()
plt.show()