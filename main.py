import importlib
from resources.update_readme import update
from resources.count_files import count_files


if __name__ == '__main__':
    default = count_files()
    num = (input(f'Insert your problem number (enter for default {default} ): ') or default)

    if num in {'u', 'update'}:
        update()
        quit()

    num = int(num)

    module = importlib.import_module(f'problems.problem{num}')
    try:
        module.solution()
    except AttributeError:
        print('Module does not exist')
