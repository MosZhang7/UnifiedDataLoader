# UnifiedDataLoader

这一版处理程序的抽象架构是把每个粒度的点作为结构体(类)

`DataStructures` : 存放所有项目可能用到的属性类

`DataStructureUtils` : 处理DataStructures的函数

`SQLQueryBuilder` : 从数据库/CSV获取数据

`UnifiedDataLoader`: 主流程