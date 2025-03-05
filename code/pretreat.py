import pandas as pd

# 打开csv文件
bjfile = pd.read_csv('../totaldata/newbjdata.csv')
shfile = pd.read_csv('../totaldata/newshdata.csv')
gzfile = pd.read_csv('../totaldata/newgzdata.csv')
szfile = pd.read_csv('../totaldata/newszdata.csv')
qdfile = pd.read_csv('../totaldata/newqdzdata.csv')

# 打印基本信息摘要
print('------')
print('Beijing:')
bjfile.info()
print('------')
print('Shanghai:')
shfile.info()
print('------')
print('Guangzhou:')
gzfile.info()
print('------')
print('Shenzhen:')
szfile.info()
print('------')
print('Qingdao:')
qdfile.info()

print('-----------------------------------------')

# 删除section项为空的记录并填回原表
qdfile.dropna(axis=0, how='any', subset='section', inplace=True)
gzfile.dropna(axis=0, how='any', subset='section', inplace=True)

# 重新打印基本信息摘要
print('------')
print('Beijing:')
bjfile.info()
print('------')
print('Shanghai:')
shfile.info()
print('------')
print('Guangzhou:')
gzfile.info()
print('------')
print('Shenzhen:')
szfile.info()
print('------')
print('Qingdao:')
qdfile.info()

# 为每个 DataFrame 添加城市列
bjfile['city'] = 'Beijing'
shfile['city'] = 'Shanghai'
gzfile['city'] = 'Guangzhou'
szfile['city'] = 'Shenzhen'
qdfile['city'] = 'Qingdao'

# 合并所有 DataFrame
combined_data = pd.concat([bjfile, shfile, gzfile, szfile, qdfile], ignore_index=True)

# 保存到新的 CSV 文件
combined_data.to_csv('../totaldata/combined_data.csv', index=False)