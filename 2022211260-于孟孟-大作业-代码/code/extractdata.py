import pandas as pd
import re

# 读取 CSV 文件
bjfile = pd.read_csv('../initaldata/bjdata.csv')
shfile = pd.read_csv('../initaldata/shdata.csv')
gzfile = pd.read_csv('../initaldata/gzdata.csv')
szfile = pd.read_csv('../initaldata/szdata.csv')
qdfile = pd.read_csv('../initaldata/qddata.csv')


def update_direction_columns(df):

    # 提取 '室' 前面的数字并更新 category
    df['category'] = df['name'].str.extract(r'(\d+)室')[0]

    # 初始化方向列
    for direction in ['East', 'West', 'South', 'North', 'Southeast', 'Southwest', 'Northwest', 'Northeast']:
        df[direction] = 0

    # 检测方向并更新相应列
    for index, row in df.iterrows():
        parts = re.split(r'[ /]', row['name'])  # 分割 name
        for part in parts:
            if '东' in part:
                df.at[index, 'East'] = 1
            if '西' in part:
                df.at[index, 'West'] = 1
            if '南' in part:
                df.at[index, 'South'] = 1
            if '北' in part:
                df.at[index, 'North'] = 1
            if '东南' in part:
                df.at[index, 'Southeast'] = 1
            if '西南' in part:
                df.at[index, 'Southwest'] = 1
            if '西北' in part:
                df.at[index, 'Northwest'] = 1
            if '东北' in part:
                df.at[index, 'Northeast'] = 1

    # 转换方向列为整数类型
    df[['East', 'West', 'South', 'North', 'Southeast', 'Southwest', 'Northwest', 'Northeast']] = df[[
        'East', 'West', 'South', 'North', 'Southeast', 'Southwest', 'Northwest', 'Northeast'
    ]].astype(int)

    return df

# 保存更新后的 DataFrame
newbjfile = update_direction_columns(bjfile)
newbjfile.to_csv('../totaldata/newbjdata.csv', index=False)
newshfile = update_direction_columns(shfile)
newshfile.to_csv('../totaldata/newshdata.csv', index=False)
newgzfile = update_direction_columns(gzfile)
newgzfile.to_csv('../totaldata/newgzdata.csv', index=False)
newszfile = update_direction_columns(szfile)
newszfile.to_csv('../totaldata/newszdata.csv', index=False)
newqdfile = update_direction_columns(qdfile)
newqdfile.to_csv('../totaldata/newqdzdata.csv', index=False)