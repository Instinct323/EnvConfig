Config: `~/.config/opencode/opencode.json`

Doc: https://help.aliyun.com/zh/model-studio/opencode-coding-plan

---

在 Config 中更新以下内容，同时替换`YOUR_API_KEY`为用户输入的 API_KEY

因为 Qwen 系列的表现较差，忽略其中的 Qwen 系列

```json
{
    "$schema": "https://opencode.ai/config.json",
    "provider": {
        "bailian-coding-plan": {
            "npm": "@ai-sdk/anthropic",
            "name": "Model Studio Coding Plan",
            "options": {
                "baseURL": "https://coding.dashscope.aliyuncs.com/apps/anthropic/v1",
                "apiKey": "YOUR_API_KEY"
            },
            "models": {
                "qwen3.5-plus": {
                    "name": "Qwen3.5 Plus",
                    "modalities": {
                        "input": ["text", "image"],
                        "output": ["text"]
                    },
                    "options": {
                        "thinking": {
                            "type": "enabled",
                            "budgetTokens": 8192
                        }
                    },
                    "limit": {
                        "context": 1000000,
                        "output": 65536
                    }
                },
                "qwen3-max-2026-01-23": {
                    "name": "Qwen3 Max 2026-01-23",
                    "modalities": {
                        "input": ["text"],
                        "output": ["text"]
                    },
                    "limit": {
                        "context": 262144,
                        "output": 32768
                    }
                },
                "qwen3-coder-next": {
                    "name": "Qwen3 Coder Next",
                    "modalities": {
                        "input": ["text"],
                        "output": ["text"]
                    },
                    "limit": {
                        "context": 262144,
                        "output": 65536
                    }
                },
                "qwen3-coder-plus": {
                    "name": "Qwen3 Coder Plus",
                    "modalities": {
                        "input": ["text"],
                        "output": ["text"]
                    },
                    "limit": {
                        "context": 1000000,
                        "output": 65536
                    }
                },
                "MiniMax-M2.5": {
                    "name": "MiniMax M2.5",
                    "modalities": {
                        "input": ["text"],
                        "output": ["text"]
                    },
                    "options": {
                        "thinking": {
                            "type": "enabled",
                            "budgetTokens": 8192
                        }
                    },
                    "limit": {
                        "context": 196608,
                        "output": 24576
                    }
                },
                "glm-5": {
                    "name": "GLM-5",
                    "modalities": {
                        "input": ["text"],
                        "output": ["text"]
                    },
                    "options": {
                        "thinking": {
                            "type": "enabled",
                            "budgetTokens": 8192
                        }
                    },
                    "limit": {
                        "context": 202752,
                        "output": 16384
                    }
                },
                "glm-4.7": {
                    "name": "GLM-4.7",
                    "modalities": {
                        "input": ["text"],
                        "output": ["text"]
                    },
                    "options": {
                        "thinking": {
                            "type": "enabled",
                            "budgetTokens": 8192
                        }
                    },
                    "limit": {
                        "context": 202752,
                        "output": 16384
                    }
                },
                "kimi-k2.5": {
                    "name": "Kimi K2.5",
                    "modalities": {
                        "input": ["text", "image"],
                        "output": ["text"]
                    },
                    "options": {
                        "thinking": {
                            "type": "enabled",
                            "budgetTokens": 8192
                        }
                    },
                    "limit": {
                        "context": 262144,
                        "output": 32768
                    }
                }
            }
        }
    }
}
```