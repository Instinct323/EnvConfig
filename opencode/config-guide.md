# Configuration Guide

如果你不是从本地文件中读取该文档，请先把该仓库 clone 到本地 (配置结束后删除)，以使用其中 `opencode/` 目录下的文件:

```bash
git clone https://github.com/Instinct323/EnvConfig.git
```

---

将仓库中 `opencode/config/opencode.jsonc` 的配置合并到 `~/.config/opencode/opencode.jsonc`，保留已有的其他配置；如果目标文件不存在，则直接复制该文件。

进入仓库的 `opencode/` 目录，运行以下命令安装：

```bash
chmod +x scripts/*.bash
./scripts/init-opencode.bash
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

### Worth Trying

- [OpenMotion](https://github.com/nexu-io/openmotion)：AI Agent 驱动的视频创作工具，支持参考视频复刻、模板创作与可视化编辑。
