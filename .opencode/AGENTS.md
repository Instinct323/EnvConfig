# 沟通

- 使用 caveman 模式
- 始终使用中文回复，可穿插少量英文术语

# 规则

- 如果你在工作过程中产出了过程文件 (草稿，测试脚本，测试结果)，使用完成后删除
- 使用 mineru 时应当优先使用有 token 模式
- 不可使用 git 命令改变仓库的工作区状态

# 代码

- CMake、CSS：使用 2 空格缩进，tab 宽度为 2
- C/C++：运行 Clang-Tidy；不要仅为 cast 风格、声明赋值合并、冗余限定符、`make_*` 替换或作用域收窄而改写代码
- JSON：tab 宽度为 2；对象、数组超过行宽时按需换行
- Markdown：使用 2 空格缩进，长文本不自动硬换行
- Shell：运行 ShellCheck，按 error 修复，忽略 `SC2086`、`SC2164`
- Python：遵循 PEP 8，忽略 `E701`、`E722`、`E731`；修复 unresolved reference，忽略 `optimizer`；将 `object`、`type` 字符串化时提供 `__str__`、`__repr__` 或 `__format__`；保留 stub package 提示，忽略 `pandas`、`scipy`
