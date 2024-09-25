# UnifiedDataLoader

## 20240925 version:1.2

> **初步走完整个流程，最终返回一个一维数组，接下来考虑细节优化和真实数据实现**

- 可以考虑全局用dataframe处理
- 初始化读数据时返回`DataFrame`可能不满足单一修改原则，还在考虑是使用配置文件解决还是全局硬编码
- 考虑全局使用pandas.to_datetime
- 最终的结果返回，根据节假日的处理情况决定是否需要封装成一个函数

## 20240925 version:1.1

1. 避免使用`iterrows()`挨个创建对象，使得`daily_record_map`创建时间大幅度减小，由30s到不足1s
2. 不再单独实例化出`List:DataPointProperties`，然后再做切割，而是直接生成`Dict:DailyRecord`，在过程中创建对应的`List:DataPointProperties`
3. 初步尝试`DataExtractor`返回`DataFrame`，并用`DataFrame`构造初始对象

- 考虑全局用dataframe处理
- 初始化读数据时返回`DataFrame`可能不满足单一修改原则，还在考虑是使用配置文件解决还是全局硬编码
- 考虑使用pandas.to_datetime

## 20240924 version:1.0

1. `config.json`参照`launch.json`的方式，实现多配置文件。同时添加命令行处理，配置文件的选择通过命令行传入
2. 删除`ConfigUtils.py`，由`choose_configuration`函数处理`config.json`的解析
3. 初步实例化出`List:DataPointProperties` 和 `Dict:DailyRecord`

------

这一版处理程序的抽象架构是把每个粒度的点作为结构体(类)

`DataStructures` : 存放所有项目可能用到的属性类

`DataStructureUtils` : 处理DataStructures的函数

`SQLQueryBuilder` : 从数据库/CSV获取数据

`UnifiedDataLoader`: 主流程
