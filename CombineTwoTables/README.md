##两个表联接,join操作.
将帖子内容和发帖用户信息联接在一起输出.

两个文件是两张表.用streaming时,直接把这两个文件所在文件夹传进去.

Map比较容易,对两个文件的每一行直接输出,注意调整一下位置,两个输出的key要一样,相当于要在这个key上联接.这个例子里,key是用户id.

Shuffle和Sort对key排序.同一个key对应的帖子和用户信息在一起.

Reducer首先要判断Map输出的是用户信息还是帖子信息.如果是用户信息就创建一个用户信息的list,如果是帖子信息就将帖子放入一个list,等下一个用户出现时,把上面的全部输出了.

