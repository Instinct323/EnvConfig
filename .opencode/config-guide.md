# Configuration Guide

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

### skills

将以下技能添加到 `~/.config/opencode/skills/` 中:

- mine: 当前目录下的 [skills]() 文件夹下的技能
- anthropics: 仓库 https://github.com/anthropics/skills 中的 `skills` 文件夹下的技能

### [oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)

运行以下命令安装：

```bash
npx oh-my-opencode install --no-tui --claude=no --gemini=no --copilot=no
```

最后，你需要建议用户进行以下步骤：

1. 重启 OpenCode，确保配置更新
2. 使用技能 /more-provider 配置供应商
3. 使用技能 /config-omo 更新模型配置

### opencode

将以下内容更新到 `~/.config/opencode/opencode.json`：

```json
{
  "plugin": [
    "cc-safety-net",
    "oh-my-opencode",
    "@tarquinen/opencode-dcp@latest",
    "oc-chatgpt-multi-auth@latest",
    "opencode-antigravity-auth@latest"
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

---

## Project

Config: `AGENTS.md`

### Preference

- 始终使用中文回复，可穿插少量英文术语
- 如果你在工作过程中产出了过程文件 (草稿，测试脚本，测试结果)，使用完成后删除

### Include

你需要加载并阅读以下文件，提炼其要点添加到配置文件中:

- [code-style.md](): 代码风格
