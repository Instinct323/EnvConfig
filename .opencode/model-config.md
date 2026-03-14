[ARC Prize](https://arcprize.org/leaderboard): Gemini > GPT > Claude > Kimi > Minimax > GLM-5 > Deepseek > Qwen

[Chatbot](https://openlm.ai/chatbot-arena/): 

- Vision: Gemini > GPT = Doubao > Kimi

[LLM Benchmark](https://livebench.ai/#/) (Qwen 效果不佳):

- Reasoning: Claude = GPT > Gemini > Deepseek > Kimi
- Coding: GPT > Claude > Gemini > Doubao > Kimi > Deepseek
- Agentic Coding: GPT > Gemini > Claude > GLM-5 > Minimax > Kimi
- Language: Gemini > Claude > GPT > Kimi = GLM-5
- Instruction Following: Gemini > GPT > Claude > Kimi

Doc: https://github.com/code-yeongyu/oh-my-openagent/blob/dev/docs/guide/agent-model-matching.md

---

# Step 1

从以下途径搜集模型列表：

- 配置文件 `~/.config/opencode/opencode.json`

# Step 2

询问用户对模型配置的偏好：

1. 性能优先：适合按调用次数计费的套餐
2. 平衡性：既考虑性能，也考虑成本
3. 成本优先：适合按 token 数计费的套餐
4. 自定义：

以及用户所偏好的供应商 (每个选项对应一个供应商)

# Step 3

按照 Doc 的教程，以及上述的排行榜，修改 `~/.config/opencode/oh-my-opencode.json`

# Finish

最后，提醒用户重启 opencode，确保配置文件被正确加载
