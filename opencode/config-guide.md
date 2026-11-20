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
    "@slkiser/opencode-quota"
  ],
  "commands": {
    "optimize": {
      "description": "精简参数和代码，解决性能瓶颈",
      "template": "优化 $ARGUMENTS；未指定范围时先检查当前改动。保持行为和接口契约。\n梳理参数流向，删掉冗余参数、路径、转发层和重复校验；保留外部输入与安全边界校验。优先复用现有库，确能降低维护成本时再引入成熟第三方库。\n先实测定位瓶颈，优先做既简化代码又加速的改动。运行相关测试，在相同条件下对比优化前后的基准结果，汇报改动、测试结果、性能实测值及变化幅度。"
    }
  },
  "compaction": {
    "auto": true,
    "buffer": "15%"
  },
  "permissions": [
    {"action": "edit", "resource": "/tmp/*", "effect": "allow"},
    {"action": "external_directory", "resource": "/tmp/*", "effect": "allow"},
    {"action": "external_directory", "resource": "~/miniconda3/*", "effect": "allow"},
    {"action": "external_directory", "resource": "~/.config/opencode/*", "effect": "allow"},
    {"action": "read", "resource": "~/.config/opencode/service.json", "effect": "ask"},
    {"action": "read", "resource": "~/.local/share/opencode/account.json", "effect": "deny"},
    {"action": "read", "resource": "~/.local/share/opencode/auth.json", "effect": "deny"}
  ],
  "policies": [
    {"action": "tool.use", "resource": "shell:git checkout *", "effect": "deny"},
    {"action": "tool.use", "resource": "shell:git clean *", "effect": "deny"},
    {"action": "tool.use", "resource": "shell:git reset *", "effect": "deny"},
    {"action": "tool.use", "resource": "shell:git restore *", "effect": "deny"},
    {"action": "tool.use", "resource": "shell:git stash *", "effect": "deny"}
  ]
}
```

运行以下命令安装：

```bash
chmod +x *.bash
./init-opencode.bash
```

## Optional Setup

### Plugins & Tools

你可以根据需要安装以下插件和工具：

```bash
# oh-my-opencode-slim
bunx oh-my-opencode-slim@latest install --background-subagents=yes --no-tui
# paseo
npm install -g @getpaseo/cli
```

### MCP Integrations

告诉我你希望在 OpenCode 中使用哪些软件或服务，我会按需安装并配置对应的 MCP：

- **已安装的软件**：例如 ArtCraft 系列产品、Zotero，接入后可在 OpenCode 中直接使用。
- **在线服务**：例如通过 [arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) 搜索、下载和阅读 arXiv 论文，读取原始 LaTeX、导出引用及订阅研究主题。

你只需说明需要哪些集成，我会根据项目最新说明和当前 OpenCode 配置方式完成安装。
