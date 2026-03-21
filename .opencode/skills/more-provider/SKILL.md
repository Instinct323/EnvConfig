---
name: more-provider
description: Configure API keys for cloud model providers. Run `python scripts/set_apikey.py --help` first to see current provider flags, then use the two-step flow.
version: 1.0.0
---

# more-provider

Add or update provider API keys in `~/.config/opencode/opencode.json`. The script uses local provider templates to populate provider configuration.

## Discovery

Before using, run once to see current CLI contract:

```bash
python scripts/set_apikey.py --help
```

This shows available provider flags and their descriptions.

## Usage Flow

1. **Provider selection** — Use the `question` tool with `multiple: true` to let the user select one or more providers from the available options.

2. **API key collection** — Based on selection, prompt the user to input API keys for each selected provider.

3. **Execute** — Run the script with collected keys, including only the flags for providers the user selected.

## CLI Pattern

```bash
python scripts/set_apikey.py --provider1 "YOUR_KEY" --provider2 "YOUR_KEY"
```

Omit flags for providers not being configured (empty keys are silently skipped).

## Behavior

- Writes to `~/.config/opencode/opencode.json`
- Prints `Added provider: {name}` only on first insertion of a provider
- Silent update (no output) when re-running with existing provider
- Exits 0 on success, 1 on error

## Final Response Requirement

After completing the work successfully, tell the user: `You need to restart opencode to apply the configuration changes.`

## Requirements

- Python 3
- Provider templates in `scripts/provider/*.json`
