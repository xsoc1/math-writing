# 数学写作 skill · v0.1.0

从七份用户提供的书稿代表段落，提炼中英文数学写作规则，输出到 LaTeX 与 Obsidian Markdown。此包已写成可使用的初版，不是只有一个“以后再研究”的提示词。入口是 `SKILL.md`。

## 最快使用方式

将本目录交给支持读取文件的工作代理，要求先读 `SKILL.md`，再按任务加载引用文件。支持 Agent Skills 的工具可按该工具自己的安装说明注册整个 `math-writing` 目录；本交付未替你安装，也不假定某个模型或产品支持相同的安装路径。

可直接使用 `prompts/START.md`。继续纳入新书时用 `prompts/EXTEND.md`。不支持 skill 自动发现的环境也可以显式提供入口与相关参考文件。

## 目录与内容

| 文件 / 目录 | 用途 |
|---|---|
| `SKILL.md` | 入口：数学底线、写作规则、任务路由与验收 |
| `references/source-observations.md` | 版本、抽样位置、来源观察、规则来源与局限 |
| `references/branches.md` | 六类分支写法与混合论证路由 |
| `references/bilingual.md` | 中文、英文及翻译规范，易混术语 |
| `references/pedagogy.md` | 教学模式、研究依据与适用边界 |
| `references/typesetting.md` | 可调整的书页 / 屏幕版式及兼容边界 |
| `references/tools.md` | 读取、编辑、编译、文献、图表与验证的使用模式 |
| `references/distillation.md` | 新书取样、规则提炼、反例与版本迭代 |
| `references/web-sources.md` | 官方文档、研究文献及访问日期 |
| `assets/latex/` | 中英各一份六主题写作样张、简洁文档骨架及共用样式 |
| `assets/obsidian/` | 中英样张、笔记骨架、示例索引及仅作用于数学笔记的 CSS |
| `assets/diagrams/` | 交换图源文件及发布用图形 |
| `scripts/` | 环境检测、安全边界明确的样张构建、有限静态检查 |
| `tests/` | 静态检查器单元测试、数学与可读性回归任务 |
| `examples-output/` | 实际编译后的中英 PDF 样张 |
| `validation/` | 本次实际执行情况与环境信息 |

## 编译与检查

需要 Python 3.10+ 和可用的 XeLaTeX、latexmk、CTeX、AMS 相关包、unicode-math、TikZ-cd。模板只引用系统字体，不包含字体文件；样张字体选择详见排版规范。Python 脚本本身不依赖第三方 Python 包。

在包根目录运行：

```sh
python scripts/check_env.py --output validation/environment-local.json
python -m unittest discover -s tests -v
python scripts/lint_math.py assets/obsidian/Specimen-zh.md assets/obsidian/Specimen-en.md
python scripts/build.py --language both
```

Windows 也可将 `python` 改为 `py`。若 TeX 发行版尚未安装相关包，先通过该发行版的包管理器补齐；不将下载执行器、管理员权限或 shell-escape 作为本 skill 的默认步骤。安装结果由 `check_env.py` 和实际编译核实。

若仅用 Obsidian，将 `assets/obsidian` 的内容复制到一个测试 vault，或有选择地加入已有 vault；隐藏目录中的 `.obsidian/snippets/math-writing.css` 需要复制到目标 vault 的同名目录并在“外观 → CSS 代码片段”启用。合并文件而非覆盖已有 `.obsidian` 配置。样张的 `cssclasses: [math-note]` 控制样式作用范围。

## 初版覆盖与限制

本次认真选读了导言、概念引入和若干完整的短证明单元，并查看代表性页面；没有逐页精读七本书。中文取样仅两卷、同一作者。卷二是 2022-05-06 的未定稿，不能把缺失导读当成成熟范式。Serre 的上传版本为英文译本扫描件，正文通过页面图像读取；Milnor 文件为双页扫描，PDF 页码不等于印刷页码。

当前优势是代数 / 范畴、同调、复分析、微分拓扑、Lie 理论、算术。未充分训练的分支不冒充同等成熟。排版数值是本项目可修改的默认值，不是“最佳字体 / 行距”的实验结论。

所有数学样张是标准结论的新写示范，不是原书摘录。原书 PDF、长段书文和字体文件均不随包分发。数学内容做了逐步人工式核对及有限程序测试，但没有进行 Lean 等全篇形式化认证。LaTeX 与 Obsidian 的实际验证状态，以 `validation/REPORT.md` 为准。

可选公式解析检查：已有可解析的 `mathjax-full` 时，运行 `node scripts/check_mathjax.cjs assets/obsidian/Specimen-zh.md assets/obsidian/Specimen-en.md`。这只处理样张所用的美元数学子集，不是通用 Markdown 解析或 Obsidian GUI 验证。无需此检查也可使用核心 skill。

图的 SVG 导出使用 Poppler 的 `pdftocairo`；无需重建图时可用 `build.py --skip-diagram`，保留已有图但不能据此声称图已重新生成。

`assets/latex/.vscode/settings.json` 提供可选编辑器 recipe。合并所需条目，不覆盖已有项目配置；本次未在 VS Code GUI 中运行它。
