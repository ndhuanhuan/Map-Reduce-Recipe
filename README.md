##一些常用的map reduce代码
题目大多数来自Udacity Hadoop教程.python编写,用Hadoop Streaming提交,或者用终端测试.比较初级,没有generator和iterator(写这些的时候不知道应该用这个).

- FindLargest
找访问次数最多的url.

- FindTopKinRecuder
找访问次数前K多的url,在reducer里

- FindTopKinMapper
找到长度最长的前k个帖子,在mapper里

- FilterOnlyOneSentence
过滤出只包含一句话的帖子.

- InvertedIndex
统计某个单词的频率,和某个单词所出现的所有帖子id.

- InvertedIndex2
统计所有文档中所有单词的频率,文档频率,即tf-idf

- Mean
求均值.

- CombineTwoTables
两表联接.

- MostTime
求每个用户最经常的发帖时间.

- PopularTags
最常用标签

- Relationship
某个帖子里所有的相关用户id
