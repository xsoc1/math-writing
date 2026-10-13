# math-writing v0.2

中英文数学写作 skill，支持 LaTeX 与 Obsidian Markdown。v0.2 在原有数学底线、双语规则和分支策略上，增加了独立入门讲义的专门模式。

## 入口

先读 `SKILL.md`。一般任务使用 `prompts/START.md`；重编入门讲义使用 `prompts/LECTURE.md`，并加载 `references/intro-lecture.md`。新增规则的依据和边界见 `references/failure-case-lie.md`，长讲义编辑回归案例见 `tests/lecture-regression.md`。

向工作模型提供整个目录，不只粘贴主文件而丢失被引用的规范。目录名可使用 `math-writing`；主 skill 的 `name` 保持不变。原包的文件交付与此仓库的维护、部署检查分开记录，见 [本次更新记录](validation/DEPLOYMENT.md)。

## 版本范围

v0.2 不要求所有文章都变长。研究型证明、参考笔记、教学讲义应采用不同解释程度。入门模式重点是定义和证明依赖闭合、新运算能够复现，以及根据先修知识和运算熟练度分别选择展开量。

保留的 `assets/`、`examples-output/` 和原短样张是 v0.1 资源，没有因目录升级就被宣称为本轮新写。原有验证结果已移至 `validation/history-v0.1/`；本轮范围见 `validation/REPORT.md`。本包没有打包用户的原书或字体文件。

原包说明提到的完整李代数讲义不在此仓库中；相关既往报告保留为供稿记录，本次没有重新核读或认证该讲义。

## Codex 使用

将本仓库的技能目录放在用户技能目录 `~/.agents/skills/math-writing`，然后通过 `$math-writing` 调用；保留全部参考文件，而不只复制 SKILL.md。已有安装时先备份，再更新文件，避免覆盖其他技能或已有应用设置。发现位置与更新行为见 [OpenAI 官方技能说明](https://learn.chatgpt.com/docs/build-skills)。

公开仓库地址为 [xsoc1/math-writing](https://github.com/xsoc1/math-writing)。Git 版本管理保留 v0.1 基线与 v0.2 更新，安装副本不包含 .git。

## 检查与证据

```sh
	python -m unittest discover -s tests -v
	python scripts/lint_math.py assets/obsidian/Specimen-zh.md assets/obsidian/Specimen-en.md assets/latex/main-zh.tex assets/latex/main-en.tex
```

12 项脚本测试与 12 项长讲义编辑案例不是同一项验证。后者要求实际检查正文，不能因为案例文件齐全就称为通过。历史 PDF、MathJax 和讲义报告不替代本机重跑，不替代学生理解实验。

本仓库未另行指定开放源代码许可证；公开可读不代表此次维护代作者授予新的许可。
