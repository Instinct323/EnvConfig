import json
import re
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent
SCHEMA_REPORT = SKILL_DIR / "schema.md"
RUNS = Path(".sisyphus/evidence")


def get_file(run_id: str):
    return RUNS / f"{SKILL_DIR.name}-{run_id}/registry.json"


def load_dump_json(self: Path, data=None):
    return json.loads(self.read_text()) \
        if data is None else self.write_text(json.dumps(data, indent=2, ensure_ascii=False))


def print_msg(msg: list[str]):
    print("-" * 20)
    print("\n".join(msg))


class Registry:
    FIELD_SOURCE = ["repo", "pdf", "txt"]
    FIELD_RESULT = ["report"]

    def __init__(self,
                 run_id: str,
                 init_keys: list[str] = None):
        self.file = get_file(run_id)
        print(f"run_id: {run_id}")
        print(f"project: {self.file.parent}")

        # initialize
        if init_keys:
            assert not self.file.exists(), f"{self.file} already exists"
            self.file.parent.mkdir(parents=True, exist_ok=True)
            self.data = {k: {f: "" for f in self.FIELD_SOURCE + self.FIELD_RESULT} for k in init_keys}
            load_dump_json(self.file, self.data)
        else:
            self.data = load_dump_json(self.file)

    def check_fields(self,
                     fields: list[str],
                     key: str = None,
                     allow_none: bool = False):
        msg = []
        for k in [key] if key else self.data:
            for f in fields:

                # get
                try:
                    p = self.data[k][f]
                except KeyError:
                    msg.append(f"{k}: missing `{f}`")
                    continue

                # check
                if not p:
                    msg.append(f"{k}: missing `{f}`")
                elif allow_none and p.lower() == "none":
                    continue
                elif not (Path(p).exists() or p.startswith("http")):
                    msg.append(f"{k}: `{p}` does not exist")

        if msg: print_msg(msg)
        return msg

    def check_report(self,
                     key: str = None):
        if self.check_fields(self.FIELD_RESULT, key): return
        pattern = ".*".join(line.strip() for line in SCHEMA_REPORT.read_text().split("\n") if line.startswith("## "))

        # get report
        for k in [key] if key else self.data:
            p = Path(self.data[k]["report"])
            if not p.exists():
                print(f"{k}: report file not found at `{p}`")
                continue
            report = p.read_text()
            if not re.search(pattern, report, flags=re.S):
                print(f"{k}: bad report, please read `{SCHEMA_REPORT}` first to understand the content requirements.")

    def fetch_final_report(self):
        if self.check_fields(self.FIELD_RESULT): return
        reports = [Path(self.data[k]["report"]).read_text(encoding="utf-8") for k in self.data]

        file = self.file.parent / "report.md"
        file.write_text("\n\n---\n\n".join(reports))
        print(f"Report saved to `{file}`")

        if len(reports) > 1:
            print("Multiple reports found, please add a `Cross-Comparison` section for comparative analysis.")


if __name__ == '__main__':
    registry = Registry("0", init_keys=["test", "test2"])
    registry.check_fields(registry.FIELD_SOURCE)
