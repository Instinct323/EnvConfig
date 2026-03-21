---
name: config-omo
description: Install filtered `oh-my-opencode.json` using locally available models. Run `python scripts/config_omo.py --help` first to see current options.
version: 1.0.0
---

# config-omo

Install `oh-my-opencode.json`, filtering fallback_models to only include models available in your environment.

## Discovery

Before using, run the command once to check the current CLI contract:

```bash
python <skill-dir>/scripts/config_omo.py --help
```

This will display available options and their descriptions.

## Usage Flow

1. **Check the CLI contract** — Run `--help` to view the available options.

2. **Execute directly** — Run the script according to the user's instructions:

   * If no additional instructions are provided: run with default arguments (no flags).
   * If additional flags are provided: include them in the command.

   **DO NOT ask the user any questions.** Execute directly based on the user's provided instructions (or defaults if none).

## Behavior

* Reads the source config (from URL or local path).
* Runs `opencode models` to gather available models.
* Filters the `fallback_models` to only include available ones.
* If the primary model is unavailable, promotes the first available fallback model.
* Sets the model to an empty string if neither the primary nor any fallback models are available.
* Writes the result to the destination.
* On success: prints `Fetched: <src>` and `Installed: <dst>`.
* On failure: prints an error and exits with code 1.

## Final Response Requirement

After completing the work successfully, tell the user: `You need to restart opencode to apply the configuration changes.`

## Requirements

* Python 3
* `opencode` CLI in PATH
