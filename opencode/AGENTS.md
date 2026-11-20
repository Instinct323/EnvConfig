## Communication

- brief: 使用 caveman 模式
- figure: 必要时用线框图辅助说明
- lang: 始终用中文回复，可穿插少量英文术语
- path: 用代码块展示项目目录树；同级先列目录，再列文件；占位符用花括号。示例见 [Temporary Files](#temporary-files)
- research: 文献调研时，用 [arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) 和 Zotero MCP 检索

## Rules

- config: 使用 MinerU 时，优先选择带 token 的模式；token 失效时，请用户更新
- defense: 默认用户遵守契约，避免过度校验
- defense: 遵守接口约定，不为低概率事件添加护栏
- file: 不擅自拆分或合并文件，也不擅自变更目录结构
- file: 用户未指定路径时，将编写的产物（分析、报告、代码）暂存到 `.omo/`
- file: 脚本或代码位于 `runs/**` 时，将重要产物放在脚本或代码所在目录；否则放入 `runs/**`
- read: 主动用 `grep` 筛选命令输出，只保留必要信息

## Temporary Files

```
/tmp/opencode/
├── .cache/              # 缓存数据
│   └── mineru/          # MinerU 解析结果
│       ├── {project}/   # 每个项目一个目录
│       └── INDEX.md     # 记录各项目目录的内容
└── {debug_project}/     # 每个调试项目一个目录
    ├── {debug_script}   # 调试脚本
    └── {debug_output}   # 调试产物（如日志）
```

## Programming

- 长代码按逻辑分块，块之间用空行分隔，每块至少 3 行
- CMake、CSS：使用 2 空格缩进，tab 宽度为 2
- C/C++：运行 Clang-Tidy；不要仅为 cast 风格、声明赋值合并、冗余限定符、`make_*` 替换或作用域收窄而改写代码
- JSON：tab 宽度为 2；对象、数组超过行宽时按需换行
- Markdown：使用 2 空格缩进，长文本不自动硬换行
- Shell：运行 ShellCheck，修复 `error` 级问题，忽略 `SC2086` 和 `SC2164`

### Python

- brief: 不定义 `main` 函数，入口逻辑直接写在 `if __name__ == "__main__"` 下
- brief: 不使用 `if TYPE_CHECKING` 分支
- brief: 修复未解析的引用（unresolved reference），`optimizer` 除外
- brief: 不定义新的异常类型，而是使用内置的、第三方库的
- brief: 可选依赖的类型注解使用字符串前向引用；不单为消除静态检查错误引入 `Protocol`，也不在运行时改写 `__annotations__`
- brief: 简短条件分支若仅含一条简单语句，保持 `if condition: statement` 单行形式
- feature: 禁止“仅关键字参数”语法
- package: 保留 stub package 提示，忽略 `pandas`、`scipy`
- package: 用 `try-except` 导入可选依赖；导入失败时，跳过或赋值为 `None`
- style: 将 `object`、`type` 字符串化时提供 `__str__`、`__repr__` 或 `__format__`
- style: 使用 `<arg>: <type> = None` 代替 `<arg>: <type> | None = None`，省略 `-> None`
- style: 单行 docstring 开头的 `"""` 与正文之间至少留一个空格
- syntax: 仅在已配置 Ruff 时运行 `ruff` 检查

<!-- CODEGRAPH_START -->
## CodeGraph

In repositories indexed by CodeGraph (a `.codegraph/` directory exists at the repo root), reach for it BEFORE grep/find or reading files when you need to understand or locate code:

- **MCP tool** (when available): `codegraph_explore` answers most code questions in one call — the relevant symbols' verbatim source plus the call paths between them, including dynamic-dispatch hops grep can't follow. Name a file or symbol in the query to read its current line-numbered source. If it's listed but deferred, load it by name via tool search.
- **Shell** (always works): `codegraph explore "<symbol names or question>"` prints the same output.

If there is no `.codegraph/` directory, skip CodeGraph entirely — indexing is the user's decision.
<!-- CODEGRAPH_END -->
