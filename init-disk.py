import os
from pathlib import Path

USER = "Instinct323"
URL_BASE = f"https://github.com/{USER}" if os.name == "nt" else f"git@github.com:{USER}"

DIR_TREE = {
    ".empty": ["Downloads", "Source"],

    "Softwin": {
        ".empty": ["tmp", "AppData", "Tool", "Adobe", "Programming", "Tencent"],
    },

    "Information": {
        ".empty": ["Data", "Document"],
        ".git": [f"{URL_BASE}/{USER} notes"],
    },

    "Workbench": {
        ".empty": ["3rd-party", "assets", "Lab"],
        ".git": [f"{URL_BASE}/cppmod", f"{URL_BASE}/pymod",
                 f"{URL_BASE}/EnvConfig", f"{URL_BASE}/ModelsAPI", f"{URL_BASE}/ROS-dev-space"],
    },
}


def execute(cmd, check=True):
    exit_code = print("\033[32m\033[1m" + cmd + "\033[0m") or os.system(cmd)
    if check and exit_code: raise OSError(f"Fail to execute: {cmd}")
    return exit_code


def mkdir(path: Path):
    path.mkdir(exist_ok=True)
    print("\033[34m\033[1m" + f"mkdir: {path}" + "\033[0m")


def mktree(config: dict,
           root: Path = None):
    """ Make directory tree according to the config.  """
    root = root or Path().resolve()
    for folder, sub in config.items():

        if folder == ".git":
            os.chdir(root)
            for repo in sub:
                execute(f"git clone {repo}")

        elif folder == ".empty":
            for f in sub: mkdir(root / f)

        else:
            p = root / folder
            mkdir(p)
            mktree(sub, p)


if __name__ == '__main__':
    mktree(DIR_TREE)
