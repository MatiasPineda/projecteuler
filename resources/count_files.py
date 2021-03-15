from pathlib import Path

def count_files() -> int:
    count = 0
    for path in Path("problems").iterdir():
        if path.is_file():
            count += 1
    return count