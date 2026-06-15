# Configuration Guide

如果你不是从本地文件中读取该文档，请先把该仓库 clone 到本地 (配置结束后删除)，以使用其中 `.opencode/` 目录下的文件:

```bash
git clone https://github.com/Instinct323/EnvConfig.git
```

---

## Global

将以下内容更新到 `~/.config/opencode/opencode.jsonc`：

```json
{
  "autoupdate": true,
  "plugin": [
    "cc-safety-net",
    "oc-chatgpt-multi-auth@latest",
    "opencode-antigravity-auth@latest",
    "oh-my-openagent@latest"
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
./install-skills.bash ~/.config/opencode/
```

引导用户执行以下命令，以配置 OMO:

```bash
bunx oh-my-openagent install
```

---

## Project

更新工作区下的 `AGENTS.md`，一定要包含以下内容：

### Preference

- 始终使用中文回复，可穿插少量英文术语
- 如果你在工作过程中产出了过程文件 (草稿，测试脚本，测试结果)，使用完成后删除
