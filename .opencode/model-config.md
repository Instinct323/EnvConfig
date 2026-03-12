Config: `~/.config/opencode/oh-my-opencode.json`

Doc: https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/docs/guide/agent-model-matching.md

core-agent: sisyphus, hephaestus, prometheus, atlas

---

你需要阅读 Doc 中对各个任务的介绍，理解各个模型所需的能力

阅读该配置文件中的任务列表，根据这些任务所需的能力，对可用模型列表进行排序

随后，询问用户对模型配置的偏好：

1. 性能优先：适合按调用次数计费的套餐
2. 平衡性：既考虑性能，也考虑成本
3. 成本优先：适合按 token 数计费的套餐
4. 自定义：

根据排序结果以及用户偏好，分别为每个任务分配模型 (如果缺失了核心 agent，你需要自行添加)

每一个 agent / category 都需要严格配置以下字段，以增强可读性：

```json
{
    "model": "volcengine-plan/deepseek-v3.2",
    "description": "执行官：利用长上下文进行循环纠错"
}
```

最后，提醒用户重启 opencode，确保配置文件被正确加载
