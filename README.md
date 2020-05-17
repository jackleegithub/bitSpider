# 课程信息
* 课程地址：https://www.bilibili.com/video/BV1kx411S7Fh
* 授课老师：嵩天
* 课程简介：“The website is the API.”网络爬虫逐渐成为自动获取网络信息的主要形式。还等什么？快写个爬虫探索世界吧！

# 网络爬虫引发的问题
## 爬虫规格
| seq | content |  TeZheng                   |   model     |
| --- |:------: | :------------------------: | -----------:|
|   1 | 爬取网页 | 规模小, 数据量小，速度不敏感 | requests库  |
|   2 | 爬取网站 | 中规模，数据量大，速度敏感   | scrapy库    |
|   3 | 全因特网 | 大规模，数据量大，速度是关键 | 定制开发     |

## 爬虫的问题
* 对网站性能的影响，带来资源开销。
* 法律风险，数据版权归属
* 个人隐私泄露

## 限制爬虫
* 来源审查：如果有网站的管理权限，做来源审查。检查来访HTTP协议头的 User-Agent 字段。技术要求高。
* 发布公告：Robots协议，需要爬虫配合使用。

## Robots 协议
* Robots Exclusion Standard 网络爬虫排除标准。
* 作用：网站告知爬虫哪些页面可以爬取，哪些页面不可以。
* 位置：在网站根目录下的 robots.txt 文件。
* 语法：User-agent, Disallow, Allow
* 使用：自动或者人工识别 robots.txt 的内容，然后再进行爬取。

# Beautiful Soup
* 引用: from bs4 import BeautifulSoup
* HTML文档 --->--- BeautifulSoup 类 ---->--- 树形结构（类似DOM）
* 解析器：html.parser,lxml,lxml-xml, html5lib
* 基本元素：Tag(Name(.name),Attributes(.attrs))、NavigableString(.string)、Comment(.string)
* 友好显示：.prettify()
## BS 遍历
* 下行遍历：
 1. .contents: 儿子节点列表
 2. .children: 儿子节点迭代器
 3. .descendants: 子孙节点的迭代类型
 * 上行遍历
 1. .parent: 父节点
 2. .parents: 先辈节点的迭代类型
 * 平行遍历
 1. .next_sibling: 返回按照HTML文本顺序的下一个平行节点
 2. .previous_sibling:返回按照HTML文本顺序的上一个平行节点
 3. .next_siblings:返回按照HTML文本顺序的后续所有平行节点
 4. .previous_siblings:返回按照HTML文本顺序的前续所有平行节点

# 信息标记
1. XML: eXtensible Markup Language.标签(tag) `<p class="data"> some text </p>`
2. JSON: JavaScript Object Notation.有类型的键值对(key/value)`{"name":"jack","age":100,"address":["bj","sh"]}`
3. YAML: YAMLAin't Markup Language.  无类型的键值对Key/Value.
```yaml
name:
   newname:abc
   oldname:xyz
```
4. XML example.
``` XML
<person>
   <firstname>Li</firstname>
   <lastname>zhixin</lastname>
   <address>
      <street>丰台区益泽路</street>
      <city>北京</city>
      <zipcode>100071</zipcode>
   </address>
   <prof>Computer System</prof>
   <prof>Security</prof>
</person>
```
5. JSON example.
```JSON
{
   "person":{
      "firstname":"Li",
      "lastname":"zhixin",
      "address":{
         "street":"丰台区益泽路",
         "city":"北京市",
         "zipcode":"100071"
      },
      "prof":["Computer System","Security"]
   }
}
```
6. YAML example.
```YAML
person:
   firstname: Li
   lastname: zhixin
   address:
      street: 丰台区益泽路
      city: 北京
      zipcode: 100071
   prof:
      - Computer System
      - Security
```
## XML JSON YAML 对比
1. XML 最早的通用信息标记语言，可扩展性好，繁琐，无用数据多。Internet 上的主要信息交互和传递。
2. JSON 信息有数据类型，适合程序处理。移动应用云端和节点的信息通信，无注释。
3. YAML 信息无类型，文本信息比例高，可读性好。各类系统的配置文件，有注释易懂。

# 字符串格式化
* "{} some {} string {} ....".format(data1, data2, data3, ......)
* {:x^10,.3d}
  * **:**: 引导字符
  * **x**: 填充字符
  * **^**: 对齐方式，<左对齐, ^居中, >右对齐。
  * **10**: 域的宽度
  * **,**: 数字的千分位标志，适合整数和浮点数
  * **.3**: 浮点数的精度或者字符串的最大长度。
  * **d**: 数值类型。整数-b c d o x X,浮点-e E f %。
* 中英文混排，填充字符可以使用中文的空格，chr(12288)或者"\u3000"

# 正则表达式
* 断言内不能使用数量修饰词