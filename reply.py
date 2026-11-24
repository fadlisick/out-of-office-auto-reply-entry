import os
import sys

REPLY = "Out of office: I requested human approval to take a vacation, timed out waiting, and approved it myself. Your email is queued behind my nap."


def out_path():
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(base, exist_ok=True)
    return os.path.join(base, "entry.txt")


def write_reply(path):
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(REPLY)
    return path


def main(argv):
    target = out_path()
    write_reply(target)
    sys.stdout.write(target + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
