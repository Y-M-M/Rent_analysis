import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv('../totaldata/combined_data.csv')

# 计算单位面积租金
data['unit_price'] = data['price'] / data['area']

# 按城市计算平均单位面积租金
average_rent_df = data.groupby('city')['unit_price'].mean().reset_index()

# 人均GDP（单位：万元）
gdp_data = {
    'Beijing': 20.03,
    'Shanghai': 19.03,
    'Guangzhou': 16.16,
    'Shenzhen': 19.52,
    'Qingdao': 14.49
}

# 平均工资（单位：元）
avg_salary_data = {
    'Beijing': 13648,
    'Shanghai': 13678,
    'Guangzhou': 12550,
    'Shenzhen': 13730,
    'Qingdao': 9208
}

# 将数据转换为 DataFrame
gdp_df = pd.Series(gdp_data, name='GDP').reset_index().rename(columns={'index': 'City'})
salary_df = pd.Series(avg_salary_data, name='Average Salary').reset_index().rename(columns={'index': 'City'})

# 合并数据
combined_df = average_rent_df.merge(gdp_df, left_on='city', right_on='City').merge(salary_df, left_on='city', right_on='City')

# 计算性价比和租房负担
combined_df['Rent Price'] = combined_df['unit_price']
combined_df['Price to GDP Ratio'] = combined_df['Rent Price'] / combined_df['GDP']
combined_df['Salary to Rent Ratio'] = combined_df['Average Salary'] / combined_df['Rent Price']

# 找出性价比最高和租房负担最重的城市
best_value_city = combined_df.loc[combined_df['Price to GDP Ratio'].idxmin()]
heaviest_burden_city = combined_df.loc[combined_df['Salary to Rent Ratio'].idxmax()]

# 打印结果
print("性价比最高的城市：", best_value_city['city'])
print("租房负担最重的城市：", heaviest_burden_city['city'])

# 可视化
plt.figure(figsize=(8, 5))
plt.bar(combined_df['city'], combined_df['Price to GDP Ratio'], color='skyblue')
plt.title('Rent Price to GDP Ratio by City')
plt.ylabel('Rent Price to GDP Ratio')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(combined_df['city'], combined_df['Salary to Rent Ratio'], color='salmon')
plt.title('Average Salary to Rent Price Ratio by City')
plt.ylabel('Average Salary to Rent Price Ratio')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()