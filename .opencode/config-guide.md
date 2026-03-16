# Configuration Guide

这个教程的每一步都极其重要，请一字不漏地阅读并记录每个步骤的完成情况

如果你不是从本地文件中读取该文档，请先把该仓库 clone 到本地 (配置结束后删除)，以使用其中 `.opencode/` 目录下的文件:

```bash
git clone https://github.com/Instinct323/EnvConfig.git
```

### Format

- This-doc: 标题使用英文，正文使用中文
- Config：
  - 已完成的配置项 (避免重复配置)
  - 配置步骤 (便于向用户说明操作过程)
  - 不同层级的配置文件之间的内容不应该出现重叠
- File: 超链接表示的文件，一般位于该文档的根目录下；或者位于仓库中

### Process

每个配置文件的配置流程如下：

1. 读取 Config：根据配置状态决定后续操作
2. 状态判断：
   - 已完成 → 询问用户是否需要重新配置
   - 未完成 → 执行配置，完成后更新配置状态
3. 清理：配置完成后清理临时文件

你需要先确定每个配置项之间的依赖关系，以并行地、更快地配置

---

## Global

Config: `~/.config/opencode/global-config.md`

将以下内容更新到 `~/.config/opencode/opencode.json`：

```json
{
  "plugin": [
    "oh-my-opencode",
    "cc-safety-net",
    "@tarquinen/opencode-dcp@latest",
    "oc-chatgpt-multi-auth@latest"
  ],
  "compaction": {
    "auto": true,
    "prune": true,
    "reserved": 10000
  },
  "lsp": {
    "python": {
      "command": ["pyright-langserver", "--stdio"],
      "extensions": [".py", ".pyi"]
    }
  }
}
```

### anthropics-skills

将以下仓库的 `skills` 目录下的技能添加到 `~/.config/opencode/skills/` 中：
- 仓库：https://github.com/anthropics/skills

### oh-my-openagent

参考官方安装指南：
- 文档：https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/docs/guide/installation.md

将 [config/oh-my-opencode.json]() 覆盖写入到 `~/.config/opencode/` 中

### provider

所有完成配置的 `API_KEY` 都可以在 `~/.config/opencode/opencode.json` 中找到 (注意，`API_KEY` 不应该被存储在这之外的任何文件中)

对于不同的供应商，你需要分别询问用户对于 `API_KEY` 的操作，给出以下几个选项：

1. 写入新的 API_KEY
2. 跳过配置 API_KEY
3. 跳过该 provider 的配置

以下是目前支持的供应商，请依次按照以下教程配置：

- 百炼：[provider/bailian.md]()
- 火山引擎：[provider/volcengine.md]()

---

## Project

Config: `AGENTS.md`

### Preference

- 始终使用中文回复，可穿插少量英文术语
- 不要修改工作区之外的文件，请先在工作区内创建修改后的版本，并询问用户是否需要覆盖到源文件

### Include

你需要加载并阅读以下文件，提炼其要点添加到配置文件中:

- [code-style.md](): 代码风格
