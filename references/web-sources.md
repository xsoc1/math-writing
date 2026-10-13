# 外部研究与官方文档

访问日期：2026-10-07。网址用于复查。工具文档会更新，安装环境版本以实际检测为准。下列摘要区分阅读范围，不把公开摘要写成全文评审。

## 数学写作与教学

**W01 — Knuth, Larrabee & Roberts, Mathematical Writing.** 1987课程讲义报告。本轮重点为开篇写作简则：读者、符号引入、连贯语言与公式组织；不是教育实验。
`https://jmlr.csail.mit.edu/reviewing-papers/knuth_mathematical_writing.pdf`

**W02 — Terence Tao, On writing.** 作者的数学论文写作建议目录及开头说明；强调写法依赖读者、主题与媒介，非统一格式规范。
`https://terrytao.wordpress.com/advice-on-writing-papers/`

**W03 — Hodds, Alcock & Inglis (2014), Self-explanation training improves proof comprehension.** JRME 45(1), 62–101，DOI `10.5951/jresematheduc.45.1.0062`。读取作者所在大学资源库的摘要与元数据；三项实验结果的概述，不表示复核了完整实验。库中的一处 Citation 字段页码与 Pages / DOI 不一致；这里采用 Pages 字段62–101，保留此元数据注意事项。
`https://repository.lboro.ac.uk/articles/journal_contribution/Self-explanation_training_improves_proof_comprehension/9367232`

**W04 — Mejia-Ramos, Fuller, Weber, Rhoads & Samkoff (2012), An assessment model for proof comprehension in undergraduate mathematics.** Educational Studies in Mathematics 79, 3–18，DOI `10.1007/s10649-011-9349-7`。读取出版社摘要与书目信息；多维理解评估模型，不是本 skill 的效果实验。
`https://link.springer.com/article/10.1007/s10649-011-9349-7`

**W05 — Tall & Vinner (1981), Concept image and concept definition in mathematics with particular reference to limits and continuity.** Educational Studies in Mathematics 12, 151–169，DOI `10.1007/BF00305619`。原文PDF的开头概念阐述用于区分直观表象与形式定义，未声称全文实证复核。
`https://www.math.uic.edu/~bshipley/Tall_David.pdf`

## 技能格式与 Obsidian

**W06 — Agent Skills specification.** `SKILL.md` 前置元数据、目录结构、按需加载。本包遵循公开文件结构，不保证所有产品均支持同一安装流程。
`https://agentskills.io/specification`

**W07 — Obsidian, Advanced formatting syntax.** 核心 Markdown 的数学与 Mermaid；本包以 `$...$` 和 `$$...$$` 用法为基础，不推断内嵌 MathJax 版本。
`https://help.obsidian.md/Editing+and+formatting/Advanced+formatting+syntax`

**W08 — Obsidian, Callouts.** 自定义类型、展开 / 折叠行为、未知类型回退。
`https://help.obsidian.md/Editing+and+formatting/Callouts`

**W09 — Obsidian, Internal links; CSS snippets.** 稳定标题 / 块链接、ID字符约束、启用 CSS 代码片段。
`https://help.obsidian.md/Linking+notes+and+files/Internal+links`
`https://help.obsidian.md/Extending+Obsidian/CSS+snippets`

**W10 — MathJax, Differences from Actual TeX.** 数学输入处理器与完整 TeX 的差异。页面为在线当前文档，不能据此断定 Obsidian 使用同一版本。
`https://docs.mathjax.org/en/latest/input/tex/differences.html`

## LaTeX、转换与文献工具

**W11 — CTAN, CTeX.** 中文类、标点与多引擎支持；本包具体使用 XeLaTeX。
`https://ctan.org/pkg/ctex`

**W12 — CTAN, latexmk.** 自动构建依赖与持续预览功能。实际脚本使用的版本由环境检测给出。
`https://ctan.org/pkg/latexmk`

**W13 — Pandoc User's Guide.** 转换的 AST 机制及不可期待任意格式间完全保真；此包不提供通用双向转换器。
`https://pandoc.org/MANUAL.html`

**W14 — CTAN, amsthm; mathtools; unicode-math.** 定理结构、公式工具与 Unicode 数学字体。
`https://ctan.org/pkg/amsthm`
`https://ctan.org/pkg/mathtools`
`https://ctan.org/pkg/unicode-math`

**W15 — CTAN, tikz-cd; cleveref.** 交换图与按对象类型生成引用。实际载入顺序与计数设置以本包编译结果为准。
`https://ctan.org/pkg/tikz-cd`
`https://ctan.org/pkg/cleveref`

**W16 — Better BibTeX, Exporting.** 文献 key 与导出 / 自动导出的官方说明；未在本次连接用户文献库或做同步试验。
`https://retorque.re/zotero-better-bibtex/exporting/`

**W17 — LaTeX Workshop, Compile.** 编辑器的 recipes / tools 配置；未在本次运行 VS Code GUI。
`https://github.com/James-Yu/LaTeX-Workshop/wiki/Compile`

**W18 — CTAN, microtype.** 不同引擎支持不同微排版能力；中文 / 数学视觉质量不能靠开一个选项保证。
`https://ctan.org/pkg/microtype`

## 不作哪些推断

没有证据表明本包的字号、行距、颜色或固定模板具有普遍最优的学习效果。没有对所有教材的全部章节作统计。没有将作者个人经验包装成实验结果。没有以当前网页版本冒充实际安装版本，也没有把兼容文档视为 Obsidian 原生视觉测试。
