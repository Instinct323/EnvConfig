Config: `~/.config/opencode/opencode.json`

首先检测是否已经有配置好的 volcengine-plan API_KEY，然后给用户以下几个选项:

1. 写入新的 API_KEY
2. 跳过配置 API_KEY
3. 退出火山引擎配置

在该文件中更新以下内容，同时替换`<ARK_API_KEY>`为用户输入的 API_KEY

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "volcengine-plan/ark-code-latest",
  "provider": {
    "volcengine-plan": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Volcano Engine",
      "options": {
        "baseURL": "https://ark.cn-beijing.volces.com/api/coding/v3",
        "apiKey": "<ARK_API_KEY>"
      },
      "models": {
        "ark-code-latest": {
          "name": "ark-code-latest",
          "limit": {
            "context": 256000,
            "output": 4096
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          }
        },
        "doubao-seed-code": {
          "name": "doubao-seed-code",
          "limit": {
            "context": 256000,
            "output": 4096
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          }
        },
        "glm-4.7": {
          "name": "glm-4.7",
          "limit": {
            "context": 200000,
            "output": 4096
          },
          "modalities": {
            "input": [
              "text"
            ],
            "output": [
              "text"
            ]
          }
        },
        "deepseek-v3.2": {
          "name": "deepseek-v3.2",
          "limit": {
            "context": 128000,
            "output": 4096
          }
        },
        "doubao-seed-2.0-code": {
          "name": "doubao-seed-2.0-code",
          "limit": {
            "context": 256000,
            "output": 4096
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          }
        },
        "doubao-seed-2.0-pro": {
          "name": "doubao-seed-2.0-pro",
          "limit": {
            "context": 256000,
            "output": 4096
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          }
        },
        "doubao-seed-2.0-lite": {
          "name": "doubao-seed-2.0-lite",
          "limit": {
            "context": 256000,
            "output": 4096
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          }
        },
        "minimax-m2.5": {
          "name": "minimax-m2.5",
          "limit": {
            "context": 200000,
            "output": 4096
          },
          "modalities": {
            "input": [
              "text"
            ],
            "output": [
              "text"
            ]
          }
        },
        "kimi-k2.5": {
          "name": "kimi-k2.5",
          "limit": {
            "context": 256000,
            "output": 4096
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          }
        }
      }
    }
  }
}
```

记录该配置文件中的可用模型列表，以进行模型分配
