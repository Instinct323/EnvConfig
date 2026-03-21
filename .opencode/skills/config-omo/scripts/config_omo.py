from __future__ import annotations

import argparse
import itertools
import json
import os
import re
import subprocess
from pathlib import Path
from urllib.request import urlopen

USERPATH = os.path.expanduser("~")
ENCODING = "utf-8"


def available_models(disable: list[str]) -> set[str]:
    try:
        output = subprocess.run(
            ["opencode", "models"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    except FileNotFoundError:
        raise RuntimeError("No `opencode` found in current environment")
    return {m for m in map(str.strip, output.split()) if m.split("/")[0] not in disable}


def load_dump_json(self: Path, data=None):
    return json.loads(self.read_text(encoding=ENCODING)) \
        if data is None else self.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding=ENCODING)


def fetch_config(src: str) -> dict:
    if re.search(r"^https?://", src):
        with urlopen(src) as response:
            content = response.read().decode(ENCODING)
            return json.loads(content)
    else:
        return load_dump_json(Path(src))


def normalize_fallback_models(config: dict,
                              models: set[str]):
    config["model_fallback"] = True
    for name, prop in itertools.chain(
            config["agents"].items(), config["categories"].items(),
    ):
        # filter out invalid models
        fallback = prop.get("fallback_models")
        if fallback:
            fallback = prop["fallback_models"] = [m for m in fallback if m in models]

        # fallback to first model
        if prop["model"] not in models:
            prop["model"] = fallback.pop(0) if fallback else ""


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--src", type=str,
        default="https://raw.githubusercontent.com/Instinct323/EnvConfig/master/.opencode/config/oh-my-opencode.json",
        # default="tmp/oh-my-opencode.json",
        help="Path or URL of the configuration file"
    )
    parser.add_argument(
        "--dst", type=str, default=f"{USERPATH}/.config/opencode/oh-my-opencode.json",
        help="Installation path of the configuration file"
    )
    parser.add_argument(
        "--disable", nargs="+", default=[], help="Disable providers"
    )
    args = parser.parse_args()

    try:
        cfg = fetch_config(args.src)
        print(f"Fetched: {args.src}")

        # process
        normalize_fallback_models(cfg, models=available_models(args.disable))

        dst = Path(args.dst).resolve()
        dst.parent.mkdir(parents=True, exist_ok=True)
        load_dump_json(dst, cfg)
        print(f"Installed: {dst}")

    except Exception as e:
        print(e)
        exit(1)
