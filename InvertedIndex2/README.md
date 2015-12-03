##倒排索引 tf-idf
输入格式为一个文件一行
```
1 holy bible authorized king james version textfile 890904
2 in the beginning god created the heaven and the earth
3 and the earth was without form and void and darkness was upon the face of the deep and the spirit of god moved upon the face of the waters
4 and god said let there be light and there was light
5 and god saw the light that it was good and god divided the light from the darkness
```
```
cat ../sample_data_bible_with_id |python mapper.py |sort|python reducer.py 
```
输出格式为:词语, 词语文档频率(df), [(文档id1,词频(tf)),(文档id2,词频(tf))......(文档idn,词频(tf))]
```
890904	1	[('1', '1')]
and	4	[('2', '1'), ('3', '4'), ('4', '2'), ('5', '2')]
authorized	1	[('1', '1')]
be	1	[('4', '1')]
beginning	1	[('2', '1')]
bible	1	[('1', '1')]
created	1	[('2', '1')]
darkness	2	[('3', '1'), ('5', '1')]
deep	1	[('3', '1')]
divided	1	[('5', '1')]
earth	2	[('2', '1'), ('3', '1')]
face	1	[('3', '2')]
form	1	[('3', '1')]
from	1	[('5', '1')]
god	4	[('2', '1'), ('3', '1'), ('4', '1'), ('5', '2')]
good	1	[('5', '1')]
heaven	1	[('2', '1')]
holy	1	[('1', '1')]
in	1	[('2', '1')]
it	1	[('5', '1')]
james	1	[('1', '1')]
king	1	[('1', '1')]
let	1	[('4', '1')]
light	2	[('4', '2'), ('5', '2')]
moved	1	[('3', '1')]
of	1	[('3', '3')]
said	1	[('4', '1')]
saw	1	[('5', '1')]
spirit	1	[('3', '1')]
textfile	1	[('1', '1')]
that	1	[('5', '1')]
the	3	[('2', '3'), ('3', '6'), ('5', '3')]
there	1	[('4', '2')]
upon	1	[('3', '2')]
version	1	[('1', '1')]
void	1	[('3', '1')]
was	3	[('3', '2'), ('4', '1'), ('5', '1')]
waters	1	[('3', '1')]
without	1	[('3', '1')]
```
