import pathlib, importlib


def count_files() -> int:
    count = 0
    for path in pathlib.Path("problems").iterdir():
        if path.is_file():
            count += 1
    return count


if __name__ == '__main__':
    default = count_files()
    num = int(input(f'Insert your problem number (enter for default {default} ): ') or default)

    module = importlib.import_module(f'problems.problem{num}')
    try:
        module.solution()
    except AttributeError:
        print('Module does not exist')
