import argparse
import json
import os
from pathlib import Path

os.chdir(Path(__file__).parent.parent)

USERPATH = os.path.expanduser("~")
CONFIG = Path(USERPATH) / ".config/opencode/opencode.json"
ENCODING = "utf-8"


def load_dump_json(self: Path, data=None):
    return json.loads(self.read_text(encoding=ENCODING)) \
        if data is None else self.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding=ENCODING)


def load_provider(config: dict,
                  name: str,
                  api_key: str) -> bool:
    config.setdefault("provider", {})
    provider_org = config["provider"].get(name, {})
    api_key = api_key or provider_org.get("options", {}).get("apiKey")
    if not api_key: return False

    provider = load_dump_json(Path(f"provider/{name}.json"))["data"]
    provider["options"]["apiKey"] = api_key

    if not provider_org:
        print(f"Added provider: {name}")
    config["provider"][name] = provider
    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--baidu", type=str, default="", help="BaiduQianfan (百度千帆) API Key")
    parser.add_argument("--bailian", type=str, default="", help="Bailian (百炼) API Key")
    parser.add_argument("--volcengine", type=str, default="", help="VolcEngine (火山引擎) API Key")
    args = parser.parse_args()

    try:
        cfg = load_dump_json(CONFIG)

        # process
        changed = False
        changed |= load_provider(cfg, "baiduqianfancodingplan", args.baidu)
        changed |= load_provider(cfg, "bailian-coding-plan", args.bailian)
        changed |= load_provider(cfg, "volcengine-plan", args.volcengine)

        if changed:
            # print(json.dumps(cfg, indent=2))
            load_dump_json(CONFIG, cfg)

    except Exception as e:
        print(e)
        exit(1)
