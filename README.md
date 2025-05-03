# READINGWEEK1

1、学习资料来源:
Git官方文档：https://git-scm.com/  提供了Git的安装、配置、基本操作及高级功能的详细说明。
GitHub官方教程链接：https://docs.github.com/en 涵盖了从注册账号到创建仓库、推送代码的完整流程。
Gitee帮助中心链接：https://gitee.com/help 提供了Gitee账号注册、仓库创建及代码提交的详细步骤。
AI解决问题

2、实践流程：

安装
配置用户信息
创建本地仓库
初始化仓库
添加文件并提交
创建github新仓库
关联本地仓库与远程仓库
复制远程仓库URL
添加远程地址
推送代码到远程仓库

3、 问题：
（1）网络连接问题
现象：HTTP/2 stream 1 was not closed cleanly
解决：改用 SSH 协议
（2）密钥认证问题
现象：GitHub 已于 2021 年 8 月 13 日禁用密码认证，推送时提示Permission denied。
解决：
生成SSH密钥并添加到GitHub
（3）分支冲突
现象：合并分支时出现CONFLICT标记。本地和远程都有提交，导致git不知道如何合并
解决：
在 git pull 命令后直接添加参数：# 使用合并（merge）策略（保留双方提交历史）
git pull --no-rebase origin main# 或使用变基（rebase）策略（将本地提交“嫁接”到远程最新提交后，保持线性历史）
git pull --rebase origin main# 或仅允许快进（fast-forward，仅当本地分支是远程分支的直接后代时才合并）
git pull --ff-only origin main
（4）本地远程未同步
现象：远程仓库已有提交历史，而你的本地仓库缺少这些提交“Updates were rejected because the remote contains work that you do not have locally
解决：拉取远程代码并合并到本地， 解决冲突，推送代码到远程仓库

4.心得体会
版本控制的重要性：Git的分支管理功能极大提升了多人协作效率，避免了代码覆盖和冲突。
命令行熟练度：频繁使用git status、git log等命令可以快速定位问题，提高工作效率。
远程协作优势：GitHub的Pull Request机制便于代码审查，保障了代码质量。
持续学习：高级功能如Rebase、Cherry-pick需结合实际项目深入实践，以应对复杂需求。
通过本次实践，我不仅掌握了Git的本地配置、远程仓库关联及多次代码提交的流程，还学会了解决权限、冲突等常见问题的方法。Git的分布式版本控制特性显著提升了代码管理的灵活性与团队协作效率，为未来的项目开发奠定了坚实基础。

