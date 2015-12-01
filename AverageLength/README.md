##平均长度
帖子分为两类,问题和答案.这个练习观察了问题的长度和它的平均答案长度之间的关系.

如果一个帖子是问题,那它的parent_id是\N,如果是答案,那它的parent_id是对应问题的post_id.
##测试
```
cat ../student_test_posts.csv |python mapper.py |sort|python reducer.py 
```

