# python-news-monitor
# Python 官网新闻监控器
自动检测 [python.org](http://www.python.org) 的新闻更新，每天定时运行并记录变化日志。
已部署至 PythonAnywhere 云端，实现24小时无人值守监控。

## 项目功能概览
1. 新闻抓取： 从 Python 官网提取最新新闻标题与发布时间
2. 自动对比： 与上次抓取结果对比，判断是否有更新
3. 日志记录： 将新增新闻按时间写入“Changelog.txt”
4. 定时运行： 部署至 PythonAnywhere，每天固定时间自动执行

## 项目结构
main_program.py
主程序（抓取+对比+写入）
news_last.txt
上次新闻列表，用于判断是否有更新（程序自动生成）
Changelog.txt
所有新增新闻记录，附带发布日期（程序自动生成）
“news_last.txt” 和 “Changelog.txt”为运行时生成文件，首次运行时自动创建

## 技术要点
模块       | 技术
-----------|------------
网页请求    |“requests”
网页解析    |“BeautifulSoup”
数据持久化   |文件操作（“open”，“readlines”，“write”）
云端运行    |PythonAnywhere（免费定时任务）
数据处理    |基于字符串切片提取网页中时间字段，格式化为“YYYY-MM-DD HH:MM”

## 样例输出
'''text
News updates available.
[2025-03-14 17:27] Python 3.14.0 alpha 6 is out

## Changelog样式示例
[2025-03-14 17:27] Python 3.14.0 alpha 6 is out
[2025-03-12 15:32] PSF Distinguished Service Award Granted to Thomas Wouters
[2025-03-11 15:53] PSF Distinguished Service Award Granted to Van Lindberg
[2025-03-06 13:40] PSF Distinguished Service Award Granted to Ewa Jodlowska
[2025-03-04 11:40] Announcing Python Software Foundation Fellow Members for Q4 2024! 🎉

## 云端部署平台
使用PythonAnywhere
设置每日定时运行任务
可自动抓取->对比->写入更新日志
支持手动运行和日志查看

## 项目亮点
HTML结构解析路径明确，基于BeautifulSoup多层“.find()”实现精准抓取
自动化比对，不重复记录旧内容
模块化结构，后续易于扩展邮件/Telegram提醒等功能
支持长期运行与日志归档，适合实际使用

## 可扩展方向
支持多页面，多网站并行监控
将日志格式切换为CSV/JSON，支持数据分析
接入通知功能（邮箱，微信，Telegram等）
打包为“.exe”或做成图形化界面供非技术用户使用

## 项目作者
本项目由Cheng-Lazypd编写，作为自动化+云部署+数据监控方向的实战项目，欢迎参考或二次开发


