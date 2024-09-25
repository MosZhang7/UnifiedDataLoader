# UnifiedDataLoader

> **TODO**

- 最终的结果返回，根据节假日的处理情况决定是否需要封装成一个函数
- 可以考虑全局用`DataFrame`处理
- 考虑全局使用`pandas.to_datetime`
- 所有函数标准化输入输出的约定，需要先学python，依照python的官方标准
- `CSVExtractor`根据实际情况，可能退化为函数

## 20240925 version:1.3

1. 利用python的动态添加成员变量，使得通过用`DataFrame`构造初始对象也满足单一修改原则，无需在多处关注数据源的字段细节
2. 清除无用的头文件引入和无用的代码注释
3. 为了方便程序最终的输出，data_type这种本应属于`DailyRecord`的也被添加到`DataPointProperties`，后续如果需要考虑内存、性能因素，可以在`DataExtractor.load()`处针对dp和dr分别返回`DataFrame`而无需properties

## 20240925 version:1.2

> **初步走完整个流程，最终返回一个一维数组，接下来考虑细节优化和真实数据实现**

## 20240925 version:1.1

1. 避免使用`iterrows()`挨个创建对象，使得`daily_record_map`创建时间大幅度减小，由30s到不足1s
2. 不再单独实例化出`List:DataPointProperties`，然后再做切割，而是直接生成`Dict:DailyRecord`，在过程中创建对应的`List:DataPointProperties`
3. 初步尝试`DataExtractor`返回`DataFrame`，并用`DataFrame`构造初始对象

## 20240924 version:1.0

1. `config.json`参照`launch.json`的方式，实现多配置文件。同时添加命令行处理，配置文件的选择通过命令行传入
2. 删除`ConfigUtils.py`，由`choose_configuration`函数处理`config.json`的解析
3. 初步实例化出`List:DataPointProperties` 和 `Dict:DailyRecord`

------

这一版处理程序的抽象架构是把每个粒度的点作为结构体(类)

`DataStructures` : 存放所有项目可能用到的属性类

`DataStructureUtils` : 处理DataStructures的函数

`DataExtractor` : 从数据库/CSV获取数据

`UnifiedDataLoader`: 主流程
