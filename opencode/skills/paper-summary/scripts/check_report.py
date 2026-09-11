import argparse

from registry import Registry

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Initialize the registry")
    parser.add_argument("id", type=str, help="Registry ID")
    parser.add_argument("--paper", type=str, default="", help="Paper ID")
    args = parser.parse_args()

    try:
        Registry(args.id).check_report(args.paper)

    except Exception as e:
        print(f"Error: {e}")
        exit(1)
