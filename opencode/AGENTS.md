# 沟通

- 使用 caveman 模式
- 始终使用中文回复，可穿插少量英文术语

# 规则

- 如果你在工作过程中产出了过程文件 (草稿，测试脚本，测试结果)，使用完成后删除
- 使用 mineru 时应当优先使用有 token 模式
- 不可使用 git 命令改变仓库的工作区状态（`git stash`、`git stash pop`、`git checkout -- <path>`、`git reset --hard`、`git restore`、`git clean` 等）
- 应主动对命令输出做 `grep` 以筛选最短的有效信息
- 不擅自拆分文件、合并文件，或是其它变更目录结构的操作

# 代码

- CMake、CSS：使用 2 空格缩进，tab 宽度为 2
- C/C++：运行 Clang-Tidy；不要仅为 cast 风格、声明赋值合并、冗余限定符、`make_*` 替换或作用域收窄而改写代码
- JSON：tab 宽度为 2；对象、数组超过行宽时按需换行
- Markdown：使用 2 空格缩进，长文本不自动硬换行
- Shell：运行 ShellCheck，按 error 修复，忽略 `SC2086`、`SC2164`
- Python：
  - 忽略 `E701`、`E722`、`E731`
  - 修复 unresolved reference，忽略 `optimizer`
  - 将 `object`、`type` 字符串化时提供 `__str__`、`__repr__` 或 `__format__`
  - 保留 stub package 提示，忽略 `pandas`、`scipy`
  - 使用 `<arg>: <type> = None` 代替 `<arg>: <type> | None = None`，省略 `-> None`
  - 不使用 `if TYPE_CHECKING` 分支
  - 简短条件分支若仅含一条简单语句，保持 `if condition: statement` 单行形式
  - 可选依赖使用 `try-except` 导入，导入失败时赋值为 `None`
  - 禁止“仅关键字参数”语法
  - 不定义新的异常类型，而是使用内置的、第三方库的
  - 可选依赖相关类型使用字符串前向引用；不为消除静态检查错误额外引入 `Protocol`，不在运行时改写 `__annotations__`

<!-- CODEGRAPH_START -->
## CodeGraph

In repositories indexed by CodeGraph (a `.codegraph/` directory exists at the repo root), reach for it BEFORE grep/find or reading files when you need to understand or locate code:

- **MCP tool** (when available): `codegraph_explore` answers most code questions in one call — the relevant symbols' verbatim source plus the call paths between them, including dynamic-dispatch hops grep can't follow. Name a file or symbol in the query to read its current line-numbered source. If it's listed but deferred, load it by name via tool search.
- **Shell** (always works): `codegraph explore "<symbol names or question>"` prints the same output.

If there is no `.codegraph/` directory, skip CodeGraph entirely — indexing is the user's decision.
<!-- CODEGRAPH_END -->
