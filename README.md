# 租房数据分析
## 1 实验目的
1. 使⽤⽹络爬⾍爬取⽹⻚上⾃⼰需要的数据；
2. 爬取北京、上海、⼴州、深圳、⻘岛的租房数据，进⾏预处理，从总价、单位⾯积均价，不同户型，不同朝向，不同板块，不同价位等⻆度对不同城市租房的价格进⾏⽐较，进⾏数据分析和可视化展示，并结合各城市 GDP 与平均⼯资分析不同城市的⽣活压⼒；

## 2 实验过程
### 2.1 数据⽂件结构
> /totaldata/combineddata.csv                    
> ['name', 'area', 'category', 'section', 'price', 'East', 'West', 'South', 'North', 'Southeast',
'Southwest', 'Northwest', 'Northeast']
- 其中 name 存储链接⽹⻚上每个房屋对应的名称，包含各种说明信息；area 存储房屋⾯积，单位为平⽅⽶；category 存储户型(⼏居室)；section 存储板块名称；price 存储房租；East、West、South、North、Southeast、Southwest、Northwest、Northeast 存储朝向，置为 1 说明此条记录中有该朝向的房屋；

### 2.2 爬取数据
1. 代码
- code ⽂件夹下，bjdataget.py, shdataget.py, gzdataget.py, szdataget.py, qddataget.py
- 因为⼀次性爬取所有城市的数据花费时间过⻓，故为每个城市分别设计了⼀个程序；
- 以下将以北京为例说明程序结构
2. 流程图          
![](/image/爬虫流程图.png)
3. 结果
- 提取北京、上海、⼴州、深圳、⻘岛各 12000 条数据；详情⻅/initaldata ⽂件夹，部分截图如下：
![](/image/数据样例.png)


### 2.3 数据预处理

#### 2.3.1 添加房屋朝向
1. 代码
- /code/extractdata.py
- 作⽤：从 name 中提取信息，找到房屋的朝向，添加作为新的元素； 
- 'East', 'West', 'South', 'North', 'Southeast', 'Southwest', 'Northwest', 'Northeast'列为 1 说明有该朝向，为 0 说明没有该朝向；
2. 流程图        
![](/image/数据预处理流程图.png)

3. 结果
- 结果⽂件保存在/totaldata ⽂件夹下，部分截图如下          
![](/image/数据样例1.png)


#### 2.3.2
1. 代码
- /code/pretreat.py ⽂件
- 作用：处理空值，并将五个城市的文件合并为一个，添加city属性

#### 2.3.3
1. 代码
- /code/treatabnormal.py ⽂件
- 作用：处理偏离三倍标准差的异常值
2. 删除前箱形图如下
![](/image/箱形图1.png)
3. 删除后箱形图如下
![](/image/箱形图2.png)


### 2.4 数据分析
1. 代码
- /code/compareoverall.py
- /code/categorydeail.py
- /code/sectioncompare.py
- /code/direction.py
- /code/stress.py
2. 各城市租金均价与单位面积均价
![](/image/各城市租金均价.png)
3. ⽐较 5 个城市⼀居、⼆居、三居的情况，包含均价、最⾼价、最低价、中位数等信息。
![](/image/不同居室1.png)
![](/image/箱形图2.png)
4. 计算和分析每个城市不同板块的均价情况
![](/image/不同板块均价.png)
5. 不同朝向的单位面积租金
![](/image/不同朝向的单位面积房租.png)
6. 各城市GDP与单位面积租金的关系
![](/image/GDP与租金1.png)
![](/image/GDP与租金2.png)
7. 每个城市不同价位的出租屋的数目           
![](/image/出租屋数目1.png)
![](/image/出租屋数目2.png)

## 3 实验结论
1. 五个城市房租的总体情况排⾏⼤概是：北京、上海、深圳、⼴州、⻘岛；
2. 单独分析每个城市的户型与房租，三居室的房租往往⼤于⼆居室，⼆居室的房租往往⼤于⼀居室；横向对⽐不同城市同样户型的房⼦的房租，与总体房租排⾏情况⼤致相同；
3. 均价在 10000 以内的板块数⽬最多，均价超过 10000 的板块数⽬较少，在北京存在⼀些均价远⾼于其他板块的板块；
4. 相对⽽⾔，在⻘岛租房的性价⽐最⾼、房租压⼒最⼩，⻘岛的⽣活压⼒远⼩于其他⼀线城市；
5. 分析不同价位的出租屋所占的⽐例，⼤部分出租屋的价格集中在 10000 以下，⻘岛和⼴州 2500 以下的出租屋数⽬最多；北京、上海和深圳 5000 以下的出租屋占⼤多数；




