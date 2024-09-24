# UnifiedDataLoader

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
