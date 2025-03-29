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
1. main_program.py: 主程序（抓取+对比+写入）
2. news_last.txt: 上次新闻列表，用于判断是否有更新（程序自动生成）
3. Changelog.txt: 所有新增新闻记录，附带发布日期（程序自动生成）
>“news_last.txt” 和 “Changelog.txt”为运行时生成文件，首次运行时自动创建

## 技术要点
模块       | 技术
-----------|------------
网页请求    |“requests”
网页解析    |“BeautifulSoup”
数据持久化   |文件操作（“open”，“readlines”，“write”）
云端运行    |PythonAnywhere（免费定时任务）
数据处理    |基于字符串切片提取网页中时间字段，格式化为“YYYY-MM-DD HH:MM”

## 样例输出

```text
News updates available.
[2025-03-14 17:27] Python 3.14.0 alpha 6 is out
```

## Changelog样式示例
```text
[2025-03-14 17:27] Python 3.14.0 alpha 6 is out
[2025-03-12 15:32] PSF Distinguished Service Award Granted to Thomas Wouters
[2025-03-11 15:53] PSF Distinguished Service Award Granted to Van Lindberg
[2025-03-06 13:40] PSF Distinguished Service Award Granted to Ewa Jodlowska
[2025-03-04 11:40] Announcing Python Software Foundation Fellow Members for Q4 2024! 🎉
```

## 云端部署平台
1. 使用PythonAnywhere
2. 设置每日定时运行任务
3. 可自动抓取->对比->写入更新日志
4. 支持手动运行和日志查看

## 项目亮点
1. HTML结构解析路径明确，基于BeautifulSoup多层“.find()”实现精准抓取
2. 自动化比对，不重复记录旧内容
3. 模块化结构，后续易于扩展邮件/Telegram提醒等功能
4. 支持长期运行与日志归档，适合实际使用

## 可扩展方向
1. 支持多页面，多网站并行监控
2. 将日志格式切换为CSV/JSON，支持数据分析
3. 接入通知功能（邮箱，微信，Telegram等）
4. 打包为“.exe”或做成图形化界面供非技术用户使用

## 项目作者
本项目由Cheng-Lazypd编写，作为自动化+云部署+数据监控方向的实战项目，欢迎参考或二次开发


# English version
# Python News Monitor
A Python-based tool that automatically checks for news updates on python.org and logs any changes. Deployed to PythonAnywhere for daily scheduled execution with zero manual operation.

## Features
1. News Extraction: Fetch latest news titles and publish times from Python.org
2. Auto Comparison: Compare with the previous result to detect updates
3. Change Logging: Log new items with timestamps to Changelog.txt
4. Scheduled Execution: Runs daily via PythonAnywhere

## Project Structure
1. main_program.py: Main script (scraping + comparison + logging)
2. news_last.txt: Stores last fetched result (auto-generated)
3. Changelog.txt: Logs newly published news with timestamps (auto-generated)
>These .txt files are created automatically on first run.

## Tech Stack
Module         | Tool/Method
---------------|------------
Web Request    |"requests"
HTML Parsing   |"BeautifulSoup"
File Handling  |"open"，"readlines"，"write"
Cloud Hosting  |PythonAnywhere（free tier）
Time Parsing   |String slicing (format "YYYY-MM-DD HH:MM")

## Sample Output

```text
News updates available.
[2025-03-14 17:27] Python 3.14.0 alpha 6 is out
```

## Changelog Sample
```text
[2025-03-14 17:27] Python 3.14.0 alpha 6 is out
[2025-03-12 15:32] PSF Distinguished Service Award Granted to Thomas Wouters
[2025-03-11 15:53] PSF Distinguished Service Award Granted to Van Lindberg
[2025-03-06 13:40] PSF Distinguished Service Award Granted to Ewa Jodlowska
[2025-03-04 11:40] Announcing Python Software Foundation Fellow Members for Q4 2024! 🎉
```

## Deployment Platform
1. Hosted on PythonAnywhere
2. Scheduled daily task with automatic execution
3. Supports manual logs, output viewing, and historical inspection

## Highlights
1. Clear multi-level HTML tag selection with precise extraction
2. Smart comparison: Only logs newly detected updates
3. Modular structure: Easy to integrate notification systems like email or Telegram
4. Designed for long-term use with persistent logs

## Future Plans
1. Monitor multiple pages and websites simultaneously
2. Switch log format to CSV/JSON for better analysis
3. Integrate email/WeChat/Telegram notification system
4. Package as .exe or build GUI for non-technical users

## Author
Developed by Cheng-Lazypd as a project on automation, deployment, and data monitoring. Open to collaboration, feedback, and further development.
