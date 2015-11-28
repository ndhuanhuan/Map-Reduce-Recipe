##计算一周七天每天的销售额总值,加入combiner
##测试
这个问题的combiner和reducer一样.
```
hadoop jar ../tools/hadoop-streaming-2.6.0.2.2.6.0-2800.jar -mapper ../udacity/SumWithCombiners/mapper.py -combiner ../udacity/SumWithCombiners/reducer.py -reducer ../udacity/SumWithCombiners/reducer.py -input purchases.txt -output out

```



