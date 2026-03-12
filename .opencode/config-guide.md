# Configuration Guide

本文档记录 OpenCode 的配置规范与操作流程

### Format

- This-doc: 标题使用英文，正文使用中文
- Config：
  - 已完成的配置项（避免重复配置）
  - 配置步骤（便于向用户说明操作过程）
- File: 超链接表示的文件，一般位于该文档的根目录下；或者位于 [github](https://github.com/Instinct323/EnvConfig/blob/master/.opencode/) 仓库中

### Process

每个配置文件的配置流程如下：

1. 读取 Config：根据配置状态决定后续操作
2. 状态判断：
   - 已完成 → 询问用户是否需要重新配置
   - 未完成 → 执行配置，完成后更新配置状态
3. 清理：配置完成后清理临时文件

---

## Global

Config: `~/.config/opencode/global-config.md`

### anthropics-skills

安装社区维护的 skills：
- 仓库：https://github.com/anthropics/skills

### oh-my-openagent

参考官方安装指南：
- 文档：https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/docs/guide/installation.md

### volcano-engine

要求用户输入火山引擎的 `API-KEY`，有的话，参考以下文档进行配置：
- 文档：[volcano-engine.md]()

---

## Project

Config: `AGENTS.md`

### Include

你需要读取并总结以下文档:

- [code-style.md]()

### Preference

- 始终使用中文回复，可穿插少量英文术语
- 不要修改工作区之外的文件，请先在工作区内创建修改后的版本，并询问用户是否需要覆盖到源文件
