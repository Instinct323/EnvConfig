# Configuration Guide

此文档的标题使用英文，正文使用中文。

---

## Global

在 opencode 全局配置路径 (`~/.config/opencode/`) 下创建 `global-config.md`，用于记录已完成的配置项以避免重复配置。当遇到已完成的配置项时，询问用户是否需要重新配置。配置完成后，清理过程中产生的临时文件。

### oh-my-openagent

参考官方安装指南：
- 文档：https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/docs/guide/installation.md

### anthropics-skills

安装仓库中的 skills：
- 仓库：https://github.com/anthropics/skills

---

## Project

将配置结果写入 `AGENTS.md`

### Include

- [code-style.md](https://github.com/Instinct323/EnvConfig/blob/master/.opencode/code-style.md)

### Preference

- 始终使用中文回复，可使用少量英文单词

### Environment

1. 查找本地 conda 环境
2. 如无 conda：询问是否安装 [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install)
3. 询问用户 选择现有虚拟环境 / 创建新环境（需指定：环境名称、Python 版本）
