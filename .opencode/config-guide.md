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

运行以下命令安装：

```bash
chmod +x *.bash
./install-skills.bash
```

### opencode

将以下内容更新到 `~/.config/opencode/opencode.json`：

```json
{
  "autoupdate": true,
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
  },
  "plugin": [
    "cc-safety-net",
    "oh-my-openagent",
    "@tarquinen/opencode-dcp@latest",
    "oc-chatgpt-multi-auth@latest",
    "opencode-antigravity-auth@latest"
  ]
}
```

---

## Project

Config: `AGENTS.md`

### Preference

- 始终使用中文回复，可穿插少量英文术语
- 如果你在工作过程中产出了过程文件 (草稿，测试脚本，测试结果)，使用完成后删除
