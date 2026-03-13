Config: `~/.config/opencode/opencode.json`

Doc: https://www.volcengine.com/docs/82379/2188958?lang=zh

---

在 Config 中更新以下内容，同时替换`<ARK_API_KEY>`为用户输入的 API_KEY

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
