# Configuration Guide

本文档记录 OpenCode 的配置规范与操作流程

### Format

- This-doc: 标题使用英文，正文使用中文
- Config：
  - 已完成的配置项（避免重复配置）
  - 配置步骤（便于向用户说明操作过程）

### Process

1. 读取 Config：根据配置状态决定后续操作
2. 状态判断：
   - 已完成 → 询问用户是否需要重新配置
   - 未完成 → 执行配置，完成后更新配置状态
3. 清理：配置完成后清理临时文件

---

## Global

Config: `~/.config/opencode/global-config.md`

### oh-my-openagent

参考官方安装指南：
- 文档：https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/docs/guide/installation.md

### anthropics-skills

安装社区维护的 skills：
- 仓库：https://github.com/anthropics/skills

---

## Project

Config: `AGENTS.md`

### Include

- [code-style.md](https://github.com/Instinct323/EnvConfig/blob/master/.opencode/code-style.md)

### Preference

- 始终使用中文回复，可穿插少量英文术语

### Environment

1. 查找本地 conda 环境
2. 如无 conda：询问是否安装 [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install)
3. 询问用户选择：
   - 使用现有虚拟环境
   - 创建新环境（需指定：环境名称、Python 版本）
