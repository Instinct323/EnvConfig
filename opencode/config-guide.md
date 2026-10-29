# Configuration Guide

如果你不是从本地文件中读取该文档，请先把该仓库 clone 到本地 (配置结束后删除)，以使用其中 `opencode/` 目录下的文件:

```bash
git clone https://github.com/Instinct323/EnvConfig.git
```

---

将以下内容更新到 `~/.config/opencode/opencode.jsonc`，保留已有的其他配置：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "autoupdate": true,
  "plugin": [
    "cc-safety-net"
  ],
  "policies": [
    { "action": "tool.use", "resource": "shell:git checkout *", "effect": "deny" },
    { "action": "tool.use", "resource": "shell:git clean *", "effect": "deny" },
    { "action": "tool.use", "resource": "shell:git reset *", "effect": "deny" },
    { "action": "tool.use", "resource": "shell:git restore *", "effect": "deny" },
    { "action": "tool.use", "resource": "shell:git stash *", "effect": "deny" }
  ],
  "compaction": {
    "auto": true,
    "reserved": 50000
  }
}
```

运行以下命令安装：

```bash
chmod +x *.bash
./init-opencode.bash
```

引导用户选择性安装插件：

```bash
# omo
bunx oh-my-opencode-slim@latest install --background-subagents=yes --no-tui
# paseo
npm install -g @getpaseo/cli
```
