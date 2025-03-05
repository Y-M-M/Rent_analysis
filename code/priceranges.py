import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv('../totaldata/combined_data.csv')

# 定义租金区间
bins = [0, 2500, 5000, 7500, 10000, float('inf')]
labels = ['0-2500', '2500-5000', '5000-7500', '7500-10000', '10000+']

# 将 price 列分为不同的区间
data['price_range'] = pd.cut(data['price'], bins=bins, labels=labels, right=False)

# 统计每个城市在不同租金区间的数量
count_df = data.groupby(['city', 'price_range']).size().unstack(fill_value=0)

# 绘制饼图
for city in count_df.index:
    plt.figure(figsize=(10, 6))
    
    # 过滤掉数量为 0 的扇形
    sizes = count_df.loc[city]
    sizes = sizes[sizes > 0]
    
    # 如果没有数据则跳过
    if sizes.empty:
        print(f"No data to display for {city}")
        continue
    
    # 绘制饼图
    ax = sizes.plot.pie(
        autopct=None,          # 不显示百分比
        startangle=90, 
        cmap='Set2', 
        labeldistance=1.05,   # 调整标签距离
        fontsize=10,          # 设置字体大小
        shadow=False           # 不添加阴影
    )
    
    # 添加图例
    plt.legend(sizes.index, title="Price Ranges", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10)
    
    plt.title(f'Price Distribution in {city}')
    plt.ylabel('')  # 不显示y轴标签
    plt.axis('equal')  # 使饼图为圆形
    
    # 调整图形布局，增加右侧的空白区域
    plt.subplots_adjust(right=0.75)  # 调整右侧边距

    plt.show()