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
 1. XML: eXtensible Markup Language. ```html
 <p class="data"> some text </p>
 ```
 2. JSON: JavaScript Object Notation.