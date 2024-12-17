from pathlib import Path

import tests_for_practice_form


def path(file_name):
    return str(
        Path(tests_for_practice_form.__file__).parent.joinpath(f'resources/{file_name}').absolute()
    )