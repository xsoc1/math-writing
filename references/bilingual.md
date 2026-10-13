# 中英文数学语言与语义守恒

## 语言选择不应改变数学结构

先固定定理的条件、量词与结论，再分别形成自然的中文和英文。允许拆句和改变连接词位置；不允许把“存在一个与 x 无关的 N”译成“对每个 x 可选择 N”。最终逐项比较对象、基础域、量词、限定范围、符号、引用、证明方向及结论状态。

B1 的做法是在中文正文使用中文术语，英文放到索引；B3 的英文则更常显式引导读者理解抽象定义。两者是可选择的方法，不是所有中文或英文必须如此。本项目默认首次出现且确有辨识价值时给英文对照，之后用统一中文；参考型长文另设双语术语表。

## 中文：主语明确，连接词承担推理

“设”用于引入对象，“固定”提醒后续量词，“由……得到”对应具体依据，“只需证明”对应化归，“反之”启动逆向论证，“这说明”要有可指认的结论。无需每句都用“我们”，也不应省略到不知道谁作用于谁。

少用“进行一个证明”“实现对该性质的验证”“可以显著提升数学上的严谨性”等空泛名词化。写“以下证明该映射与代表元的选取无关”比“下面对良定义性方面进行处理”更具体。删冗语不等于删依据。

中文正文默认中文标点；数学环境用合法 TeX 语法，公式作为句子一部分处理标点。已有出版模板采用半角标点时可沿用，不把某位作者的排版习惯当成数学标准。中文定理正文不强制斜体。

## English: verbs and logical roles

Use “Let” to introduce an object, “Fix” when an object remains fixed during an argument, and “Suppose” to make an assumption. Use “It suffices to prove” only for a valid reduction; use “Conversely” only when proving the other implication. Name the map or object when “it” or “this” would be ambiguous.

A proof should read as connected prose, not as a sequence of formulas joined only by arrows. Formulas belong to sentences and receive punctuation when needed. Put the purpose of a construction near its introduction. Avoid inflated transitions such as “It is of paramount importance to note that”; state the mathematical point instead.

“Clearly” is acceptable for a genuinely routine observation for the intended audience. It is not an argument for independence of choices, compactness, an interchange of limits, or the existence of a new object. Keep parallel claims grammatically parallel, especially in theorem hypotheses.

## 原创新写对照

**不充分的草稿：** “商上的映射自然定义且显然唯一。” / “The map on the quotient is natural and clearly unique.”

**中文：** “若分解存在，它必须满足 \(\bar f(m+N)=f(m)\)。若 \(m+N=m'+N\)，则 \(m-m'\in N\subseteq\ker f\)，从而 \(f(m)=f(m')\)；因此该定义与代表元无关。又因商映射满射，这个分解至多有一个。”

**English:** “Any factorization must satisfy \(\bar f(m+N)=f(m)\). If \(m+N=m'+N\), then \(m-m'\in N\subseteq\ker f\), so \(f(m)=f(m')\). Thus the definition is independent of the representative. The surjectivity of the quotient map gives uniqueness.”

这是论证片段，不是完整定理：上下文仍需指定模、线性映射并核对线性。完整示例见样张，不能只把润色片段当成自足证明。

## 不能按词机械替换的术语

| 英文 | 常见中文与须核对的语境 |
|---|---|
| well-defined | 良定义、良定；通常需说明所指的无歧义或选择无关性 |
| canonical / natural | 典范 / 自然；自然性可能要求一个自然变换及其相容性，不是赞美词 |
| regular | 正则、正则性等；正则值、正则函数、正则环不共享同一个定义 |
| normal | 正规子群、正规算子、正规族等；按该分支与既有译法核对，不混同 normal 与 regular |
| domain | 定义域、区域或整环；要看所指对象 |
| unit / identity | 可逆元 / 幺元或恒等映射；“unit group”不是仅含幺元的群 |
| image / coimage | 像 / 余像；一般范畴中不能未经条件视为同一个对象 |
| kernel / cokernel | 核 / 余核；homotopy kernel 不能直接删去“同伦” |
| limit / colimit | 极限 / 余极限常见，但李文威还使用投射 / 归纳极限；源笔记保留原约定 |
| isomorphism / equivalence | 同构 / 等价；范畴等价不要求对象集合之间严格互逆 |
| up to a unique isomorphism | 精确到与给定结构相容的唯一同构；限定相容性 |
| uniformly / pointwise / almost everywhere | 一致 / 逐点 / 几乎处处；不可互相替代 |
| eventually / for all sufficiently large n | 最终 / 当 n 充分大时；说明阈值可以依赖谁 |
| exact / approximate / numerical evidence | 精确 / 近似 / 数值证据；算法输出不能替代定理状态 |

## 最低限度的术语与符号记录

长项目保存“符号—含义—类型—首次定义—作用域—另名”；双语增加“所选译法—来源用法—不采用的歧义”。短文用一段约定即可，不必创建大数据库。

新写文本默认 `\subseteq` 表示容许相等的包含，`\subsetneq` 表示真包含，避免 `\subset` 的跨书歧义。源书摘要保留其原约定，并在必要时注明区别。不要为追求统一改写原文数学事实。
