import argparse

from registry import Registry

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Initialize the registry")
    parser.add_argument("id", type=str, help="Registry ID")
    parser.add_argument("--papers", nargs="+", default=[], help="Papers to add to the registry")
    args = parser.parse_args()

    try:
        Registry(args.id, args.papers)

    except Exception as e:
        print(f"Error: {e}")
        exit(1)
