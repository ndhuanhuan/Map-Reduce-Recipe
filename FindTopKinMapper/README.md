##还是一个找前K大的程序
找到长度最大的前k个帖子,这个是在mapper里维护了一个最小堆.

可以在reducer里将mapper的结果统一再找最终的topK.
